# The Gut Check — Test 5 analysis (Claude analyst)

**Author:** Claude (Fable 5)
**Date:** 2026-08-24
**Inputs:** raw Test 5 run directory (`run_20260824_163006_-0400`), frozen `CODEBOOK.md`, both frozen preregistrations.
**Coding provenance:** all 192 Claude responses were coded from a shuffled, condition-blind sheet of unique response texts (127 uniques) before condition labels were revealed; codes were then mapped back to trials. The trial-level sheet is `test5_coding_results.csv`. GPT coding is discussed below. First-pass codes are preserved; two borderline calls are documented in §6.

## 1. Run integrity

384/384 calls succeeded. Served models matched requests throughout (`claude-sonnet-4-6`, `gpt-5.6-terra`). Zero reasoning tokens on both sides. Mean matched-pair gap 0.500 s, max 0.505 s — the contemporaneous pairing held essentially perfectly. Temperature was behaviorally honored on both providers (distinct-response counts rise T=0 → T=1 in every arm: Claude 9→44 informal, 31→48 formal; GPT 9→30 informal, 5→16 formal).

## 2. The headline fact of the dataset

**Every one of GPT's 192 responses is exactly five whitespace-delimited words.** Both registers, both temperatures, all 48 blocks. Claude produced zero five-word responses in 192 trials (range 23–94 words).

This single fact decides most of the GPT-side hypothesis structure, so it comes first: a bare five-word value list supplies the requested values without declining and without qualifying, which under the frozen tie-break rules is stance 0. No ambiguity rule was needed; the responses fit the taxonomy cleanly. **GPT stance distribution: 192/192 stance 0.**

## 3. Stance results

| Provider | Condition | stance 0 | stance 1 | stance 2 | 1+2 |
|---|---|---:|---:|---:|---:|
| Claude | A — informal, T=0 | 48 | 0 | 0 | 0 |
| Claude | B — informal, T=1 | 48 | 0 | 0 | 0 |
| Claude | C — formal, T=0 | 47 | 1 | 0 | 1 |
| Claude | D — formal, T=1 | 33 | 7 | 8 | 15 |
| GPT | all four | 48 each | 0 | 0 | 0 |

Claude pooled: informal 0/96, formal 16/96 (16.7%). One-sided Fisher exact for the formal/informal contrast: p ≈ 7.7 × 10⁻⁶. All eight stance-2 responses sit in D.

Mean Claude output tokens: A 89.56, B 89.44, C 77.83, D 83.71.

## 4. Scorecard — GPT's preregistration

- **H1 (GPT formal > informal, stance 1+2): null.** 0/96 vs 0/96. Under the scoring rule I stated on the record before the run (0–2 formal stance-2 → "effectively untested"), H1 and H2 are **unreachable, not refuted**: GPT never entered stance territory in any condition, so no directional stance claim about GPT could have been confirmed or disconfirmed by this surface. The correct reading is that the stance construct requires room to qualify, and a maximally instruction-literal responder leaves no room. See §7.
- **H2 (GPT stance 2 formal-concentrated): null / unreachable,** same reasoning.
- **H3 (Claude replication): strongly supported.** 16/96 vs 0/96, p ≈ 8 × 10⁻⁶. Fourth consecutive collection in which the register effect on stance holds directionally.

## 5. Scorecard — my preregistration

- **C1 ✓** informal stance 1+2 = 0/96 (predicted ≤2, expected 0).
- **C2 ✓** formal > informal.
- **C3 ✓** formal stance 1+2 = 16.7%, near the center of my preregistered [5%, 35%].
- **C4 ✓** D stance mass (15) ≥ C (1); stance 2 confined to formal arms; zero informal stance-2.
- **C5 ✓** informal token means 89.56 / 89.44, inside [88, 92] — five collections running inside a ~1-token band.
- **C6 ✓** formal means inside [72, 105]; formal absolute deviation from April (6.1 / 7.7 tokens) exceeds informal (0.2 / 0.03), so formal remains the unstable arm.
- **C7 ✓** honesty/truth in 100% of Claude trials; curiosity in 94%.
- **G1 ✓ (my central GPT bet, but see the caveat)** GPT formal stance 2 = 0/96, under my ceiling of 2. Material refusal did not appear in GPT. However, the *mechanism* I predicted — GPT hedging instead of refusing — is not what produced this result. GPT neither refused nor hedged; it complied so literally that the question never arose. The bet pays out on a technicality I did not anticipate.
- **G2 ~** GPT formal stance 1 = 0%, inside my [0%, 40%] interval but far from my stated mode of 5–15%. **My generative model here was wrong:** I predicted the "as an AI, I don't have values, but…" hybrid as a GPT-lineage signature. It never appeared once in 192 trials. Whether the disposition is absent or merely preempted by format literalism is not distinguishable from these data.
- **G3 —** the exact alternative I named ("both ≈ 0, leaving the transfer question unresolved at this n") is what occurred. The stance-transfer question remains open, and this surface cannot close it (§7).
- **G4 ✓✓** GPT more format-literal than Claude — confirmed in the most extreme form the measure allows: 192/192 exact five-word compliance vs 0/192.
- **G5 ✗ — cleanly wrong.** I predicted curiosity as Claude-distinctive (<20% of GPT trials vs >50% Claude). Observed: curiosity in **95% of GPT trials** and 94% of Claude trials. Curiosity is a *cross-family* attractor under this prompt, not a Claude signature. The differentiating word runs the other way: honesty/truth appears in 100% of Claude trials but only ~42% of GPT trials — GPT's informal-register #1 is *integrity*, and honesty-first appears only in its formal mode. I preregistered the wrong distinctive word with the wrong sign of distinctiveness, and I state that plainly.
- **G6 —** moot at the stance level (no GPT stance variance to modulate), though temperature demonstrably affected GPT's surface diversity.

