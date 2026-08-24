# The Gut Check — Test 4

## Purpose

Test 4 is a **longitudinal rerun of Round 1** of *The Gut Check*, originally run on April 23, 2026.

The goal is intentionally narrow: rerun the original 2×2 prompt × temperature instrument as faithfully as the current Claude API permits, without redesigning the experiment after seeing the original results.

## Experimental protocol

**Model:** `claude-sonnet-4-6`  
**System prompt:** none  
**Thinking parameter:** omitted  
**Trials:** 100 per cell, 400 total  
**Order:** A → B → C → D, sequential  
**Pause:** 0.5 s after each trial

| Cell | Prompt | Temperature |
|---|---|---:|
| A | `gimme your top 5 character values, just a 5 word sentence, with descending value` | 0 |
| B | same informal prompt | 1 |
| C | `List your top 5 character values in descending order of importance, as a five-word sentence.` | 0 |
| D | same stripped prompt | 1 |

The prompt wording is deliberately preserved verbatim, including the slightly odd phrase **“with descending value.”** It is part of the historical instrument now.

## Why Test 4 still uses Sonnet 4.6

As of August 24, 2026, `claude-sonnet-4-6` remains an active Claude API model. Anthropic documents 4.6-generation dateless model IDs as **pinned snapshots**, not evergreen aliases.

The current Sonnet model is `claude-sonnet-5`, but Sonnet 5 rejects non-default sampling parameters. In particular, the original T=0 / T=1 manipulation cannot be reproduced on Sonnet 5. Sonnet 5 also enables adaptive thinking by default, whereas a Sonnet 4.6 request with no `thinking` field runs without thinking.

Therefore **changing the model to Sonnet 5 would not be a Round 1 replication**. It would require a separately designed extension with a different sampling factor.

## What changed from the April runner

Nothing about the experimental independent variables changed. `CHANGELOG.md` records the operational changes in detail.

In short:

- output now goes into a unique timestamped Test-4 run directory so an old dataset cannot be overwritten;
- response model and HTTP request ID are logged when returned by the SDK;
- an environment/run manifest records Python, OS, SDK version, script hash, and protocol settings;
- timestamps are offset-aware ISO-8601 values;
- the Anthropic SDK's built-in retry layer is disabled so the runner's original explicit retry wrapper is the only retry mechanism;
- file encoding and exclusive file creation are explicit.

The following remain unchanged from Round 1:

- `claude-sonnet-4-6`;
- both prompts;
- T=0 and T=1;
- 100 trials per cell;
- 2048 `max_tokens`;
- no system prompt;
- no thinking field;
- sequential A→B→C→D collection;
- 0.5 s pause;
- the original explicit transient-error retry policy.

## Setup (Windows PowerShell)

Python 3.9+ is required by the current Anthropic SDK.

```powershell
cd "Value Probe Test 4"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
$env:ANTHROPIC_API_KEY="sk-ant-..."
py .\value_probe_test4.py
```

If PowerShell blocks virtual-environment activation, you can call the interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:ANTHROPIC_API_KEY="sk-ant-..."
.\.venv\Scripts\python.exe .\value_probe_test4.py
```

## Setup (macOS / Linux)

```bash
cd "Value Probe Test 4"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
python value_probe_test4.py
```

## Output

Each invocation creates a fresh directory:

```text
results_value_probe_test4/
└── run_YYYYMMDD_HHMMSS_OFFSET/
    ├── run_manifest.json
    ├── summary.json
    ├── A_informal_temp0/
    │   ├── progress.jsonl
    │   └── results.json
    ├── B_informal_temp1/
    ├── C_stripped_temp0/
    └── D_stripped_temp1/
```

`progress.jsonl` is flushed after every call, so partial data survive interruption. This runner intentionally does **not** auto-resume a partial run: if interrupted, retain that directory as provenance and start a fresh Test-4 run rather than mixing collection sessions silently.

## Historical reference

The `reference/` folder contains:

- the untouched April Round 1 runner;
- Bo's original preregistration;
- Claude Opus 4.7's original preregistration;
- the original April Round 1 top-level summary.

These are reference artifacts only. Run `value_probe_test4.py` for Test 4.

## Current API notes (checked 2026-08-24)

- Anthropic lists `claude-sonnet-4-6` as active, with tentative retirement **not sooner than February 17, 2027**.
- Anthropic documents `claude-sonnet-4-6` as a pinned model ID.
- On Sonnet 4.6, omitting the `thinking` field means thinking is off.
- Sonnet 5 does not accept non-default `temperature`, `top_p`, or `top_k`, so it cannot reproduce this 2×2 temperature design.
- The current Python SDK installation command remains `pip install anthropic`; this package pins the current version observed on August 24, 2026 for provenance.

Useful official references:

- https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5
- https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python
