"""
models/matrix.py

Flattened matrix models used for indexed schedule queries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, slots=True)
class MatrixEntry:
    cycle_day: int
    slot_no: Optional[int]
    event_id: str
    activity: str
    event_type: str
    start_time: str
    end_time: str


@dataclass(slots=True)
class TeacherLoad:
    teacher: str
    total_slots: int = 0


@dataclass(slots=True)
class RoomLoad:
    room: str
    total_slots: int = 0


@dataclass(slots=True)
class SubjectLoad:
    subject: str
    total_slots: int = 0
