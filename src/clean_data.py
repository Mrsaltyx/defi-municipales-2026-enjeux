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
    code_str = str(code).strip().replace(" ", "")
    if code_str.endswith(".0"):
        code_str = code_str[:-2]
    code_str = code_str.split("/")[0]
    if not code_str:
        return ""
    return code_str.zfill(5)


def normalize_code_departement(code):
    if pd.isna(code):
        return code
    code_str = str(code).strip().upper().replace(" ", "").replace("-", "")
    if code_str.endswith(".0"):
        code_str = code_str[:-2]
    if len(code_str) == 1:
        code_str = "0" + code_str
    if code_str in ("2A", "2B"):
        return code_str
    return code_str.zfill(2)


def clean_pct(col):
    if pd.api.types.is_numeric_dtype(col):
        return pd.to_numeric(col, errors="coerce")
    cleaned = (
        col.astype(str)
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


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
