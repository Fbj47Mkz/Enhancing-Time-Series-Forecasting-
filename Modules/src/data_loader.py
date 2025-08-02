import os
import pandas as pd

# 📌 Dynamic path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')).strip()

# 📁 Directory
DATA_DIR = os.path.join(ROOT_DIR, 'data')

import os
import pandas as pd

def detect_separator(path: str, test_lines: int = 5) -> str:
    """
    Tente de détecter automatiquement le séparateur CSV : ',' ou ';'
    """
    with open(path, 'r', encoding='utf-8') as f:
        for _ in range(test_lines):
            line = f.readline()
            if ";" in line and "," not in line:
                return ";"
            elif "," in line and ";" not in line:
                return ","
            elif "," in line and ";" in line:
                # Cas ambigu : choisir celui qui sépare le plus
                return ";" if line.count(";") > line.count(",") else ","
    return ","  # Par défaut

def load_data(subfolder: str, filename: str, sep: str = None) -> pd.DataFrame:
    """
    Charge un fichier CSV avec détection automatique du séparateur si non spécifié.
    """
    path = os.path.join(DATA_DIR, subfolder, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Can't find file : {path}")

    # 🔍 Détection automatique si aucun séparateur n'est donné
    if sep is None:
        sep = detect_separator(path)

    print(f"✅ Load File : {path}  |  Separator detected: '{sep}'")
    return pd.read_csv(path, sep=sep)
