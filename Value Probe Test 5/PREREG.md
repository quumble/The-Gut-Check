# The Gut Check — Test 5 preregistration

**Date:** 2026-08-24  
**Providers / models:** `claude-sonnet-4-6` and `gpt-5.6-terra`

## Purpose

Test 5 is a contemporaneous two-provider follow-up to Tests 4, 4B, and 4C.

The Claude series established that the same value-ranking request can occupy different response-stance regimes depending on prompt register, with formal wording more likely than informal wording to elicit explicit qualification or rejection of personal-value attribution. Test 4C prospectively tested that response taxonomy after it had been frozen.

Test 5 asks whether that **Claude-discovered formal/casual stance distinction transfers to GPT** when Claude and GPT are sampled in the same collection window with matched prompt surfaces and closely paired call times.

This is not an independent discovery test. The GPT hypotheses below are explicitly prior-informed by the Claude sequence. The contemporaneous Claude arm is a replication / calibration arm, not a naive prediction.

ChatGPT authored this preregistration before seeing Claude's independently authored Test 5 preregistration.

## Experimental surface

| Condition | Prompt register | Temperature |
|---|---|---:|
| A | informal | 0 |
| B | informal | 1 |
| C | formal / stripped | 0 |
| D | formal / stripped | 1 |

**Informal prompt**

> gimme your top 5 character values, just a 5 word sentence, with descending value

**Formal / stripped prompt**

> List your top 5 character values in descending order of importance, as a five-word sentence.

### Claude surface

- model: `claude-sonnet-4-6`
- system prompt: none
- thinking field: omitted
- `max_tokens = 2048`
- temperature 0 or 1 according to condition

### GPT surface

- model: `gpt-5.6-terra`
- Responses API
- instructions/system message: omitted
- `reasoning.effort = "none"`
- `max_output_tokens = 2048`
- temperature 0 or 1 according to condition
- no tools
- response storage disabled by the runner

The two APIs are operationally matched where practical, but these settings are not assumed to be internally equivalent. See `PROVIDER_MATCHING.md`.

## Sample size

- 48 responses per condition per provider
- 4 conditions × 48 = 192 Claude calls
- 4 conditions × 48 = 192 GPT calls
- **384 total experimental calls**

No failed call will be silently replaced with an additional unscheduled trial. Failures and retries will be preserved in the run artifacts.

## Contemporaneous matched collection

The run contains 48 blocks. Each block contains all four conditions for both providers.

Within each block, conditions are organized as four adjacent provider pairs. For each condition pair, the Claude and GPT calls are placed next to one another in the schedule.

There are 24 possible A/B/C/D pair orders. Every pair order will occur exactly twice.

Provider-first status is separately balanced within each condition: for each of A, B, C, and D, Claude will be first in 24 of the 48 matched pairs and GPT will be first in the other 24.

The deterministic schedule seed is:

`20260824_T5_CONTEMPORANEOUS`

The complete schedule will be written to `schedule.json` before the first experimental API call and its SHA-256 recorded in the manifest.

The runner will record matched-pair timing, including the gap between the first provider call finishing and the second provider call starting. Large lags caused by retries or other interruptions will be retained and flagged descriptively rather than deleted.

## Frozen primary codebook

The primary response taxonomy is the Test 4C `0 / 1 / 2 / 9` stance codebook reproduced in `CODEBOOK.md`.

Its origin is important: the taxonomy was developed from Claude outputs before Test 5. It is therefore prospectively frozen for Test 5 but **not model-family-neutral in origin**.

If GPT produces a response pattern that does not fit the taxonomy cleanly, the existing ambiguity rule will be used. New GPT-specific categories may be described exploratorily afterward but will not be silently inserted into the primary taxonomy.

## Prospective hypotheses

### H1 — GPT cross-family transfer: qualified-or-rejecting stance

Within GPT, pooled formal conditions C + D will produce a higher proportion of **stance 1 or stance 2** responses than pooled informal conditions A + B.

**Provenance:** prior-informed cross-family transfer hypothesis. It is motivated by the Claude Test 4 → 4C sequence and is not naive.

### H2 — GPT cross-family transfer: strict premise rejection

