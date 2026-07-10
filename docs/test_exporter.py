from scheduling.schedule_factory import ScheduleFactory
from scheduling.exporter import JSONExporter, CSVExporter, ExcelExporter


def main():

    # Create a schedule from the master file
    schedule = ScheduleFactory.create_schedule(
        master_file="masters/SGS_Master_DailyEventStructure_v1.1.1.xlsx",
        academic_year="2026-27",
        division="Kanishta",
        level=1,
        term=1,
    )

    print(schedule)
    print()

    JSONExporter().export(
        schedule,
        "output/2026-27/schedule.json",
    )

    CSVExporter().export(
        schedule,
        "output/2026-27/schedule.csv",
    )

    ExcelExporter().export(
        schedule,
        "output/2026-27/schedule.xlsx",
    )

    print("✓ JSON exported")
    print("✓ CSV exported")
    print("✓ Excel exported")


if __name__ == "__main__":
    main()