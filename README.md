🗳️ Défi Municipales 2026 — Enjeux locaux

Analyse des grands enjeux locaux en vue des élections municipales de 2026 : logement social, éducation prioritaire et disparités de revenus. Ce projet exploite les données ouvertes pour éclairer le débat public.
📌 Contexte

Ce projet explore trois thématiques majeures pour les communes françaises en s'appuyant sur l'Open Data national :
Thématique	Indicateurs clés
🏠 Logement	Taux de logement social (loi SRU), loyers au m²
📚 Éducation	Ratio élèves/enseignant, part d'écoles en éducation prioritaire (REP/REP+)
💶 Revenus & Pauvreté	Niveau de vie médian, taux de pauvreté (FiloSoFi)
📊 Sources de données

L'intégralité des données provient de la plateforme nationale data.gouv.fr et des portails ministériels associés.
#	Jeu de données	Producteur / Source
1	Communes SRU	MTE / data.gouv.fr
2	Carte des loyers 2025	MTE / data.gouv.fr
3	Éducation prioritaire	MENJ / data.education.gouv.fr
4	Effectifs élèves par école	MENJ / data.education.gouv.fr
5	Personnels 1er degré	MENJ / data.education.gouv.fr
6	Revenus & Pauvreté (FiloSoFi)	INSEE / data.gouv.fr
7	Géométrie départements	france-geojson / data.gouv.fr
📂 Structure du projet
Plaintext

defi-municipales-2026-enjeux/
├── data/
│   ├── raw/            # Données brutes (data.gouv.fr)
│   ├── processed/      # Données nettoyées (Parquet)
│   └── external/       # Géométries et référentiels
├── notebooks/
│   ├── 01_acquisition_donnees.ipynb      # Téléchargement
│   ├── 02_nettoyage_preparation.ipynb    # ETL & Normalisation
│   ├── 03_analyse_logement.ipynb         # Focus SRU & Loyers
│   ├── 04_analyse_education.ipynb        # Disparités scolaires
│   ├── 05_analyse_revenus.ipynb          # Pauvreté & Corrélations
│   └── 06_carte_interactive.ipynb        # Dashboard Folium
├── outputs/            # Cartes HTML et exports graphiques
├── src/
│   ├── download_data.py    # Scripts de récupération automatisée
│   ├── clean_data.py       # Logique de traitement des données
│   └── utils.py            # Configuration des chemins
└── requirements.txt

⚙️ Installation & Utilisation
1. Installation

Python 3.10+ est requis.
Bash

# Cloner le dépôt
git clone https://github.com/Mrsaltyx/defi-municipales-2026-enjeux.git
cd defi-municipales-2026-enjeux

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

2. Exécution

    Télécharger les données brutes :
    Bash

    python src/download_data.py

    Lancer l'analyse :
    Exécutez les notebooks dans l'ordre (01 à 06) via jupyter notebook ou votre IDE favori.

📈 Résultats attendus

    Visualisations statiques : Analyses de corrélations via Seaborn/Matplotlib.

    Cartographie interactive : Une carte Folium (générée dans outputs/) permettant de visualiser les indicateurs au niveau départemental et communal.

    Indicateurs croisés : Mise en évidence des liens entre niveau de revenus et accès au logement social.

⚖️ Licence

Projet réalisé dans le cadre du défi open data « Élections municipales 2026 et enjeux locaux ». Les données sont issues de sources publiques françaises (Ministères, INSEE) via data.gouv.fr et sont redistribuées sous Licence Ouverte / Open Licence v2.0.
