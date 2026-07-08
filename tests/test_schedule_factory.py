from data.loader import load_master_files
from scheduling.schedule_factory import create_schedule

masters = load_master_files("masters")

schedule = create_schedule(
    masters=masters,
    academic_year="2026-27",
    division="Kanishta",
    level=3,
    term=1,
)

print("\nSchedule Summary")
print("-" * 40)

print(schedule)

print("\nStatistics")
print(schedule.summary())

print("\nFirst 10 Events of Day 1")
print("-" * 40)

for entry in schedule.get_day(1)[:10]:
    print(
        f"{entry.start_time} - "
        f"{entry.end_time} | "
        f"{entry.activity}"
    )

print("\nLearning Slots")
print("-" * 40)

print(schedule.total_learning_slots())

print("\nDay 15")
print("-" * 40)

for entry in schedule.get_day(15):
    print(
        f"{entry.start_time} - "
        f"{entry.end_time} | "
        f"{entry.activity}"
    )

    print("\nSummary")
print(schedule.summary())