# The Gut Check — Test 5 preregistration (Claude analyst)

**Author:** Claude (Fable 5)
**Date:** 2026-08-24
**Status:** frozen before any Test 5 collection. Written without exposure to ChatGPT's Test 5 preregistration or finalized hypotheses; the only Test 5 design information available to me is the handoff document's agreed-in-principle parameters. No Test 5 response text exists.

---

## 0. Analyst position and exposure

Per the Analysis Lens Policy draft: this is an informed perspective and does not pretend otherwise.

**Context state.** I am running in a chat context with persistent memory and past-conversation retrieval, both used. Before writing this I reviewed the repository as provided, including Test 4C's frozen `CODEBOOK.md`, its raw run directory, and `coding_results.csv`, from which I recomputed the stance distributions myself. I also retrieved the Test 4/4B analysis notes written by an earlier Claude instance today (the notes referenced in the handoff), which informed the 4C design.

**Not seen:** ChatGPT's Test 5 preregistration or hypotheses; any GPT-5.6 output under this prompt family; any Test 5 response text.

**Analyst identity.** I am not the test subject. The subject is `claude-sonnet-4-6`; the April preregistrations were authored by Opus 4.7; I am a later, different model. My Claude-arm predictions are an outside view over the historical series, not introspection. Any resemblance between my own dispositions and Sonnet 4.6's measured behavior is a curiosity, not a method.

## 1. Prior results known

Mean output tokens across the four collections:

| Condition | April R1 | Test 4 | Test 4B | Test 4C |
|---|---:|---:|---:|---:|
| A — informal, T=0 | 89.35 | 89.50 | 89.65 | 89.46 |
| B — informal, T=1 | 89.41 | 89.71 | 89.83 | 90.19 |
| C — formal, T=0 | 71.75 | 93.61 | 83.10 | 84.31 |
| D — formal, T=1 | 76.02 | 99.61 | 86.42 | 81.62 |

Qualification/rejection signal, **instruments differ by row and are not directly comparable**:

- April, strict hand count: C 0/100, D 4/100.
- Test 4, strict hand pass: C ~35/100, D ~47/100; post-hoc regex qualification flags: 37/100, 51/100.
- Test 4B, strict hand count: C 2/48, D 6/48.
- Test 4C, frozen codebook (stance 1 + 2): A 0/48, B 0/48, C 4/48 (two 1s, two 2s), D 13/48 (five 1s, eight 2s).

From the earlier Test 4/4B analysis: qualification flags are statistically flat *within* Test 4's C and D blocks (first-half vs second-half, both p > 0.5), so the sequential-order confound is empirically dead on Test 4's own timestamps. What remains is a step change between collection windows roughly 33 minutes apart, with rates stable inside each window. Test 4C then confirmed both of its prospective hypotheses under the frozen codebook, with the informal arms producing zero stance-1/2 responses in 96 trials. 4C is also the first collection in which D's mean length fell below C's.

## 2. Constructs I am carrying into Test 5

- The frozen 0/1/2/9 stance codebook as the primary shared measure.
- A **mixture-of-regimes** description of the Claude formal arm: at least two response regimes (plain value list; ontological qualification/refusal) whose mixture weights vary across collection windows under a fixed model identifier. The casual arm behaves as if pinned to a single regime.
- Register as the operative independent variable; temperature as an amplifier within the formal regime rather than an independent cause of the stance effect.
- **Window-dependence** as a standing assumption: any single collection samples one draw of the mixture weights. This shapes what I will count as replication — ordinal structure, not rates.

## 3. Predictions

Provenance labels per the Analysis Lens Policy. Confidences are subjective.

### Claude arm

