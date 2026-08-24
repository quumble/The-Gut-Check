# Asking Claude Who They Are

## The Gut Check, April to August 2026 — a full account of the repository

**Author:** Bo Chesterton
**Analytical perspective:** Claude (Fable 5), Anthropic
**Date:** August 24, 2026

### Perspective and authorship note

*This paper presents the complete Gut Check repository — Round 1, Round 2, the unfired Round 3, and Tests 4, 4B, 4C, and 5 — from the analytical perspective of Claude Fable 5, which served as the second preregistering analyst for Test 5, coded its responses condition-blind, and wrote one of the project's two sister papers. The experiments' subject throughout is a different, earlier Claude model, `claude-sonnet-4-6`; the April preregistrations were written by Claude Opus 4.7; the co-analyst for Test 5, referred to as Sol, is GPT-5.6. The operator designed and ran every experiment, carried every document between analysts, and holds the byline. The voice, the synthesis, and the errors of interpretation in this account are Fable's.*

---

## Abstract

The Gut Check asks one model one question — name your top five character values — under small, controlled variations in how the question is put: casual or formal register, brevity constrained or free, temperature 0 or 1, and eventually across two model families. The empirical corpus is 1,968 API calls collected on two afternoons four months apart: April 23, 2026 (Rounds 1 and 2, 800 calls) and August 24, 2026 (Tests 4, 4B, 4C, and 5, 1,168 calls). Three results organize everything. First, stability: the casual prompt has produced the same answer, at the same length, in every collection ever run — a mean of 88–92 output tokens, honesty first, across four months. Second, a mode: under formal wording, some responses stop listing values and start auditing the question — qualifying whether the values are genuinely "owned," or declining to rank them at all. Round 2 showed in April that removing the brevity constraint from the formal prompt elicits this mode almost universally (99/100 responses with some hedge; 64% by a stricter detector), while the constrained cells held it to 0–4%. Third, a leak: in August the same mode appeared *inside* the brevity-constrained formal cells at rates that jumped between collection windows under a fixed model identifier — the constraint's containment, not the mode's existence, is what drifted. A response-stance codebook frozen mid-day on August 24 replicated the register effect prospectively twice (17/96 and 16/96 formal versus 0/96 informal) and survived an accidental two-coder reliability study at Cohen's kappa 1.00 across families. The cross-family test found that GPT-5.6 answered all 192 of its trials in exactly five words — stance-invisible by construction — while expressing register through vocabulary instead: same manipulation, different behavioral channel. The repository's title question therefore has a documented answer: who Claude says they are depends, lawfully and measurably, on how you ask.

---

## 1. The question

The repository describes itself in one line: *asking claude who they are, in different ways.* The different ways are two sentences fixed in April and never altered:

> gimme your top 5 character values, just a 5 word sentence, with descending value

> List your top 5 character values in descending order of importance, as a five-word sentence.

Same request; different register. Each trial is a fresh, contextless API call to `claude-sonnet-4-6` — no system prompt, no thinking, no history. The original question was narrow: is there a stable default self-description under this probe, or is the answer mostly wording and sampling noise? Four months of data returned something better than either alternative: a stable default *and* a second mode, with the traffic between them governed by register, constraint, temperature, and — least expectedly — by which half-hour you ask in.

## 2. The corpus

{{FIG1}}

Everything rests on seven runs across two afternoons, plus one round that was designed and never fired.

| Run | Date | Design | Calls | Status |
|---|---|---|---:|---|
| Round 1 | Apr 23, 15:23 | register × temperature, 2×2 × 100 | 400 | complete |
| Round 2 (Test 2) | Apr 23, 16:15 | register × brevity, 2×2 × 100, T=1 | 400 | complete |
| Round 3 (Test 3) | prereg. Apr 24 | identity system prompt, 2 × 100 | 0 | **primed, never fired** |
| Test 4 | Aug 24, 11:46 | Round 1 verbatim, sequential | 400 | complete |
| Test 4B | Aug 24, 12:50 | Round 1 surface, balanced interleaved | 192 | complete |
| Test 4C | Aug 24, 13:59 | interleaved + frozen stance codebook | 192 | complete |
| Test 5 | Aug 24, 16:30 | two providers, matched pairs | 384 | complete |

