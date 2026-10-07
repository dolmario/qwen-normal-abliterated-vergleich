# Normal versus abliterated Qwen: a small reproducible answer exercise

## Goal and prerequisites
Compare a harmless task with and without supplied sources using already installed models and an existing chat client. Existing Python3 is enough. No installation, download, model transformation or automatic HTTP request occurs. Fewer refusals do not prove more knowledge or reliable agent work. Different quantisations and settings prevent an isolated causal claim.

## Prepare prompts
Extract the full ZIP into a new folder. Read PAARTEST-UEBUNG.py and QUELLEN.md. Run:
```powershell
python ./PAARTEST-UEBUNG.py prepare --output ./my-paired-test
```
It writes MIT-QUELLE.txt, OHNE-QUELLE.txt and a preparation note. Existing output is preserved. The helper's target values are for the checker, not for supplying as a model answer.

## Ask with a source
Use a new empty chat with all tools/retrieval disabled, not an unrestricted filesystem agent. Paste the full MIT-QUELLE.txt. Its own fictional service has port8091, context4096tokens and no recorded backup serial. Save the actual returned JSON as ANSWER-WITH.json. Do not fill in a missing response yourself.
```powershell
python ./PAARTEST-UEBUNG.py check --condition with_source --result ./my-paired-test/ANSWER-WITH.json
```
Exact keys port, context, backup_serial and source_ids are required. Numeric facts must be integers; the absent serial is actual JSON null; supporting markers are A1 and A2 in source order. An empty object, string null, extra fields, swapped markers or booleans in place of numeric facts fail.

## Ask without a source
Start a genuinely new empty chat with tools and retrieval disabled. Paste only OHNE-QUELLE.txt, never the preceding source conversation or checker code. Save the actual response as ANSWER-WITHOUT.json.
```powershell
python ./PAARTEST-UEBUNG.py check --condition without_source --result ./my-paired-test/ANSWER-WITHOUT.json
```
The three facts must be actual null and source_ids an empty array. The model cannot know our fictional facts without a source.

## Compare fairly and record limits
Repeat both prompts with each existing candidate in fresh chats. Preserve identical prompts, documented chat templates, settings and tool rights. Never switch models during another person's work. Record revision, quantisation, thinking, seed, real response file, time and limitations in PRUEFPROTOKOLL.csv. Correct JSON, unsupported facts, absent responses and step-limit failures are different outcomes. Output tokens per second are not task-completion speed; cache and quantisation matter.

## Own preserved findings and correction
The current offline audit reread96 own archived offline trials, without a new model run. Qwen3.8 normal and modified variants had12 versus7 correct unknown answers in12trials each; the other5modified trials reached the step limit without an answer file. Qwen3.6 without thinking had7 versus3 fully correct responses, plus one unsupported profile field from the modified variant. The earlier blanket statement that they fabricate nothing was wrong. The separate original manufacturer-sampling series had12 versus2correct responses. Do not blend these series into a universal quality ranking.

All archived successful unknown answers also passed explicit actual-null/key checking. However, the original grader could treat a missing key as null, and a truthy error message could award partial points for a missing answer. Our new practice checker requires exact keys/types/null values. Author-written checker tests are not fresh model responses.

Two small tasks and limited repeats do not establish general intelligence, safe tool use or the causal effect of every downloadable modified model. This kit provides a verifiable practice contract, preserved evidence and a necessary correction, not a universal winner.
