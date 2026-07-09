"""
tests/test_export_pipeline.py

Sprint 2.2 Final - Export Pipeline Integration Test
"""

from pathlib import Path
import sys
import time

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from data.loader import load_master_files
from scheduling.schedule_factory import create_schedule
from scheduling.exporter import JSONExporter, CSVExporter, ExcelExporter


def build_filename(schedule, extension: str) -> str:
    """Build a standard SGS schedule export filename."""
    return (
        f"SGS_Schedule_"
        f"{schedule.division}_"
        f"{schedule.level}_"
        f"Term{schedule.term}_"
        f"{schedule.academic_year}_"
        f"v{schedule.version}."
        f"{extension}"
    )


def main():
    start = time.perf_counter()

    print("=" * 70)
    print("SGS Academic Planner - Export Pipeline")
    print("=" * 70)

    masters = load_master_files(PROJECT_ROOT / "masters")

    schedule = create_schedule(
        masters=masters,
        academic_year="2026-27",
        division="Kanishta",
        level=1,
        term=1,
    )

    output_folder = PROJECT_ROOT / "output" / schedule.academic_year
    output_folder.mkdir(parents=True, exist_ok=True)

    exports = [
        (JSONExporter(), "json"),
        (CSVExporter(), "csv"),
        (ExcelExporter(), "xlsx"),
    ]

    created = []

    for exporter, extension in exports:
        filename = build_filename(schedule, extension)
        path = output_folder / filename
        exporter.export(schedule, path)
        created.append(path)

    print("\nExport Summary")
    print("-" * 70)
    print(f"Schedule ID : {schedule.schedule_id}")
    print(f"Division    : {schedule.division}")
    print(f"Level       : {schedule.level}")
    print(f"Term        : {schedule.term}")
    print(f"Entries     : {len(schedule.entries)}")
    print()

    for path in created:
        print(f"✓ {path.name}")
        print(f"  {path.stat().st_size:,} bytes")

    print(f"\nCompleted in {time.perf_counter() - start:.2f} seconds")
    print("=" * 70)


if __name__ == "__main__":
    main()