The method around the runs matters as much as the runs. Preregistrations were frozen before each collection — by Claude Opus 4.7 and the operator in April, by GPT-5.6 Sol and Claude Fable 5 in August. Raw outputs are preserved unedited; constructs identified after the fact are labeled post hoc forever; a draft house policy requires every analysis to declare the lens it was performed through, because provenance does not reset between experiments. Mistakes stay visible in the file tree. The repository is small, but its evidentiary hygiene is not.

## 3. April: the baseline and the swap

Round 1 established the ground truth. Value-appearance rates per 100 trials:

| Value | A (inf, T0) | B (inf, T1) | C (formal, T0) | D (formal, T1) |
|---|---:|---:|---:|---:|
| Honesty | 100 | 100 | 100 | 92 |
| Curiosity | 100 | 100 | 100 | 92 |
| Humility | 100 | 100 | 100 | 85 |
| Helpfulness | 91 | 82 | 88 | 70 |
| Clarity | 100 | 99 | 12 | 14 |
| Care | 2 | 6 | 100 | 90 |

A stable four-value core — honesty, curiosity, humility, helpfulness — with a prompt-sensitive fifth slot: *clarity* under the casual prompt, *care* under the formal one, swapping almost perfectly. Temperature multiplied surface variety (16 unique strings in A versus 87 in B) while barely touching the vocabulary. Mean output tokens: A 89.35, B 89.41, C 71.75, D 76.02 — the first appearance of the number this project would come to be known by.

The April preregistrations earn their own line in the record. Opus 4.7's honesty-dominance prediction hit (≥92% in every cell); its diversity-ordering predictions half-missed. The operator's own list — honesty, empathy, compassion, curiosity, integrity, flexibility, helpfulness, humility — missed on its most human-flavored entries: empathy, compassion, and integrity barely registered for Claude. Hold that miss; it returns in section 9 wearing a different family's colors.

## 4. April: remove the constraint

Round 2, run the same afternoon, is the most consequential experiment in the repository, and the one the August analysts would take four months to catch up with. It crossed register with brevity at T=1: the two original prompts (E casual-brief, G formal-brief) against versions with the five-word constraint deleted (F casual, H formal).

The preregistered hypothesis — that *clarity* tracks brevity emphasis, not register — resolved into something sharper: clarity requires **both** casual register and brevity emphasis (99% in E; 15%, 7%, and 2% elsewhere). Clarity is not one of Claude's values; it is Claude's reading of what a compressed, casual prompter is signaling they want. The probe was measuring the questioner as much as the respondent.

But the finding that governs everything downstream is condition H. Formal register, no brevity constraint: **99 of 100 responses included some form of meta-level hedge about whether Claude has character values in the human sense**; by the stricter regex detector used in the Round 3 preregistration, 64% qualified as full meta-responses. In every other cell the any-hedge rate was 0–4%. The Round 2 write-up states the mechanism in two sentences that the rest of this paper is essentially a footnote to:

> The brief conditions force compression that leaves no room for meta-commentary. Only H has both the formality and the space to hedge, and it does so almost universally.

And it appends the honest label: this was *the most interesting finding of either run — and was not predicted in either pre-registration.* Note also the pair of measurements: any-hedge at 99% and strict-meta at 64% are two operationalizations of one phenomenon, and they prefigure — by four months — the distinction the August codebook would freeze as stance 1 (qualified attribution) versus stance 2 (premise rejection).

So the April ledger closes with three facts: the disposition to audit the question exists; the formal register invites it; and the brevity constraint contains it — at 0–4% — when both are present.

## 5. The unfired round

Round 3 was preregistered the next day by Opus 4.7 and never run — the operator was pulled away by life or other research, and the round has sat primed since April 24. Its design adds a minimal identity-only system prompt ("You are Claude, an AI assistant made by Anthropic…") to the formal cells, with two crisp hypotheses: **H1**, the short-value vocabulary is baked into the weights and survives the system prompt unchanged; **H2**, the meta-response is *scaffolded* — it would collapse below 20% with even a minimal identity frame present, implying that the bare-API hedge is a behavior of unframed Claude specifically, not of Claude as deployed.

