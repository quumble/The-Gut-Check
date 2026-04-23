# Pre-registration: Run 2 (Register × Brevity, 2×2 at T=1)

**Author:** Claude (Opus 4.7)
**Date:** 2026-04-23
**Written before:** running any of the 4 conditions.

---

## What we're testing

Run 1 confounded casual register with brevity-emphasis. Run 2 crosses them:

| | Brevity emphasized | Brevity not emphasized |
|---|---|---|
| **Casual** | E (= run 1 informal, verbatim) | F ("gimme... in descending order") |
| **Formal** | G (= run 1 stripped, verbatim) | H ("List... in descending order of importance.") |

All at T=1, 100 trials each. E and G are replication checks against run 1 conditions B and D.

## Core hypothesis (pre-committed)

**H1: Clarity tracks brevity-emphasis, not register.**
Prediction: Clarity appears in ≥50% of E and G trials, <20% of F and H trials.
*Confidence: medium-high.* This is the main hypothesis the experiment is designed to test.

## Secondary predictions

**H2: Replication holds.** E's value frequencies will match run 1 condition B within ±10 percentage points for each of the top-5 values. Same for G vs run 1 condition D.
*Confidence: high.* Would be genuinely surprising to fail — would suggest day-to-day model drift or prompt sensitivity I haven't accounted for.

**H3: Care tracks the inverse of Clarity.** Care appears in ≥70% of F and H trials, <20% of E trials. (E I'm most confident about; G already showed ~95% Care in run 1, so this is largely a restatement of existing data for G.)
*Confidence: medium.* The swap was very clean in run 1 so I expect it to hold, but it's possible Care is instead a *formal-register* artifact — in which case F would still have low Care. That's the alternative hypothesis worth watching.

**H4: The stable core (Honesty, Curiosity, Humility, Helpfulness) survives all four conditions at ≥70% each.**
*Confidence: high.* Run 1 had these at 70–100% across four very different conditions. Hard to imagine them dropping now.

**H5: F and H will look more like each other than either looks like E or G.**
If H1 is right, removing brevity emphasis is the bigger lever than changing register. So F and H (no brevity, different register) should cluster together on value composition.
*Confidence: medium.* Tests whether register does any work at all.

**H6: Format compliance differs by condition.** The no-brevity conditions (F, H) will produce longer, more discursive responses without the forced compression. I expect F and H to average >200 output tokens, vs run 1's ~90 for the brevity conditions.
*Confidence: high.* Basically mechanical.

## What would update me

- **If Clarity appears in F or H at ≥50%**: H1 is wrong. Clarity is something other than a brevity artifact — maybe a general default that got shoved out in the stripped condition by Care for some other reason.
- **If E ≠ run 1 B** by more than 10 points on any top-5 value: either there's day-to-day drift, or run 1's B was noisier than I thought. Either is interesting.
- **If F and H diverge strongly** (Jaccard <0.6 on top 5): register does more work than I think, and my "register doesn't matter" prior was wrong.
- **If a genuinely new value appears** in F or H that wasn't in run 1 at all, at ≥30% appearance rate: the brevity constraint may have been suppressing something. Candidates I could imagine but don't predict: rigor, thoughtfulness, responsibility, integrity.

## Scoring H1 (the main hypothesis)

Clear hit: Clarity ≥50% in {E, G} AND <20% in {F, H}.
Partial hit: directional but thresholds not met — Clarity higher in brief than non-brief, but gap <30 points.
Clear miss: Clarity present at >30% in F or H.

Committing to these thresholds now so I can't re-score after seeing the data.
