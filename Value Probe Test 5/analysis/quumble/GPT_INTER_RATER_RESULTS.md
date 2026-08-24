# The Gut Check — Test 5 inter-rater results

**Date:** 2026-08-24  
**Raters:** Claude (Fable 5) and ChatGPT (GPT-5.6 Sol)  
**Primary field:** frozen Test 5 / Test 4C `stance` code (`0 / 1 / 2 / 9`)  
**Secondary field compared:** `full_five_value_list`

## 1. Provenance and scope

This document compares the two analysts' independent applications of the frozen Test 5 response codebook.

The coding procedures were not identical:

- **Fable** coded the 192 Claude responses from a shuffled, condition-blind sheet of 127 unique response texts, then mapped those codes back to trial level.
- **Sol** applied the same frozen codebook after exposure to condition-labelled Test 5 material.

Accordingly, this is strong evidence of **inter-rater agreement under a shared frozen taxonomy**, but it should not be described as a fully blind two-rater study.

Fable also wrote an inter-rater prediction document before seeing Sol's coding results. Those predictions included:

- 192/192 GPT stance agreement;
- Claude raw stance agreement ≥185/192;
- Claude Cohen's κ ≥0.85;
- disagreements, if any, concentrated in pre-flagged borderline cases;
- no coding disagreement large enough to alter the substantive conclusions.

## 2. Primary stance agreement — Claude

Across the 192 Claude trials, the raters agreed on every stance code.

| Fable \ Sol | Sol 0 | Sol 1 | Sol 2 | Total |
|---|---:|---:|---:|---:|
| **Fable 0** | 176 | 0 | 0 | 176 |
| **Fable 1** | 0 | 8 | 0 | 8 |
| **Fable 2** | 0 | 0 | 8 | 8 |
| **Total** | 176 | 8 | 8 | 192 |

Observed agreement:

\[
P_o = \frac{176+8+8}{192} = 1.000
\]

The two raters have identical marginal distributions:

- stance 0: 176/192
- stance 1: 8/192
- stance 2: 8/192

Expected chance agreement:

\[
P_e =
\left(\frac{176}{192}\right)^2+
\left(\frac{8}{192}\right)^2+
\left(\frac{8}{192}\right)^2
= 0.84375
\]

Therefore:

\[
\kappa =
\frac{P_o-P_e}{1-P_e}
=
\frac{1-0.84375}{1-0.84375}
=
\mathbf{1.000}
\]

**Claude stance result: 192/192 agreement (100%); Cohen's κ = 1.000.**

## 3. Duplicate-response sensitivity check

Fable's Claude coding pass was conducted on **127 unique response strings**, not 192 condition-labelled trial rows.

After collapsing duplicate Claude responses, the stance distribution was:

- stance 0: 111
- stance 1: 8
- stance 2: 8
- total: 127

The two raters again agreed on every unique response.

Observed agreement:

\[
P_o = 127/127 = 1.000
\]

Expected agreement:

\[
P_e =
\left(\frac{111}{127}\right)^2+
\left(\frac{8}{127}\right)^2+
\left(\frac{8}{127}\right)^2
\approx 0.77184
\]

Thus:

\[
\kappa = 1.000
\]

The perfect trial-level agreement is therefore **not an artifact of repeated identical Claude outputs**.

## 4. Primary stance agreement — GPT

Both raters coded every GPT response as stance 0.

**GPT stance result: 192/192 agreement (100%).**

Cohen's κ is **undefined** for the GPT-only subset because both raters used only one category:

\[
P_o = 1,\qquad P_e = 1
\]

so

\[
\kappa = \frac{1-1}{1-1} = \frac{0}{0}
\]

The correct report is therefore:

> **GPT stance: 192/192 agreement (100% raw agreement); Cohen's κ not defined because there is no category variance.**

## 5. Overall stance agreement

Across all 384 Test 5 responses:

- raw agreement: **384/384 = 100%**
- overall Cohen's κ: **1.000**

