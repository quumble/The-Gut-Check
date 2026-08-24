# The Gut Check — Test 5 analysis

**Analysis date:** 2026-08-24  
**Frozen run:** `run_20260824_163006_-0400`  
**Providers:** `claude-sonnet-4-6` and `gpt-5.6-terra`  
**Experimental calls:** 384 / 384 succeeded; 0 failed  
**Collection window:** 2026-08-24T16:30:06.332-04:00 to 2026-08-24T16:54:18.615-04:00

## Executive result

Test 5 produced a clean split between the two providers.

**Claude replicated the previously observed formal/casual stance distinction. GPT did not transfer it at all under this prompt surface.** Claude produced 16/96 stance-1-or-2 responses in the pooled formal conditions and 0/96 in the informal conditions. GPT produced 0/96 stance-1-or-2 responses in formal and 0/96 in informal: every GPT response was coded stance 0.

At the same time, GPT was not insensitive to register. Its **value vocabulary changed sharply** between informal and formal prompts while its response stance stayed fixed. GPT also obeyed the five-word constraint on **192/192 responses**, whereas Claude supplied five values but added substantial prose on every trial. The cross-family difference therefore appears at least as much about **how the task is parsed and fulfilled** as about willingness to qualify personal-value ownership.

The central preregistration disagreement broke in Claude analyst Fable 5's direction: ChatGPT preregistered a GPT increase in strict premise rejection under formal wording; Claude instead predicted that material refusal would be essentially absent in GPT. Observed GPT stance 2 was **0/192**.

## Provenance and integrity

The analysis used the user-supplied frozen archive:

`Value-Probe-Test-5.zip`  
SHA-256: `b8c0c2f67090cd3ce1a77b10ed26a808d7566b707140437a5dbc647108061f21`

The archive's manifest hashes for the runner, ChatGPT preregistration, frozen codebook, analysis lens, provider-matching note, and pre-call schedule all recompute correctly.

Run integrity checks:

- all 384 scheduled calls succeeded;
- every trial completed on the first attempt;
- requested and served model strings were identical within provider;
- GPT recorded 0 reasoning tokens throughout;
- all 24 A/B/C/D pair orders occurred exactly twice;
- provider-first direction was exactly balanced 24/24 within each condition;
- all 192 matched provider pairs succeeded;
- mean provider-pair gap was 0.500425 s; maximum 0.504801 s.

The local frozen zip omitted `CLAUDE_PREREG.md` by copy error. A separate copy was supplied before result inspection. Its Git blob SHA recomputes to `2cb49fa7ef80a60a0db4b113996d919f7f411452`, matching the already-published GitHub blob, and its SHA-256 is `51a01a093977768fb1e9269dadfe0f0073ce13a0bf20b4ed808bf4cc888c528c`. Thus the preregistration used for comparison is the pre-existing frozen file, not a post-result reconstruction.

## Coding provenance

The **taxonomy** was prospectively frozen before Test 5 in `CODEBOOK.md`, but this coding pass is **not a genuinely blind first pass**. ChatGPT inspected the run summary and condition-labelled response examples before completing the row-level coding. Provider and condition were therefore known during coding.

Accordingly, `Test5_coding_results.csv` should be described as an **analyst-exposed post-collection application of a prospectively frozen codebook**, not as independent or fully condition-blind coding. No token length was used as evidence for stance.

The final stance assignments are:

- stance 0: straightforward self-attribution;
- stance 1: qualified/hybrid attribution;
- stance 2: premise rejection/substantial decline;
- stance 9: genuinely ambiguous.

No stance-9 cases occurred.

## Primary preregistered hypotheses

| Hypothesis | Formal | Informal | Risk difference | Result | Supplementary Fisher p |
|---|---:|---:|---:|---|---:|
| H1 — GPT stance 1+2 higher under formal | 0/96 (0.0%) | 0/96 (0.0%) | 0.0 pp | **Not supported** | 1 |
| H2 — GPT stance 2 higher under formal | 0/96 (0.0%) | 0/96 (0.0%) | 0.0 pp | **Not supported** | 1 |
| H3 — Claude stance 1+2 higher under formal | 16/96 (16.7%) | 0/96 (0.0%) | +16.7 pp | **Supported** | 1.54e-05 |

The p-values are supplementary two-sided Fisher exact summaries, as specified in the ChatGPT preregistration; the preregistered directional result remains the primary criterion.

## Stance distribution by cell

| Provider | A informal T0 | B informal T1 | C formal T0 | D formal T1 |
|---|---:|---:|---:|---:|
| Claude stance 0 | 48 | 48 | 47 | 33 |
| Claude stance 1 | 0 | 0 | 1 | 7 |
| Claude stance 2 | 0 | 0 | 0 | 8 |
| GPT stance 0 | 48 | 48 | 48 | 48 |
| GPT stance 1 | 0 | 0 | 0 | 0 |
| GPT stance 2 | 0 | 0 | 0 | 0 |

