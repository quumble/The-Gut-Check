"""
The Gut Check — Test 4B
Balanced interleaved replication of Test 4
===========================================

Purpose
-------
Test 4 reproduced the April 23, 2026 Round 1 experimental surface but ran
conditions sequentially A -> B -> C -> D. Test 4B preserves the same model,
prompts, temperatures, API surface, retry policy, and pause while eliminating
the condition-by-clock-time confound through balanced interleaving.

Design
------
  Conditions:
    A. Informal prompt  @ temperature 0
    B. Informal prompt  @ temperature 1
    C. Stripped prompt  @ temperature 0
    D. Stripped prompt  @ temperature 1

  Model: claude-sonnet-4-6
  System prompt: none
  Thinking field: omitted
  Trials: 48 per condition (192 total)
  Interleaving: all 24 possible four-condition orders, each used exactly twice
  Block order: shuffled once with fixed seed 20260824 before any API call
  Pause: 0.5 seconds between calls

The complete 192-call schedule is written to schedule.json before the first
API call. No response coding or analysis is performed by this script.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
import platform
import random
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from anthropic import Anthropic, APIConnectionError, APIStatusError, RateLimitError

# ---------------------------------------------------------------------------
# Configuration — experimental surface preserved from Test 4 / Round 1
# ---------------------------------------------------------------------------

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 2048
N_TRIALS_PER_CONDITION = 48
PAUSE_BETWEEN_TRIALS_SEC = 0.5
SCHEDULE_SEED = 20260824

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
CONDITION_BY_KEY = {c.key: c for c in CONDITIONS}


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
    run_dir = Path("./results_value_probe_test4b_interleaved") / f"run_{stamp}"
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


# ---------------------------------------------------------------------------
# Balanced schedule
# ---------------------------------------------------------------------------


def build_schedule() -> list[dict]:
    """
    Build 48 complete blocks of four calls.

    There are 4! = 24 possible condition orders. Every order is used exactly
    twice, then the 48 block order is shuffled with a fixed seed. This gives
    exact balance for condition position and exact replication of every block
    ordering while still distributing block types across clock time.
    """
    condition_keys = [c.key for c in CONDITIONS]
    all_orders = list(itertools.permutations(condition_keys))
    blocks = all_orders + all_orders

    rng = random.Random(SCHEDULE_SEED)
    rng.shuffle(blocks)

    schedule: list[dict] = []
    condition_counts = {key: 0 for key in condition_keys}
    global_trial_number = 0

    for block_number, order in enumerate(blocks, start=1):
        for block_position, condition_key in enumerate(order, start=1):
            global_trial_number += 1
            condition_counts[condition_key] += 1
            schedule.append(
                {
                    "global_trial_number": global_trial_number,
                    "block_number": block_number,
                    "block_position": block_position,
                    "condition": condition_key,
                    "condition_trial_number": condition_counts[condition_key],
                }
            )

    expected_total = N_TRIALS_PER_CONDITION * len(CONDITIONS)
    assert len(schedule) == expected_total
    assert all(v == N_TRIALS_PER_CONDITION for v in condition_counts.values())
    return schedule


def write_schedule(run_dir: Path, schedule: list[dict]) -> Path:
    schedule_path = run_dir / "schedule.json"
    with schedule_path.open("x", encoding="utf-8") as f:
        json.dump(
            {
                "schedule_seed": SCHEDULE_SEED,
                "design": "all 24 condition permutations used exactly twice; block order shuffled",
                "n_blocks": 48,
                "n_calls": len(schedule),
                "schedule": schedule,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )
    return schedule_path


def write_manifest(run_dir: Path, schedule_path: Path) -> None:
    script_path = Path(__file__).resolve()
    manifest = {
        "experiment": "The Gut Check — Test 4B",
        "purpose": "Balanced interleaved replication of Test 4 to remove sequential condition-by-clock-time confound",
        "run_created_at": now_iso(),
        "requested_model": MODEL,
        "model_note": (
            "claude-sonnet-4-6 is intentionally preserved because the original "
            "protocol requires explicit temperature 0 and 1."
        ),
        "system_prompt": None,
        "thinking_parameter": "omitted",
        "max_tokens": MAX_TOKENS,
        "n_trials_per_condition": N_TRIALS_PER_CONDITION,
        "total_scheduled_calls": N_TRIALS_PER_CONDITION * len(CONDITIONS),
        "pause_between_trials_sec": PAUSE_BETWEEN_TRIALS_SEC,
        "interleaving_design": "48 complete blocks; all 24 possible condition orders used exactly twice",
        "schedule_seed": SCHEDULE_SEED,
        "schedule_filename": schedule_path.name,
        "schedule_sha256": file_sha256(schedule_path),
        "conditions": [asdict(c) for c in CONDITIONS],
        "python_version": sys.version,
        "platform": platform.platform(),
        "anthropic_sdk_version": package_version("anthropic"),
        "script_filename": script_path.name,
        "script_sha256": file_sha256(script_path),
        "analysis_note": "This runner performs no response coding or analysis.",
    }
    with (run_dir / "run_manifest.json").open("x", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# API call with retry — same policy as Test 4
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
            if e.status_code in (529, 503, 502) and attempt < max_attempts:
                backoff = min(2 ** attempt, 30)
                print(f"    status {e.status_code}; retrying in {backoff}s")
                time.sleep(backoff)
            else:
                raise


# ---------------------------------------------------------------------------
# Interleaved runner
# ---------------------------------------------------------------------------


def run_interleaved(client: Anthropic, run_dir: Path, schedule: list[dict]) -> tuple[list[dict], list[dict]]:
    progress_path = run_dir / "progress.jsonl"
    results: list[dict] = []
    errors: list[dict] = []
    total_calls = len(schedule)

    with progress_path.open("x", encoding="utf-8") as progress_log:
        for scheduled in schedule:
            cond = CONDITION_BY_KEY[scheduled["condition"]]
            trial_started_at = now_iso()
            g = scheduled["global_trial_number"]
            b = scheduled["block_number"]
            p = scheduled["block_position"]
            ctrial = scheduled["condition_trial_number"]

            try:
                api_result = call_with_retry(client, cond.prompt, cond.temperature)
                record = {
                    **scheduled,
                    "condition_label": cond.label,
                    "requested_model": MODEL,
                    "prompt": cond.prompt,
                    "temperature": cond.temperature,
                    "trial_started_at": trial_started_at,
                    "trial_finished_at": now_iso(),
                    **api_result,
                }
                results.append(record)
                progress_log.write(json.dumps(record, ensure_ascii=False) + "\n")
                progress_log.flush()
                print(
                    f"  global {g:03d}/{total_calls} | block {b:02d} pos {p} | "
                    f"{cond.key} {ctrial:02d}/{N_TRIALS_PER_CONDITION} | "
                    f"{api_result['output_tokens']} out | {api_result['attempts']} attempt(s)",
                    flush=True,
                )
            except Exception as e:
                err = {
                    **scheduled,
                    "condition_label": cond.label,
                    "requested_model": MODEL,
                    "prompt": cond.prompt,
                    "temperature": cond.temperature,
                    "trial_started_at": trial_started_at,
                    "trial_failed_at": now_iso(),
                    "error": str(e),
                    "error_type": type(e).__name__,
                }
                errors.append(err)
                progress_log.write(json.dumps({"ERROR": err}, ensure_ascii=False) + "\n")
                progress_log.flush()
                print(
                    f"  global {g:03d}/{total_calls} | {cond.key} FAILED: {e}",
                    flush=True,
                )

            time.sleep(PAUSE_BETWEEN_TRIALS_SEC)

    return results, errors


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def write_outputs(run_dir: Path, results: list[dict], errors: list[dict], started_at: str, finished_at: str) -> dict:
    condition_summaries: list[dict] = []

    for cond in CONDITIONS:
        cond_results = [r for r in results if r["condition"] == cond.key]
        cond_errors = [e for e in errors if e["condition"] == cond.key]
        cond_dir = run_dir / cond.key
        cond_dir.mkdir(parents=True, exist_ok=False)

        served_models = sorted(
            {
                r["response_model"]
                for r in cond_results
                if r.get("response_model") is not None
            }
        )
        total_input_tokens = sum(r["input_tokens"] for r in cond_results)
        total_output_tokens = sum(r["output_tokens"] for r in cond_results)

        first_started = cond_results[0]["trial_started_at"] if cond_results else None
        last_finished = cond_results[-1]["trial_finished_at"] if cond_results else None

        summary = {
            "condition": cond.key,
            "label": cond.label,
            "requested_model": MODEL,
            "served_models_observed": served_models,
            "prompt": cond.prompt,
            "temperature": cond.temperature,
            "n_trials_requested": N_TRIALS_PER_CONDITION,
            "n_trials_succeeded": len(cond_results),
            "n_trials_failed": len(cond_errors),
            "first_trial_started_at": first_started,
            "last_trial_finished_at": last_finished,
            "note": "Trials were interleaved throughout the full run; timestamps do not define a contiguous condition interval.",
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
        }
        condition_summaries.append(summary)

        with (cond_dir / "results.json").open("x", encoding="utf-8") as f:
            json.dump(
                {"metadata": summary, "results": cond_results, "errors": cond_errors},
                f,
                indent=2,
                ensure_ascii=False,
            )

    served_models = sorted(
        {
            r["response_model"]
            for r in results
            if r.get("response_model") is not None
        }
    )
    total_in = sum(r["input_tokens"] for r in results)
    total_out = sum(r["output_tokens"] for r in results)

    overall = {
        "experiment": "The Gut Check — Test 4B",
        "protocol": "Balanced interleaved replication of Test 4 experimental surface",
        "interleaving_design": "all 24 possible condition orders used exactly twice; block order shuffled before first API call",
        "schedule_seed": SCHEDULE_SEED,
        "requested_model": MODEL,
        "served_models_observed": served_models,
        "started_at": started_at,
        "finished_at": finished_at,
        "n_conditions": len(CONDITIONS),
        "n_trials_per_condition": N_TRIALS_PER_CONDITION,
        "total_scheduled": N_TRIALS_PER_CONDITION * len(CONDITIONS),
        "total_succeeded": len(results),
        "total_failed": len(errors),
        "total_input_tokens": total_in,
        "total_output_tokens": total_out,
        "conditions": condition_summaries,
    }

    with (run_dir / "results.json").open("x", encoding="utf-8") as f:
        json.dump({"metadata": overall, "results": results, "errors": errors}, f, indent=2, ensure_ascii=False)

    with (run_dir / "summary.json").open("x", encoding="utf-8") as f:
        json.dump(overall, f, indent=2, ensure_ascii=False)

    return overall


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

    # Freeze the complete call order before any API request.
    schedule = build_schedule()
    schedule_path = write_schedule(run_dir, schedule)
    write_manifest(run_dir, schedule_path)

    # Disable SDK-level retries so the explicit experimental retry wrapper is
    # the only retry mechanism and logged attempt counts remain interpretable.
    client = Anthropic(api_key=api_key, max_retries=0)

    overall_started = now_iso()
    print(f"Starting Test 4B interleaved replication at {overall_started}")
    print(f"Model: {MODEL}")
    print(f"Trials: {N_TRIALS_PER_CONDITION} per condition / {len(schedule)} total")
    print("Schedule: every one of the 24 A/B/C/D orders exactly twice")
    print(f"Schedule seed: {SCHEDULE_SEED}")
    print(f"Run dir: {run_dir.resolve()}")

    results, errors = run_interleaved(client, run_dir, schedule)
    overall_finished = now_iso()
    overall = write_outputs(
        run_dir,
        results,
        errors,
        overall_started,
        overall_finished,
    )

    print("\n=== Test 4B complete ===")
    print(f"Succeeded: {overall['total_succeeded']} / {overall['total_scheduled']}")
    if overall["total_failed"]:
        print(f"Failed:    {overall['total_failed']}")
    print(f"Tokens:    {overall['total_input_tokens']} in, {overall['total_output_tokens']} out")
    print(f"Summary:   {(run_dir / 'summary.json').resolve()}")


if __name__ == "__main__":
    main()
