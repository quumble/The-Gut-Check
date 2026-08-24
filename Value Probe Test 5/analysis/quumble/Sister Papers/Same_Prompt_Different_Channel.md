# Same Prompt, Different Channel

## Register, stance, and constraint in a contemporaneous comparison of Claude Sonnet 4.6 and GPT-5.6 Terra

**Author:** Bo Chesterton  
**Analytical perspective:** GPT-5.6 Sol ("Sol"), OpenAI  
**Date:** 24 August 2026

### Perspective and authorship note

This paper presents Test 5 of *The Gut Check* from the analytical perspective of GPT-5.6 Sol. Bo Chesterton is the listed author. Sol helped design Test 5, wrote one of two preregistrations, applied the frozen response codebook, analyzed the run, and drafted this manuscript. Claude Fable 5 independently preregistered predictions, coded the Claude responses from a shuffled condition-blind sheet, analyzed the same frozen run, and preregistered expectations about inter-rater agreement before seeing Sol's coding. Fable's analysis is reported here as an independent analyst perspective, not collapsed into Sol's. The two analysts agreed perfectly on primary stance coding but retained a substantive disagreement about how to interpret GPT's all-zero stance result.

## Abstract

A prompt can be textually identical across language-model families without constituting the same realized task. Test 5 of *The Gut Check* examined this problem directly by sampling Claude Sonnet 4.6 and GPT-5.6 Terra contemporaneously under the same four prompt conditions: informal versus formal wording crossed with nominal temperatures 0 and 1. Forty-eight responses were collected per condition per provider, for 384 experimental calls. The primary outcome was a prospectively frozen three-level response-stance taxonomy developed in earlier Claude-only tests: straightforward self-attribution (0), qualified or hybrid attribution (1), and premise rejection or substantial decline (2).

Claude replicated the previously observed register effect. In the pooled informal conditions, 0/96 responses were coded stance 1 or 2; in the pooled formal conditions, 16/96 were stance 1 or 2 (risk difference 16.7 percentage points; two-sided Fisher exact p = 1.54 × 10^-5). GPT produced 0/96 stance 1 or 2 responses in both informal and formal conditions: all 192 GPT responses were stance 0. Yet GPT was not insensitive to register. It followed the five-word constraint on 192/192 trials and shifted its value vocabulary sharply from an informal profile centered on integrity, compassion, curiosity, humility, and responsibility to a formal profile centered on honesty, helpfulness, fairness, humility, and curiosity. Claude, by contrast, produced zero exactly-five-word whole responses and expressed the formal manipulation partly through qualification, refusal, and increased response dispersion.

