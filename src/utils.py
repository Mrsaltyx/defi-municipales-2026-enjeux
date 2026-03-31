from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_EXTERNAL = PROJECT_ROOT / "data" / "external"
OUTPUTS = PROJECT_ROOT / "outputs"

for d in [DATA_RAW, DATA_PROCESSED, DATA_EXTERNAL, OUTPUTS]:
    d.mkdir(parents=True, exist_ok=True)
