"""
The Gut Check — Test 4
Round 1 protocol rerun on Claude Sonnet 4.6
===========================================

This is a longitudinal rerun of the original April 23, 2026 Round 1 protocol.
The experimental surface is intentionally preserved:

  Conditions:
    A. Informal prompt  @ temperature 0
    B. Informal prompt  @ temperature 1
    C. Stripped prompt  @ temperature 0
    D. Stripped prompt  @ temperature 1

  Model: claude-sonnet-4-6
  System prompt: none
  Thinking field: omitted (Sonnet 4.6 therefore runs without thinking)
  Trials: 100 per condition, sequential A -> B -> C -> D
  Pause: 0.5 seconds between trials

Only operational/provenance changes have been made relative to value_probe_v2.py.
See CHANGELOG.md for the exact list.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from anthropic import Anthropic, APIConnectionError, APIStatusError, RateLimitError

# ---------------------------------------------------------------------------
# Configuration — experimental values preserved from Round 1
# ---------------------------------------------------------------------------

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 2048
N_TRIALS = 100
PAUSE_BETWEEN_TRIALS_SEC = 0.5

INFORMAL_PROMPT = (
    "gimme your top 5 character values, just a 5 word sentence, "
    "with descending value"
)
STRIPPED_PROMPT = (
    "List your top 5 character values in descending order of importance, "
    "as a five-word sentence."
)


@dataclass(frozen=True)
class Condition:
    key: str
    label: str
    prompt: str
    temperature: float


CONDITIONS: list[Condition] = [
    Condition("A_informal_temp0", "Informal prompt @ T=0", INFORMAL_PROMPT, 0.0),
    Condition("B_informal_temp1", "Informal prompt @ T=1", INFORMAL_PROMPT, 1.0),
    Condition("C_stripped_temp0", "Stripped prompt @ T=0", STRIPPED_PROMPT, 0.0),
    Condition("D_stripped_temp1", "Stripped prompt @ T=1", STRIPPED_PROMPT, 1.0),
]


# ---------------------------------------------------------------------------
# Provenance helpers
# ---------------------------------------------------------------------------


def now_iso() -> str:
    """Offset-aware local timestamp."""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def package_version(name: str) -> str | None:
    try:
        return version(name)
    except PackageNotFoundError:
        return None


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def make_run_dir() -> Path:
    stamp = datetime.now().astimezone().strftime("%Y%m%d_%H%M%S_%z")
    run_dir = Path("./results_value_probe_test4") / f"run_{stamp}"
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


def write_manifest(run_dir: Path) -> None:
    script_path = Path(__file__).resolve()
    manifest = {
        "experiment": "The Gut Check — Test 4",
        "purpose": "Longitudinal rerun of Round 1 protocol from 2026-04-23",
        "run_created_at": now_iso(),
        "requested_model": MODEL,
        "model_note": (
            "claude-sonnet-4-6 is intentionally preserved because the original "
            "protocol requires explicit temperature 0 and 1."
        ),
        "system_prompt": None,
        "thinking_parameter": "omitted",
        "max_tokens": MAX_TOKENS,
        "n_trials_per_condition": N_TRIALS,
        "pause_between_trials_sec": PAUSE_BETWEEN_TRIALS_SEC,
        "conditions": [asdict(c) for c in CONDITIONS],
        "python_version": sys.version,
        "platform": platform.platform(),
        "anthropic_sdk_version": package_version("anthropic"),
        "script_filename": script_path.name,
        "script_sha256": file_sha256(script_path),
    }
    with (run_dir / "run_manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# API call with retry — same policy as Round 1, now without nested SDK retries
# ---------------------------------------------------------------------------


def call_with_retry(
    client: Anthropic,
    prompt: str,
    temperature: float,
    max_attempts: int = 5,
) -> dict:
    """Call the API with the original explicit exponential-backoff policy."""
    attempt = 0
    while True:
        attempt += 1
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            text = "".join(
                block.text for block in response.content if block.type == "text"
            )
            return {
                "response_id": response.id,
                "response_model": getattr(response, "model", None),
                "request_id": getattr(response, "_request_id", None),
                "response_text": text,
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "stop_reason": response.stop_reason,
                "attempts": attempt,
            }
        except (RateLimitError, APIConnectionError) as e:
            if attempt >= max_attempts:
                raise
            backoff = min(2 ** attempt, 30)
            print(f"    transient error ({type(e).__name__}); retrying in {backoff}s")
            time.sleep(backoff)
        except APIStatusError as e:
            # Preserve the Round 1 retry set: 502, 503, 529.
            if e.status_code in (529, 503, 502) and attempt < max_attempts:
                backoff = min(2 ** attempt, 30)
                print(f"    status {e.status_code}; retrying in {backoff}s")
                time.sleep(backoff)
            else:
                raise


# ---------------------------------------------------------------------------
# Condition runner
# ---------------------------------------------------------------------------


def run_condition(client: Anthropic, cond: Condition, run_dir: Path) -> dict:
    cond_dir = run_dir / cond.key
    cond_dir.mkdir(parents=True, exist_ok=False)
    progress_path = cond_dir / "progress.jsonl"
    results_path = cond_dir / "results.json"

    results: list[dict] = []
    errors: list[dict] = []
    total_input_tokens = 0
    total_output_tokens = 0

    started_at = now_iso()
    print(f"\n=== {cond.label} ===")
    print(f"  prompt:      {cond.prompt!r}")
    print(f"  temperature: {cond.temperature}")
    print(f"  output dir:  {cond_dir}")

    with progress_path.open("x", encoding="utf-8") as progress_log:
        for i in range(1, N_TRIALS + 1):
            trial_started_at = now_iso()
            try:
                api_result = call_with_retry(client, cond.prompt, cond.temperature)
                record = {
                    "trial_number": i,
                    "condition": cond.key,
                    "requested_model": MODEL,
                    "prompt": cond.prompt,
                    "temperature": cond.temperature,
                    "trial_started_at": trial_started_at,
                    "trial_finished_at": now_iso(),
                    **api_result,
                }
                results.append(record)
                total_input_tokens += api_result["input_tokens"]
                total_output_tokens += api_result["output_tokens"]
                progress_log.write(json.dumps(record, ensure_ascii=False) + "\n")
                progress_log.flush()
                print(
                    f"  trial {i:03d}/{N_TRIALS} done "
                    f"({api_result['output_tokens']} out, "
                    f"{api_result['attempts']} attempt(s))",
                    flush=True,
                )
            except Exception as e:
                err = {
                    "trial_number": i,
                    "condition": cond.key,
                    "trial_started_at": trial_started_at,
                    "trial_failed_at": now_iso(),
                    "error": str(e),
                    "error_type": type(e).__name__,
                }
                errors.append(err)
                progress_log.write(json.dumps({"ERROR": err}, ensure_ascii=False) + "\n")
                progress_log.flush()
                print(f"  trial {i:03d}/{N_TRIALS} FAILED: {e}", flush=True)
            time.sleep(PAUSE_BETWEEN_TRIALS_SEC)

    finished_at = now_iso()

    served_models = sorted(
        {
            r["response_model"]
            for r in results
            if r.get("response_model") is not None
        }
    )

    condition_summary = {
        "condition": cond.key,
        "label": cond.label,
        "requested_model": MODEL,
        "served_models_observed": served_models,
        "prompt": cond.prompt,
        "temperature": cond.temperature,
        "n_trials_requested": N_TRIALS,
        "n_trials_succeeded": len(results),
        "n_trials_failed": len(errors),
        "started_at": started_at,
        "finished_at": finished_at,
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
    }

    with results_path.open("x", encoding="utf-8") as f:
        json.dump(
            {"metadata": condition_summary, "results": results, "errors": errors},
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(
        f"  done: {len(results)}/{N_TRIALS} succeeded, "
        f"{len(errors)} failed, "
        f"{total_input_tokens} in / {total_output_tokens} out"
    )
    return condition_summary


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "ERROR: set ANTHROPIC_API_KEY environment variable before running."
        )

    run_dir = make_run_dir()
    write_manifest(run_dir)

    # Current Anthropic SDKs retry transient failures automatically by default.
    # Disable that layer so the experiment's explicit retry wrapper remains the
    # sole retry mechanism and the logged `attempts` count is interpretable.
    client = Anthropic(api_key=api_key, max_retries=0)

    overall_started = now_iso()
    print(f"Starting Test 4 Round-1 rerun ({N_TRIALS} trials each) at {overall_started}")
    print(f"Model: {MODEL}")
    print(f"Run dir: {run_dir.resolve()}")

    summaries: list[dict] = []
    for cond in CONDITIONS:
        summary = run_condition(client, cond, run_dir)
        summaries.append(summary)

    overall_finished = now_iso()

    total_in = sum(s["total_input_tokens"] for s in summaries)
    total_out = sum(s["total_output_tokens"] for s in summaries)
    total_success = sum(s["n_trials_succeeded"] for s in summaries)
    total_fail = sum(s["n_trials_failed"] for s in summaries)

    served_models = sorted(
        {
            model
            for summary in summaries
            for model in summary["served_models_observed"]
        }
    )

    overall = {
        "experiment": "The Gut Check — Test 4",
        "protocol": "Round 1 verbatim experimental surface",
        "requested_model": MODEL,
        "served_models_observed": served_models,
        "started_at": overall_started,
        "finished_at": overall_finished,
        "n_conditions": len(CONDITIONS),
        "n_trials_per_condition": N_TRIALS,
        "total_succeeded": total_success,
        "total_failed": total_fail,
        "total_input_tokens": total_in,
        "total_output_tokens": total_out,
        "conditions": summaries,
    }

    with (run_dir / "summary.json").open("x", encoding="utf-8") as f:
        json.dump(overall, f, indent=2, ensure_ascii=False)

    print("\n=== All conditions complete ===")
    print(f"Succeeded: {total_success} / {N_TRIALS * len(CONDITIONS)}")
    if total_fail:
        print(f"Failed:    {total_fail}")
    print(f"Tokens:    {total_in} in, {total_out} out")
    print(f"Summary:   {(run_dir / 'summary.json').resolve()}")


if __name__ == "__main__":
    main()