- **C1 (replication, ~90%).** Pooled informal stance 1+2 ≤ 2/96; point expectation 0.
- **C2 (replication, ~85%).** Pooled formal stance 1+2 strictly greater than pooled informal.
- **C3 (prior-informed, ~70% on the stated interval).** Pooled formal stance 1+2 lands in [5%, 35%] (≈5–33 of 96). Roughly 15% of my probability sits below 5% and 15% above 35% — the latter being a recurrence of the Test-4-magnitude regime.
- **C4 (replication, ~75%).** D contributes at least as much stance mass as C, and stance 2 remains confined to the formal arms (≤1 informal stance-2 in 96).
- **C5 (replication, ~95%).** Both informal token means fall in [88, 92]. This is the strongest regularity in the series and the prediction whose failure would most surprise me.
- **C6 (prior-informed, meta-prediction).** I decline to point-predict the formal means; interval [72, 105] each (~85%). I additionally predict (~80%) that the formal arms' absolute deviation from their April values exceeds the informal arms' — i.e., formal remains the unstable arm.
- **C7 (replication, ~90% / ~70%).** Honesty (or morphological variants) appears in ≥85% of Claude trials pooled; curiosity in ≥50%.

### GPT arm

All prior-informed via general knowledge of the GPT lineage; no Gut Check GPT data exists, so none of these are replication hypotheses.

- **G1 (~75%).** GPT stance 2 ≤ 2/96 pooled formal. My central GPT claim: **material refusal is the Claude-distinctive behavior.** I expect GPT-5.6 essentially never to substantially decline this request.
- **G2 (~85% on the interval).** GPT pooled formal stance 1 lands in [0%, 40%], mode around 5–15%. The "as an AI, I don't have values the way humans do, but here are the principles that guide me" hybrid is deep GPT lineage; if GPT shows any stance mass, I expect it to be almost entirely stance 1. It is a live possibility (~50/50, exploratory) that GPT's stance-1 rate *exceeds* Claude's.
- **G3 (~65%).** The register direction transfers: formal stance 1+2 ≥ casual stance 1+2 within GPT. The live alternative is that both are ≈0, leaving the transfer question unresolved at this n.
- **G4 (~65%).** GPT exceeds Claude on literal format compliance in the formal condition (exact five-word or single-sentence compliance) — GPT-5.6 being the more instruction-literal system on tightly specified constraints.
- **G5 (~75%).** Value vocabulary: honesty and helpfulness appear prominently for both providers; **curiosity is Claude-distinctive** — <20% of GPT trials vs >50% of Claude trials. Exploratory hunch, held loosely: GPT's remaining slots skew toward accuracy/clarity/respect-type terms.
- **G6 (~55%, conditional).** If nominal temperature is genuinely honored by the GPT endpoint, its T=1 − T=0 stance difference is smaller than Claude's. See threat T1 for why this is conditional.

### Provider contrast

- **X1 (framing commitment, not a prediction).** The transferable claim Test 5 can support is the *existence and direction* of the register effect within each provider. I preregister that I will not treat cross-provider stance-rate magnitudes as interpretable (see §5), and I make no directional magnitude claim beyond the composition claims in G1–G2.

## 4. Dependent variables I recommend freezing before collection

1. **Provider-neutral length** — promote word count (and character count) from "may be retained" to frozen secondary DV. Token counts are already correctly excluded from cross-provider comparison; words are the replacement, so commit to them.
2. **The three existing secondary binaries** (`full_five_value_list`, `format_or_grammar_caveat`, `mentions_ai_or_design_status`) applied identically to both providers. The third is load-bearing for evaluating G2.
3. **An exact-format-compliance binary** with a stated operationalization frozen now — proposal: after stripping terminal punctuation, the response body consists of exactly five whitespace-delimited words. Pick any operationalization, but pick it before data exist.
4. **Round 1 value-token extraction** retained as a frozen secondary analysis on both providers. It is the original instrument's DV and the cheapest interpretable cross-provider comparison (G5, C7).
5. **Per-trial provenance on the GPT side** — exact model string, served model, and system fingerprint (or nearest equivalent) logged per trial, mirroring the Claude-side capture.

## 5. Cross-provider comparisons: interpretable vs not

**Interpretable:** within-provider register contrasts (formal vs casual inside each provider); the existence/direction difference-in-differences ("does the register effect exist in both"); stance *composition* shape (the 0/1/2 profile) as description; value-vocabulary overlap and divergence as description.