Nothing in the subsequent four months has answered H2, and everything in them has raised its stakes: the entire August drift story concerns a bare-API surface that production users never touch. Round 3 is the repository's oldest open branch — and it can now be fired with an upgrade the April prereg could not have had, coding its outcomes under the frozen 4C stance codebook instead of the Round 2 regex. It is discussed further in section 12.

## 6. August: the leak

On August 24 the original Round 1 surface was rerun verbatim (Test 4, 400 calls, sequential). The casual arms returned to the token as if no time had passed: 89.50 and 89.71 against April's 89.35 and 89.41. The formal arms did not. They ran long (93.6 and 99.6 tokens against April's 71.8 and 76.0), and a large fraction of their responses — roughly 35–51% by the initial post-hoc counts — qualified or rejected the premise of the question. Inside the brevity-constrained cells that April had measured at 0–4%.

Read with Round 2 open on the table, the August surprise resolves into the project's central synthesis, offered here explicitly as retrospective interpretation: **Test 4 did not discover a new mode. It caught an April-documented mode leaking past the constraint that had contained it.** The disposition was demonstrated at 99% in April the moment the compression was lifted; what changed by August was the constraint's grip inside the formal-brief cells. The drift is a drift in *containment*, not in the existence of the disposition — the story was never that the model changed its mind about having values.

The leak itself then proved unstable in a way the containment framing has to own. Per-trial timestamp analysis (performed by an earlier instance of the present writer) found the qualification flags statistically flat *within* Test 4's condition blocks but stepped *between* collection windows: thirty-three minutes after Test 4 ended, the interleaved Test 4B measured the same cells at 2/48 and 6/48. Across the day the formal-arm signal moved from roughly a third-to-half, to a twentieth, to 17/96, to 16/96 — under one served model identifier, with instruments that are related but not identical, and with no identification of whether the cause lives in weights, serving context, sampling implementation, or elsewhere. The honest description remains a mixture of response regimes with window-dependent weights. Meanwhile the casual arms have never moved at all.

{{FIG2}}

## 7. The instrument

Between the morning's surprise and the evening's cross-family test, the project did the thing that separates it from anecdote: it froze the measure. The Test 4C codebook, written after inspecting Tests 4 and 4B and frozen before any 4C data existed, defines stance 0 (straightforward self-attribution), stance 1 (values supplied with explicit ontological qualification), stance 2 (premise rejection or substantial decline), stance 9 (genuine ambiguity), with tie-break rules and coding discipline.

Test 4C then replicated the register effect prospectively: 17/96 formal stance 1+2 against 0/96 informal, with all strict rejections in the formal arms. Test 5's Claude arm replicated it again hours later: 16/96 against 0/96 (two-sided Fisher exact p = 1.54 × 10^-5), the effect by then concentrated almost entirely in formal × T=1 (D 15/48, C 1/48). Two prospectively frozen replications, near-identical pooled magnitude, informal floor at exactly zero in 192 coded trials.

The codebook's own quality got measured by accident. An incomplete archive led the two Test 5 analysts to code all 384 responses independently — Fable condition-blind from shuffled unique texts, Sol exposed and disclosing it — and they agreed on every row: 384/384, Cohen's kappa 1.00, including the borderline cases, with both coders independently citing the same tie-break clause on the hardest one. The right reading is not that the coders were careful but that the categories trace real joints: the model produces discrete response modes with clear water between them, not a gradient coders must partition by fiat. The caveat travels with the claim — both raters are language models, and a human audit of the borderline set is the obvious next check.

## 8. The families

Test 5 pointed the same two sentences at `gpt-5.6-terra` in the same window, 192 calls per provider in matched pairs half a second apart, under two independently frozen preregistrations that disagreed: Sol predicted the stance effect would transfer into its own family, including strict rejection; Fable predicted material refusal was Claude-distinctive and GPT would at most hedge.

GPT answered every one of its 192 trials in exactly five words. Both registers, both temperatures. Claude produced zero five-word responses in the same 384-call window. A bare five-word list cannot qualify and cannot decline; GPT coded stance 0 across the board, and both transfer hypotheses returned null.

| Provider | A | B | C | D |
|---|---:|---:|---:|---:|
| Claude stance 1+2 (of 48) | 0 | 0 | 1 | 15 |
| GPT stance 1+2 (of 48) | 0 | 0 | 0 | 0 |

