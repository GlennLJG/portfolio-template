---
title: 'ML : Maintenance prédictive d’équipement industriel'
publishDate: 2025-01-22 00:00:00
img: /assets/ML_maintenance_predictive.jpg
img_alt: ML_maintenance_predictive
description: |
tags:
  - Imbalanced data
  - Ensemble learning
  - Time series
---

### 🎯 Contexte & Objectif
#### · Présentation du besoin métier
Dans le secteur industriel, les pannes de machines imprévues entraînent des temps d'arrêt coûteux, des retards de production et des risques de sécurité. L'objectif de la maintenance prédictive est de passer d'une approche réactive (réparer après la panne) à une stratégie proactive, en anticipant les défaillances pour optimiser les plannings de maintenance.
Ce projet vise à construire un système de maintenance prédictive intelligent pour les équipements industriels. En prédisant les pannes avant qu'elles ne surviennent, on peut réduire les temps d'arrêt, minimiser les coûts de maintenance et augmenter la durée de vie et la fiabilité des équipements. Le défi principal réside dans la rareté des événements de panne, ce qui crée des jeux de données fortement déséquilibrés.

#### · Objectif final à atteindre
Développer un modèle de machine learning performant capable de prédire la défaillance d'un équipement (ici, un disque dur) dans une fenêtre de temps définie, en se basant sur les données de capteurs historiques. Le modèle doit être particulièrement efficace pour identifier les pannes (la classe minoritaire), malgré leur faible fréquence.

***

### 🧰 Données
#### · Source des données
Les données utilisées proviennent du jeu de données public **"Hard Drive Test Data" de Backblaze**, disponible sur Kaggle. Ce dataset contient les relevés S.M.A.R.T. quotidiens de dizaines de milliers de disques durs en opération.
[Lien vers le dataset sur Kaggle](https://www.kaggle.com/datasets/backblaze/hard-drive-test-data)

#### · Volume et structure
Le jeu de données complet est massif, contenant des millions d'enregistrements. Pour ce projet, une analyse est menée sur un sous-ensemble pertinent (données sur un mois), représentant **1 897 482 observations** avant la création de séquences temporelles. La structure est une série temporelle où chaque ligne est un snapshot journalier des indicateurs S.M.A.R.T. pour un disque dur unique.

#### · Type de variables
- **Identifiants/Temporelles :** `date`, `serial_number`.
- **Catégorielles :** `model`.
- **Numériques (Capteurs) :** Une multitude de variables `smart_..._raw` (ex: `smart_5_raw` - Reallocated Sectors Count) qui sont les indicateurs bruts de santé.
- **Cible :** `failure` (variable binaire, 1 pour une panne, 0 pour une opération normale).

***

### 🧪 Méthodologie
#### · Exploration et nettoyage des données (EDA)
Une analyse exploratoire a été menée pour comprendre la distribution des features, identifier les corrélations et visualiser le déséquilibre extrême entre les pannes et les opérations normales. Le nettoyage a impliqué la suppression des colonnes avec un grand nombre de valeurs manquantes et une gestion spécifique des valeurs `NaN`.

#### · Feature Engineering
Pour capturer les tendances dynamiques des données de capteurs, de nouvelles caractéristiques temporelles ont été créées, notamment des **moyennes glissantes (`rolling averages`)**. Cette étape est cruciale pour que le modèle puisse apprendre non seulement à partir des valeurs instantanées, mais aussi de leur évolution dans le temps.

#### · Modélisation avec Apprentissage d'Ensemble (Ensemble Learning)
Pour améliorer la robustesse et la précision des prédictions, des méthodes d'ensemble learning ont été appliquées :
-   **Bagging :** Un modèle **Random Forest** a été entraîné comme approche de référence.
-   **Boosting :** Des modèles plus puissants comme **Gradient Boosting** et **XGBoost** ont été mis en œuvre pour améliorer les performances, en particulier dans ce contexte de données déséquilibrées.

#### · Gestion des Données Déséquilibrées (Handling Imbalanced Data)
C'est le cœur du projet. Plusieurs techniques ont été combinées pour forcer le modèle à prêter attention à la classe minoritaire (pannes) :
1.  **Sur-échantillonnage (Over-sampling) :** La technique **SMOTE** (Synthetic Minority Over-sampling Technique) a été utilisée pour créer synthétiquement de nouveaux exemples de pannes.
2.  **Sous-échantillonnage (Under-sampling) :** La classe majoritaire (opérations normales) a été sous-échantillonnée pour réduire le déséquilibre.
3.  **Apprentissage sensible aux coûts (Cost-Sensitive Learning) :** Des poids ont été ajustés dans les modèles (ex: `scale_pos_weight` dans XGBoost) pour pénaliser plus lourdement les erreurs de classification sur les pannes.

#### · Fine tuning
- Pour atteindre les meilleures performances, une comparaison a été menée sur différents jeux d'hyperparamètres pour les techniques de gestion du déséquilibre.
- Pour le fine tuning des modèles entraînés, 2 GridSearch ont été appliquées, l'une ayant pour objectif de maximiser le f1-score de chaque classe et l'autre de maximiser le rappel de chaque classe.

#### · Évaluation
Étant donné le déséquilibre des classes, la simple `accuracy` n'est pas une métrique pertinente. L'évaluation s'est concentrée sur :
-   **AUC-ROC :** Pour mesurer la capacité du modèle à discriminer entre les deux classes.
-   **F1-Score, Précision et Rappel (Precision & Recall) :** Pour évaluer le compromis entre la détection correcte des pannes et le risque de fausses alertes.

***

### 📊 Résultats
#### · Performances des modèles
Les modèles de base entraînés sur les données brutes ont montré une faible capacité à détecter les pannes, avec des F1-Scores très bas (autour de 0.14-0.21). Après l'application des techniques de ré-échantillonnage et d'apprentissage sensible aux coûts, le modèle **XGBoost optimisé a atteint un F1-Score de 0.60 et une précision de 0.80** pour la classe "panne" sur les données de test, tout en gardant de très bons scores pour l'autre classe.

#### · Comparaison des approches
La comparaison a clairement démontré l'amélioration drastique apportée par les stratégies de gestion de données déséquilibrées. L'approche combinant SMOTE et le sous-échantillonnage a fourni les meilleurs résultats. Le modèle **XGBoost** s'est avéré supérieur aux autres, offrant le meilleur compromis entre la détection des pannes réelles et la minimisation des fausses alertes.

#### · Interprétation des résultats
Les résultats confirment que les techniques d'ensemble comme XGBoost, combinées à une gestion rigoureuse du déséquilibre des classes, sont essentielles pour construire un système de maintenance prédictive efficace. Le modèle final est capable d'identifier une part significative des pannes imminentes, permettant une intervention proactive.

***

### 💡 Ce que j'ai appris
#### · Compétences acquises ou renforcées
-   **Apprentissage d'Ensemble :** Mise en œuvre et comparaison de techniques de Bagging (Random Forest) et de Boosting (Gradient Boosting, XGBoost) pour un problème de classification complexe.
-   **Gestion de Données Déséquilibrées :** Maîtrise des techniques fondamentales comme SMOTE, le sous-échantillonnage et l'apprentissage sensible aux coûts pour des problèmes réels où la classe d'intérêt est rare.
-   **Feature Engineering pour Séries Temporelles :** Manipulation de séries temporelles et création de caractéristiques pertinentes (moyennes glissantes) pour améliorer le pouvoir prédictif des modèles.
-   **Évaluation de Modèles en Conditions Déséquilibrées :** Utilisation et interprétation de métriques adaptées au contexte (AUC-ROC, F1-Score, Rappel)