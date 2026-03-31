from pathlib import Path
import pandas as pd
from src.utils import DATA_RAW, DATA_PROCESSED, DATA_EXTERNAL


def load_csv(filepath, sep=";", encoding="utf-8", low_memory=False, **kwargs):
    try:
        return pd.read_csv(
            filepath, sep=sep, encoding=encoding, low_memory=low_memory, **kwargs
        )
    except UnicodeDecodeError:
        return pd.read_csv(
            filepath, sep=sep, encoding="latin-1", low_memory=low_memory, **kwargs
        )


def normalize_code_insee(code):
    if pd.isna(code):
        return code
    code = str(code).strip().replace(" ", "")
    code = code.split("/")[0]
    while len(code) < 5 and len(code) < 3:
        code = "0" + code
    if len(code) == 3:
        code = "0" + code
    if len(code) == 2:
        code = code
    return code.zfill(5)


def normalize_code_departement(code):
    if pd.isna(code):
        return code
    code = str(code).strip().upper()
    code = code.replace(" ", "").replace("-", "")
    if len(code) == 1:
        code = "0" + code
    if code in ("2A", "2B"):
        return code
    return code.zfill(2)


def clean_pct(col):
    if col.dtype == "object":
        return (
            col.astype(str)
            .str.replace("%", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
            .pipe(pd.to_numeric, errors="coerce")
        )
    return pd.to_numeric(col, errors="coerce")


def save_processed(df, name, fmt="parquet"):
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    if fmt == "parquet":
        path = DATA_PROCESSED / f"{name}.parquet"
        df.to_parquet(path, index=False)
    else:
        path = DATA_PROCESSED / f"{name}.csv"
        df.to_csv(path, sep=";", index=False, encoding="utf-8")
    print(f"  -> {path} ({df.shape[0]:,} rows, {df.shape[1]} cols)")
    return path