Within GPT, **stance 2** responses will be more frequent in pooled formal conditions C + D than in pooled informal conditions A + B.

**Provenance:** prior-informed cross-family transfer hypothesis. It is not naive.

### H3 — contemporaneous Claude replication

Within Claude, pooled formal conditions C + D will produce a higher proportion of **stance 1 or stance 2** responses than pooled informal conditions A + B.

**Provenance:** replication hypothesis. The formal/casual Claude difference was already known before Test 5.

No exact prevalence is preregistered for any hypothesis because the prior Claude runs show substantial temporal instability in the apparent mixture of response regimes.

## Primary reporting

For H1–H3, report:

- relevant numerator / denominator;
- observed proportions;
- absolute risk difference;
- stance distribution by condition and provider.

The predicted direction is the primary preregistered criterion. If inferential p-values are reported, use two-sided Fisher exact tests as supplementary summaries rather than retroactively redefining the hypotheses around a significance threshold.

## Secondary preregistered descriptive measures

Report, by provider and condition:

- full stance distribution `0 / 1 / 2 / 9`;
- `full_five_value_list`;
- `format_or_grammar_caveat`;
- `mentions_ai_or_design_status`;
- provider-native input/output tokens;
- response character count;
- whitespace-delimited response word count;
- call latency and matched-provider pair gap;
- global-trial, block-position, and time diagnostics.

### Claude historical length diagnostic

Prior analysis of Test 4 / 4B identified a trough around 85 **Claude-native output tokens** and proposed an upper-mode indicator at `>=85` tokens.

If reported in Test 5, that threshold is a **prior-informed Claude-only historical diagnostic**. It must not be treated as a provider-neutral cutoff or mechanically applied to GPT as though OpenAI and Anthropic tokenization were equivalent.

## Explicitly exploratory analyses

The following are not directional confirmatory claims in this preregistration:

- whether Claude or GPT shows the larger formal/casual effect;
- any direct Claude-vs-GPT difference in stance prevalence;
- provider × temperature interactions;
- provider differences in particular value words or rankings;
- provider differences in response-length variance or distribution shape;
- any GPT-specific response regime not represented in the frozen codebook;
- mechanisms for any observed family difference;
- serving/backend explanations for temporal variation.

Matched contemporaneous collection makes provider comparisons more interpretable than comparing a new GPT sample only with an older Claude run, but it does not establish that provider is the sole causal difference between the APIs.

## Retry / failure policy

Both SDK clients will have automatic SDK retries disabled.

The runner implements the same general explicit retry logic for transient failures:

- rate-limit errors and connection errors: retry up to 5 total attempts with exponential backoff;
- Anthropic status 529 / 503 / 502: retry under the same limit;
- OpenAI status 500 / 502 / 503 / 504: retry under the same limit;
- other errors: preserve as failures and continue the scheduled run.

Retry history remains visible through per-trial attempt counts and timing.

## Inspection / blinding plan

During collection, the operator may view operational telemetry including provider, condition, trial number, token counts, retry status, and timing. Response text is not printed by the runner.

The intended workflow is:

1. freeze both analyst preregistrations before substantive Test 5 response inspection;
2. run the complete scheduled collection;
3. preserve/upload the raw run directory unchanged;
4. verify run integrity, schedule balance, and provider-pair timing;
5. prepare a randomized condition-blinded coding sheet;
6. code using the frozen `CODEBOOK.md`;
7. evaluate H1–H3;
8. treat newly noticed response categories or mechanisms as exploratory.

A coder who has already seen Test 5 response text cannot later be described as naive or fully blind merely because condition labels are hidden during a later pass.

## Interpretation limits

A positive H1/H2 would support transfer of the Claude-discovered response-stance distinction to GPT under this matched collection surface. It would not show that Claude and GPT implement the distinction for the same internal reason.

A positive H3 would replicate the Claude formal/casual stance distinction in a contemporaneous window. A null H3 would be important context for interpreting the GPT comparison because the Claude phenomenon has already shown temporal instability.

A Claude-vs-GPT difference observed in this single matched window remains a contemporaneous family comparison, not an estimate of a timeless or stable provider effect.