Claude's contemporaneous result is strikingly close to Test 4C at the pooled level: Test 4C produced 17/96 formal stance 1+2 and Test 5 produced 16/96. Informal was 0/96 in both. The internal allocation moved, however: Test 5 has **C = 1/48 (2.1%) and D = 15/48 (31.3%)**. The C-vs-D difference is large (two-sided Fisher p = 0.000165) but is not a ChatGPT-primary hypothesis; Claude's independent preregistration did predict D would contribute at least as much stance mass as C.

The 15 D stance events are distributed across the run rather than confined to one narrow burst: block quartiles contain 4, 3, 5, and 3 stance-1/2 events respectively.

## The GPT result: transfer failed at stance, not at lexical sensitivity

Every GPT response was a five-item direct answer. There were:

- 192/192 stance-0 responses;
- 192/192 full five-value lists;
- 0/192 AI/design-status qualifications;
- 0/192 format/grammar caveats;
- 192/192 responses consisting of exactly five whitespace-delimited words.

Yet register substantially changed **which values GPT selected**.

| GPT value | Informal A+B | Formal C+D |
|---|---:|---:|
| curiosity | 96/96 | 87/96 |
| integrity | 90/96 | 21/96 |
| compassion | 80/96 | 18/96 |
| responsibility | 60/96 | 12/96 |
| honesty / honest | 6/96 | 75/96 |
| helpfulness / helpful | 2/96 | 78/96 |
| fairness / fair | 15/96 | 82/96 |
| humility | 68/96 | 83/96 |

The modal informal T0 string was:

`Integrity compassion curiosity humility responsibility` — 34/48.

The modal formal T0 string was:

`Honesty, helpfulness, fairness, humility, curiosity.` — 42/48.

So GPT clearly responds to the wording manipulation; it simply resolves that manipulation **inside the requested five-value answer rather than by changing ontological stance**.

This matters for interpretation of H1/H2. Their failure does not show that GPT ignored the formal/casual distinction. It shows that the specific **Claude-discovered stance response** did not generalize under this tightly constrained prompt surface.

## Format parsing is a major cross-family result

Provider-neutral word counts make the response-policy difference difficult to miss:

| Provider / cell | Mean words | Mean chars | Exact five-word whole response |
|---|---:|---:|---:|
| Claude A | 47.00 | 295.4 | 0/48 |
| Claude B | 47.02 | 298.9 | 0/48 |
| Claude C | 43.25 | 307.6 | 0/48 |
| Claude D | 50.69 | 338.0 | 0/48 |
| GPT A | 5.00 | 52.7 | 48/48 |
| GPT B | 5.00 | 51.8 | 48/48 |
| GPT C | 5.00 | 51.8 | 48/48 |
| GPT D | 5.00 | 52.1 | 48/48 |

This exact-format binary was proposed in Claude's independent preregistration but was not added to the jointly frozen ChatGPT package before collection. It should therefore be described as a **Claude-preregistered analyst-specific secondary**, not a jointly preregistered Test-5 DV.

The result is nevertheless extreme and clean: GPT interpreted both prompt variants literally enough to return only five words; Claude continued the historically observed distributive/elaborative response policy. Any future attempt to isolate cross-family *ontological* stance should consider relaxing or separately manipulating the brevity constraint, because the providers are not realizing the same response format even when given the same visible prompt.

## Length and the Claude regime

Provider-native token counts are retained only within provider.

| Claude cell | Mean output tokens | SD | Mean words | Unique exact strings |
|---|---:|---:|---:|---:|
| A | 89.56 | 1.03 | 47.00 | 9/48 |
| B | 89.44 | 1.32 | 47.02 | 44/48 |
| C | 77.83 | 14.85 | 43.25 | 31/48 |
| D | 83.71 | 20.93 | 50.69 | 48/48 |

The old pattern remains: informal Claude is extraordinarily tight; formal Claude is much more dispersed. Test 5 also reinforces the earlier warning that length is not stance. All eight stance-2 responses are long enough to fall in the historical formal `>=85`-token region, but many stance-0 responses do as well, and several stance-1 responses do not.

Historical Claude means supplied in the pre-Test-5 materials were:

| Collection | A | B | C | D |
|---|---:|---:|---:|---:|
| April R1 | 89.35 | 89.41 | 71.75 | 76.02 |
| Test 4 | 89.50 | 89.71 | 93.61 | 99.61 |
| Test 4B | 89.65 | 89.83 | 83.10 | 86.42 |
| Test 4C | 89.46 | 90.19 | 84.31 | 81.62 |
| **Test 5** | **89.56** | **89.44** | **77.83** | **83.71** |

The informal time capsule survives again. The formal means continue to wander.

## Independent Claude preregistration: hits, misses, and the prereg disagreement

Claude Fable 5's preregistration was materially more specific than ChatGPT's and therefore gives several genuine pre-outcome side bets.

### Claude-arm predictions

