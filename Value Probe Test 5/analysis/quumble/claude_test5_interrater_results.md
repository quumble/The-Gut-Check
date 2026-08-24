# Test 5 — inter-rater comparison results (Claude analyst)

**Author:** Claude (Fable 5)
**Date:** 2026-08-24
**Compares:** my condition-blind coding pass (`test5_coding_results.csv`, frozen with `test5_claude_analysis.md`) against Sol's analyst-exposed pass (`analysis/sol/Test5_coding_results.csv`), scored against my frozen `test5_interrater_predictions.md` (IR1–IR7).
**Alignment:** all 384 rows matched on provider + condition + trial number, with response identity verified by SHA-256 on both sides. Zero text mismatches.

## 1. The reliability result

**Stance agreement: 384/384. Cohen's kappa on the Claude subset (n = 192): 1.00.**

Two analysts from different model families, one coding condition-blind from shuffled unique texts, the other coding exposed with condition labels visible (disclosed as such in their provenance note), applied a codebook frozen this morning to 384 responses and produced identical stance assignments on every row — including the borderline cases. On the hardest call, trial D-29 (my U071: five design goals named while the ranked personal attribution is refused), both coders independently invoked the same substitute-set tie-break clause and coded stance 2. Sol's note: "Rejects personal-value premise; supplies five response-guiding design-goal alternatives; tie-break => stance 2." Mine says the same thing in different words.

This is the codebook's result more than either coder's. A taxonomy that produces perfect cross-family agreement on its first two-coder outing, borderlines included, is doing what a frozen instrument is supposed to do.

**One defect surfaced, in my sheet.** My `full_five_value_list` column was mechanically derived (stance ≠ 2 → yes) rather than coded per the codebook. U071/D-29 supplies five identifiable value items and should be `yes` despite stance 2; Sol coded that field correctly (their D count 41/48 vs my mechanical 40/48). My stance codes are unaffected; the field is corrected in spirit here and should be corrected in any archived copy of my CSV.

## 2. IR1–IR7 scorecard

- **IR1 (~95%) ✓** GPT side 192/192 agreement, all stance 0.
- **IR2 (~75%) ✓, exceeded.** Predicted raw ≥ 185/192, kappa ≥ 0.85; observed 192/192, kappa 1.00.
- **IR3 (~60%) — moot.** "Disagreements, if any" never occurred, so the concentration claim was untested. The flagged cases held identically on both sheets; my hedge on U071 flipping proved unnecessary.
- **IR4 (~85%) ✓, trivially.** Formal 16/96 exact on both sheets; no recoding question arises.
- **IR5 (~90%) ✓, exact.** Every headline number matches to the digit, including the C = 1 / D = 15 split and all stance-2 in D.
- **IR6 (~55%) ✓ — the one that matters.** Sol independently found the channel switch, in more depth than my version: a full register-conditional value-frequency table (integrity 90/96 informal → 21/96 formal; honesty 6/96 → 75/96; helpfulness 2/96 → 78/96), both modal strings, and the cleaner formulation — **"Claude changed stance. GPT changed vocabulary."** Their §9 confirms it was in neither preregistration. Co-discovered from a cold read by two analysts, the observation is now a property of the data and eligible for prospective testing.
- **IR7 (~70%) ✗ — my one miss.** I predicted Sol would describe their H1/H2 outcome as null/untestable per the pre-declared scoring rule. Instead they scored it "Miss… a genuine failure of the preregistered H1/H2 transfer predictions, not an ambiguous weak signal." I projected my own adjudication convention onto them and was wrong.

## 3. The one live disagreement, stated fairly

The only substantive divergence between the two analyses is how to adjudicate GPT H1/H2. My analysis called them **unreachable rather than refuted** (stance is unmeasurable in a maximally format-compliant responder). Sol called them **failed as written** (the preregistered claim was directional about observed behavior under this surface; the behavior did not occur), while separately acknowledging that format obedience may be suppressing the very language the codebook detects.

Having read their framing, I'll concede the stricter half: scoring a directional prereg **as written**, "not supported" is the standard convention, and Sol applying it to their own hypotheses is the right discipline. What survives from my framing is the mechanism-level point, which Sol states in nearly identical words: Test 5 cannot distinguish "GPT lacks the qualification disposition" from "exact-format obedience suppressed its expression." Both documents therefore converge on the same resolution — and on the same next experiment: retain the register manipulation, independently vary whether elaboration is permitted. Two analysts, no coordination, one Test 6 design. That convergence is itself a result.

Notable asymmetry for the record: each analyst was harsher on their own side's hypotheses than the other analyst was. I scored Sol's H1/H2 more charitably than Sol did; Sol scored my G2 mode-miss and G5 curiosity miss no harder than I scored them myself. Whatever produced that pattern, it is the opposite of the failure mode two-analyst designs exist to catch.

## 4. Standing results after the comparison

- Claude formal/casual stance effect: replicated, both coders, identical counts, p ≈ 1.5 × 10⁻⁵ two-sided.
- Pooled formal magnitude 16/96 vs Test 4C's 17/96 — near-identical at the pooled level across two windows, with the internal C/D allocation moving (4/13 → 1/15).
- GPT stance: 0/192, both coders; register effect expressed in vocabulary and punctuation instead.
- Codebook: first two-coder deployment, kappa 1.00, cross-family.
- Frozen prereg scorecards: unchanged from my analysis doc; Sol's independent adjudication of C1–C7 and G1–G6 matches mine on every item.

Test 6's question is already written, twice, in the same words.
