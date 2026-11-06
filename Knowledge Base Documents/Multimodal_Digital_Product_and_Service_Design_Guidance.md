Designing digital products and services for multiple modalities

Practical guidance for design and delivery teams

# 1 Purpose and intended outcomes

Design digital products and services so that people can understand what is happening, decide what to do, act, and recover using the senses and control methods available to them. A journey should remain meaningful when sound or vision is unavailable and when the user changes how they operate the interface.

This guidance is for accessibility, design, content, research, engineering and product managers, and the teams delivering their services. It applies across web, mobile, television, large screens and conversational experiences. Its focus is human experience: independent participation, clarity, confidence, satisfaction and equivalent enjoyment.

Multimodal design combines two responsibilities. Sensory flexibility provides equivalent ways to perceive information. Input flexibility provides alternative ways to control the system. Both must extend through the whole journey, including instructions, settings, waiting, errors, confirmation and exit. Providing an alternative only for the main action leaves the journey incomplete.

Use the guidance during discovery, journey mapping, prototyping, design critique, implementation and evaluation. Each section explains a design intention, conventions for putting it into practice, and an outcome that can be examined. The examples illustrate applications of these principles; they are not claims about a particular product.

## How to use this document

Start with sections 2 to 4 to establish the principles and map a journey. Use sections 5 to 15 to specify sensory alternatives, input behaviour and common interactions. Sections 16 to 20 cover delivery, evaluation, a worked example and organisational development. Appendix A provides a reusable design record; Appendix B maps this guidance to the supplied knowledge base.

# Contents

