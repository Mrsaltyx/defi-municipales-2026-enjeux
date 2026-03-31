import requests
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.utils import DATA_RAW, DATA_EXTERNAL

RESOURCES = {
    "sru": {
        "filename": "donnees-sru-data-gouv-2025-v2.csv",
        "url": "https://static.data.gouv.fr/resources/communes-et-inventaire-sru/20251219-143258/donnees-sru-data-gouv-2025-v2.csv",
    },
    "loyers_appartements": {
        "filename": "pred-app-mef-dhup.csv",
        "url": "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2025/20251211-145010/pred-app-mef-dhup.csv",
    },
    "loyers_t1t2": {
        "filename": "pred-app12-mef-dhup.csv",
        "url": "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2025/20251211-144934/pred-app12-mef-dhup.csv",
    },
    "loyers_t3plus": {
        "filename": "pred-app3-mef-dhup.csv",
        "url": "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2025/20251211-144951/pred-app3-mef-dhup.csv",
    },
    "loyers_maisons": {
        "filename": "pred-mai-mef-dhup.csv",
        "url": "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2025/20251211-145039/pred-mai-mef-dhup.csv",
    },
    "education_prioritaire": {
        "filename": "fr-en-etablissements-ep.csv",
        "url": "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-etablissements-ep/exports/csv?use_labels=true",
    },
    "effectifs_eleves": {
        "filename": "fr-en-ecoles-effectifs-nb_classes.csv",
        "url": "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv?use_labels=true",
    },
    "personnels_1er_degre": {
        "filename": "fr-en-indicateurs_personnels_etablissements1d.csv",
        "url": "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-indicateurs_personnels_etablissements1d/exports/csv?use_labels=true",
    },
    "filosofi": {
        "filename": "filosofi_commut.csv",
        "url": "https://www.insee.fr/fr/statistiques/fichier/6457248/base-filosofi-communes-2021.zip",
    },
    "departements_geojson": {
        "filename": "departements.geojson",
        "url": "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson",
    },
}


def download_file(url, dest, chunk_size=8192):
    r = requests.get(url, stream=True, timeout=30)
    r.raise_for_status()
    total = int(r.headers.get("content-length", 0))
    downloaded = 0
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            downloaded += len(chunk)
            if total > 0:
                pct = downloaded / total * 100
                print(
                    f"\r  {pct:5.1f}% ({downloaded / 1e6:.1f} / {total / 1e6:.1f} MB)",
                    end="",
                    flush=True,
                )
    print(f"\r  100.0% ({downloaded / 1e6:.1f} MB)                         ")
    return dest


def download_all():
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    DATA_EXTERNAL.mkdir(parents=True, exist_ok=True)

    for key, resource in RESOURCES.items():
        filename = resource["filename"]
        url = resource["url"]

        if key == "departements_geojson":
            dest = DATA_EXTERNAL / filename
        else:
            dest = DATA_RAW / filename

        if dest.exists():
            print(
                f"[SKIP] {filename} (already exists, {dest.stat().st_size / 1e6:.1f} MB)"
            )
            continue

        print(f"[DOWNLOAD] {filename}")
        try:
            download_file(url, dest)
        except requests.RequestException as e:
            print(f"  [ERROR] {e}")

    print("\nDone!")


if __name__ == "__main__":
    download_all()