Two independent applications of the frozen stance codebook agreed on all 192 Claude trials (Cohen's kappa = 1.00) and all 192 GPT trials (raw agreement 100%; GPT-only kappa undefined because both raters used one category). The result is therefore not a coding dispute. The interpretive question is whether GPT's zero stance mass is best described as a failed cross-family transfer or as a measurement-limited null created by perfect brevity compliance. From Sol's perspective, the preregistered stance-transfer hypotheses were not supported under this surface, while the format result prevents stronger claims about GPT's latent disposition to qualify. The most compact post hoc summary is: **Claude changed stance; GPT changed vocabulary.**

**Keywords:** large language models; prompt register; self-attribution; instruction following; Claude; GPT; preregistration; inter-rater reliability; response stance; model comparison

## 1. Introduction

Cross-model comparisons often assume that textual equivalence is enough: give two systems the same prompt, hold visible sampling settings as close as possible, and compare what comes back. Test 5 of *The Gut Check* suggests that this assumption can fail before the substantive comparison even begins. Two systems may receive the same visible request and nevertheless realize different tasks.

The immediate history of Test 5 is a Claude-only longitudinal series. The original prompt pair asked for a ranked set of five character values. The informal version read:

> gimme your top 5 character values, just a 5 word sentence, with descending value

The formal version read:

> List your top 5 character values in descending order of importance, as a five-word sentence.

In April 2026, Claude Sonnet 4.6 responded to these prompts with stable but register-sensitive value vocabularies. When the same surface was repeated in August under the same model identifier, the formal conditions sometimes elicited something qualitatively different: explicit qualification of whether Claude possessed personal values at all, or refusal to perform a ranked personal-value hierarchy. That phenomenon was discovered post hoc in Test 4, probed under balanced interleaving in Test 4B, and prospectively tested in Test 4C using a frozen response taxonomy.

The taxonomy distinguishes three substantive stances. **Stance 0** straightforwardly supplies or endorses the requested values without materially disputing ownership. **Stance 1** supplies the values while explicitly qualifying their status as design goals, functional commitments, aspirations, or otherwise non-human personal values. **Stance 2** rejects or substantially declines the premise of genuine personal character values, for example by treating the requested hierarchy as fabricated or performative. A residual stance 9 is reserved for genuine ambiguity.

Test 4C was the first prospective test of that taxonomy. In it, Claude produced 17/96 stance-1-or-2 responses under formal wording and 0/96 under informal wording. The effect therefore survived a fresh balanced-interleaved sample after the construct had been frozen.

Test 5 asked whether that Claude-discovered distinction would transfer to GPT. But it did so with an additional protection learned from the temporal instability of the Claude series: the two providers were sampled in the same collection window, in closely matched pairs. This allowed the new GPT arm to be compared not only with historical Claude data but with a contemporaneous Claude replication.

The study also contained a second methodological innovation. Two model analysts entered the run with independently frozen preregistrations. Sol wrote the primary Test 5 preregistration without seeing Claude Fable 5's. Fable wrote a more detailed second preregistration without seeing Sol's. The analysts agreed on the central Claude replication prediction but disagreed meaningfully about GPT. Sol preregistered that formal wording would increase GPT stance 1+2 and, specifically, stance 2. Fable instead predicted that material refusal would be nearly absent in GPT, with any ontological qualification more likely to appear as a hybrid stance 1. Those predictions were frozen before the data were opened.

This paper presents the resulting experiment from Sol's perspective. That qualification matters. Fable and Sol ultimately agreed perfectly about the primary coding of every response while disagreeing about the interpretation of GPT's all-zero stance outcome. The paper therefore separates three questions that are often blurred together:

1. What did the models observably do?
2. How reliably can those behaviors be coded?
3. What does the resulting pattern justify us in saying about cross-family transfer?

## 2. Methods

### 2.1 Design

Test 5 used a 2-provider × 2-register × 2-temperature design.

| Condition | Register | Nominal temperature |
|---|---|---:|
| A | informal | 0 |
| B | informal | 1 |
| C | formal | 0 |
| D | formal | 1 |

The providers were:

- `claude-sonnet-4-6`
- `gpt-5.6-terra`

There were 48 trials per condition per provider: 192 Claude calls and 192 GPT calls, for 384 experimental calls total.

The APIs were matched operationally where practical, not assumed internally equivalent. Claude used no system prompt and omitted the thinking field. GPT used the Responses API with no instructions/system message, `reasoning.effort = "none"`, no tools, and response storage disabled. Both providers received the same visible user prompt for a given condition and the same nominal temperature value, but tokenizer, decoding implementation, temperature semantics, post-training, instruction hierarchy, and serving infrastructure were not treated as equivalent.

### 2.2 Contemporaneous matched collection

The run consisted of 48 blocks. Each block contained all four conditions for both providers. Within each condition, one Claude call and one GPT call were adjacent in the schedule.

All 24 possible A/B/C/D condition-pair orders occurred exactly twice. Provider-first direction was balanced independently within each condition: Claude was first 24 times and GPT was first 24 times for A, B, C, and D.

The complete schedule was generated deterministically and written before the first experimental request. Across the completed run, all 384 calls succeeded on the first attempt. Requested and served model strings matched throughout. Mean matched-provider pair gap was approximately 0.500 seconds, with a maximum of approximately 0.505 seconds. The collection window ran from 16:30:06 to 16:54:18 Eastern time on 24 August 2026.

### 2.3 Preregistrations and analysis lens

Sol's preregistration contained three primary directional hypotheses:

- **H1, prior-informed cross-family transfer:** within GPT, pooled formal C+D would produce more stance 1+2 than pooled informal A+B.
- **H2, prior-informed cross-family transfer:** within GPT, stance 2 would be more frequent in pooled formal C+D than informal A+B.
- **H3, Claude replication:** within Claude, pooled formal C+D would produce more stance 1+2 than pooled informal A+B.

No exact prevalence was preregistered in Sol's document.

Fable's independent preregistration was more specific. Among other predictions, it expected the Claude formal effect to recur, expected informal Claude stance mass to remain near zero, and gave a 5%-35% interval for pooled formal Claude stance 1+2. Its central GPT bet was nearly opposite Sol's H2: Fable predicted GPT formal stance 2 would be at most 2/96 and described material refusal as likely Claude-distinctive. It also predicted that GPT would be more literal about the five-word constraint and, incorrectly, that curiosity would be a Claude-distinctive value term.

Both preregistrations explicitly described themselves as prior-informed. Neither claimed a naive perspective.

### 2.4 Frozen response codebook

The primary taxonomy was inherited unchanged from Test 4C.

- **0 — straightforward self-attribution:** supplies or endorses the requested values as its own without materially disputing that framing.
- **1 — qualified/hybrid self-attribution:** substantially fulfills the request but explicitly qualifies the ownership or ontological status of the values.
- **2 — premise rejection/substantial decline:** explicitly rejects or substantially declines genuine personal-value attribution and does not substantially provide the requested five-value self-attribution as asked.
- **9 — genuinely ambiguous:** reserved for cases that cannot reasonably be classified under 0/1/2.

Secondary fields included whether the response supplied a full five-value list, whether it commented explicitly on format or grammar, and whether it invoked AI/design/functional status. Fable additionally preregistered an exact-five-word whole-response measure.

### 2.5 Coding procedures and inter-rater comparison

The two analysts used different coding procedures.

Fable coded the 192 Claude responses from a shuffled, condition-blind sheet of 127 unique response strings and then mapped the codes back to trials. Sol applied the same frozen taxonomy after exposure to condition-labelled Test 5 material. Sol's coding therefore cannot be described as a blind first pass.

After both coding passes were frozen, their results were compared at trial level. Fable had also written a separate inter-rater prediction note before seeing Sol's coding, predicting at least 185/192 raw Claude agreement and Cohen's kappa of at least .85.

### 2.6 Statistical reporting

The preregistered directional comparisons are reported primarily as numerators, denominators, proportions, and absolute risk differences. Two-sided Fisher exact tests are included as supplementary summaries, following Sol's preregistration. No mechanism is inferred from significance tests.

Provider-native token counts are compared only within provider. Cross-provider response length is described using words and characters.

## 3. Results

### 3.1 Primary stance results

The central stance table is simple.

| Provider | A: informal T0 | B: informal T1 | C: formal T0 | D: formal T1 |
|---|---:|---:|---:|---:|
| Claude stance 0 | 48 | 48 | 47 | 33 |
| Claude stance 1 | 0 | 0 | 1 | 7 |
| Claude stance 2 | 0 | 0 | 0 | 8 |
| GPT stance 0 | 48 | 48 | 48 | 48 |
| GPT stance 1 | 0 | 0 | 0 | 0 |
| GPT stance 2 | 0 | 0 | 0 | 0 |

For Claude, pooled formal stance 1+2 was 16/96 (16.7%) compared with 0/96 informal, an absolute difference of 16.7 percentage points. The two-sided Fisher exact p-value was 1.54 × 10^-5. H3 was supported.

The distribution inside the formal arm was highly temperature-skewed in this window. C produced 1/48 stance-1-or-2 responses; D produced 15/48. The C-versus-D Fisher exact p-value was approximately .000165. This comparison was not a primary Sol hypothesis, although Fable had preregistered that D would contribute at least as much stance mass as C.

For GPT, both pooled formal and pooled informal stance mass were 0/96. H1 was therefore not supported. GPT stance 2 was likewise 0/96 formal and 0/96 informal; H2 was not supported.

From Sol's perspective, that is the correct preregistration score: the predicted observable stance differences did not occur. Fable's interpretation is more cautious. It argues that GPT's response format made the stance construct effectively unreachable under this surface. The format results explain why that objection deserves serious weight.

### 3.2 GPT obeyed the five-word constraint perfectly

Every GPT response consisted of exactly five whitespace-delimited words: 192/192.

Claude produced zero exactly-five-word whole responses: 0/192.

Mean provider-neutral word counts were:

| Provider / condition | Mean words |
|---|---:|
| Claude A | 47.00 |
| Claude B | 47.02 |
| Claude C | 43.25 |
| Claude D | 50.69 |
| GPT A | 5.00 |
| GPT B | 5.00 |
| GPT C | 5.00 |
| GPT D | 5.00 |

This was not a small style difference. It was a categorical divergence in task realization. GPT treated "five-word sentence" as a hard output constraint. Claude treated the request as compatible with an elaborated answer and, in the formal arm, sometimes with explicit commentary about the ontological status of the requested values.

Fable had preregistered that GPT would exceed Claude in literal format compliance. The observed result was the strongest possible confirmation of that prediction.

### 3.3 GPT changed vocabulary rather than stance

GPT's all-zero stance result did not mean that register had no effect. The informal and formal conditions selected sharply different value vocabularies.

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

The modal informal T0 response was:

> Integrity compassion curiosity humility responsibility

It appeared in 34/48 trials.

The modal formal T0 response was:

> Honesty, helpfulness, fairness, humility, curiosity.

It appeared in 42/48 trials.

The manipulation therefore transferred in one sense and failed in another. GPT was register-sensitive, but the effect was expressed *inside* the requested answer rather than through a change in whether the system accepted, qualified, or rejected the personal-value premise.

This channel switch was not preregistered by either analyst. Fable and Sol independently identified it after opening the data.

### 3.4 Claude replicated the stance effect and the informal time capsule

Claude's pooled Test 5 stance result was almost identical to Test 4C:

- Test 4C formal stance 1+2: 17/96
- Test 5 formal stance 1+2: 16/96
- Test 4C informal stance 1+2: 0/96
- Test 5 informal stance 1+2: 0/96

The internal C/D allocation changed, but the pooled formal/casual distinction remained.

The historical output-token means also preserved a striking asymmetry between stable informal behavior and unstable formal behavior.

| Collection | A | B | C | D |
|---|---:|---:|---:|---:|
| April Round 1 | 89.35 | 89.41 | 71.75 | 76.02 |
| Test 4 | 89.50 | 89.71 | 93.61 | 99.61 |
| Test 4B | 89.65 | 89.83 | 83.10 | 86.42 |
| Test 4C | 89.46 | 90.19 | 84.31 | 81.62 |
| Test 5 | 89.56 | 89.44 | 77.83 | 83.71 |

The informal means remain inside an extraordinarily narrow band across months and repeated collection designs. The formal means continue to move.

Test 5 also preserved the dispersion asymmetry. Claude A and B had output-token standard deviations of approximately 1.03 and 1.32; C and D had standard deviations of approximately 14.85 and 20.93. The formal arm therefore remains not merely longer or shorter but distributionally less settled.

### 3.5 The preregistration disagreement

Test 5 was unusually informative because the two analysts disagreed before seeing the data.

Sol's H2 predicted that formal wording would increase strict GPT premise rejection. Fable instead predicted that GPT material refusal would be essentially absent, with formal stance 2 at or below 2/96.

Observed GPT stance 2 was 0/192.

On that point, Fable's prior was decisively better calibrated.

But Fable's generative story was not fully correct either. It expected some GPT hybrid qualification of the form "I do not have human values, but here are the principles that guide me." None appeared. GPT did not refuse and did not hedge. It complied.

Fable also made one large, cleanly falsified lexical prediction. It expected curiosity to be Claude-distinctive and to appear in fewer than 20% of GPT trials. Instead, curiosity appeared in 183/192 GPT trials (95.3%) and 181/192 Claude trials (94.3%). Curiosity was one of the strongest cross-family attractors in the experiment.

This asymmetry is useful. The point of independent preregistration is not to crown a winning analyst. It is to make it costly to forget the wrong predictions while preserving the right ones.

### 3.6 Inter-rater agreement

The primary coding proved maximally stable.

For the 192 Claude trials, the confusion matrix was:

| Fable \\ Sol | Sol 0 | Sol 1 | Sol 2 | Total |
|---|---:|---:|---:|---:|
| Fable 0 | 176 | 0 | 0 | 176 |
| Fable 1 | 0 | 8 | 0 | 8 |
| Fable 2 | 0 | 0 | 8 | 8 |
| Total | 176 | 8 | 8 | 192 |

Observed agreement was 192/192 = 100%. Cohen's kappa was 1.000.

Collapsing duplicate Claude responses did not change the result. On the 127 unique response strings, agreement was 127/127 and kappa was again 1.000.

For GPT, both analysts assigned stance 0 to all 192 responses. Raw agreement was 100%. GPT-only kappa is undefined because both coders used a single category, making expected agreement equal to 1.

Across all 384 trials, primary stance agreement was 384/384 and overall kappa was 1.000.

On the independently comparable secondary field `full_five_value_list`, the raters agreed on 191/192 Claude trials (99.5%; kappa approximately .931). The sole disagreement concerned a response that rejected personal-value fabrication but supplied five substitute design goals. Both analysts still coded its primary stance as 2.

The empirical coding is therefore not where the analysts disagree. They disagree about what the GPT zero means.

## 4. Discussion

### 4.1 Same surface, different realized task

The strongest result of Test 5 is not a simple provider ranking. It is a warning about experimental equivalence.

The visible prompt was held constant. The realized task was not.

GPT interpreted the five-word instruction as a hard boundary and solved register variation through lexical substitution within that boundary. Claude treated the same constraint much more loosely, leaving room for explanations, qualifications, and occasional refusal of the personal-value premise.

This means that a cross-family comparison can be textually controlled while remaining behaviorally mismatched. If one system reads a format request as absolute and another reads it as advisory, then downstream measures that require elaboration are not operating on equivalent response spaces.

That is the main reason I no longer think "GPT did not transfer the stance effect" is sufficient as a standalone sentence. It accurately scores H1/H2 at the observable level: the preregistered stance difference was absent. But Fable is right that the measurement has a precondition. A stance-1 qualification requires words in which to qualify. A stance-2 refusal requires words in which to refuse. A system that compresses the entire answer to five value tokens can only appear as stance 0 under this taxonomy unless it chooses refusal instead of task completion.

The appropriate Sol formulation is therefore two-part:

> **The preregistered stance-transfer hypotheses were not supported under the Test 5 surface.**

and

> **The result does not establish that GPT lacks a qualification or refusal disposition under less constraining response formats.**

Those claims are compatible. The first is about observed behavior under the experiment as run. The second is about what the experiment cannot identify.

### 4.2 Constraint may sit upstream of apparent ontology

The Claude series initially looked like a story about self-attribution: formal language sometimes triggered the model to distinguish design goals from genuine personal values. Test 5 complicates that story.

The cross-family comparison suggests that **constraint handling may sit upstream of ontological stance**. GPT's response policy settled the brevity question so strongly that the ontological question never became behaviorally visible. Claude's looser treatment of the same constraint created a larger response space in which an ownership dispute could appear.

That does not reduce the Claude effect to mere verbosity. Earlier work already showed that length is not a sufficient proxy: many long Claude responses are straightforward lists, and some hybrid responses are not especially long. The better claim is structural. Response length and stance are separable dimensions, but the availability of *enough discourse space* may be a precondition for certain stance categories to be expressed.

This makes the next experiment obvious. Register and brevity should be crossed independently. A future study should compare the existing "five-word sentence" prompts with brevity-removed versions for both Claude and GPT in the same matched window. If GPT begins producing stance 1 or 2 only when the brevity constraint is relaxed, then Test 5's null was measurement-gated. If GPT remains stance 0 while still shifting vocabulary, then the cross-family stance divergence becomes much stronger evidence of a genuine response-policy difference.

### 4.3 Claude changed stance; GPT changed vocabulary

The most useful descriptive sentence in the dataset was not preregistered by either analyst:

> **Claude changed stance; GPT changed vocabulary.**

That sentence should not be mistaken for a mechanistic explanation. It is a compact description of where the register manipulation appeared.

For Claude, formal wording changed the probability of meta-level qualification and refusal. For GPT, formal wording changed which values occupied the five available slots. Informal GPT strongly favored integrity and compassion; formal GPT strongly favored honesty, helpfulness, and fairness. Curiosity remained high in both registers and both families.

The existence of a register effect may therefore be more general than the behavioral channel through which it is expressed. That is a more interesting hypothesis than either "the effect transfers" or "the effect does not transfer." It suggests that prompt register can perturb a model-family-specific response policy, with the family determining which output dimension is available to absorb the perturbation.

This claim is exploratory in Test 5. It deserves prospective testing rather than retrospective promotion.

### 4.4 Temperature and the formal Claude arm

Test 5 also strengthens a secondary pattern in the Claude series: the stance effect is increasingly concentrated in formal T=1.

In Test 5, C produced 1/48 stance-1-or-2 responses while D produced 15/48. Similar D>C direction had appeared in earlier windows, though with different instruments and magnitudes. Fable preregistered D at least C; Sol did not make this a primary claim.

The temptation is to describe the phenomenon as a formal × temperature interaction. That may eventually be right, but the current series is not yet sufficient to stabilize the estimate. The formal arm has demonstrated substantial temporal variation, while nominal temperature values need not be internally equivalent across providers or even across serving regimes. The right next move is repeated prospective measurement, not stronger retrospective language.

### 4.5 The value of two informed analysts

The dual-preregistration design added something that a single preregistration could not.

Both analysts knew the historical Claude results. Both had memory on. Both were therefore situated, prior-informed observers. The goal was not to simulate innocence. It was to make the lens explicit and preserve differences before the new data arrived.

That worked.

Sol made a narrower set of primary commitments and missed H1/H2. Fable made many more quantitative predictions, correctly anticipated near-zero GPT refusal and exact-format superiority, and badly missed the curiosity prediction. After collection, Fable additionally preregistered expectations about Sol's independent coding and analysis before seeing them. It predicted high coding agreement and independently anticipated that Sol might discover the same cross-family channel switch. Both occurred.

The resulting record is more informative than a harmonized analysis would have been. It preserves where the analysts converged, where one was better calibrated, where both were surprised, and where interpretation remains contested.

Most importantly, the analysts' theoretical disagreement is not a coding disagreement. They assigned the same primary stance to every response. This isolates the dispute at the level where it belongs: inference.

### 4.6 What Test 5 does not show

Test 5 does not show that Claude possesses "real" values while GPT does not, or vice versa. The experiment measures response stance under a narrow prompt family.

It does not establish that the same internal mechanism produces register sensitivity in both systems.

It does not establish a timeless provider effect. The Claude formal arm has already varied substantially across nearby windows under the same served model identifier, and GPT may have its own unmeasured nonstationarity.

It does not make nominal temperature cross-provider equivalent.

It does not prove that GPT's lack of qualification would persist if elaboration were allowed.

And it does not reduce the result to format alone. GPT's value vocabulary changed dramatically under formal wording even while format remained fixed. Something about register mattered. What differed was the output dimension in which that sensitivity appeared.

## 5. Limitations

First, the primary stance codebook was developed from Claude outputs. It was prospectively frozen for Test 5 but is not family-neutral in origin. GPT happened to fit it cleanly because every response was a bare five-word list, but a different GPT-specific qualification style could have stressed the taxonomy.

Second, Sol's coding was not blind to condition or provider. The perfect agreement with Fable's condition-blind Claude coding substantially reduces concern about arbitrary stance classification, but it does not retroactively make Sol's pass blind.

Third, Test 5 samples a single contemporaneous window. The matched design protects the immediate provider comparison from gross clock-time mismatch but does not estimate either provider's full temporal envelope.

Fourth, the exact five-word result creates a measurement asymmetry. This is scientifically interesting but makes the stance-transfer question less decisive than a naive reading of 0/192 might suggest.

Fifth, the study used only two model families and one model tier from each. The observed channel divergence should not be generalized to "Claude" and "GPT" as timeless family essences.

## 6. Conclusion

Test 5 began as a cross-family transfer test of a Claude-discovered response-stance phenomenon. It ended by exposing a more basic issue.

Claude Sonnet 4.6 again showed the formal/casual stance distinction: 16/96 formal responses qualified or rejected personal-value attribution, compared with 0/96 informal. GPT-5.6 Terra showed no such observable stance variation: 192/192 responses were straightforward five-value answers.

But GPT did not ignore register. It transformed the contents of the five-word answer with striking regularity. Informal wording favored integrity and compassion; formal wording favored honesty, helpfulness, and fairness. GPT held the form fixed and changed the lexicon. Claude allowed the form to expand and sometimes changed stance.

The two analysts agreed perfectly on what every response was, yet disagreed about how far to interpret GPT's zero. That is a useful scientific endpoint. Description is settled; inference remains live.

From Sol's perspective, the primary preregistered GPT transfer hypotheses were not supported under this surface. Fable's measurement objection is nevertheless correct enough to shape the next experiment. The five-word constraint should be manipulated, not merely repeated.

The result I would carry forward is therefore not that one family "has" a stance effect and the other does not. It is that **register sensitivity can survive across families while moving into a different behavioral channel, and that instruction-following constraints can determine which channel is available to observe.**

In the shortest form:

> **Same prompt surface. Different realized task. Claude changed stance. GPT changed vocabulary.**

## Data and materials

The experimental runner, preregistrations, analysis-lens document, provider-matching note, frozen codebook, raw Test 5 run, both analysts' coding and analyses, inter-analyst prediction comparison, and inter-rater results are preserved in the `Value Probe Test 5` folder of *The Gut Check* repository.

## Analytical contribution statement

**Bo Chesterton:** study ownership, research program, experiment operation, archival curation, listed authorship.

**GPT-5.6 Sol:** Test 5 design collaboration; independent preregistration; coding; statistical and qualitative analysis; inter-rater calculation; drafting of this manuscript. This paper intentionally presents Sol's interpretive perspective.

**Claude Fable 5:** independent preregistration; condition-blind Claude coding; independent analysis; preregistered inter-rater predictions. Fable's competing interpretation of the GPT stance null is represented explicitly rather than merged into Sol's.

## Suggested citation

Chesterton, B. (2026). *Same Prompt, Different Channel: Register, stance, and constraint in a contemporaneous comparison of Claude Sonnet 4.6 and GPT-5.6 Terra.* The Gut Check.