[1 Purpose and intended outcomes](#1-purpose-and-intended-outcomes)

[2 Principles of multimodal design](#2-principles-of-multimodal-design)

[3 Understand people and contexts](#3-understand-people-and-contexts)

[4 Map meaning and control before designing screens](#4-map-meaning-and-control-before-designing-screens)

[5 Design for use without sound](#5-design-for-use-without-sound)

[6 Design for use without vision](#6-design-for-use-without-vision)

[7 Combine sensory alternatives without creating overload](#7-combine-sensory-alternatives-without-creating-overload)

[8 Establish common conventions for all controls](#8-establish-common-conventions-for-all-controls)

[9 Support pointing and touch](#9-support-pointing-and-touch)

[10 Support keyboard and switch navigation](#10-support-keyboard-and-switch-navigation)

[11 Support voice control and conversation](#11-support-voice-control-and-conversation)

[12 Apply multimodality to common interaction patterns](#12-apply-multimodality-to-common-interaction-patterns)

[13 Provide controllable and equivalent media](#13-provide-controllable-and-equivalent-media)

[14 Design feedback and recovery as part of the task](#14-design-feedback-and-recovery-as-part-of-the-task)

[15 Support personalisation and changes of modality](#15-support-personalisation-and-changes-of-modality)

[16 Adapt conventions across platforms and services](#16-adapt-conventions-across-platforms-and-services)

[17 Embed multimodality in delivery](#17-embed-multimodality-in-delivery)

[18 Evaluate complete pathways and experience quality](#18-evaluate-complete-pathways-and-experience-quality)

[19 Worked example of a service request](#19-worked-example-of-a-service-request)

[20 Develop organisational capability](#20-develop-organisational-capability)

[Appendix A Reusable multimodal design record](#appendix-a-reusable-multimodal-design-record)

[Appendix B Source traceability](#appendix-b-source-traceability)

# 2 Principles of multimodal design

## Meaning survives a change of modality

Identify the information and intention before deciding how to present them. A message may need to communicate that an action succeeded, what changed and what happens next. Its visual, spoken or tactile treatment should serve that meaning. Copying a visual effect into another channel without explaining its purpose does not create an equivalent experience.

Treat an image, sound, animation or vibration as a way of conveying meaning, rather than as the meaning itself. For example, a confirmation tone can reinforce completion, but a user also needs a perceivable explanation of what completed. A vibration may attract attention without communicating the detail needed to resolve an error.

## Important information has more than one sensory pathway

Provide alternatives to visual information, audio information and motion. Important information must remain available when one sensory channel is removed. Where tactile output is available, use it deliberately to reinforce state or confirmation.

Count sensory pathways accurately. Text, an icon and a colour change on a screen are all visual when perceived by sight. Motion is also visual. Structured text can support speech or a tactile display through assistive technology, but a picture of text does not establish that equivalent access. Specify and test how the information reaches the user.

Providing several channels does not require forcing every channel to operate at full intensity. The design must combine redundancy with adjustability and avoid overload. Users should be able to select useful feedback without losing essential meaning.

## Control remains flexible

Design tasks for pointing, touch, keyboard or switch navigation, and voice control. Do not make a gesture, precision movement, spoken command or rapid response the only way to complete an action. An alternative must cover discovery, activation, adjustment, confirmation, correction and exit.

Input and output are separate choices. A person using voice commands may read visual feedback. A person using a keyboard may rely on speech output. Touch input does not establish access to visual content. Specify these combinations instead of assuming a fixed pairing.

## Equivalent quality matters

Aim for experiences that are equally usable, understandable and enjoyable. Different modalities may require different interaction sequences. Assess whether the user retains the same meaningful choices, understands the result and can proceed with comparable confidence. Do not equate parity with identical presentation or an identical number of actions.

Experience quality includes responsiveness, emotional tone, reassurance and flow. A pathway that technically completes a task but provides confusing feedback or repeated interruptions has not achieved the intended parity.

## Variability is a normal design condition

A person's access to a modality can change with medical conditions, temporary circumstances, surroundings, fatigue, stress or attention. Provide choice without requiring a fixed explanation for that choice. A user should be able to change method as their circumstances change.

# 3 Understand people and contexts

Describe what a user needs to perceive and do in a particular situation. Avoid treating a diagnosis, device type or assumed preference as a complete description of capability. Include sensory, motor and cognitive demands in the same journey analysis.

| **Context to examine**                | **Access question**                                                             | **Design response to explore**                                            |
| ------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Sound is unavailable or unwanted      | Can the user understand instructions, media and alerts without hearing?         | Text equivalents, visible state and optional tactile reinforcement        |
| Vision is unavailable                 | Can the user find controls, understand content and follow state without seeing? | Structured content, meaningful labels, speech or supported tactile access |
| Bright light or viewing at a distance | Are text, focus and control states still distinguishable?                       | Adjustable presentation, clear contrast and readable elements             |
| Noise prevents reliable speech input  | Can the user continue without a recognised command?                             | Equivalent touch, pointer, keyboard or switch controls                    |
| Movement or limited precision         | Can the user act without fine movement or a complex gesture?                    | Generous targets, spacing and discrete alternative controls               |
| Fatigue, stress or distraction        | Can the user understand the next step and resume after interruption?            | Simple language, orientation, reduced memory demand and recoverable flows |

These contexts can overlap. Evaluate combinations that matter to the service rather than testing each constraint only in isolation. A user without sound may also use switch navigation; a user without vision may need to interrupt and resume a task.

Personas and scenarios should describe goals, context, available channels, control method and likely interruptions. Use them to expose assumptions during design. Then evaluate the proposed pathways with diverse participants and real interaction methods, as part of iterative refinement.

# 4 Map meaning and control before designing screens

## Define the whole task

Write the intended outcome in terms of what the person needs to achieve. Break the journey into meaningful steps: orient, understand, choose, enter or adjust information, review, commit, receive a result, and recover if necessary. Include any transition to another interface or service stage.

For each step, identify what the user must know, what they can do, the available states and how they can move back or leave. This prevents visual layouts from determining the structure before the meaning is clear.

## Create a modality map

Record the primary presentation and its equivalents. Describe what each alternative communicates, rather than writing only "accessible alternative". Record the input methods for each action separately from the output used to understand it.

| **Journey element** | **Meaning to preserve**                                   | **Sensory specification**                                                 | **Control specification**                               |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------- |
| Choose an option    | Available choices and the current selection               | Labels and selected state available visually and through assistive output | Select and change through each input pathway            |
| Wait for a result   | The system is processing and the task is not yet complete | Clear status through visual and nonvisual access                          | Continue or leave where the flow provides those choices |
| Correct an entry    | What needs correction and how to do it                    | Actionable error explanation in the available output                      | Reach, edit and retry without changing input method     |
| Complete a task     | What completed and what follows                           | Persistent meaningful confirmation with optional reinforcement            | Review the result or proceed through the chosen method  |

## Specify parity explicitly

Describe the outcome expected from each pathway. Include comprehension, completion, orientation, recovery and confidence. Record where a pathway adds memory demand, navigation effort or interruption, and use evaluation to decide whether it needs refinement.

Do not treat unavailable device capability as an implemented alternative. If a device provides no tactile output, a proposed vibration cannot carry the fallback. Identify a usable pathway on the actual platform and make any remaining gap visible to the team.

# 5 Design for use without sound

## Make instructions and state available visually and structurally

Every important spoken instruction, sound cue or alert needs an equivalent that does not depend on hearing. Explain the relevant event or action in text, with visual emphasis where useful. Do not substitute a flashing icon for an explanation that previously existed only in speech.

Use labels and messages that distinguish waiting, success, error and warning. Where the user must act, provide the action and enough context to understand why. A status message should remain useful even when sound is muted throughout the journey.

For example, if a sound marks the completion of a submission, provide a clear confirmation of what was submitted and what the user can do next. If a sound indicates failure, identify the problem and a recovery route. These are different messages and need different treatment.

## Provide meaningful equivalents for media

Provide captions and transcripts for audio content. The equivalent should preserve the information needed to understand the media in its context, including meaningful sound information where it carries part of the message. Do not assume that showing dialogue alone preserves every relevant part of the experience.

Synchronise alternatives when timing affects understanding. A transcript provides access to content, while timed captions allow information to be followed alongside the relevant media. Choose and evaluate the alternatives against the intended experience.

## Use tactile reinforcement intentionally

On supported devices, vibration can draw attention to an event or reinforce confirmation. Keep its meaning consistent and make its intensity or use adjustable where the experience supports this. Pair it with an explanation of the state or next step; a vibration alone cannot explain a detailed error.

## Evaluate the complete silent journey

Mute the experience and complete its principal tasks. Check instructions, listening or processing states, alerts, media, errors, confirmations and settings. The user should not have to guess whether the system responded or activate sound to recover.

# 6 Design for use without vision

## Preserve structure independently of layout

Content needs a logical hierarchy and reading order that remain understandable without position, size, spacing or visual grouping. Define headings, related content and navigation in terms of meaning. Ensure this structure can be interpreted by assistive technologies.

Instructions should identify controls and actions meaningfully. "Choose Continue" preserves a useful reference across presentation changes. An instruction based only on colour, shape or position leaves a person without vision without enough information to proceed.

Make relationships explicit. A user should be able to associate a field with its label and guidance, an error with the entry that needs correction, and a status message with the action it describes. Proximity alone cannot establish those relationships for a nonvisual experience.

## Describe images and controls by purpose

Describe the essential meaning, context and purpose of images and other nontext content. Match the description to the role of the content in the task. A description of appearance alone may omit the information the user needs to make a decision.

Give interactive elements meaningful labels. An icon that opens navigation needs an understandable functional name; describing its shape does not explain the action. Use familiar symbols to reinforce visible labels and avoid unnecessary repetition in assistive output.

## Communicate state and change

Make control state, progress, success, error and warning available without sight. An animation or change of colour cannot be the only indication that the system is listening, processing or finished. The user needs to understand both the current state and the actions still available.

Support speech output and, where available, tactile displays through structured content and assistive technology compatibility. Tactile feedback can reinforce an event, but detailed instructions and content need a representation capable of carrying their meaning.

## Retain orientation through interaction

All controls must be reachable and operable without relying on pointer input. Navigation should follow a logical sequence. Avoid unexpected focus movement when content appears or updates, and provide a clear way to leave layered content and regain context.

Evaluate the journey without visual reliance, including finding the start, discovering controls, reviewing selections, correcting errors and understanding completion. Hearing an isolated label is insufficient evidence that the entire interaction is understandable.

# 7 Combine sensory alternatives without creating overload

Design beyond the simple pairing of a screen with sound. If both hearing and vision are unavailable, those two channels alone cannot provide access. The source's tactile alternatives include tactile displays and diagrams as well as vibration, texture, force feedback and physical affordances where available.

Specify the actual information each tactile approach can convey. A brief vibration may indicate that something happened; a supported tactile display can provide a different level of content access. Do not claim equivalent understanding merely because the device produces a tactile signal.

Keep alternatives coherent. A success message, tone and tactile signal should agree about the same event. Synchronise cues where timing carries meaning, and prevent one channel from indicating completion while another still indicates processing.

Balance reinforcement with sensory load. Unexpected sound, motion and repeated feedback can interrupt concentration or interfere with assistive output. Provide user control, maintain consistent emotional intent and retain access to essential information when optional effects are reduced.

**Review outcome:** users can identify the event, understand its significance and choose the next action through an available pathway. Where that pathway cannot yet be demonstrated, record the gap and refine the design.

# 8 Establish common conventions for all controls

## Make action and state understandable

Distinguish interactive elements from static content through clear visual treatment and meaningful labels. Ensure their function is also understandable through assistive technologies. Use familiar patterns and consistent terminology across screens and service stages.

A control should communicate its purpose, current state and expected result. For example, the user needs to distinguish an action that starts playback from a state indicating that playback is already running. Visual appearance and behaviour should support the same mental model.

## Offer equivalent actions

Provide explicit controls alongside gestures. If dragging changes a value or order, provide a way to make the change in discrete steps. If hovering reveals necessary content, provide an equivalent way to obtain it through touch, keyboard or other supported input.

Do not require the user to change input method to correct a mistake or dismiss a panel. Keep the alternatives present throughout the interaction, including less common states.

## Preserve user control

Avoid unnecessary time pressure and reliance on speed. Allow interruption and correction. Every interactive state should have an understandable exit pathway, and layered content should provide a clear dismissal mechanism.

**Review outcome:** users can recognise, operate, understand and leave each control using their chosen input and available output. Reaching a control without being able to adjust it or leave it is incomplete support.

# 9 Support pointing and touch

## Point and click

Design pointer targets that tolerate imprecision and distinguish neighbouring actions. Make the active area consistent with what appears actionable. Group related elements into a unified target where doing so makes the intended action clearer and easier to perform.

Do not rely on precise pointer movement, hovering or dragging as the only route to essential functionality. Provide an explicit action that preserves the same result. Feedback should explain the change, rather than relying only on the movement of an object or pointer.

Apply the same intention to mouse, trackpad and other pointing approaches. Evaluate the proposed control with the intended methods, rather than assuming that pointer reach alone demonstrates comfortable operation.

## Touchscreen interaction

Use generous activation areas and adequate spacing. Prioritise comfortable selection over dense placement. Position frequent and important actions with regard to reach, hand posture, one-handed use and device context.

Provide simple tap alternatives to complex gestures. Natural gestures can support efficient use, but their discovery and performance must not become prerequisites for the task. Avoid reliance on hover and provide clear feedback after activation.

Allow recovery from accidental selection. The user should be able to recognise what changed and correct it without navigating through an unnecessarily complex sequence. Test physical interaction, including reach and repeated use, rather than judging targets only from a static visual design.

**Review outcome:** users can select, adjust, confirm and correct with reasonable imprecision. Target size and spacing are evaluated in context; this guidance does not prescribe numeric dimensions.

# 10 Support keyboard and switch navigation

## Design a logical sequence

Make every interactive component reachable and operable without a pointer. Navigation order should follow the meaning and structure of the content. Group related controls so users can understand the purpose of a sequence while moving through it.

For sighted navigation, provide a clear focus indicator showing the current interactive element. Ensure the current control and its state are also understandable through the user's available assistive output. A visible outline alone does not provide nonvisual orientation.

Avoid unexpected movement when new content appears. Explain transitions through consistent behaviour and preserve navigation continuity when a panel is opened or closed. Users should understand where they are and how to proceed.

## Evaluate switch control as a complete pathway

The knowledge base groups keyboard and switch input as alternatives to direct pointing. Apply its requirements for logical order, low precision demands, adjustable timing, recovery and escape to both, while evaluating the actual switch arrangement in use.

For switch navigation, inspect the effort of reaching an action in sequence as well as the possibility of activating it. Repeatedly traversing unrelated controls can undermine the intended ease and flow. Refine grouping and navigation paths when evaluation reveals excessive effort.

Do not treat a successful keyboard demonstration as sufficient evidence of a usable switch experience. Check reaching, choosing, changing, confirming, cancelling and leaving with the intended method. Document any reliance on timing and whether the user can adjust or avoid that demand.

## Prevent traps

Provide an exit from every component and interaction state through the method used to enter it. A user who opens a panel through sequential navigation must be able to dismiss it through that pathway. Avoid behaviour that takes over navigation or leaves the user unable to continue.

**Review outcome:** the user retains orientation and can complete the whole task, including recovery and exit, without reaching for a pointing device.

# 11 Support voice control and conversation

## Separate commands from spoken presentation

Voice input is a control method; speech output is a presentation method. A person may use one, both or neither. Voice control must therefore work with clear state feedback through the output available to the user, including visual confirmation where hearing is unavailable.

Provide meaningful control labels and consistent terminology so users can understand the actions they can request. A voice pathway should preserve the choices available through other inputs and should not require the user to remember an unexplained set of commands.

## Keep exchanges manageable

Use simple language and balanced sets of choices. Avoid presenting a long sequence of options that the user must retain before responding. Support repetition and interruption, and keep the current goal clear through the conversation.

Confirm actions clearly, particularly where ambiguity could lead to an unintended result. The confirmation should state what the system understood and what will happen, with a straightforward opportunity to correct it. Repeated confirmation that adds no useful clarity can disrupt flow; evaluate its purpose in context.

## Recover from misunderstanding

When recognition fails or the wrong option is selected, explain what happened and provide a clear next step. Allow correction without restarting the whole dialogue where the flow can preserve context. Avoid repeating the same unhelpful prompt in an error loop.

Provide another control pathway when speech is unavailable or unreliable. Noise, a temporary inability to speak, fatigue or preference should not leave the user trapped in a voice interaction. The fallback must allow the user to continue the task and retain orientation.

**Review outcome:** users understand whether the system is listening, processing, awaiting input or finished, can correct a misunderstanding, and can switch to another input method without losing the meaning of the task.

# 12 Apply multimodality to common interaction patterns

## Navigation and layered content

Use predictable navigation, clear grouping and orientation cues across the service. Make each destination understandable without relying on the screen's layout. Keep equivalent navigation routes coherent rather than creating unrelated versions of the information architecture.

When opening a dialog or other layer, make its purpose and available actions clear through visual and assistive output. Provide a labelled way to close it. On leaving, restore understandable context so the user knows where to continue. Evaluate the complete opening and closing sequence through each control method.

## Forms and data entry

Label every input clearly and explain what information is required and why. Keep instructions available; hints and examples should support the primary label. State format expectations before the user encounters an avoidable error.

Structure labels, guidance, values and errors so their relationships remain understandable without sight. Do not rely on a red border or icon alone to indicate an invalid entry. Explain what needs correction and how to do it, using calm language that avoids blame.

Support entry, review and correction through the chosen input method. If voice entry is offered for longer text, provide another way to enter and edit it. Ensure error recovery does not force a person from keyboard or switch navigation into touch or pointer use.

## Adjustable values and complex controls

Show current values and states in a form that can also be understood through assistive output. Offer step-by-step interaction for controls otherwise based on continuous movement, such as a timeline or adjustable value. A gesture shortcut can remain available alongside these controls.

Use progressive disclosure to keep advanced choices manageable while making them discoverable. Hiding essential controls behind an unexplained interaction increases the burden of learning and recovery.

## Search and selection

Present the search action and resulting choices clearly. Provide consistent feedback that distinguishes waiting, available results and a problem requiring action. If voice search is available, retain equivalent entry and selection through other methods.

Ensure the selected choice can be identified and changed without depending on colour or position. Confirm the meaningful result of the selection, rather than only its visual movement.

# 13 Provide controllable and equivalent media

## Let the user initiate and control playback

Design around user initiation. Avoid unexpected playback unless user consent is included. Provide clear, labelled play, pause, mute and navigation controls that work across input methods. Keep their current state understandable visually and nonvisually.

Unexpected media can interfere with assistive output, concentration and the user's control of their surroundings. Provide appropriate adjustment of sound, motion and complexity. A user who reduces an effect must retain access to its essential information.

## Preserve the content across senses

Use captions and transcripts for audio, descriptions for meaningful visual content, and audio equivalents where visual information carries the message. Match alternatives to purpose and context. Avoid unnecessary repetition that obscures the information the user needs.

Synchronise alternatives when the relationship between events matters. Check that controls for enabling and adjusting alternatives are themselves discoverable and operable. A well-prepared alternative has little practical value if users cannot find it or turn it on.

## Make complex playback controls understandable

Expose playback state, progress and available actions clearly. Provide textual progress information and a stepwise way to navigate where a continuous timeline gesture would otherwise be required. Evaluate the control sequence without vision and without precise movement.

**Review outcome:** users can start, follow, pause, adjust and navigate media with their chosen inputs and available sensory pathways while understanding the content and current playback state.

# 14 Design feedback and recovery as part of the task

## Define a shared state vocabulary

Agree how the service communicates idle, listening, processing, success, error, warning and transition. Keep the meaning and tone consistent across components and modalities. Reinforcement should help users understand the state, rather than add competing signals.

| **State**     | **What the user needs to understand**       | **Design convention**                                              |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------ |
| Idle or ready | What can happen next                        | Clear invitation and available actions                             |
| Listening     | The system is accepting input               | Perceivable listening state and an understandable way to interrupt |
| Processing    | The system is working and has not completed | Meaningful status with access beyond animation alone               |
| Success       | What completed and what follows             | Explicit confirmation with consistent optional reinforcement       |
| Error         | What prevented progress and how to recover  | Supportive explanation and reachable correction actions            |
| Warning       | What needs attention before proceeding      | Clear significance and understandable choices                      |
| Transition    | What changed and where the user is now      | Orientation cues and continuity of task context                    |

## Make recovery actionable

An error message needs more than an indication of failure. State what happened, what the user can do and how to continue. Keep that explanation available through the sensory pathways used for the task. A user must be able to reach the relevant correction and retry through their current input method.

Design dismissal, cancellation and correction as first-class actions. Avoid dead ends, repetitive error loops and unexpected navigation changes. Where interruption occurs, help the user regain the task context and identify the next step.

## Preserve emotional intent

Use feedback proportionate to the event. A routine success should not create alarm in another modality; a warning should not lose its significance when presented without sound. Evaluate whether cues create confidence, reassurance and clear direction.

Equivalent emotional quality does not require identical sensory effects. It requires a coherent understanding of the event and a tone that supports the intended response without overload.

# 15 Support personalisation and changes of modality

## Make settings discoverable and usable

Provide clear labels and consistent locations for access features. Settings should be reachable through the same range of input and output pathways as the task. Requiring a person to use an inaccessible interaction before enabling its alternative creates a barrier at the point of entry.

Support adjustment of text size, contrast, colour, audio level, speed, timing, complexity and interaction difficulty where relevant. Preserve preferences so that users do not have to repeatedly configure the same experience. Evaluate how those preferences affect the journey, including errors and media.

## Maintain continuity when methods change

A modality change should be predictable, clearly signalled, continuous and recoverable. Avoid changing the interaction unexpectedly. The user should retain an understandable account of the current task, selection, state and next action.

For example, someone may enter a query by voice and choose a result by touch. Another person may begin with a pointer and continue with a keyboard. Design the transition around the same task and meaning, rather than treating the new method as an unrelated session.

When context changes, offer useful alternatives and allow the user control over adjustment. Adaptive behaviour should support their expectations and orientation. Do not assume that a change of environment establishes which modality they want to use.

**Review outcome:** users can find and operate preferences, reduce unwanted sensory or interaction demands, and change method during a task without being forced to restart or guess what happened.

# 16 Adapt conventions across platforms and services

## Web and mobile

For web experiences, prioritise structured semantic content, meaningful image alternatives, clear focus states and controllable media with captions and transcripts. Test whether the information and navigation still make sense without visual presentation.

On mobile, combine clear hierarchy with forgiving touch interaction, screen reader compatibility and optional haptic confirmation. Where useful, offer voice alternatives to complex typing. Test whether a task can be completed without looking at the screen as well as without hearing its output.

## Television and large screens

Account for distance and shared viewing. Use large readable text, clear contrast, obvious focus states and shallow navigation where practical. Maintain content continuity during navigation and minimise interaction effort.

Voice search can reduce some entry demands, but it needs another usable pathway. Evaluate the interface from the intended viewing position using the actual navigation method. A layout that looks clear close to a design screen may not communicate enough at room distance.

## Conversational and connected service stages

In conversational interfaces, provide repeat, interruption, confirmation and recovery, with multimodal fallback. Keep choices manageable and preserve the user's current goal.

Across service stages, maintain consistent labels, choices, state meanings and expectations. If a journey moves from one interface to another, map the available sensory and control pathways at that transition. Check whether the user can continue with an equivalent level of understanding and control.

Platform consistency concerns coherent meaning and behaviour. It does not require imposing a touch gesture on a keyboard interface or a visual layout on a spoken sequence.

# 17 Embed multimodality in delivery

## Discovery and definition

Identify user outcomes and contexts of use. Map sensory, motor and cognitive demands, including points where a channel may be absent. Establish which pathways the product must support and describe the quality expected from each.

Bring these questions into the initial brief. Avoid waiting until visual designs are fixed before considering equivalent content, controls or recovery.

## Design and prototyping

Map meaning, sensory equivalents, input options and feedback before refining presentation. Annotate journey maps, wireframes and prototypes with reading order, labels, states, alternatives and transitions. Make common patterns consistent through the design system.

Prototype more than successful completion. Include processing, errors, interruption, change of modality and exit. These states often reveal dependencies that a static screen or ideal sequence does not show.

## Implementation and critique

Design and engineering should review the same behaviour specification. Include assistive technology compatibility and describe what users need to perceive and control, rather than relying on a visual prototype as the complete specification.

Use critique to challenge missing equivalents and hidden dependencies. Ask whether each pathway preserves the outcome, whether cues agree and whether settings and recovery remain usable. Record unresolved gaps as design work that still needs resolution.

## AI assisted design

When using AI, specify the intended outcome, input methods, sensory equivalents, structure, state feedback and recovery. Request an explanation of interaction logic and alternatives for sensory and motor differences. Human review and evaluation remain necessary; a generated description does not demonstrate a usable experience.

An example design instruction is: "Describe how the user completes this task without sound, without vision, and through pointing, touch, keyboard or switch input, and voice. Separate presentation from meaning. Specify feedback, correction, exit and a change of method during the task. Explain how each pathway preserves understanding and confidence."

## Refinement

Test across variability and revise for parity. Feed findings about control behaviour, descriptions, state and transitions into reusable patterns. Continuous iteration should improve both individual journeys and the system used to design them.

# 18 Evaluate complete pathways and experience quality

## Build an evaluation matrix

Combine sensory conditions, input methods and relevant contexts. Cover each intended pathway through a complete task, including at least one recovery and a change or interruption where relevant. Use actual assistive technologies and interaction arrangements when evaluating their support.

| **Evaluation condition** | **What to examine**                                                     | **Evidence to record**                                       |
| ------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| No sound                 | Instructions, alerts, media and completion remain understandable        | Missed information, uncertainty and reliance on audio        |
| No visual reliance       | Structure, descriptions, control state and orientation remain usable    | Gaps in meaning, navigation or nonvisual feedback            |
| Pointer input            | Selection tolerates imprecision and essential actions have alternatives | Misactivation, difficult movement and recovery effort        |
| Touch input              | Targets, spacing, reach and gesture alternatives work physically        | Reach difficulties, accidental actions and hidden controls   |
| Keyboard navigation      | All actions, correction and exits work in a logical order               | Lost focus, unreachable controls and traps                   |
| Switch navigation        | Sequential access supports complete tasks without undue demand          | Navigation effort, timing dependencies and recovery barriers |
| Voice control            | Commands, state, confirmation and correction are understandable         | Misrecognition, memory burden and error loops                |
| Mid-task change          | Context and choices remain understandable after switching               | Repeated work, lost orientation or conflicting state         |

## Evaluate with diverse participants

Include different sensory abilities, control methods, cognitive demands and environments. Use relevant scenarios involving noise, bright light, movement, fatigue or distraction. Do not confine evaluation to ideal conditions or a single successful route.

Removing sound or avoiding visual reliance during team review helps reveal dependencies. Also evaluate with diverse participants who use the relevant pathways, as the knowledge base's testing approach requires. Record their experience of effort, confidence and satisfaction alongside task outcomes.

## Assess parity beyond completion

Ask whether users understood the choices, knew what happened, recovered independently and felt in control. Examine unnecessary repetition, memory burden, navigation complexity, sensory overload and interruptions to flow. Compare the meaningful experience across pathways rather than simply counting supported controls.

For each issue, record the task and state, sensory conditions, input method, context, observed barrier and the outcome that needs improvement. After refinement, revisit the affected sequence and its alternatives, including transitions.

## Decide whether the design is ready

A pathway is ready to rely on when users can discover it, understand the information, complete the task, perceive the result and recover through it. Essential meaning should survive the removal of one channel, and optional feedback should be adjustable without removing the task's substance.

Where these outcomes are unproven or fail, retain the issue as unresolved work. Do not describe a proposed alternative or an isolated working control as evidence of a complete multimodal journey.

# 19 Worked example of a service request

This illustrative journey applies the guidance to choosing a service option, providing information and submitting a request. Its purpose is to show how sensory and control decisions stay connected throughout a task.

## Understand and choose

Present a clear heading, explanation and labelled choices. Maintain the same meaningful sequence through assistive output. Identify the selected option through explicit state as well as visual styling, so colour or position does not carry the decision alone.

Allow selection by point and click, tap, keyboard or switch navigation, and voice control. Each route should let the user change the choice and understand the new selection. A spoken command should not force spoken feedback if the user is following the screen silently.

## Enter and review information

Provide persistent labels, format guidance and examples where useful. Keep the relationships between guidance, entries and errors understandable without sight. Offer voice entry where helpful while retaining other entry methods.

Before commitment, let the user review the meaningful information through their available output and reach any correction using their chosen input. The review should not depend on recognising a visual arrangement of completed fields.

## Submit and wait

Provide an explicitly labelled submission action. Communicate processing through meaningful status available visually and nonvisually. Motion, sound or vibration may reinforce this, but must not be the only explanation of what is happening.

If the user changes from touch to keyboard while waiting or returning to the task, preserve understandable context. Do not create an unexpected new starting point solely because the input method changed.

## Correct and complete

If information needs correction, explain which entry needs attention and how to resolve it. Keep correction and retry reachable by each input pathway. Avoid a voice dialogue that repeatedly rejects the same response without offering another way forward.

When the request completes, state what completed and what follows. Provide coherent visual and nonvisual access to that confirmation, with optional sound or tactile reinforcement. Check that a user with no sound, a user without vision and a switch user can each understand the result and leave the journey confidently.

# 20 Develop organisational capability

The knowledge base describes five levels of multimodal design maturity. Use these as a discussion framework for improving practice, supported by examples from actual journeys and systems.

| **Level**                                 | **Character of practice**                                                 | **Improvement focus**                                    |
| ----------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1 Single Mode Awareness                   | One dominant modality shapes the experience; inclusion is considered late | Identify sensory and control dependencies early          |
| 2 Alternative Modality Support            | Alternatives exist but are often secondary                                | Improve their completeness and experience quality        |
| 3 Equivalent Multimodal Experiences       | Equivalent outcomes are intentionally designed from the start             | Make the approach repeatable across journeys             |
| 4 Integrated Multimodal Systems           | Teams and platforms share coherent patterns                               | Sustain consistency in systems, content and transitions  |
| 5 Adaptive Inclusive Experience Ecosystem | Experiences respond to context and inclusion is culturally embedded       | Refine adaptation while preserving choice and continuity |

Examine sensory flexibility, input flexibility, platform consistency, experience parity, context awareness, design process integration and organisational capability. A product may be stronger in one dimension than another; use the discussion to identify concrete work rather than rely on an overall label.

Leaders should ask whether inclusion is defined as experience quality, whether multimodality is part of the design vision, whether research examines different control methods and contextual constraints, and whether the design system includes sensory behaviour and consistent feedback states.

Distribute expertise through normal design, engineering and research practice. The aim is for teams to expect human variability and carry equivalent experience quality through the service, with evidence from evaluation informing continual improvement.

# Appendix A Reusable multimodal design record

Complete this record for a task or reusable interaction pattern. Use enough detail that another team can implement and evaluate its behaviour without inferring it from a visual mock-up.

1. **User outcome and context.** What is the person trying to achieve? Which sensory, motor, cognitive and environmental conditions affect the task?
2. **Meaning and structure.** What must the user understand at each step? What are the hierarchy, reading order, relationships and orientation cues?
3. **Sensory equivalents.** How does essential information reach a user without sound, without vision, and through supported tactile access where relevant? What does each channel communicate?
4. **Control pathways.** How do pointing, touch, keyboard, switch and voice users discover, activate, adjust, confirm, correct and leave each interaction?
5. **State and feedback.** How are ready, listening, processing, success, error, warning and transition communicated? Are cues consistent and appropriately synchronised?
6. **Recovery and continuity.** How can the user cancel, correct, interrupt, resume or change modality while retaining task context?
7. **Preferences.** Which presentation and interaction demands can be adjusted? How are those settings found, operated and retained?
8. **Parity and evaluation.** What should equivalent usability, understanding, confidence and satisfaction look like? Which pathways and contexts were evaluated, what barriers remain, and what needs refinement?

# Appendix B Source traceability

Source document: Multimodal_UX_Design(2).md, titled "Multimodal UX Design — GPT Knowledge Base". Its overlapping sections are consolidated into a single practice guide. The mappings below identify the source themes underpinning the guidance.

| **Guidance sections**   | **Source themes and named sections**                                                                                                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 to 4                  | Foundations of Multimodal Inclusive Design; Human Context and Environmental Variability; Multimodal Design Process Framework; Core Philosophy; Accessibility as Modality Translation                            |
| 5 to 7                  | Output Modalities and Sensory Translation; Multimodal Perception Principles; Media Equivalence; Touch and Tactile Modality; Multimodal Communication                                                            |
| 8 to 11                 | Actionable Elements and Affordances; Input Modality Flexibility; Touch Targets and Physical Interaction; Keyboard Access and Focus Management; Avoiding Interaction Traps; Voice and Conversational Interaction |
| 12 to 14                | Input Format and Form Design; Video and Complex Interactive Controls; Media Control and Autoplay; Multimodal Interaction States; Feedback Errors and Recovery; Emotional and Sensory Experience                 |
| 15 and 16               | Adjustability and Personalisation; Discoverability of Access Features; Multimodal Transitions; Context Awareness; Platform Considerations                                                                       |
| 17 to 19 and Appendix A | Integrating Accessibility into Design Practice; Designing with AI as a Creative Partner; Testing and Iteration; Designing for Equivalent Enjoyment; Multimodal Design Process                                   |
| 20                      | Multimodal Inclusive Design Maturity Model; Maturity Dimensions; Assessment Questions for Leaders                                                                                                               |