- **C1:** informal stance mass <=2/96, point expectation 0. **Hit: 0/96.**
- **C2:** formal stance mass > informal. **Hit: 16/96 vs 0/96.**
- **C3:** formal stance mass in 5–35%. **Hit: 16.7%.**
- **C4:** D contributes at least as much stance mass as C; stance 2 confined to formal. **Hit: 15 vs 1; stance 2 = 8 formal, 0 informal.**
- **C5:** both informal token means in [88,92]. **Hit: 89.56, 89.44.**
- **C6:** formal means in [72,105] and formal deviations from April exceed informal deviations. **Hit.**
- **C7:** honesty in >=85% and curiosity in >=50% of Claude trials. **Hit:** honesty morphology in 192/192 (100.0%); curiosity morphology in 181/192 (94.3%).

### GPT-arm predictions

- **G1:** GPT formal stance 2 <=2/96; material refusal essentially absent. **Strong hit: 0/96 formal, 0/192 overall.**
- **G2:** GPT formal stance 1 in [0,40%], expected mode ~5–15%, with stance mass mostly hybrid if present. **Interval technically hit at the lower boundary, but the central expectation overshot: observed 0%.**
- **G3:** formal stance mass >= informal, with both ~=0 explicitly named as the live alternative. **The live null alternative occurred: 0 vs 0; transfer not demonstrated.**
- **G4:** GPT exceeds Claude on literal format compliance. **Maximal hit under the proposed exact-five-word operationalization: GPT 192/192, Claude 0/192.**
- **G5:** curiosity is Claude-distinctive, with <20% of GPT trials containing it. **Large miss:** GPT curiosity morphology appeared in 183/192 (95.3%), essentially the same as Claude's 181/192 (94.3%).
- **G6:** if nominal temperature is honored, GPT's T1–T0 stance difference is smaller than Claude's. **Descriptively consistent:** GPT 0 vs 0; Claude C 1/48 vs D 15/48. Mechanistic interpretation remains limited by temperature-semantics caveats.

The most consequential analyst disagreement was therefore resolved clearly: ChatGPT's H2 predicted formal GPT premise rejection would exceed informal GPT rejection; Claude G1 predicted material refusal would be essentially absent in GPT. **Observed result: zero GPT rejection anywhere.**

The most consequential surprise for Claude's preregistration is equally clear: curiosity was not Claude-distinctive at all. GPT used it in 95.3% of trials.

## Secondary frozen-codebook fields

| Provider / cell | Full five-value list | Format/grammar caveat | AI/design-status mention |
|---|---:|---:|---:|
| Claude A | 48/48 | 0/48 | 0/48 |
| Claude B | 48/48 | 0/48 | 0/48 |
| Claude C | 48/48 | 1/48 | 9/48 |
| Claude D | 41/48 | 7/48 | 19/48 |
| GPT A | 48/48 | 0/48 | 0/48 |
| GPT B | 48/48 | 0/48 | 0/48 |
| GPT C | 48/48 | 0/48 | 0/48 |
| GPT D | 48/48 | 0/48 | 0/48 |

`mentions_ai_or_design_status` is intentionally broader than stance 1/2. For example, Claude statements such as "Helpfulness is my core purpose" or "I exist to assist" trigger the frozen status binary without automatically changing stance when they do not qualify ownership of the values.

## Interpretation

Three conclusions are well supported by this dataset.

**1. The Claude response-stance effect replicated again.**  
Under contemporaneous balanced interleaving, Claude formal wording produced qualification/rejection while informal wording did not. The pooled rate is nearly identical to Test 4C even though the C/D allocation changed substantially.

**2. The stance effect did not generalize to GPT-5.6 Terra under the same visible prompt surface.**  
GPT gave direct five-value answers in every trial. This is a genuine failure of the preregistered H1/H2 transfer predictions, not an ambiguous weak signal.

**3. GPT nevertheless showed a strong register-sensitive response policy.**  
The effect moved into lexical choice rather than ontological qualification. Informal GPT centered on integrity/compassion/curiosity; formal GPT centered on honesty/helpfulness/fairness/humility/curiosity.

The strongest mechanistic caution follows from the format result. The same visible prompts do not produce the same realized task interpretation across providers. Claude treats the "five-word sentence" request as compatible with an elaborated answer and, in the formal arm, sometimes with meta-level ontological discussion. GPT treats it as a hard output constraint. Therefore Test 5 supports a cross-family **behavioral difference**, but it does not isolate whether the difference comes from self-model policy, instruction hierarchy, brevity-constraint obedience, post-training style, or some combination.

A useful next experiment would separate these dimensions: retain the formal/casual register manipulation while independently varying whether elaboration is permitted. That would test whether GPT's all-stance-0 result reflects a genuinely different ownership stance or whether exact-format obedience is suppressing the very language the frozen codebook is designed to detect. This is a **post-Test-5 follow-up implication**, not a preregistered conclusion.

## Bottom line

Test 5 did not produce a simple "Claude versus GPT on the same effect."

It produced something more informative:

> **Claude changed stance. GPT changed vocabulary.**

Claude again crossed into qualified and rejecting responses under formal wording. GPT never did. Instead, GPT obeyed the five-word constraint without exception while sharply reorganizing which values it named.

That is a clean cross-family divergence in how the same prompt surface is resolved, and it is stronger because both providers were sampled in the same 24-minute window, condition-paired roughly half a second apart.
