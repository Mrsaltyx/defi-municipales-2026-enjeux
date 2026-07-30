# Défi Municipales 2026 — Enjeux locaux

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Licence Ouverte](https://img.shields.io/badge/data-Licence%20Ouverte%20v2.0-green.svg)](https://www.etalab.gouv.fr/licence-ouverte-open-licence/)
[![GitHub stars](https://img.shields.io/github/stars/Mrsaltyx/defi-municipales-2026-enjeux)](https://github.com/Mrsaltyx/defi-municipales-2026-enjeux)

Analyse des grands enjeux locaux en vue des élections municipales de 2026 : logement social, éducation prioritaire et disparités de revenus, à partir de l'open data national.

## Ce que fait le projet

- **Logement** : taux de logement social (loi SRU) et loyers au m² par territoire.
- **Éducation** : ratio élèves / enseignant et part d'écoles en éducation prioritaire (REP / REP+).
- **Revenus & pauvreté** : niveau de vie médian et taux de pauvreté (FiloSoFi).
- Produits attendus : visualisations statiques (Seaborn / Matplotlib), indicateurs croisés (revenus × logement social) et une carte interactive Folium au niveau départemental et communal.

## Sources de données

Intégralité des données issues de data.gouv.fr et des portails ministériels associés :

| # | Jeu de données | Producteur |
|---|---|---|
| 1 | Communes soumises à la loi SRU (2025) | MTE / data.gouv.fr |
| 2 | Carte des loyers 2025 | MTE / data.gouv.fr |
| 3 | Établissements d'éducation prioritaire | MENJ / data.education.gouv.fr |
| 4 | Effectifs d'élèves par école (rentrée 2024) | MENJ / data.education.gouv.fr |
| 5 | Personnels du 1er degré (rentrée 2024) | MENJ / data.education.gouv.fr |
| 6 | Revenus & pauvreté FiloSoFi 2021 | INSEE / data.gouv.fr |
| 7 | Géométrie des départements | france-geojson / data.gouv.fr |

> Le fichier SRU ne couvre que les 2 196 communes soumises à obligation de logement social — il ne contient pas les communes non soumises.

## Prérequis

- Python 3.10 ou plus récent

## Installation

```bash
git clone https://github.com/Mrsaltyx/defi-municipales-2026-enjeux.git
cd defi-municipales-2026-enjeux

python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate

pip install -r requirements.txt
```

## Utilisation

Télécharger les données brutes :

```bash
python src/download_data.py
```

Puis exécuter les notebooks dans l'ordre (01 → 06) depuis le dossier `notebooks/` :

```bash
jupyter notebook
```

La carte interactive est générée dans `outputs/carte_interactive.html`.

## Structure du projet

```text
defi-municipales-2026-enjeux/
  data/
    raw/                                  # Données brutes (non versionnées)
    processed/                            # Parquets nettoyés et agrégés
    external/                             # Géométries (geojson)
  notebooks/
    01_acquisition_donnees.ipynb          # Téléchargement
    02_nettoyage_preparation.ipynb        # ETL & normalisation
    03_analyse_logement.ipynb             # Focus SRU & loyers
    04_analyse_education.ipynb            # Disparités scolaires
    05_analyse_revenus.ipynb              # Pauvreté & corrélations
    06_carte_interactive.ipynb            # Carte Folium multi-couches
  outputs/                                # Graphiques PNG + carte interactive HTML
  src/
    download_data.py                      # Récupération automatisée
    clean_data.py                         # Traitement des données
    utils.py                              # Configuration des chemins
  requirements.txt
```

## Licence

Projet réalisé dans le cadre du défi open data « Élections municipales 2026 et enjeux locaux ».
Données publiques (Ministères, INSEE) via data.gouv.fr, redistribuées sous Licence Ouverte / Open Licence v2.0.
