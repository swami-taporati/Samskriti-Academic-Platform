"""
scheduling/schedule_matrix.py

Creates indexed views over a Schedule.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Optional

from models.schedule import Schedule
from models.matrix import MatrixEntry


class ScheduleMatrix:

    def __init__(self, schedule: Schedule):
        self.schedule = schedule
        self.entries: List[MatrixEntry] = []
        self.day_index: Dict[int, List[MatrixEntry]] = defaultdict(list)
        self.slot_index: Dict[tuple[int, Optional[int]], List[MatrixEntry]] = defaultdict(list)
        self._build()

    def _build(self):
        for e in self.schedule.entries:
            m = MatrixEntry(
                cycle_day=e.cycle_day,
                slot_no=e.slot_no,
                event_id=e.event_id,
                activity=e.activity,
                event_type=e.event_type,
                start_time=e.start_time,
                end_time=e.end_time,
            )
            self.entries.append(m)
            self.day_index[m.cycle_day].append(m)
            self.slot_index[(m.cycle_day, m.slot_no)].append(m)

    def get_day(self, day: int):
        return list(self.day_index.get(day, []))

    def get_slot(self, day: int, slot: Optional[int]):
        return list(self.slot_index.get((day, slot), []))

    def summary(self):
        return {
            "days": len(self.day_index),
            "entries": len(self.entries),
        }
