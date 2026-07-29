# Défi « Élections municipales 2026 » — Enjeux locaux

Analyse des disparités territoriales françaises autour de trois thématiques
d'enjeux locaux : **logement**, **éducation** et **revenus & pauvreté**.

## Sources de données

| # | Dataset | Source |
|---|---------|--------|
| 1 | Communes soumises à la loi SRU (2025) | MTE / data.gouv.fr |
| 2 | Carte des loyers 2025 (4 fichiers) | MTE / data.gouv.fr |
| 3 | Établissements d'éducation prioritaire | MENJ / data.education.gouv.fr |
| 4 | Effectifs d'élèves par école (rentrée 2024) | MENJ / data.education.gouv.fr |
| 5 | Personnels du 1er degré (rentrée 2024) | MENJ / data.education.gouv.fr |
| 6 | Revenus & pauvreté FiloSoFi 2021 | INSEE |
| 7 | Géométrie des départements | france-geojson |

> ⚠️ Le fichier SRU ne couvre que les **2 196 communes soumises** à obligation
> de logement social — il ne contient pas les communes non soumises.

## Pipeline

Les notebooks sont à exécuter dans l'ordre, depuis le dossier `notebooks/` :

1. `01_acquisition_donnees.ipynb` — téléchargement des datasets (`src/download_data.py`)
2. `02_nettoyage_preparation.ipynb` — nettoyage, normalisation des codes INSEE /
   département, agrégations départementales → `data/processed/*.parquet`
3. `03_analyse_logement.ipynb` — SRU et loyers
4. `04_analyse_education.ipynb` — effectifs, ratios élèves/enseignant, éducation prioritaire
5. `05_analyse_revenus.ipynb` — niveau de vie et pauvreté (FiloSoFi)
6. `06_carte_interactive.ipynb` — carte Folium multi-couches → `outputs/carte_interactive.html`

## Installation

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows
# source .venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
```

## Structure

```
├── data/
│   ├── raw/         # fichiers sources (non versionnés)
│   ├── processed/   # parquets nettoyés et agrégés
│   └── external/    # géométries (geojson)
├── notebooks/       # pipeline d'analyse (01 → 06)
├── outputs/         # graphiques PNG + carte interactive HTML
└── src/             # utilitaires (téléchargement, nettoyage, chemins)
```
