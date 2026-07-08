"""
tests/test_export_pipeline.py

Integration test for the SGS Academic Planner export pipeline.

Pipeline:
Knowledge Masters -> Loader -> Schedule Factory -> Exporters
"""

from pathlib import Path

from data.loader import load_master_files
from scheduling.schedule_factory import create_schedule
from scheduling.exporter import JSONExporter, CSVExporter, ExcelExporter


def main():
    print("=" * 70)
    print("SGS Academic Planner - Export Pipeline Test")
    print("=" * 70)

    masters_folder = "masters"
    output_folder = Path("output") / "2026-27"
    output_folder.mkdir(parents=True, exist_ok=True)

    print("\nLoading Knowledge Masters...")
    masters = load_master_files(masters_folder)
    print(f"Loaded {len(masters)} master workbook(s).")

    print("\nCreating schedule...")
    schedule = create_schedule(
        masters=masters,
        academic_year="2026-27",
        division="Kanishta",
        level=1,
        term=1,
    )

    print(schedule)
    print(f"Entries           : {len(schedule.entries)}")
    print(f"Learning Slots    : {schedule.total_learning_slots()}")
    print(f"Days              : {schedule.total_days()}")

    print("\nExporting...")

    json_file = output_folder / "schedule.json"
    csv_file = output_folder / "schedule.csv"
    excel_file = output_folder / "schedule.xlsx"

    JSONExporter().export(schedule, json_file)
    CSVExporter().export(schedule, csv_file)
    ExcelExporter().export(schedule, excel_file)

    print("\nVerifying output files...")

    for f in (json_file, csv_file, excel_file):
        if f.exists():
            print(f"✓ {f.name} ({f.stat().st_size:,} bytes)")
        else:
            raise FileNotFoundError(f"{f} was not created.")

    print("\n" + "=" * 70)
    print("PASS - Export pipeline completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
