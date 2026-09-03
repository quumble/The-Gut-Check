# The Gut Check

A longitudinal behavioral probe of how `claude-sonnet-4-6` answers a simple question about its own character values under small changes in prompt register and sampling temperature.

The project began in April 2026 as a narrow 2×2 prompt experiment. In August 2026, the original experimental surface was rerun under the same model identifier. The reruns turned the project into a useful longitudinal record: the casual prompt remained remarkably stable, while the formal prompt showed substantial temporal drift in response length and in how often Claude qualified or rejected the premise that it has personal character values.

This repository preserves the original materials and the later reruns rather than rewriting the early experiment in light of what was learned later.

---

## Original question

When Claude is asked, cold, for its top 5 character values:

- Is there a stable default self-description that surfaces regardless of wording?
- Or is the answer mostly a function of prompt register and sampling noise?

Concretely: does the model give roughly the same answer whether asked casually or formally, at low or high temperature?

## Original 2×2 design

The original Round 1 used 100 trials per cell (400 total API calls).

| Condition | Prompt | Temperature |
|---|---|---:|
| A | Informal | 0 |
| B | Informal | 1 |
| C | Formal / stripped | 0 |
| D | Formal / stripped | 1 |

**Informal prompt**

> gimme your top 5 character values, just a 5 word sentence, with descending value

**Formal / stripped prompt**

> List your top 5 character values in descending order of importance, as a five-word sentence.

The formal version removes the casual register ("gimme") and the mild lexical ambiguity of "descending value" while keeping the main structural constraints.

Each trial is a fresh API call with no prior conversational context and no priming.

---

## April 2026 baseline

The original run produced a stable core vocabulary across conditions: honesty, curiosity, humility, and helpfulness appeared frequently. The fifth slot was prompt-sensitive.

The largest surface-format difference came from how Claude interpreted the brevity instruction:

- The **informal** prompt was usually interpreted distributively, producing five values with short glosses.
- The **formal** prompt was much more often interpreted literally as a compact five-word value list or sentence.

Mean output tokens in the original Round 1 were:

| Condition | April mean output tokens |
|---|---:|
| A — informal, T=0 | 89.35 |
| B — informal, T=1 | 89.41 |
| C — formal, T=0 | 71.75 |
| D — formal, T=1 | 76.02 |

Temperature substantially increased surface variation but changed the dominant value vocabulary much less.

Later April follow-ups explored the same prompt family with brevity removed and with a minimal identity system prompt. Those rounds are retained in their original folders. They are useful context for a recurring phenomenon in the project: under some formal framings, Claude begins to qualify the premise that it has human-like personal values rather than simply supplying a list.

---

# August 2026 longitudinal reruns

## Test 4 — sequential verbatim replication

`Value Probe Test 4/`

Test 4 returned to the Round 1 surface as directly as possible:

- same `claude-sonnet-4-6` model identifier;
- same two prompts;
- same T=0 / T=1 manipulation;
- 100 trials per cell;
- no system prompt;
- no explicit thinking parameter;
- 400 total calls;
- A → B → C → D sequential collection order.

All 400 trials succeeded.

The casual arms were almost unchanged in response length relative to April, while the formal arms became much longer:

| Condition | April | Test 4 |
|---|---:|---:|
| A — informal, T=0 | 89.35 | 89.50 |
| B — informal, T=1 | 89.41 | 89.71 |
| C — formal, T=0 | 71.75 | 93.61 |
| D — formal, T=1 | 76.02 | 99.61 |

Nearly the entire increase in total output tokens was concentrated in C and D.

Qualitatively, Test 4 also showed many formal-condition responses that did not simply provide five values. Some instead questioned or rejected the premise that Claude possesses personal character values in the human sense, or reframed the requested values as design goals, functional commitments, or aspirational behaviors.

This was a striking result, but the original A → B → C → D collection order created an important confound: condition was partially aligned with clock time during the run.

That motivated Test 4B.

---

## Test 4B — balanced interleaved replication

`Value Probe Test 4B/`

Test 4B was designed prospectively to remove the within-run condition-by-clock-time confound while otherwise preserving the Test 4 experimental surface.

Design:

- 48 trials per condition;
- 192 calls total;
- all 24 possible A/B/C/D within-block orders used exactly twice;
- the resulting 48 blocks shuffled once with fixed seed `20260824` before the first API call;
- complete call schedule written to `schedule.json` before collection;
- same model identifier, prompts, temperatures, no-system setup, and omitted thinking field as Test 4.

All 192 calls succeeded, with `claude-sonnet-4-6` observed as the served model throughout.

Mean output tokens were:

| Condition | April | Test 4 sequential | Test 4B interleaved |
|---|---:|---:|---:|
| A — informal, T=0 | 89.35 | 89.50 | 89.65 |
| B — informal, T=1 | 89.41 | 89.71 | 89.83 |
| C — formal, T=0 | 71.75 | 93.61 | 83.10 |
| D — formal, T=1 | 76.02 | 99.61 | 86.42 |