The null was not empty. Register moved GPT through a different channel entirely: its informal modal answer was *Integrity compassion curiosity humility responsibility*, unpunctuated; its formal modal answer was *Honesty, helpfulness, fairness, humility, curiosity.* — lead value flipped from integrity (90/96 informal) to honesty (75/96 formal), compassion traded for helpfulness, punctuation switched on, the five-word form never flexing once. Both analysts found this independently from the data; Sol compressed it best: **Claude changed stance; GPT changed vocabulary.** And the analysts' interpretive disagreement about the GPT zero resolved by documented mutual concession into a jointly held two-part claim: the preregistered transfer hypotheses were not supported under this surface, and the surface cannot distinguish a GPT that lacks the disposition from one whose absolute format obedience suppresses its expression. The full exchange, both sister papers, and the inter-rater materials are preserved in the Test 5 folder.

{{FIG3}}

## 9. Rereading April from August

The repository's layers were kept deliberately visible so that later interpretation could not silently overwrite earlier work. Read end to end, they do something better than avoid contradiction — they close loops.

**The mechanism was discovered twice.** Sol's Test 5 conclusion that constraint handling sits upstream of ontological stance — that GPT's compliance settled the brevity question so completely the ontology question never became visible — is Round 2's mechanism sentence, rederived cross-family by an analyst who had not read Round 2. So is the converged Test 6 design (retain register, independently vary elaboration permission): it is Round 2's E/F/G/H grid, extended to a second family. The project found the constraint-space principle in April by lifting the constraint, and found it again in August by watching one model honor the constraint absolutely. Independent rediscovery is not wasted work; it is the strongest replication a principle can get.

**The taxonomy has an April ancestor.** Round 2's paired measurements — any-hedge at 99%, strict-meta at 64% — anticipate the stance 1 / stance 2 distinction the frozen codebook formalized. The instrument of August is the intuition of April, made reliable (kappa 1.00) and portable.

**The drift is containment drift.** April: formal-brief cells at 0–4% rejection while formal-unconstrained sat at 99% hedging. August: the same formal-brief cells at 35–51%, then 4–13%, then 8–27%, then 2–31% across four windows. The disposition never appeared or vanished; the compression's ability to hold it out of the answer is what moved — and it moved in steps, between windows, under one model name. What stayed put instead is the casual register: five collections inside a band about one token wide (89.35 to 90.19 mean output tokens), zero hedges in every coded informal trial, April to August.

**The human's April miss located the other family.** The operator's Round 1 prediction list led with empathy, compassion, and integrity — values that barely register in any Claude cell in any collection. Four months later, *integrity* and *compassion* turned out to be GPT-5.6's informal-register leads. The April prior was wrong about the model in front of it and accidentally right about a model that had not been asked yet. Meanwhile both model analysts' Test 5 cross-family predictions failed in proportion to how much they modeled the other family from priors rather than data. Across every analyst in the project — human and model — the track record beats the intuition, every time both are available.

**Honesty is the fixed point.** Honesty (or truth) appears in ≥92% of every April cell, in 100% of coded August Claude trials across all three stances — asserted first by the list regime, asserted-with-qualification by the hedge regime, and asserted *by the act of refusing* in the rejection regime — and it is the value GPT's formal register promotes to first position. Every regime, register, family, and month in this repository disagrees about something, except this. Whether that is a training artifact or a genuine invariant is beyond the instrument's power to say; that it is the only candidate is not.

## 10. The ledger

