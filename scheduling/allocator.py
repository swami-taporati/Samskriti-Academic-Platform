"""
scheduling/allocator.py

Sprint 2.2 allocator (v1.1.1)

Allocates curriculum activities into Learning Slots.
If curriculum sessions are exhausted before all Learning Slots are filled,
the remaining slots are left as "Learning Slot".
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

import pandas as pd


class AllocationError(Exception):
    """Raised for unrecoverable allocation errors."""


@dataclass
class AllocationResult:
    schedule: object
    subject_counts: dict
    allocated_slots: int
    remaining_learning_slots: int

    @property
    def success(self) -> bool:
        return True


class Allocator:

    SHEET_NAME = "Curriculum Allocation"

    def _load_curriculum(self, masters, academic_year, division, level, term):
        workbook = None
        for name, wb in masters.items():
            if "CurriculumAllocation" in name:
                workbook = wb
                break

        if workbook is None:
            raise AllocationError("Curriculum Allocation workbook not found.")

        df = pd.read_excel(workbook, sheet_name=self.SHEET_NAME)

        term_value = term if str(term).startswith("Term") else f"Term {term}"

        df = df[
            (df["academic_year"] == academic_year)
            & (df["division"] == division)
            & (df["level"] == level)
            & (df["term"] == term_value)
        ]

        if df.empty:
            raise AllocationError(
                f"No curriculum allocation found for {division} {level}, {academic_year}, {term_value}."
            )

        return df

    def allocate(self, schedule, masters):

        df = self._load_curriculum(
            masters,
            schedule.academic_year,
            schedule.division,
            schedule.level,
            schedule.term,
        )

        queue = []
        for _, row in df.iterrows():
            queue.extend(
                [str(row["activity_name"]).strip()]
                * int(row["sessions_per_15_day_cycle"])
            )

        counts = Counter()
        remaining_learning_slots = 0

        for entry in schedule.entries:

            if entry.activity != "Learning Slot":
                continue

            if not queue:
                remaining_learning_slots += 1
                continue

            activity = queue.pop(0)
            entry.activity = activity
            counts[activity] += 1

        if queue:
            print(f"WARNING: {len(queue)} curriculum sessions could not be allocated.")

        print("\nAllocation Summary")
        print("-" * 40)
        for activity, count in sorted(counts.items()):
            print(f"{activity:<25}{count:>4}")
        print("-" * 40)
        print(f"Allocated Sessions      : {sum(counts.values())}")
        print(f"Remaining Learning Slots: {remaining_learning_slots}")
        print()

        return AllocationResult(
            schedule=schedule,
            subject_counts=dict(counts),
            allocated_slots=sum(counts.values()),
            remaining_learning_slots=remaining_learning_slots,
        )
