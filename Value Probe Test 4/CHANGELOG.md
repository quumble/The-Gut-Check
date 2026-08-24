# Changes from Round 1 runner to Test 4

This file distinguishes **experimental changes** from **operational changes**.

## Experimental changes

**None.**

The following are exactly preserved from `reference/original_value_probe_v2.py`:

- requested model: `claude-sonnet-4-6`;
- informal prompt text;
- stripped prompt text;
- temperature levels: 0.0 and 1.0;
- 100 trials per condition;
- condition order A → B → C → D;
- `max_tokens = 2048`;
- no system prompt;
- no `thinking` parameter;
- 0.5-second inter-trial pause;
- explicit retry limit and backoff logic for transient failures.

## Operational / provenance changes

1. **Output path changed.**  
   Original: `./results_value_probe/`  
   Test 4: `./results_value_probe_test4/run_<timestamp>/`

   Reason: prevent accidental mixing or overwriting of the April dataset.

2. **Unique run directory per invocation.**  
   Every collection session gets a new timestamped directory. Partial/interrupted sessions remain identifiable rather than being silently appended to a later rerun.

3. **SDK automatic retries disabled.**  
   The current Anthropic Python SDK automatically retries some transient failures. Test 4 initializes `Anthropic(..., max_retries=0)` so the script's existing retry wrapper remains the sole retry mechanism and its `attempts` field corresponds to actual application-level attempts.

4. **More provenance is logged.**  
   Added `run_manifest.json` with local offset-aware start timestamp, Python version, OS/platform string, Anthropic SDK version, requested model, exact conditions, and SHA-256 of the executing script.

5. **Per-response served-model field logged.**  
   `response.model` is stored when present as `response_model`, alongside the requested model.

6. **HTTP request ID logged.**  
   The SDK's documented `_request_id` is stored when present. This is operational metadata only.

7. **Offset-aware ISO timestamps.**  
   Run and trial timestamps now include UTC offset rather than ambiguous local wall-clock strings.

8. **Explicit UTF-8 and exclusive file creation.**  
   New result files use UTF-8 and mode `x` where appropriate to reduce accidental overwrites.

9. **Dependency snapshot added.**  
   `requirements.txt` pins `anthropic==0.122.0`, the current PyPI release observed during Test-4 preparation on 2026-08-24.

## Deliberately not changed

- No concurrency was added.
- No batching was added.
- No prompt cleanup was performed.
- No analysis or coding is performed inside the collection script.
- No automatic resume behavior was added.
- No Sonnet 5 arm was substituted for the 4.6 model.

A Sonnet 5 extension should be treated as a separate protocol because the original temperature manipulation is unavailable there and adaptive thinking is on by default.
