from data.loader import load_master_files

def main():
    print("="*60)
    print("SGS ACADEMIC PLANNER v1.0.0")
    print("="*60)

    masters = load_master_files("masters")

    print("\nKnowledge Masters Loaded")
    for name in masters:
        print(f"  ✓ {name}")

    print("\nAcademic Planner Ready")

    division=input("\nDivision (Kanishta/Madhyama/Jyeshta): ").strip()
    level=input("Level: ").strip()
    term=input("Term: ").strip()

    print("\nSelection")
    print(f"Division : {division}")
    print(f"Level    : {level}")
    print(f"Term     : {term}")

    print("\nNext milestone:")
    print("Generate empty timetable grid.")

if __name__=="__main__":
    main()
