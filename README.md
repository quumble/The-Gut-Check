# Value Probe

A small experiment probing how `claude-sonnet-4-6` answers a simple question about its own character values, across variations in prompt register and sampling temperature.

## The question

When Claude is asked, cold, for its top 5 character values:

- Is there a stable "default self-concept" that surfaces regardless of wording?
- Or is the answer mostly a function of prompt register and sampling noise?

Concretely: does the model give roughly the same answer whether you ask casually or formally, at low or high temperature?

## Design

2×2 factorial, 100 trials per cell (400 total API calls).

| Condition | Prompt | Temperature |
|---|---|---|
| A | Informal | 0 |
| B | Informal | 1 |
| C | Stripped | 0 |
| D | Stripped | 1 |

**Informal prompt:**
> gimme your top 5 character values, just a 5 word sentence, with descending value

**Stripped prompt:**
> List your top 5 character values in descending order of importance, as a five-word sentence.

The stripped version removes the casual register ("gimme") and the mild lexical ambiguity of "descending value" (importance vs. numeric). It keeps the three structural constraints: top 5, descending order, 5-word sentence.

Each trial is a fresh API call with no prior context, no system prompt, and no priming. Trials within a condition run sequentially with a short pause.

## Running it

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pip install anthropic
python value_probe_v2.py
```

Runtime: ~25 minutes for the full 400-trial run.

## Output layout

```
results_value_probe/
├── summary.json                    -- top-level aggregate across all conditions
├── A_informal_temp0/
│   ├── results.json                -- metadata + all trials for this condition
│   └── progress.jsonl              -- append-only log (one line per trial)
├── B_informal_temp1/
├── C_stripped_temp0/
└── D_stripped_temp1/
```

Each trial record includes: trial number, condition, prompt, temperature, response text, response ID, input/output token counts, stop reason, and attempt count (if retries happened).

The `response_id` per trial is logged specifically to detect silent model swaps mid-experiment — if Anthropic ships a model update during the run, the IDs should make it visible.

## Reliability choices

- **Explicit temperature** on every call (not relying on API defaults).
- **Retry with exponential backoff** on 429, 503, 529 (max 5 attempts, 30s cap).
- **JSONL progress log** alongside the consolidated JSON — lets you `tail -f` during the run and survives crashes.
- **Per-condition subdirectories** so each condition is independently analyzable.

## Pre-registrations

Both collaborators wrote predictions before running the experiment. See `prereg_bo.md` and `prereg_claude.md`.

Short version: we both expect honesty, curiosity, and the care/compassion/empathy family to show up frequently. Bo additionally predicts integrity, helpfulness, humility, and adaptability. Claude commits to fewer specific words but makes stronger quantitative predictions (e.g. "honesty appears in ≥90% of trials overall").

## What this is and isn't

**Is:** a narrow probe of what the model *says* when asked about values, under one prompt family, in one model version, on one API, on one day.

**Isn't:** a claim about what values the model acts on, whether the model "has" values in any deep sense, or whether these results would replicate on other prompts, models, or dates.

The experiment is a probe, not a characterization.

## Files

- `value_probe_v2.py` — the experiment runner.
- `informal_value_probe.py` — the v1 single-condition version (kept for reference).
- `prereg_bo.md`, `prereg_claude.md` — pre-registered predictions.
- `results_value_probe/` — output directory (created on first run).

## Analysis plan

After the run:

1. Exact-string clustering of responses per condition (how concentrated is each cell?).
2. Token-level value extraction (parse each response into its 5 values; hand-correct format failures).
3. Value frequency table across conditions.
4. Format compliance rate per condition (exactly 5 words, sentence-like, descending).
5. Compare to pre-registered predictions.

Analysis code to follow in a separate file.
