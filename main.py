from data.loader import load_master_files
from scheduling.planner import generate_empty_schedule
from ui.menu import (
    get_academic_year,
    get_term,
    get_generation_mode,
    get_division,
    get_level,
    confirm_generation,
)

def build_groups(mode):
    if mode == "school":
        return [
            ("Kanishta",1),("Kanishta",2),("Kanishta",3),("Kanishta",4),
            ("Madhyama",1),("Madhyama",2),("Madhyama",3),
            ("Jyeshta",1),("Jyeshta",2),("Jyeshta",3),("Jyeshta",4),
        ]
    if mode == "division":
        division = get_division()
        levels = {"Kanishta":4,"Madhyama":3,"Jyeshta":4}[division]
        return [(division,i) for i in range(1,levels+1)]
    division = get_division()
    level = get_level(division)
    return [(division,level)]

def main():
    print("="*60)
    print("SGS Academic Planner v1.1.0")
    print("="*60)

    masters = load_master_files("masters")

    academic_year = get_academic_year()
    term = get_term()
    mode = get_generation_mode()

    groups = build_groups(mode)

    if not confirm_generation(academic_year, term, mode, groups):
        print("Generation cancelled.")
        return

    for division, level in groups:
        print(f"\nGenerating {division} Level {level}")
        generate_empty_schedule(
            masters,
            academic_year,
            division,
            level,
            term
        )

    print("\nAll schedules generated successfully.")

if __name__ == "__main__":
    main()
