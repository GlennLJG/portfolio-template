---
title: 'Étude Comparative : Ensemble Learning vs Algorithmes Évolutionnaires' 
publishDate: 2024-10-30 00:00:00
img: /assets/comparative_study.jpg
img_alt: Étude Comparative Ensemble Learning vs Algorithmes Évolutionnaires
description: |
tags:  
  - Ensemble learning  
  - DEAP  
---

### 🎯 Contexte & Objectif
#### · Présentation du problème
En physique des particules, la détection du boson de Higgs est un problème de classification fondamental. Après des collisions de particules à haute énergie, il est crucial de distinguer les événements "signaux" (indiquant la présence d'un boson de Higgs) du "bruit de fond". Ce projet s'attaque à ce défi en utilisant des techniques de Machine Learning avancées pour automatiser et fiabiliser cette classification.

#### · Intérêt du projet
Ce projet explore et compare deux familles de méthodes de Machine Learning pour un problème de classification complexe. L'objectif est de comprendre leurs forces, faiblesses et compromis respectifs, non seulement en termes de performance pure, mais aussi d'efficacité de calcul et d'interprétabilité des modèles.

#### · Objectif final à atteindre
L'objectif principal est de mettre en œuvre, d'évaluer et de comparer :
1.  Les techniques d'**Ensemble learning** (Bagging et Boosting).
2.  L'**Apprentissage Évolutionnaire** (Programmation Génétique avec DEAP).
L'analyse comparative se base sur leurs performances sur le jeu de données de détection du Boson de Higgs.

***

### 🧰 Données
#### · Source des données
Les données proviennent du jeu de données public **"Higgs Boson Machine Learning Challenge"** disponible sur Kaggle. Il contient des caractéristiques de haut niveau dérivées de simulations de collisions de particules.
[Lien vers le dataset sur Kaggle](https://www.kaggle.com/competitions/higgs-boson/data)

#### · Volume et structure
Le jeu de données complet contient plus de 800 000 événements. Pour ce projet, une analyse a été menée sur un **échantillon d'environ 80 000 observations**.

#### · Type de variables
- **Identifiant :** `EventId`.
- **Numériques (Physique des particules) :** 30 caractéristiques primitives (`PRI_*`) et dérivées (`DER_*`) de type `float64`.
- **Cible :** `Label`, une variable binaire ('s' pour signal, 'b' pour bruit de fond), transformée en 0 et 1.

***

### 🧪 Méthodologie
#### · Exploration et nettoyage des données
Prétraitement des données :
- Suppression des colonnes non informatives.
- Gestion des valeurs manquantes (-999.0), remplacées par la **moyenne** de chaque colonne via `SimpleImputer`.
- **Normalisation** des caractéristiques numériques à l'aide d'un `MinMaxScaler` pour les ramener entre 0 et 1.

#### · Feature Engineering
Une **Analyse en Composantes Principales (PCA)** a été appliquée pour réduire la dimensionnalité des données, en conservant 90% de la variance expliquée, réduisant ainsi l'espace des caractéristiques pour améliorer l'efficacité computationnelle.

#### · Modélisation et Comparaison  
**Méthodes d'Ensemble testées :**
- **Bagging :** 
  - Bagging avec Random Forest 
  - Bagging avec Logistic Regression
  - Bagging avec GaussianNB 
- **Boosting :** 
  - AdaBoost 
  - Gradient Boosting 

**Apprentissage Évolutionnaire :**
- Implémentation avec la bibliothèque **DEAP** utilisant la programmation génétique
- **Grid Search** extensive avec 8 combinaisons de paramètres pour chaque algorithme (Métriques d'optimisation : accuracy et f1_score).
- Algorithmes testés : `eaSimple` et `eaMuPlusLambda`

#### · Évaluation
Les performances de chaque modèle ont été évaluées sur un jeu de test (30% des données) en utilisant les métriques suivantes :
- **Accuracy**
- **Precision & Recall**
- **F1-Score**
- **Temps d'entraînement**

***

### 📊 Résultats

#### · Performances des modèles d'ensemble

**Gradient Boosting** s'impose comme le leader avec **71.5% d'accuracy** et **57.8% de F1-Score**, démontrant la supériorité des techniques de boosting pour ce problème complexe. 

**Bagging avec Random Forest** se distingue par son excellent compromis performance/efficacité, atteignant **69.2% d'accuracy** en seulement **3 secondes**, soit 5 fois plus rapide que Gradient Boosting.

Les autres modèles d'ensemble (AdaBoost, Bagging LR, Bagging Gauss) montrent des performances intermédiaires entre 64% et 68% d'accuracy.

#### · Performances DEAP

L'apprentissage évolutionnaire révèle des résultats plus contrastés. Sur **32 configurations testées**, la performance moyenne atteint **66.7% d'accuracy** et **43.6% de F1-Score**.

La **configuration optimale** (eaMuPlusLambda avec optimisation F1) rivalise avec les meilleurs modèles d'ensemble en atteignant **65.2% d'accuracy** et **56.3% de F1-Score**, mais au prix d'un temps d'exécution de **614 secondes**.

#### · Comparaison globale

**Gradient Boosting domine** avec le meilleur F1-Score (0.578), suivi de près par la **configuration DEAP optimale** (0.563). Cependant, les **méthodes d'ensemble sont 20 à 200 fois plus rapides** que DEAP.

**Bagging Random Forest** émerge comme la **solution la plus équilibrée**, offrant 92% de la performance de Gradient Boosting en seulement 20% du temps d'exécution.

**Tous les modèles souffrent du déséquilibre des classes**, particulièrement visible dans les métriques de recall qui restent modestes.

***

### 💡 Ce que j'ai appris
#### · Compétences acquises ou renforcées
- **Prétraitement de Données :** Maîtrise complète du pipeline de nettoyage, normalisation et réduction de dimensionnalité (PCA).
- **Apprentissage d'Ensemble :** Implémentation et comparaison de techniques de **Bagging** et de **Boosting**.
- **Apprentissage Évolutionnaire :** Application approfondie de la bibliothèque **DEAP** avec programmation génétique, incluant la définition de primitives, fonctions de fitness et grid search.
- **Optimisation d'Hyperparamètres :** Mise en œuvre d'une recherche exhaustive sur 32 configurations pour identifier les paramètres optimaux.
- **Analyse Comparative :** Évaluation des compromis entre performance prédictive, efficacité computationnelle et robustesse pour des familles d'algorithmes distinctes.
