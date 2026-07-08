from pathlib import Path
import pandas as pd
from config.settings import MASTER_PREFIXES

def load_master_files(folder):
    folder = Path(folder)
    loaded = {}

    for prefix in MASTER_PREFIXES:
        matches = list(folder.glob(prefix + "*.xlsx"))
        if matches:
            loaded[prefix] = pd.ExcelFile(matches[0])

    if not loaded:
        raise FileNotFoundError(
            "No Knowledge Master workbooks found in the masters folder."
        )

    return loaded
