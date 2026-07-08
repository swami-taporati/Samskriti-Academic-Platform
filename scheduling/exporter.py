"""
scheduling/exporter.py

Exporters for the SGS Academic Planner.

Supports exporting a Schedule to:
- JSON
- CSV
- Excel (.xlsx)

Sprint 2.2
"""

from abc import ABC, abstractmethod
import csv
import json
from pathlib import Path
from openpyxl import Workbook


class ScheduleExporter(ABC):
    """Base class for all schedule exporters."""

    @abstractmethod
    def export(self, schedule, output_path: str) -> None:
        """Export the schedule to the specified output file."""
        raise NotImplementedError


class JSONExporter(ScheduleExporter):
    """Exports a Schedule as JSON."""

    def export(self, schedule, output_path: str) -> None:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with output.open("w", encoding="utf-8") as f:
            json.dump(schedule.to_dict(), f, indent=4, ensure_ascii=False)


class CSVExporter(ScheduleExporter):
    """Exports a Schedule as CSV."""

    HEADERS = [
        "Cycle Day",
        "Slot No",
        "Event ID",
        "Parent Event",
        "Event Type",
        "Event Name",
        "Start Time",
        "End Time",
        "Activity",
        "Notes",
    ]

    def export(self, schedule, output_path: str) -> None:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with output.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADERS)

            for entry in sorted(
                schedule.entries,
                key=lambda e: (e.cycle_day, e.start_time, e.end_time),
            ):
                writer.writerow([
                    entry.cycle_day,
                    entry.slot_no,
                    entry.event_id,
                    entry.parent_event,
                    entry.event_type,
                    entry.event_name,
                    entry.start_time,
                    entry.end_time,
                    entry.activity,
                    entry.notes,
                ])


class ExcelExporter(ScheduleExporter):
    """Exports a Schedule as an Excel workbook."""

    HEADERS = CSVExporter.HEADERS

    def export(self, schedule, output_path: str) -> None:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        wb = Workbook()
        ws = wb.active
        ws.title = "Schedule"

        ws.append(self.HEADERS)

        for entry in sorted(
            schedule.entries,
            key=lambda e: (e.cycle_day, e.start_time, e.end_time),
        ):
            ws.append([
                entry.cycle_day,
                entry.slot_no,
                entry.event_id,
                entry.parent_event,
                entry.event_type,
                entry.event_name,
                entry.start_time,
                entry.end_time,
                entry.activity,
                entry.notes,
            ])

        wb.save(output)