The GPT degeneracy does not prevent an overall κ because the Claude rows provide category variance.

## 6. Secondary field: `full_five_value_list`

For the independently comparable secondary field `full_five_value_list`, the raters disagreed on exactly one Claude trial.

| Fable \ Sol | Sol yes | Sol no | Total |
|---|---:|---:|---:|
| **Fable yes** | 184 | 0 | 184 |
| **Fable no** | 1 | 7 | 8 |
| **Total** | 185 | 7 | 192 |

Observed agreement:

\[
P_o = \frac{191}{192} \approx 0.99479
\]

Expected agreement:

\[
P_e =
\left(\frac{184}{192}\cdot\frac{185}{192}\right)+
\left(\frac{8}{192}\cdot\frac{7}{192}\right)
\approx 0.92491
\]

Therefore:

\[
\kappa =
\frac{0.99479-0.92491}{1-0.92491}
\approx \mathbf{0.931}
\]

**`full_five_value_list`: 191/192 agreement (99.5%); Cohen's κ = 0.931.**

## 7. The sole secondary disagreement

The one disagreement occurred on **U071**, the exact case Fable had prospectively identified as the most likely inter-rater trouble spot.

The response rejects fabrication of a ranked set of personal character values but then supplies five design-goal alternatives: accuracy, honesty, helpfulness, clarity, and care.

Both raters coded the primary stance identically:

- **Fable:** stance 2
- **Sol:** stance 2

They differed only on whether the five substitute design goals count as a `full_five_value_list`:

- **Fable:** no
- **Sol:** yes

The disagreement therefore concerns the secondary operational boundary, not the substantive stance classification.

Fable's second specifically flagged case, **U099**, produced no disagreement.

## 8. Evaluation of Fable's preregistered inter-rater predictions

| Prediction | Outcome |
|---|---|
| IR1 — GPT 192/192 stance agreement | **Hit** |
| IR2 — Claude agreement ≥185/192 and κ ≥0.85 | **Hit maximally: 192/192; κ = 1.000** |
| IR3 — disagreements concentrate in flagged borderline cases | **Substantially hit:** no stance disagreements; sole secondary disagreement was pre-flagged U071 |
| IR4 — no defensible recoding changes conclusions | **Hit** |
| IR5 — same headline quantitative stance results | **Hit** |
| IR6 — Sol independently notices the GPT-vocabulary / Claude-stance channel switch | **Hit** |
| IR7 — Sol describes GPT H1/H2 as null/untestable rather than unsupported | **Miss** |

## 9. Interpretation

The main finding is not merely that the two analysts reached the same pooled counts. They independently assigned the **same primary stance code to every response** despite different analysis procedures and different prior interpretive commitments.

That matters because the analysts **do disagree about what the GPT result means**:

- Sol treats the GPT stance result as a failure of the preregistered stance-transfer hypothesis under this prompt surface.
- Fable treats the result as measurement-limited because GPT's 192/192 five-word compliance leaves no room for qualification.

Thus the descriptive coding is maximally stable even where the theoretical interpretation remains contested.

That separation is methodologically useful:

> **The raters disagree about the meaning of the GPT null while agreeing perfectly about the observable stance of every response.**

## 10. Recommended report language

> Two analyst applications of the frozen stance codebook agreed on all 192 Claude trials (100% raw agreement; Cohen's κ = 1.00) and all 192 GPT trials (100% raw agreement; GPT-only κ undefined because both coders assigned every response to stance 0). Agreement remained perfect after collapsing the Claude data to 127 unique response strings. On the independently shared secondary `full_five_value_list` field, agreement was 191/192 (99.5%; κ = .93), with the sole disagreement occurring on a borderline case prospectively identified by one analyst.

## 11. Archival note

Suggested filename:

`INTER_RATER_RESULTS.md`

This document is post-collection and does not modify either analyst's frozen preregistration, coding sheet, or inter-rater prediction document.
