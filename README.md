# Défi Municipales 2026 — Enjeux locaux

Analyse des grands enjeux locaux en vue des **élections municipales de 2026** : logement social, éducation prioritaire et disparités de revenus.

---

## Contexte

Ce projet explore trois thématiques majeures pour les communes françaises :

| Thématique | Indicateurs clés |
|---|---|
| 🏠 **Logement** | Taux de logement social (loi SRU), loyers au m² |
| 📚 **Éducation** | Ratio élèves/enseignant, part d'écoles en éducation prioritaire (REP/REP+) |
| 💶 **Revenus & Pauvreté** | Niveau de vie médian, taux de pauvreté (FiloSoFi – INSEE 2021) |

---

## Sources de données

| # | Jeu de données | Source |
|---|---|---|
| 1 | Communes SRU | MTE / [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/communes-et-inventaire-sru/) |
| 2 | Carte des loyers 2025 | MTE / [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2025/) |
| 3 | Éducation prioritaire | MENJ / [data.education.gouv.fr](https://data.education.gouv.fr/explore/dataset/fr-en-etablissements-ep/) |
| 4 | Effectifs élèves par école | MENJ / [data.education.gouv.fr](https://data.education.gouv.fr/explore/dataset/fr-en-ecoles-effectifs-nb_classes/) |
| 5 | Personnels 1er degré | MENJ / [data.education.gouv.fr](https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs_personnels_etablissements1d/) |
| 6 | Revenus & Pauvreté (FiloSoFi) | [INSEE](https://www.insee.fr/fr/statistiques/6457248) |
| 7 | Géométrie départements | [france-geojson](https://github.com/gregoiredavid/france-geojson) |

---

## Structure du projet

```
defi-municipales-2026-enjeux/
├── data/
│   ├── raw/            # Données brutes téléchargées (ignorées par git)
│   ├── processed/      # Données nettoyées au format Parquet (ignorées par git)
│   └── external/       # Ressources externes, ex. géométrie (ignorées par git)
├── notebooks/
│   ├── 01_acquisition_donnees.ipynb      # Téléchargement des datasets
│   ├── 02_nettoyage_preparation.ipynb    # Nettoyage et normalisation
│   ├── 03_analyse_logement.ipynb         # Analyse logement (SRU & loyers)
│   ├── 04_analyse_education.ipynb        # Analyse éducation
│   ├── 05_analyse_revenus.ipynb          # Analyse revenus & pauvreté
│   └── 06_carte_interactive.ipynb        # Carte Folium multi-thématique
├── outputs/            # Cartes et graphiques générés (ignorés par git)
├── src/
│   ├── __init__.py
│   ├── download_data.py    # Téléchargement des fichiers sources
│   ├── clean_data.py       # Fonctions de nettoyage et normalisation
│   └── utils.py            # Chemins et configuration
└── requirements.txt
```

---

## Installation

**Python 3.10+** requis.

```bash
# Cloner le dépôt
git clone https://github.com/Mrsaltyx/defi-municipales-2026-enjeux.git
cd defi-municipales-2026-enjeux

# Créer un environnement virtuel (recommandé)
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

---

## Utilisation

### 1. Télécharger les données brutes

```bash
python src/download_data.py
```

Cela télécharge tous les jeux de données dans `data/raw/` et `data/external/`.

### 2. Exécuter les notebooks dans l'ordre

```bash
jupyter notebook
```

| Notebook | Description |
|---|---|
| `01_acquisition_donnees` | Vérifie et documente les données téléchargées |
| `02_nettoyage_preparation` | Nettoie, normalise et exporte les fichiers Parquet |
| `03_analyse_logement` | Visualisations SRU et loyers par département |
| `04_analyse_education` | Disparités éducatives, ratios élèves/enseignant |
| `05_analyse_revenus` | Taux de pauvreté, corrélations multi-thématiques |
| `06_carte_interactive` | Carte Folium exportée dans `outputs/` |

---

## Résultats

Les analyses produisent :

- Des **graphiques** (matplotlib / seaborn / plotly) sauvegardés dans `outputs/`
- Une **carte interactive** Folium (`outputs/carte_interactive.html`) croisant les 3 thématiques au niveau départemental

---

## Dépendances principales

| Bibliothèque | Usage |
|---|---|
| `pandas` | Manipulation des données |
| `numpy` | Calculs numériques |
| `matplotlib` / `seaborn` | Visualisations statiques |
| `plotly` | Graphiques interactifs |
| `folium` | Carte interactive |
| `pyarrow` | Lecture/écriture Parquet |
| `scikit-learn` | Analyses statistiques |
| `requests` | Téléchargement des datasets |

---

## Licence

Projet réalisé dans le cadre du défi open data **« Élections municipales 2026 et enjeux locaux »**.  
Les données utilisées sont issues de sources publiques françaises (Licence Ouverte / Open Licence v2.0).