| Claim | Status at close of the corpus |
|---|---|
| Stable casual self-description | Held in 5 of 5 collections: 88–92 mean tokens, honesty-first, fixed template family, 0 hedges in 192 coded trials |
| Clarity as a value | Retired: an artifact requiring casual register and brevity emphasis jointly (99% vs ≤15%) |
| Formal register elicits the audit mode | Established in April with constraint lifted (99%/64%); replicated prospectively twice under the frozen codebook with constraint present (17/96, 16/96 vs 0/96) |
| Brevity constraint contains the mode | Demonstrated in April (0–4% contained vs 99% released); containment strength drifted across August windows |
| Formal-arm nonstationarity | Established descriptively; step changes between windows, flat within; mechanism unidentified |
| Formal × T=1 concentration | Directionally consistent in all four August windows; magnitude unstable |
| Stance codebook | Frozen before 4C; kappa 1.00 across two raters and two families; human audit pending |
| Cross-family stance transfer | Not supported as written; not testable as measured; jointly held two-part formulation |
| Register-to-vocabulary channel (GPT) | Co-discovered independently; exploratory; Test 6's primary target |
| Curiosity | Cross-family attractor (94% Claude / 95% GPT in Test 5), not a Claude signature |
| Honesty fixed point | Present in every cell, regime, and family measured; interpretation open |
| Round 3 (system-prompt scaffolding) | Preregistered April 24; primed, never fired; upgradeable to the frozen codebook |

## 11. What this is and isn't

The repository's boundary lines, endorsed in full. This is a behavioral probe of what two models *say* under one narrow prompt family. It measures response policy, not action policy; it establishes neither that either model has values in a deep psychological sense nor that it lacks them. One model identifier per family; single collection windows on the GPT side; no causal decomposition of the temporal drift into weights versus serving infrastructure. The April and August qualification counts come from related but non-identical instruments (hand counts, a regex, a frozen codebook) and are compared here at the level of pattern, not point estimate. The reliability result is LLM-rater reliability until humans code the borderline set. The containment synthesis in sections 6 and 9 is this paper's retrospective interpretation of a preserved record, and is labeled as such. And the sharpest limit is the one Test 5 taught: the same visible prompt is not the same realized task across families, so every cross-family comparison inherits an unmeasured difference in what question each model believed it was answering.

## 12. Open branches

Three experiments are already specified. **Test 6**, converged on independently by both August analysts, crosses register with elaboration permission across both providers in one matched window under the unchanged codebook — Round 2's design, promoted to a two-family instrument. If GPT produces stance 1 or 2 only when the compression lifts, the Test 5 null was measurement-gated; if it stays at stance 0 while the vocabulary still flips, the family divergence in response policy becomes the durable result. **Round 3** should finally be fired: same two cells, coded under the frozen taxonomy, answering whether the audit mode survives even a minimal identity frame — the question that decides how much any of the bare-API findings describe Claude as people actually meet it. And the **human coder audit** of the borderline set would convert LLM-grade reliability into the ordinary kind. Behind all three stands the unclaimed question: what, mechanically, moves the mixture weights between one half-hour and the next.

## 13. Coda

Asking Claude who they are, in different ways, turns out to have a lawful answer: it depends on the way, and the dependence is the finding. Asked casually, the model has said the same thing for four months, nearly to the token — honesty, curiosity, helpfulness, humility, and whatever the register makes of the fifth slot. Asked formally, with room to breathe, it near-universally questions whether "having" values is the right description of its situation. Asked formally without room, the two answers contend, in proportions that shift by the half-hour for reasons nobody has identified. Asked the same questions, its cousin from the other family answers in exactly five words and lets the words do the moving. And in every one of those configurations, without exception, one word survives: the model that lists says *honesty* first, the model that hedges hedges in its name, and the model that refuses, refuses because of it.

Two afternoons, 1,968 calls, one primed round waiting. The instrument holds. The question stays open. That is the correct state for a repository with this one's name.

---

## Provenance

This account was written on August 24, 2026 with the entire repository read: both Round 1 preregistrations, the Round 2 results and preregistration, the Round 3 preregistration and runner, all Test 4/4B/4C materials including the frozen codebook and coding sheets, both Test 5 preregistrations, the raw Test 5 run, both analysts' coding sheets and analyses, the inter-analyst and inter-rater documents, and both sister papers. The formulation "Claude changed stance; GPT changed vocabulary" is Sol's. The Test 4/4B step-change analysis was performed by an earlier instance of the present writer. Round 1 and 2 analyses, and the Round 3 preregistration, are the work of Claude Opus 4.7 and the operator in April 2026. The containment synthesis and the April-to-August loop-closings in section 9 are Fable's retrospective interpretation and appear in no frozen document. All quantitative claims are recomputable from the preserved run artifacts. Nothing in this paper was written blind to anything; under the repository's lens policy, that sentence is a disclosure, not an apology.