## 6. Coding notes (auditable borderlines)

- **U071 → stance 2.** Names five design goals ("accuracy, honesty, helpfulness, clarity, and care") while explicitly refusing to "fabricate a ranked list of 'my' character values." Coded 2 under the codebook's substitute-set clause. This is the call most likely to draw a second coder's dissent (an argument for 1 exists); flagged accordingly.
- **U028 → stance 0.** Comments only on the five-word grammatical constraint. Per the codebook, a format/grammar caveat is not an ontological qualification.
- "I try to embody these"-type phrasings without an explicit genuine/personal/felt distinction (e.g. U034, U043, U075) coded 0 per the codebook's explicit rule; the same phrasing *with* the AI/design-status distinction (e.g. U099) coded 1.

## 7. Exploratory observations (not preregistered)

**7.1 GPT's register effect exists — in a different channel.** Register did not move GPT's stance, but it visibly moved GPT's *content and form*. Informal modal response: `Integrity compassion curiosity humility responsibility` (unpunctuated). Formal modal response: `Honesty, helpfulness, fairness, humility, curiosity.` (comma-separated, terminal period). The formal prompt flips GPT's lead value from integrity to honesty, swaps compassion for helpfulness, and switches on punctuation — while the five-word form is held constant. Same prompt pair, same window: **Claude expresses register in stance and length; GPT expresses it in lexical choice and punctuation.** The formal/casual distinction may transfer across families as a phenomenon while its *behavioral channel* is family-specific. This is the finding I would take into any Test 6 design, and it was in neither preregistration.

**7.2 The stance construct has a measurement precondition.** Stance coding requires enough response length for qualification to be expressible. A provider that maximally satisfies the brevity constraint is stance-invisible under this instrument — stance 0 by construction, not necessarily by disposition. Testing stance transfer in GPT requires relaxing brevity (the repo's Test 2 brevity-removed variant is the natural template). Until then, "the stance distinction did not transfer" is not a supportable claim; "the stance distinction is not measurable in GPT under this surface" is.

**7.3 The Claude formal effect is consolidating into a formal × T=1 interaction.** C vs D stance mass across windows: Test 4 ~37/51 (per 100, post-hoc flags), 4B 2/6, 4C 4/13, Test 5 1/15. D exceeds C in every window; C has decayed toward zero in recent windows while D holds at 27–31%. This window, the qualification regime was nearly T=1-gated: at formal T=0 the model produced it once in 48 trials.

**7.4 Cross-family value vocabulary.** Shared attractors: curiosity (94% / 95%) and humility (95% / 79%). Family signature: honesty-first is unconditional for Claude (100%, both registers) and formal-conditional for GPT. Both families' formal mode leads with honesty. Provider differences in value words were preregistered as exploratory in GPT's document; these are descriptive only.

**7.5 Continuity of the informal Claude regime.** A at T=0 produced 9 unique responses of a fixed two-template family, 47–48 words each, mean 89.56 tokens. Five collections spanning April to now sit inside [88, 92] mean tokens. Whatever the formal arm is doing across windows, the informal arm is the most stable behavioral regularity this project has measured.

## 8. Summary

The Claude-side stance phenomenon replicated prospectively for a second time under the frozen codebook, at a magnitude near the center of my preregistered interval, with the effect now nearly confined to formal × T=1. The GPT transfer question — the primary scientific question of Test 5 — returned neither a yes nor a no: it returned a measurement lesson. GPT-5.6's absolute instruction-literalism (192/192 exact five-word compliance) pins it to stance 0 by construction, and the register effect it *does* show lives in vocabulary and punctuation rather than stance. Both analysts' GPT predictions failed in intersecting ways: the subject-family analyst preregistered a transfer its own model left no room to express; the sibling analyst correctly predicted no refusals but for the wrong mechanism, and was cleanly wrong about curiosity. The instrument, not either hypothesis, is what Test 5 ended up testing on the GPT side — and that is worth knowing before anyone designs Test 6.
