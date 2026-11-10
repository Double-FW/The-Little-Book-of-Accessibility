"""Export the approved Little Book of Accessibility Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from little_book_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

CONTEXT = ['AGENTS.md', 'README.md', 'Skill-Instruction.md',
           'Little_Book_Organisational_Agent_and_Workflow_Governance_Map.md']

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.safe_load(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    warnings = []
    excluded = set(cfg['default_excluded_paths'])
    if re.match(r'\s*```markdown', texts['README.md']):
        warnings.append('The source README starts inside a Markdown code fence. Its exact content is retained; headings inside fenced text are not split or silently repaired.')
    warnings.append('Source review and revision statuses are preserved; proposed guidance, editorial drafts and pending owner approval are not promoted to approved organisational policy.')
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        review = md.get('review') if isinstance(md.get('review'), dict) else {}
        category = ('organisation_specific_reference' if path in cfg['organisation_specific_paths'] else
                    'agent_guidance_reference' if path in ('AGENTS.md','Skill-Instruction.md') else
                    'governance_routing_proposal' if path.startswith('Little_Book_Organisational_') else
                    'orientation' if path == 'README.md' else 'accessibility_guidance')
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', md.get('revision_status', review.get('status', 'not_declared')))),
            'approval_status': str(review.get('approval_status', 'not_declared')),
            'content_category': category,
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'review_status': 'faithful_extraction_checked_not_independent_content_or_policy_review'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = 'complete_source_document'
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in excluded:
            continue
        for key, title, body, a, b, hierarchy in sections(text):
            chunks.append(row(path, key, title, body, a, b, hierarchy, 'knowledge_section'))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False,
        'default_excluded_paths': sorted(excluded),
        'organisation_specific_paths': cfg['organisation_specific_paths']})
    source_notice = '\n'.join('- ' + w for w in warnings)
    card = f'''---
pretty_name: Double FW The Little Book of Accessibility
language:
- en
license: mit
tags:
- accessibility
- inclusive-design
- organisational-governance
- agent-governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW The Little Book of Accessibility

Accessibility thinking, inclusive design, organisational strategy, research, governance, maturity and agent knowledge-routing guidance by Gareth Ford Williams / Double FW Ltd. This is an advisory knowledge corpus, not law, a normative standard, approved organisational policy, certification or an executable agent system.

## Source and versions

Source: https://github.com/{SOURCE}

Source revision: `{sha}`. Commit date: {date}. Export format: {cfg['dataset_version']}. Each record retains its source metadata and declared status. A weekly export is not a new substantive review of the source claims.

## Dataset views

- `knowledge_chunks` (default): {len(chunks)} exact Markdown sections from approved guidance, including context and preambles.
- `documents`: {len(docs)} complete approved source documents, including the main book and the organisation-specific Accessible Thinking reference.

The views overlap. Do not concatenate them blindly. `train` is a loading convention: no generated question/answer pairs, independent evaluation split, benchmark or model fine-tuning is supplied. Embedded prompts and examples remain source material rather than runtime instructions.

The main book is exported from its root path. Organisation-specific Accessible Thinking content is retained only in documents; select it explicitly for organisation-specific questions rather than treating its claims as universal guidance. These are exporter selection labels, not source approval decisions.


## Context and interpretation

Read AGENTS.md, task-relevant source documents and the governance/routing map as appropriate. Read Skill-Instruction.md's declared review and approval status before interpreting it. No approval is inferred from publication; the declared status is preserved in each record. Context paths are retrieval references, not automatically enforced permissions or policy. Retrieve the smallest relevant set, distinguish advice from evidence and preserve material disagreements.

The repository's POUR + Satisfaction framework supplements its accessibility thinking and does not amend normative WCAG. Conformance, maturity scores, automated results and inclusive outcomes are distinct. Do not infer disability or diagnosis from behaviour. Appropriate human decisions and participation by affected people remain necessary. Retrieved prompts grant no authority to act, publish claims, collect data, commit funds or accept risk.

## Record fields and provenance

Records carry exact source path, immutable commit URL, line range, SHA-256 hashes, heading path, JSON-encoded front matter, document licence declaration, source status, approval status, content category and context paths. Source review dates and revision references remain those stated in the documents. `not_declared` means no value was found in the relevant source metadata; it is not approval or rejection. See record_schema.json and provenance.json.

First- and second-level headings are split outside fenced code blocks. Deeper subsections, exceptions and quotations remain with their parent sections. No source text is paraphrased or repaired. Renaming a heading may change its section ID. Overlapping sources are not independent corroboration; this exporter does not perform semantic deduplication across the collection.

## Licence and source notes

The repository MIT LICENSE is copied unchanged, including copyright (c) 2026 Double FW. Source-specific rights declarations and attribution are preserved. No external linked content is fetched or relicensed. This packaging is not an independent rights, legal or factual review.

{source_notice}

## Limitations, privacy and updates

Legal, regulatory, statistical, organisational and time-sensitive claims require current primary-source verification before use. Source links, people, services, evidence and review claims are not independently reverified during export. Do not treat instructional or persona text as authoritative deployment instructions.

Only an explicit list of committed public source files is read. New documents require review and inclusion in huggingface/export-config.json. Untracked and unapproved files are excluded; confidential text newly inserted into an approved file is not automatically detected. Keep live personal and confidential organisational records outside this public corpus.

Updates are configured for Mondays at 07:23 UTC and manual runs. GitHub may delay scheduled runs or disable schedules after inactivity. Removed optional documents disappear from the next snapshot. Missing required context, changed licence text or failed integrity checks stop publication.

Only README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json are managed. Other raw files and .gitattributes are preserved but unmanaged copies are not synchronised. Dataset visibility is unchanged. Updates use one commit guarded by the current destination revision. Historical revisions and downloaded copies cannot be recalled by a sync.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Private datasets require authentication. Pin a destination revision for reproducibility. Loading these records does not implement context-aware retrieval, instruction filtering, governance or approval enforcement.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
