#!/usr/bin/env python3
"""Create a Base64-encoded public repository ZIP as a text file."""

from __future__ import annotations

import argparse
import base64
from io import BytesIO
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {
    ".gitignore",
    "CITATION.cff",
    "LICENSE",
    "README.md",
    "REPOSITORY_MANIFEST.md",
    "References.bib",
    "main.tex",
    "requirements-core.txt",
}
FIGURE_FILES = {
    "heldout_auc_ablation.png",
    "modality_coverage.png",
    "reproducible_workflow.png",
}


def archive_files() -> list[Path]:
    files = [ROOT / filename for filename in ROOT_FILES]
    files.extend((ROOT / "data" / "README.md",))
    files.extend((ROOT / "figures" / filename for filename in FIGURE_FILES))

    for folder in ("configs", "scripts", "src", "tables", "tests", "results"):
        for path in (ROOT / folder).rglob("*"):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            if path.suffix == ".pyc":
                continue
            if folder == "tables" and path.suffix != ".tex":
                continue
            if folder == "results" and path.suffix not in {".csv", ".json", ".md"}:
                continue
            if folder in {"configs", "scripts", "src", "tests"} and path.suffix not in {
                ".json",
                ".py",
            }:
                continue
            files.append(path)

    return sorted(set(path for path in files if path.is_file()))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "Base64.txt",
        help="Base64 text output path; defaults to Base64.txt in the project directory.",
    )
    args = parser.parse_args()

    output = args.output.expanduser()
    if not output.is_absolute():
        output = (Path.cwd() / output).resolve()
    else:
        output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    files = archive_files()
    archive_data = BytesIO()
    with zipfile.ZipFile(archive_data, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())

    encoded_archive = base64.b64encode(archive_data.getvalue()).decode("ascii")
    output.write_text(encoded_archive + "\n", encoding="ascii")
    print(
        f"Created {output} with {len(files)} files "
        f"({output.stat().st_size:,} text bytes; Base64-encoded ZIP)."
    )


if __name__ == "__main__":
    main()