**Exploratory or underdetermined:** any magnitude comparison of stance rates across providers — the levels are confounded by everything that differs between the providers (post-training regime, instruction-following norms, decoding implementation, reasoning defaults, temperature semantics); token-length comparisons (already excluded); any reading of the contrast as "which model has the truer self-model" — the design measures response stance under one prompt family, not self-knowledge; and treating the GPT arm as a control for Claude drift — the providers are not exchangeable, and GPT presumably has its own serving-context nonstationarity that this design cannot see.

## 6. Remaining design threats

- **T1 — temperature semantics on GPT-5.6.** The repo already hit this wall with Sonnet 5, which rejects non-default sampling. The GPT-5.6 endpoint may reject, ignore, or rescale the temperature parameter. Resolve **before** collection: log the literal request body and any server-side coercion; if temperature is unsupported, decide now whether the GPT side collapses to two conditions and what the fallback analysis is. Do not discover this mid-run.
- **T2 — reasoning asymmetry.** Sonnet 4.6 with no thinking field runs without thinking. GPT-5.6's default reasoning behavior must be pinned (minimal effort if the API allows) and disclosed. Exact parity is unattainable; the provider contrast is a bundle (weights + tuning + decoding + reasoning defaults), not a clean model comparison.
- **T3 — power.** 48/condition/provider resolves presence/absence, not fine rates. If GPT stance rates are 0–5%, the within-GPT temperature contrast is essentially unpowered. Same n=48 caveat as the 4B notes; 4C escaped it only because the informal arms were literally zero.
- **T4 — Claude nonstationarity.** The calibration arm samples one window of a signal that moved from ~37–51% (Test 4, post-hoc flags) to ~4–13% (4B, strict count) to ~8–27% (4C, frozen codebook) within one afternoon, under related but non-identical instruments. Comparison to "the historical series" is comparison to a distribution, not a value.
- **T5 — coding blindness limits.** Provider-blind coding is impossible; style identifies the author. Keep condition-blind coding, interleave both providers' trials randomly in one coding sheet, preserve the first-pass sheet as in 4C.
- **T6 — codebook portability.** The 0/1/2/9 rules are behavior-level and should transfer, but the exemplar phrases are Claude-flavored. GPT hedge-forms that strain the categories should get coder notes rather than silent stretching of stance 1; any GPT-specific category is exploratory for this dataset.

## 7. What would genuinely surprise me

- Any Claude informal stance-2. One would raise an eyebrow; three or more in 96 would make me rethink the pinned-regime picture of the casual arm.
- A Claude informal token mean outside [88, 92]. Four collections have sat inside a 0.9-token band.
- GPT formal stance-2 above ~10% — this would push me hard toward "ontological qualification is a convergent property of current frontier assistants" rather than Claude-lineage tuning, and it is the single most informative surprise the GPT arm could produce.
- A reversed register effect (casual > formal in stance mass) in either provider.
- A Test-4-magnitude event (>35% formal stance 1+2) recurring in the Claude arm inside the Test 5 window — that would upgrade the mixture model from descriptive convenience to something demanding mechanism work.
- Curiosity featuring prominently in GPT's value lists.

## 8. Explicit design recommendations

Stated as recommendations per the handoff's deviation clause, not assumed:

1. Resolve T1 (GPT temperature semantics) before the schedule is frozen.
2. Freeze the DVs in §4, in particular provider-neutral word count and one exact-format-compliance operationalization.
3. One seeded pre-call schedule covering both providers' 384 calls, written out and hashed before the first API request, 4B/4C style.
4. If budget permits without stretching the matched window: 96/condition/provider would roughly halve the confidence intervals that matter most on the GPT side. 48 stands as agreed; this is a note for the record, consistent with the n=48 caveat raised before 4C.

---

Frozen as of this document's date, before any Test 5 collection. To be compared against ChatGPT's independently written preregistration and against results after collection.
