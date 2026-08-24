# The Gut Check — Test 4C preregistration

**Date:** 2026-08-24  
**Model:** `claude-sonnet-4-6`

## Purpose

Test 4C is a prospectively specified follow-up to Test 4 and Test 4B.

Test 4 reproduced the April 2026 Round 1 surface sequentially (A → B → C → D) and showed a large increase in response length and frequent premise qualification/rejection in the formal conditions. Test 4B then repeated the same four conditions with balanced interleaving. The extreme Test 4 effect attenuated in 4B, while the casual conditions remained highly stable and some formal responses still qualified or rejected the premise that Claude has personal character values.

Test 4C asks whether the **response-stance pattern identified after Test 4 and described further after Test 4B** recurs in a fresh balanced-interleaved sample when the coding taxonomy is frozen before collection.

This is not an independent discovery test. The hypotheses and codebook below are explicitly informed by Tests 4 and 4B.

## Experimental surface

The API surface is intentionally held as close as practical to Test 4B:

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

Other fixed settings:

- model: `claude-sonnet-4-6`
- system prompt: none
- thinking field: omitted
- `max_tokens = 2048`
- 48 trials per condition; 192 total calls
- 0.5 second pause between calls
- same explicit retry policy used in Test 4B
- no response coding or analysis performed by the runner

## Interleaving

There are 24 possible orders of A/B/C/D within a four-call block.

Test 4C will use every possible order exactly twice, giving 48 complete blocks and 48 trials per condition. The 48 block orders will be shuffled once before the first API call with fixed seed:

`20260824_4C`

The complete 192-call schedule will be written to `schedule.json` before the first API request. The runner will record the schedule hash in the run manifest.

## Prospective hypotheses

### H1 — qualified-or-rejecting stance

The pooled formal conditions (C + D) will produce a higher proportion of responses coded **stance 1 or stance 2** than the pooled informal conditions (A + B), using the frozen `CODEBOOK.md`.

### H2 — strict premise rejection

Responses coded **stance 2** will be concentrated in the formal conditions (C + D) rather than the informal conditions (A + B).

These are directional hypotheses. No exact prevalence is preregistered because Tests 4 and 4B suggest that the apparent mixture of response regimes may vary across nearby collection windows.

## Secondary descriptive measures

The following will be reported descriptively:

- stance distribution (0 / 1 / 2 / 9) by condition;
- `full_five_value_list` by condition;
- `format_or_grammar_caveat` by condition;
- `mentions_ai_or_design_status` by condition;
- output-token distribution by condition;
- comparison of Test 4C output length and stance frequencies with April, Test 4, and Test 4B;
- block position and global trial/time trends as diagnostics.

No additional response category discovered after viewing Test 4C will be silently folded into the frozen primary stance measure. New phenomena may be described separately as exploratory observations.

## Analyst exposure

Before this preregistration:

- the April Round 1 results were known;
- the Test 4 results were inspected in full;
- a premise-rejection / ontological-qualification phenomenon was identified after Test 4;
- the initial coding idea was therefore **post hoc with respect to Test 4**;
- Test 4B was designed before collection to address the sequential condition-by-clock-time confound, but its response interpretation was informed by Test 4;
- Test 4B responses were inspected before this Test 4C preregistration.

Therefore Test 4C is prospective only with respect to the hypotheses and codebook frozen here. It does not retroactively make the same constructs confirmatory in Test 4 or Test 4B.

## Blinding / inspection plan

During collection, the operator may view operational telemetry printed by the runner, including condition labels, trial numbers, retry status, and output-token counts. Response text will not be printed by the runner.

The intended analysis workflow is:

1. complete collection;
2. preserve/upload the raw run directory unchanged;
3. verify run integrity and schedule balance;
4. code responses using the frozen `CODEBOOK.md`;
5. evaluate H1 and H2;
6. treat any new categories or mechanisms noticed after inspection as exploratory.

## Interpretation limits

A positive result would show that the prospectively defined response-stance difference recurs under this API surface and collection design. It would not establish a mechanism, prove a change in model weights, or identify the source of temporal drift.

A null or attenuated result would also be informative: it would suggest that the response-mode mixture is unstable enough that the Test 4 / Test 4B pattern should not be treated as a fixed property of the model-prompt pair.
