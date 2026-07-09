from scheduling.schedule_matrix import ScheduleMatrix
from models.schedule import Schedule, ScheduleEntry

def test_matrix_build():
    s = Schedule(
        schedule_id="T",
        academic_year="2026",
        division="Kanishta",
        level=1,
        term=1,
    )

    s.add_entry(
        ScheduleEntry(
            cycle_day=1,
            event_id="E1",
            parent_event=None,
            event_type="Learning",
            event_name="Math",
            start_time="08:00",
            end_time="08:50",
            slot_no=1,
            activity="Math",
        )
    )

    matrix = ScheduleMatrix(s)

    assert matrix.summary()["entries"] == 1
    assert len(matrix.get_day(1)) == 1
