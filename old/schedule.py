"""
models/schedule.py

Core domain models for the SGS Academic Planner.

These classes represent a schedule in memory. They do not contain any
allocation logic or Excel-specific code.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ScheduleEntry:
    cycle_day: int

    event_id: str
    parent_event: Optional[str]

    event_type: str
    event_name: str

    start_time: str
    end_time: str

    slot_no: Optional[int]

    # Initially this will be "Learning Slot".
    # Later the allocator replaces it with "English", "Math", etc.
    activity: str

    notes: str = ""

    @property
    def is_learning_slot(self) -> bool:
        return self.event_type.lower() == "learning"

    @property
    def is_fixed_event(self) -> bool:
        return not self.is_learning_slot


@dataclass
class Schedule:
    schedule_id: str

    academic_year: str
    division: str
    level: int
    term: int

    version: str = "1.0"

    entries: List[ScheduleEntry] = field(default_factory=list)

    def add_entry(self, entry: ScheduleEntry) -> None:
        self.entries.append(entry)

    def get_day(self, cycle_day: int) -> List[ScheduleEntry]:
        return sorted(
            [e for e in self.entries if e.cycle_day == cycle_day],
            key=lambda x: (x.start_time, x.end_time),
        )

    def get_learning_slots(self) -> List[ScheduleEntry]:
        return [e for e in self.entries if e.is_learning_slot]

    def get_fixed_events(self) -> List[ScheduleEntry]:
        return [e for e in self.entries if e.is_fixed_event]

    def total_days(self) -> int:
        if not self.entries:
            return 0
        return max(e.cycle_day for e in self.entries)

    def total_learning_slots(self) -> int:
        return len(self.get_learning_slots())

    def summary(self) -> dict:
        return {
            "schedule_id": self.schedule_id,
            "academic_year": self.academic_year,
            "division": self.division,
            "level": self.level,
            "term": self.term,
            "version": self.version,
            "days": self.total_days(),
            "entries": len(self.entries),
            "learning_slots": self.total_learning_slots(),
        }

    def __str__(self) -> str:
        s = self.summary()
        return (
            f"{s['schedule_id']} | "
            f"{self.division} {self.level} | "
            f"{self.academic_year} | "
            f"Term {self.term} | "
            f"{s['days']} days | "
            f"{s['entries']} entries"
        )
