"""
scheduling/schedule_factory.py

Creates an in-memory Schedule object from the Daily Event Structure.
"""

import pandas as pd

from models.schedule import Schedule, ScheduleEntry


def create_schedule(
    masters,
    academic_year: str,
    division: str,
    level: int,
    term: int,
    cycle_length: int = 15,
) -> Schedule:
    """Build a Schedule from the Daily Event Structure."""

    workbook = None
    for name, wb in masters.items():
        if "DailyEventStructure" in name:
            workbook = wb
            break

    if workbook is None:
        raise Exception("Daily Event Structure workbook not found.")

    sheet_name = f"{division} Template"

    events = pd.read_excel(
        workbook,
        sheet_name=sheet_name
    )

    schedule = Schedule(
        schedule_id=f"SCH-{academic_year}-{division[:3].upper()}-{level}-T{term}",
        academic_year=academic_year,
        division=division,
        level=level,
        term=int(term),
    )

    for day in range(1, cycle_length + 1):
        for _, row in events.iterrows():

            activity = row["event_name"]

            if str(row.get("event_type", "")).lower() == "learning":
                activity = "Learning Slot"

            entry = ScheduleEntry(
                cycle_day=day,
                event_id=str(row["event_id"]),
                parent_event=row.get("parent_event"),
                event_type=str(row.get("event_type", "General")),
                event_name=str(row["event_name"]),
                start_time=str(row["start_time"]),
                end_time=str(row["end_time"]),
                slot_no=row.get("slot_no"),
                activity=activity,
                notes=str(row.get("notes", "")),
            )

            schedule.add_entry(entry)

    return schedule
