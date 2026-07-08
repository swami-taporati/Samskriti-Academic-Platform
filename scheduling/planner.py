from pathlib import Path
import pandas as pd


def generate_empty_schedule(
    masters,
    academic_year,
    division,
    level,
    term,
):
    """
    Generates an empty schedule for the selected group.
    """

    # --------------------------------------------------
    # Locate Daily Event Structure workbook
    # --------------------------------------------------

    workbook = None

    for name, excel_file in masters.items():
        if "DailyEventStructure" in name:
            workbook = excel_file
            break

    if workbook is None:
        raise Exception("Daily Event Structure workbook not found.")

    # --------------------------------------------------
    # Read Division Template
    # --------------------------------------------------

    sheet_name = f"{division} Template"

    print(f"\nReading sheet : {sheet_name}")

    events = pd.read_excel(
        workbook,
        sheet_name=sheet_name
    )

    # --------------------------------------------------
    # Extract Learning Blocks
    # --------------------------------------------------

    learning = events[
        events["can_host_learning"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.lower()
        == "yes"
    ]

    print(f"Learning Blocks Found : {len(learning)}")

    if len(learning) == 0:
        print("\nWARNING : No learning blocks were found.")
        print("Check the values in 'can_host_learning'.")
    else:

        for _, row in learning.iterrows():

            print(
                f"   {row['event_name']} "
                f"({row['start_time']} - {row['end_time']})"
            )

    # --------------------------------------------------
    # Create Schedule Columns
    # --------------------------------------------------

    columns = ["Cycle Day"]

    for _, row in learning.iterrows():

        column_name = f"{row['start_time']} - {row['end_time']}"

        columns.append(column_name)

    # --------------------------------------------------
    # Create Empty Schedule
    # --------------------------------------------------

    # TODO:
    # Read this value from Global Scheduling Rules
    cycle_length = 15

    rows = []

    for day in range(1, cycle_length + 1):

        row = {
            "Cycle Day": day
        }

        for column in columns[1:]:
            row[column] = ""

        rows.append(row)

    schedule = pd.DataFrame(rows)

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    output_folder = (
        Path("output")
        / academic_year
        / division
    )

    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        output_folder
        / f"{division}_Level{level}_Term{term}.xlsx"
    )

    with pd.ExcelWriter(
        filename,
        engine="openpyxl"
    ) as writer:

        schedule.to_excel(
            writer,
            sheet_name="Schedule",
            index=False
        )

    print(f"\nCreated : {filename}")