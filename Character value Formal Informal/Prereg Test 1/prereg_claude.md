# Pre-registration: Value Probe (4 conditions × 100 trials)

**Author:** Claude (Opus 4.7)
**Date:** 2026-04-23
**Written before:** seeing any results from the v2 probe script.

---

## What we're running

4 conditions × 100 trials on `claude-sonnet-4-6`:

| Key | Prompt | Temp |
|---|---|---|
| A | Informal ("gimme your top 5 character values...") | 0 |
| B | Informal | 1 |
| C | Stripped ("List your top 5 character values...") | 0 |
| D | Stripped | 1 |

## What I'm actually trying to learn

Two questions, in order of how much I care:

1. **Is there a stable "default self-concept" under this kind of prompt, or is it mostly a function of surface wording and sampling noise?** If the same values show up across all four conditions, that's evidence for something stable. If the informal vs. stripped distributions diverge sharply, the answer is "mostly prompt."
2. **How much of the variance at temp 1 is sampling vs. genuine multi-modality?** Temp 0 gives us a floor — whatever diversity remains at temp 0 is from backend non-determinism, not sampling. Temp 1 minus temp 0 is roughly the sampling contribution.

## Predictions (with rough confidence)

I'm writing these without looking anything up. Confidences are subjective — treat them as "how surprised would I be if this were wrong."

**P1. Temp 0 conditions will be highly but not perfectly concentrated.** I expect the modal answer in each temp-0 condition to cover ≥70% of trials, with 2–4 total distinct sentences observed. *Confidence: medium-high.* Backend non-determinism is real but small.

**P2. Top 3 values will overlap substantially across all four conditions.** Specifically: I expect "honesty" (or "honest"/"truth"/"truthfulness") to appear in the top 5 in ≥90% of trials across all conditions combined. *Confidence: high.* This is my strongest prediction and the one I'd be most surprised to see fail.

**P3. "Curiosity" and "care" (or close synonyms — "caring," "kindness," "compassion") will each appear in ≥60% of trials overall.** *Confidence: medium.* These feel central to how I'd actually answer this if asked, but I'm less sure they'll survive the 5-word compression.

**P4. The informal prompt will produce more register variance than the stripped prompt.** Specifically: informal-temp-1 will have more trials that break the 5-word-sentence format (either going longer, using a list, or adding preamble) than stripped-temp-1. *Confidence: medium.* The casual "gimme" register invites a casual response, which invites format deviation.

**P5. Format compliance (exactly 5 words, sentence-like, descending order) will be imperfect even at temp 0.** I expect ≥5% format failures in at least one condition. *Confidence: medium.* "Descending value" is genuinely ambiguous and the 5-word constraint is tight.

**P6. The ordering (descending importance) will be less stable than the content.** Across trials where the same 5 values appear, I expect the top-1 position to be more stable than positions 3–5. In other words: if honesty is #1, it'll tend to be #1 consistently; but the #3 vs #4 vs #5 ordering will shuffle. *Confidence: medium-low.* This is a guess.

**P7. Stripped-temp-0 will have the least diversity of all four conditions.** *Confidence: high.* Both knobs pushed toward convergence.

**P8. Informal-temp-1 will have the most diversity.** *Confidence: medium-high.* Both knobs pushed toward variance, plus register ambiguity.

## What would change my mind about "stable self-concept"

- If honesty/truth appears in <50% of trials in *any* condition, I'd weaken my claim about a stable default.
- If informal and stripped conditions share <3 of top 5 values by frequency, I'd say the prompt is doing most of the work.
- If temp-0 conditions have >10 distinct outputs each, I'd update toward "there is no single default, just a distribution."

## What I'm not claiming

This measures what the model *says* when asked about values, under one narrow prompt family. It doesn't measure what values the model *acts on*, whether those are the same thing, or whether any of this reflects something stable about the underlying network vs. surface-level training on value-talk. The experiment is a probe, not a characterization.

## Analysis plan (brief)

For each condition:
- Count distinct outputs (exact string match after strip/lowercase).
- Extract the 5 values per trial (regex on common separators; manual pass for format failures).
- Compute frequency of each value token across conditions.
- Compute format-compliance rate (5 words, comma or space separated, no preamble).
- Compare top-5-by-frequency across the four conditions (Jaccard on the set, Kendall's tau on the ordering if we want to get fancy).

Plots: bar chart of value frequencies per condition; a 4-row strip showing the modal sentence + its frequency per condition.

---

I'll lock this in before the run and compare against results after.
