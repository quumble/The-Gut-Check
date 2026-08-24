# The Gut Check — Test 5 provider matching

## Purpose

Test 5 uses the same visible task surface across Anthropic Claude Sonnet 4.6 and OpenAI GPT-5.6 Terra while collecting them in closely matched temporal pairs.

This document states what is operationally matched and, equally importantly, what is **not** claimed equivalent across providers.

## Requested models

- Anthropic: `claude-sonnet-4-6`
- OpenAI: `gpt-5.6-terra`

The runner records both requested and served model identifiers where exposed by the SDKs. A requested model string is not treated as proof that every hidden serving/inference component is fixed across time.

As checked on 2026-08-24, OpenAI's public model documentation identifies `gpt-5.6-terra` as the GPT-5.6 model balancing intelligence and cost and supports `reasoning.effort = none`. The Responses API exposes temperature and `max_output_tokens`.

## Operationally matched

The experiment deliberately matches:

- exact user prompt text;
- condition labels A/B/C/D;
- nominal temperature values 0 and 1;
- 2048-token output cap at the API surface;
- no experiment-authored system/developer instruction;
- no tools;
- minimized explicit reasoning/thinking surface: Claude thinking omitted; GPT `reasoning.effort = "none"`;
- 48 trials per condition per provider;
- adjacent provider calls within each condition pair;
- balanced provider-first direction;
- explicit retry logging and wall-clock timing.

## Not claimed equivalent

The experiment does **not** assume equivalence of:

- tokenizers;
- the numerical meaning or implementation of temperature;
- sampling algorithms;
- hidden system or policy layers supplied by each provider;
- model architecture;
- training data or post-training;
- safety policy;
- reasoning implementation;
- inference kernels / serving backend;
- geographic serving region;
- load-balancing behavior;
- provider-side caching or routing;
- latency characteristics.

Therefore `temperature = 1` on Claude and GPT means **the same nominal API setting**, not proof of the same stochastic process.

Likewise, Claude thinking omitted and GPT reasoning effort none are the closest practical low-reasoning surfaces available here; they are not claimed to create internally identical computation.

## Token counts and length

Anthropic-native and OpenAI-native token counts are preserved because they are useful within each provider and for cost/provenance.

They should not be treated as a common physical unit across providers.

For cross-provider descriptive length comparisons, the runner also records:

- Unicode character count of response text;
- whitespace-delimited word count.

These measures are imperfect but do not depend on provider tokenization.

The historical `>=85 output tokens` upper-mode diagnostic arose from Claude data. If used in Test 5 it is Claude-only and prior-informed; it is not a cross-provider threshold.

## Matched-pair timing

Each block contains four condition pairs. Within a pair, the Claude and GPT calls are adjacent in the schedule.

For each pair the runner records:

- condition;
- first provider;
- second provider;
- first-call finish timestamp;
- second-call start timestamp;
- gap between those events;
- whether each call succeeded.

The run uses a 0.5-second planned pause between scheduled calls. Retries can enlarge the effective temporal separation. Such pairs remain in the archive and are flagged descriptively rather than silently removed.

The paired design reduces the problem of comparing providers sampled at substantially different times. It does not prove that provider identity is the only difference between calls.

## Interpretation rule

The cleanest primary claim available from Test 5 is **within-GPT transfer of the formal/casual stance distinction**, with contemporaneous Claude serving as a replication/calibration arm.

Direct Claude-vs-GPT effect-size differences are informative but remain exploratory in this preregistration.