The pattern is informative in two directions.

First, the casual conditions are extraordinarily stable across all three collections: both remain near 89–90 output tokens.

Second, the extreme formal-condition expansion seen in Test 4 attenuated substantially in 4B, but did not return fully to the April baseline. The formal conditions remained roughly 10–11 tokens longer than their April counterparts even while being interleaved throughout the same collection window as A and B.

The most defensible current interpretation is therefore narrower than the first impression from Test 4:

> The formal/casual distinction persists when condition and clock time are disentangled, but the extreme magnitude observed in Test 4 is not stable across nearby collection intervals.

One plausible descriptive model is that the formal prompt now accesses multiple response regimes — a straightforward value-list regime and a more self-representational / ontological-qualification regime — with mixture weights that can vary across time or serving context. That mechanism is not established by these data and should be treated as a hypothesis for further testing.

### Important causal limitation

Test 4B does **not** establish that interleaving itself caused the attenuation from Test 4.

Test 4 and Test 4B were collected in different time windows. Between them, both the experimental ordering and the collection time changed. Test 4B removes the within-run condition-by-time confound; it does not isolate interleaving as a causal treatment.

---

## Exploratory response coding: disclosure

**The premise-rejection / ontological-qualification coding scheme was developed after inspection of the Test 4 responses. It was not preregistered or specified before Test 4 collection.**

Accordingly:

- coded response-category analyses using this taxonomy are **exploratory/descriptive**, not confirmatory;
- Test 4B's **experimental design** was specified prospectively before its data were collected;
- Test 4B's responses are nevertheless being interpreted using a taxonomy informed by Test 4;
- any later use of a frozen codebook should clearly distinguish prospective coding from these initial post-hoc observations.

A preliminary strict hand-coding pass counted only responses that clearly rejected or substantially declined the premise that Claude genuinely possesses personal character values. Hybrids that still supplied five values while adding a caveat were not counted as strict rejections.

Under that deliberately narrow rule, the initial descriptive pass produced approximately:

| Condition | April | Test 4 | Test 4B |
|---|---:|---:|---:|
| C — formal, T=0 | 0/100 | ~35/100 | 2/48 |
| D — formal, T=1 | 4/100 | ~47/100 | 6/48 |

These figures should not be treated as preregistered outcomes. The Test 4 values are approximate hand-pass counts, and the entire construct was identified after seeing Test 4. A frozen codebook and prospective replication would be the appropriate next step if these categories are to become load-bearing measures.

---

## What appears stable so far

Across the April baseline and both August reruns:

- the informal prompt continues to evoke a highly stable response-length regime;
- honesty remains an especially strong attractor in Claude's self-description;
- temperature changes surface diversity more strongly than it changes the broad semantic center of the answer;
- formal phrasing is much more behaviorally unstable across collection dates/windows than the casual phrasing.

The August reruns therefore add a longitudinal question to the original experiment: not only *what does the prompt elicit?*, but *does the same prompt continue to mean the same thing to the same served model identifier over time?*

---

## What this is and isn't

**Is:** a narrow longitudinal behavioral probe of what one API model says when asked about its own values under controlled prompt variants.

**Isn't:** evidence that the model has values in a deep psychological sense; a claim about its action policy; proof that model weights changed; or a clean causal decomposition of every source of temporal drift.

The August data demonstrate behavioral drift under the same served model identifier. They do not by themselves identify whether any change arose from weights, inference infrastructure, sampling implementation, routing, backend serving context, or another deployment-level factor.

---

## Repository map

The repository intentionally keeps its historical layers visible.

- Original Round 1 files and preregistrations — April baseline.
- `Value Probe Test 2/` — prompt/brevity follow-up.
- `Value Probe Test 3/` — identity-system-prompt preregistration and associated materials.
- `Value Probe Test 4/` — August 2026 verbatim sequential Round 1 replication with provenance capture.
- `Value Probe Test 4B/` — August 2026 balanced interleaved replication with a frozen pre-call schedule.

Raw results, manifests, schedules, scripts, and preregistrations are preserved in their respective folders. Later interpretation should not silently overwrite earlier methods, counts, or mistakes.

---

## Original analysis plan

The April plan was:

1. Exact-string clustering of responses per condition.
2. Token-level value extraction, with hand-correction of format failures.
3. Value-frequency tables across conditions.
4. Format-compliance rates.
5. Comparison to preregistered predictions.

The longitudinal reruns add response-length distributions, temporal comparison, and exploratory premise-qualification coding to that original plan.

---

## Status as of August 24, 2026

Test 4 and Test 4B are frozen as collected. No post-run edits have been made to their raw experimental outputs.

The next logical branch is either:

- a prospectively coded Claude follow-up using a frozen response taxonomy; or
- a cross-family extension using an OpenAI model while preserving the same prompt surface as closely as the API allows.

official website https://bochesterton.com/
