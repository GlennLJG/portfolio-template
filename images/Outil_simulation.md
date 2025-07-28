---
title: 'Dev/Data management : Outil de simulation' 
publishDate: 2025-08-19 00:00:00
img: /assets/outil_simu.jpg
img_alt: Outil de simulation python
description: |
  
tags:
  - Python
  - Data
  - Dev
  - streamlit
---

### 🎯 Contexte & Objectif  
#### · Présentation du besoin métier  
En production, les différents outils du SI reçoivent normalement des données en temps réel depuis des sources externes. Or, l'environnement de formation, destiné aux essais et à la montée en compétences des opérateurs, ne bénéficie d'aucune alimentation. L'enjeu est donc de simuler un flux de données crédible et adapté à ce contexte de test.

#### · Intérêt du projet  
Ce dispositif est essentiel pour offrir aux équipes une formation pratique sur des données fiables. Il permet également de valider de nouvelles fonctionnalités ou intégrations sans impacter le SI en production. L'automatisation garantit un gain de temps significatif et une actualisation régulière des jeux de données de formation.

#### · Objectif final à atteindre
Développer et déployer un outil Python, doté d'une interface utilisateur simple, capable d'extraire des données historiques pour une date choisie, de les modifier, de les formater, et de les injecter automatiquement dans les outils SI de l'environnement de formation.

---

### 🧰 Données
#### · Source des données
Les données sont issues de la base de données de l'entreprise et correspondent aux données en production sur les journées passées.

#### · Type de variables
Les données sont des séries temporelles comprenant différents types : numériques, temporelles, et textuelles.
Les fichiers générés par l'outil en sortie sont de type `.csv`, `.xml`. 

---

### 🧪 Méthodologie
#### · Extraction des données
Selon leur emplacement, les données sont récupérées via trois canaux :  
- **API REST** à l'aide de requêtes HTTP.  
- **Data lake** de l'entreprise via des requêtes SQL, puis export des vues en utilisant pyarrow via une API.  
- **Outil de production** par extraction manuelle de fichiers `.xml`, nécessitant une conversion en tables respectant l'architecture d'origine.  
Les jeux de données sont ensuite chargés dans des DataFrame pandas et nettoyés pour optimiser leur exploitation.

#### · Feature engineering
Le projet requiert de nombreuses transformations de données pour satisfaire les contraintes des outils SI, conçus pour la production :  
- **Actualisation des dates** : remplacer tous les formats de date historiques par la date du jour, pour s'adapter aux outils qui n'acceptent que des fichiers à la date du jour.  
- **Agrégation de séries temporelles complexes** : certains outils nécessitant un dépôt de fichier toutes les heures. Pour éviter les envois en dehors des plages ouvrées, il était nécessaire de créer un fichier agrégeant l'ensemble des fichiers supposés être déposés sur une période. Une étape complexe car chaque fichier possède des points temporels ayant pour référentiel l'horaire de dépôt de ce dernier.

#### · Génération et dépôt des fichiers
Après traitement, l'outil fabrique plus d'une centaine de fichiers dans une quinzaine de formats conformes aux attentes des outils SI.  
Ces fichiers sont ensuite transférés vers cinq outils SI différents via **API** ou **FTP**, en respectant les fenêtres horaires imposées.

#### · Interface 
Le projet est pensé pour être utilisable par des profils métier non-codeurs, pour ce faire il bénéficie d'une interface streamlit facile à prendre en main tout en offrant le plus de possibilités à l'utilisateur :
- Choix de la date d'origine des données et de la date cible pour les fichiers générés.  
- Sélection des outils SI à alimenter (un, plusieurs ou tous).  
- À chaque heure, liste des fichiers disponibles pour ce créneau, avec possibilité de sélection individuelle ou collective.  
- Modification manuelle des dates pour tout fichier non pris en compte automatiquement.

#### · Organisation du code
Afin de garantir la transmission et la maintenance du code, le projet est organisé en plusieurs fichiers/**bibliothèques Python** :  
- Configuration (`config.ini`, `credentials.ini`) séparée du code pour protéger les identifiants.  
- Librairie principale orchestrant les appels de fonctions.  
- Modules dédiés à chaque outil SI, avec un script `.py` par type de fichier à formater.  
- Bibliothèque utilitaire regroupant les fonctions communes.  
- Fichiers `requirements.txt` pour gérer les dépendances.  
- Suite de tests unitaires garantissant la robustesse du code.  
- Dossier des pages Streamlit composant l'interface.  
Le projet est versionné avec **Git** et documenté par un guide d'utilisation détaillé.
---

### 💡 Ce que j'ai appris
#### · Compétences acquises ou renforcées
- **Architecture logicielle :** Concevoir une solution modulaire, réutilisable et facilement transmissible.
- **Développement Python :** Utiliser des librairies avancées comme Pandas pour la manipulation de `DataFrames`, pyarrow pour la récupération de données et Streamlit pour l'interface utilisateur.
- **Gestion de projet en autonomie :** Mener un projet de bout en bout, de la compréhension du besoin métier (en contact avec les Product Owners) jusqu'à la mise en place d'une solution fonctionnelle.
- **Interaction avec des systèmes complexes :** Comprendre les contraintes et l'interconnexion d'un Système d'Information (SI) pour y intégrer une solution.

