# Weekly dataset update setup

THE LITTLE BOOK OF ACCESSIBILITY — WEEKLY HUGGING FACE UPDATES

GitHub source: https://github.com/Double-FW/The-Little-Book-of-Accessibility
Hugging Face destination: https://huggingface.co/datasets/GarethFW/The_Little_Book_of_Accessibility
Dataset ID (already filled in): GarethFW/The_Little_Book_of_Accessibility
Secret name: HF_TOKEN (underscore, not a hyphen)
No HF_DATASET_ID repository variable is needed.

Work through one stage at a time. Return to the chat after each stage if useful.
No coding or Terminal commands are needed for this setup.

STAGE 1 — OPEN THE DOWNLOAD
1. Download the ZIP from the chat.
2. Find it in Downloads on your Mac and double-click it.
3. Open the folder: Little_Book_of_Accessibility_Weekly_Update_Setup
4. You should see UPLOAD_TO_GITHUB, WORKFLOW_TO_COPY.txt,
   START_HERE.txt and CHECKS_AND_SOURCE_INVENTORY.md.
Stop here if following the chat one step at a time. Reply: done.

STAGE 2 — UPLOAD THREE FOLDERS TO GITHUB
1. Open https://github.com/Double-FW/The-Little-Book-of-Accessibility
2. On the Code tab, use the default branch (currently main).
3. Choose Add file, then Upload files.
4. On your Mac, open UPLOAD_TO_GITHUB.
5. Drag its THREE folders together into the GitHub upload area:
   huggingface
   scripts
   tests
6. Drag the folders themselves so their internal paths are preserved.
   Do not upload the enclosing UPLOAD_TO_GITHUB folder or the ZIP.
7. Check the uploaded paths include huggingface/export-config.json,
   scripts/export_huggingface.py and tests/test_little_book_huggingface.py.
   They must not begin with UPLOAD_TO_GITHUB/.
8. Enter this commit message: Add weekly Hugging Face update files
9. Click Commit changes. Commit directly to main if permitted; if GitHub
   requires a pull request, create it and merge it before the next stage.

STAGE 3 — CREATE THE WEEKLY WORKFLOW
1. Open https://github.com/Double-FW/The-Little-Book-of-Accessibility
2. Choose Add file, then Create new file.
3. In Name your file, type EXACTLY:
   .github/workflows/huggingface-sync.yml
4. The dot belongs at the start of .github only. The filename is
   huggingface-sync.yml — with NO dot before huggingface.
5. GitHub creates the folders automatically. You do not need to upload a
   hidden folder or reveal any hidden Mac files.
6. On your Mac, open WORKFLOW_TO_COPY.txt in TextEdit or another text editor.
7. Press Command+A, then Command+C to copy ALL its contents.
8. Click inside GitHub's large file editor and press Command+V.
9. Check the first line is:
   name: Update Little Book of Accessibility Hugging Face dataset
10. Choose Commit changes. Use this message: Add weekly Hugging Face workflow
11. Confirm the commit to main if permitted, or merge the required pull request.

STAGE 4 — CREATE A HUGGING FACE TOKEN FOR THIS DATASET
Never put a token in a public file, screenshot or this chat.
1. Open https://huggingface.co/settings/tokens
2. Choose Create new token.
3. Name it: Little Book of Accessibility weekly sync
4. Select Custom or Fine-grained, depending on the page's labels.
5. Find Repositories permissions and select:
   GarethFW/The_Little_Book_of_Accessibility
6. Enable Read contents of selected repos and Write contents/settings of
   selected repos. Leave unrelated permissions unselected.
7. If View access requests for selected gated repos is selected automatically
   by the interface, it can remain selected.
8. Choose Create token.
9. Copy the displayed token privately. Keep that page open until the token
   is saved in GitHub. If you lose the value, create a replacement token.

STAGE 5 — SAVE THE TOKEN IN GITHUB
1. Open https://github.com/Double-FW/The-Little-Book-of-Accessibility/settings/secrets/actions
2. Under Repository secrets, choose New repository secret.
3. Name: HF_TOKEN
4. Secret: paste the actual copied Hugging Face token value (Command+V).
5. Click Add secret. Confirm HF_TOKEN appears under Repository secrets.
6. If HF_TOKEN already exists, use its edit button to replace the value.
   GitHub does not show saved secret values again.
7. This is a SECRET, not a Variable. No destination variable is needed.

STAGE 6 — RUN THE FIRST UPDATE
1. Open https://github.com/Double-FW/The-Little-Book-of-Accessibility/actions
2. Select Update Little Book of Accessibility Hugging Face dataset.
3. If GitHub asks you to enable Actions/workflows for this repo, enable them.
4. Choose Run workflow. Leave the branch as main and click the green
   Run workflow button.
5. Refresh the page if necessary, then open the newest run.
6. Wait for it to finish. Send the run page's link to the chat for checking.
7. A green tick indicates success. A red cross means a step needs attention;
   share the run link, not the secret token.
8. After success, open https://huggingface.co/datasets/GarethFW/The_Little_Book_of_Accessibility/tree/main
9. Look for README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl,
   provenance.json, record_schema.json and validation_report.json.
   .gitattributes is expected and is preserved.
10. In the dataset viewer, select knowledge_chunks or documents. Allow time
    for the viewer to refresh after publication.

AFTER THE FIRST SUCCESSFUL RUN
Updates are configured for Mondays at 07:23 UTC (07:23 UK winter time,
08:23 UK summer time). GitHub may delay schedules or disable them in public
repositories after 60 days of inactivity. Manual Run workflow remains available.
This chat does not have to remain open for GitHub to perform an update.

Edit the existing GitHub source documents as usual. Only approved files in
huggingface/export-config.json are exported. If you add or rename a document,
return to the chat so we can review and update the list. Do not put live personal
or confidential organisational records in the public source documents.

ABOUT THIS EXPORT
The main book is taken from the root file The_Little_Book_Of_Accessibility_Thinking.md.
The removed Knowledge Base Documents copy is excluded from the approved list.
20 complete Markdown documents are exported. The default guidance view has
399 exact source sections at the checked source revision. These counts can
change after future source edits. The organisation-specific Accessible Thinking
reference is available in documents only, outside the default guidance view.
Source editorial/review status and qualifications remain intact. Publishing is
not approval of organisational policy, legal claims or accessibility outcomes.

The source README starts inside a Markdown code fence. Its exact text is
preserved rather than silently repaired; the generated dataset card is a
separate document. Source metadata and the MIT licence are retained unchanged.

Seven destination files are managed. Other raw files and .gitattributes are
preserved; unmanaged raw copies are not kept in sync. Dataset visibility is
unchanged. Historical copies and downloads are not recalled by an update.

IF SOMETHING LOOKS DIFFERENT
Stop at the current screen and describe what you can see in the chat. We can
work through it one action at a time. Exclude token values from screenshots.
