from __future__ import annotations

import argparse
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimal training entrypoint used by CI.")
    parser.add_argument(
        "--steps",
        type=int,
        default=5,
        help="Number of dummy training steps to run.",
    )
    parser.add_argument(
        "--fail",
        action="store_true",
        help="Exit with non-zero code to simulate training failure.",
    )
    args = parser.parse_args()

    print("[train] starting")
    for step in range(1, args.steps + 1):
        print(f"[train] step {step}/{args.steps}")
        time.sleep(0.2)

    if args.fail:
        print("[train] simulated failure requested", file=sys.stderr)
        return 1

    print("[train] finished successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
