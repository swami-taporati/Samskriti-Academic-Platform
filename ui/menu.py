DIVISIONS = {
    1: ("Kanishta",4),
    2: ("Madhyama",3),
    3: ("Jyeshta",4)
}

def get_academic_year():
    return input("Academic Year (e.g. 2026-27): ").strip()

def get_term():
    print("\nSelect Term")
    print("1. Term 1")
    print("2. Term 2")
    while True:
        c=input("Choice: ").strip()
        if c in ("1","2"):
            return c

def get_generation_mode():
    print("\nGenerate")
    print("1. Entire School")
    print("2. One Division")
    print("3. One Group")
    print("4. Exit")
    while True:
        c=input("Choice: ").strip()
        if c=="1": return "school"
        if c=="2": return "division"
        if c=="3": return "group"
        if c=="4": raise SystemExit

def get_division():
    print("\nSelect Division")
    for k,(name,_) in DIVISIONS.items():
        print(f"{k}. {name}")
    while True:
        c=input("Choice: ").strip()
        if c.isdigit() and int(c) in DIVISIONS:
            return DIVISIONS[int(c)][0]

def get_level(division):
    levels={"Kanishta":4,"Madhyama":3,"Jyeshta":4}[division]
    print(f"\nSelect {division} Level")
    for i in range(1,levels+1):
        print(f"{i}. {division} {i}")
    while True:
        c=input("Choice: ").strip()
        if c.isdigit() and 1<=int(c)<=levels:
            return int(c)

def confirm_generation(year, term, mode, groups):
    print("\n"+"="*60)
    print("Generation Summary")
    print("="*60)
    print(f"Academic Year : {year}")
    print(f"Term          : {term}")
    print(f"Mode          : {mode}")
    print(f"Schedules     : {len(groups)}")
    return input("\nProceed? (Y/N): ").strip().lower()=="y"
