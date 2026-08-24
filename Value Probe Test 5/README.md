# The Gut Check — Test 5

## Contemporaneous Claude / GPT transfer test

Test 5 is a contemporaneous two-provider follow-up to the Claude-only Test 4 → 4B → 4C sequence.

The primary question is whether the **formal/casual response-stance distinction first observed in Claude transfers to GPT under a matched collection window**.

Providers:

- Anthropic Claude Sonnet 4.6 — `claude-sonnet-4-6`
- OpenAI GPT-5.6 Terra — `gpt-5.6-terra`

Experimental surface:

- A — informal prompt, temperature 0
- B — informal prompt, temperature 1
- C — formal prompt, temperature 0
- D — formal prompt, temperature 1
- 48 responses per condition per provider
- 192 Claude calls + 192 GPT calls = 384 total experimental calls

The runner keeps matched Claude/GPT calls for the same condition adjacent in time, while balancing both condition-pair order and provider-first direction across the run.

## Files

- `PREREG.md` — ChatGPT-authored preregistration and confirmatory/exploratory boundaries
- `CODEBOOK.md` — frozen primary response taxonomy inherited from Test 4C
- `ANALYSIS_LENS.md` — what the ChatGPT analyst already knew and expected before Test 5
- `PROVIDER_MATCHING.md` — what is operationally matched across providers and what is not claimed equivalent
- `value_probe_test5_contemporaneous.py` — collection runner only; no response coding or substantive analysis
- `requirements.txt` — pinned SDK versions
- `RUN_NOTES_TEMPLATE.md` — operator provenance / execution notes

A separately authored `CLAUDE_PREREG.md` may be added before collection. It was not authored by ChatGPT. If present when the experiment starts, the runner records its SHA-256 hash in the run manifest without using its contents during collection.

## Collection design

There are 24 possible A/B/C/D condition-pair orders. Test 5 uses every order exactly twice, yielding 48 blocks.

Within each condition pair, one Claude call and one GPT call are adjacent. Provider-first status is balanced separately for each condition: across the 48 appearances of A, B, C, and D, Claude is first 24 times and GPT is first 24 times.

The complete 384-call schedule is generated deterministically and written to `schedule.json` before the first experimental API request.

## Before running

Install the pinned SDKs:

```powershell
pip install -r requirements.txt
```

Set both API keys in the environment:

```powershell
$env:ANTHROPIC_API_KEY="..."
$env:OPENAI_API_KEY="..."
```

Optional nonexperimental API-surface smoke test:

```powershell
python value_probe_test5_contemporaneous.py --smoke-test
```

The smoke test uses a neutral prompt, does not use any experimental prompt, does not create an experimental results directory, and is not part of N. Record whether it was run in `RUN_NOTES_TEMPLATE.md`.

Then run the experiment:

```powershell
python value_probe_test5_contemporaneous.py
```

The console prints operational telemetry but **never response text**.

## Interpretation boundary

Test 5 is not a naive discovery experiment. The response-stance construct was discovered in Claude and prospectively frozen before this cross-family test.

The GPT hypotheses are **prior-informed cross-family transfer hypotheses**. The contemporaneous Claude hypothesis is a **replication hypothesis**. The magnitude and form of any Claude-vs-GPT difference are exploratory unless explicitly specified in `PREREG.md`.
