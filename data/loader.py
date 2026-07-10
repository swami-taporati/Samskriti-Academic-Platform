from pathlib import Path
import pandas as pd

def load_master_files(folder):

    folder=Path(folder)

    masters={}

    for file in folder.glob("*.xlsx"):

        masters[file.stem]=pd.ExcelFile(file)

    return masters