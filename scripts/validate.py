#!/usr/bin/env python3
"""Validate the structured paper catalogue without third-party dependencies."""

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
REQUIRED = {
    "id", "title", "year", "venue", "publication_status", "task", "family",
    "paper_url", "code_url", "core_idea_zh", "training", "evaluation", "audit"
}
TRAINING_REQUIRED = {
    "datasets", "crop_or_resolution", "optimizer", "learning_rate", "batch_size",
    "schedule", "hardware", "pretrained_models", "notes"
}


def is_url_or_empty(value):
    if value in (None, ""):
        return True
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main():
    papers = json.loads(DATA.read_text(encoding="utf-8"))
    errors = []
    ids = set()
    for index, paper in enumerate(papers):
        label = paper.get("id", f"index:{index}")
        missing = REQUIRED - paper.keys()
        if missing:
            errors.append(f"{label}: missing {sorted(missing)}")
        if label in ids:
            errors.append(f"{label}: duplicate id")
        ids.add(label)
        if paper.get("task") not in {"image", "video", "image+video"}:
            errors.append(f"{label}: invalid task")
        if paper.get("publication_status") not in {"peer_reviewed", "preprint"}:
            errors.append(f"{label}: invalid publication_status")
        if not is_url_or_empty(paper.get("paper_url")):
            errors.append(f"{label}: invalid paper_url")
        if not is_url_or_empty(paper.get("code_url")):
            errors.append(f"{label}: invalid code_url")
        training = paper.get("training", {})
        missing_training = TRAINING_REQUIRED - training.keys()
        if missing_training:
            errors.append(f"{label}: missing training fields {sorted(missing_training)}")
        if not paper.get("core_idea_zh", "").strip():
            errors.append(f"{label}: empty Chinese summary")
    if errors:
        print("Validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(papers)} paper records.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

