---
title: 'NLP : TripAdvisor Recommendation Challenge'
publishDate: 2024-11-30 00:00:00
img: /assets/NLP_BM25.jpg
img_alt: NLP vs BM25, TripAdvisor Recommendation Challenge.
description: |
  
tags:
  - NLP
  - Embedding
---

### 🎯 Contexte & Objectif
#### · Présentation du problème
L'algorithme **BM25**, une amélioration de TF-IDF, reste une des approches les plus performantes pour la recherche d'information basée sur les mots-clés. Cependant, cette méthode se base principalement sur la fréquence et la rareté des mots, sans capturer le sens sémantique profond du texte.

#### · Intérêt du projet
Le défi est de développer un système de recommandation d'hôtels plus pertinent que BM25, en se basant uniquement sur le contenu textuel des avis clients. L'objectif est de proposer des lieux similaires non pas par les mots qu'ils partagent, mais par le sens et les expériences décrites dans les commentaires.

#### · Objectif final à atteindre
L'objectif est de construire un modèle non supervisé qui, pour un hôtel donné, recommande l'hôtel le plus similaire en se basant sur ses avis. La performance sera mesurée en comparant les notes moyennes (sur des aspects comme la propreté, le service, etc.) entre l'hôtel de la requête et l'hôtel recommandé. **Le but est d'obtenir une Erreur Quadratique Moyenne (MSE) inférieure à celle du modèle de référence BM25.**

***

### 🧰 Données
#### · Source des données
Le projet utilise le jeu de données **"TripAdvisor Hotel Reviews"** disponible sur Kaggle. Il contient des centaines de milliers d'avis d'hôtels.
[Lien vers le dataset sur Kaggle](https://www.kaggle.com/datasets/joebeachcapital/hotel-reviews/data)

#### · Volume et structure
Le jeu de données initial a été filtré pour ne conserver que les avis possédant des notes sur un ensemble strict de 7 aspects ("service", "cleanliness", "overall", etc.), ce qui a permis de garder **436 356 avis pertinents**. Pour la modélisation, un échantillon de **5000 avis** a été créé, correspondant à 50 avis pour 100 hôtels différents, afin d'avoir un corpus de travail équilibré.

#### · Type de variables
-   **Texte :** Les colonnes `title` et `text` ont été fusionnées en une seule colonne `avis` pour former le corpus de chaque hôtel.
-   **Identifiants :** `offering_id` pour identifier chaque hôtel.
-   **Notes (pour évaluation uniquement) :** Les notes moyennes pour chaque aspect (`avg_service`, `avg_cleanliness`, etc.) ont été calculées par hôtel et utilisées exclusivement pour mesurer la MSE du modèle. Le modèle lui-même n'a pas accès à ces notes pendant la recommandation.

***

### 🧪 Méthodologie
#### · Feature Engineering & Modélisation
Plusieurs approches ont été testées pour battre la baseline BM25.

1.  **Baseline : BM25**
    -   Une implémentation standard de BM25 a été utilisée comme modèle de référence. Cette méthode fonctionne en tokenisant le texte et en calculant un score de pertinence basé sur la fréquence des termes (TF-IDF).

2.  **Approche 1 : Word Embedding avec Word2Vec**
    -   **Prétraitement :**
        1.  Retrait des stopwords, de la ponctuation et mise en minuscules.
        2.  Séparation des avis en tokens (mots).
    -   **Vectorisation :**
        1.  Un modèle **Word2Vec** est entraîné sur l'ensemble des tokens du corpus pour apprendre une représentation vectorielle pour chaque mot.
        2.  Le vecteur associé à chaque mot du vocabulaire est calculé par le modèle.
        3.  Pour chaque avis, un vecteur global est obtenu en calculant la **moyenne des vecteurs de tous les mots** qui le composent.

3.  **Approche 2 : Sentence Embedding avec Sentence-Transformers**
    -   **Vectorisation Sémantique :**
        1.  Le modèle pré-entraîné **`all-MiniLM-L6-v2`** est utilisé pour transformer directement chaque phrase des avis en un vecteur sémantique.
        2.  Le vecteur global d'un avis est ensuite calculé en faisant la moyenne des vecteurs de ses phrases.

#### · Stratégies de Recommandation Testées
Pour chaque méthode d'embedding (Word Embedding et Sentence Embedding), quatre stratégies de prédiction ont été évaluées pour trouver la plus performante :

1.  **Niveau Avis - Distance Euclidienne :** trouver l'avis le plus proche en utilisant la plus petite distance euclidienne.
2.  **Niveau Avis - Similarité Cosinus :** trouver l'avis le plus proche en utilisant la plus grande similarité cosinus.
3.  **Niveau Établissement - Distance Euclidienne :** calculer le vecteur moyen par hôtel, puis trouver l'hôtel le plus proche via la plus petite distance euclidienne entre ces vecteurs moyens.
4.  **Niveau Établissement - Similarité Cosinus :** calculer le vecteur moyen par hôtel, puis trouver l'hôtel le plus proche via la plus grande similarité cosinus.

#### · Évaluation
Le protocole d'évaluation pour chaque stratégie est le suivant :
-   Chaque avis du jeu de test est soumis au modèle comme requête.
-   Le modèle retourne l'hôtel qu'il juge le plus similaire.
-   On calcule l'**Erreur Quadratique Moyenne (MSE)** entre les 7 notes moyennes de l'hôtel-requête et celles de l'hôtel retourné.
-   Le score final est la moyenne de toutes les MSE calculées. **Un score plus bas signifie un meilleur modèle.**

***

### 📊 Résultats
#### · Performances des modèles
Les résultats de l'évaluation ont montré qu'une des approches basées sur les embeddings sémantiques était significativement plus performante que la baseline.
-   **MSE (BM25) :** `1.91`
-   **MSE (Meilleure Approche : Sentence-Transformers + distance euclidienne au niveau avis) :** `1.05`
-   **MSE (autres approches):** `1.12 - 1.28`

#### · Comparaison des approches
L'approche avec **Sentence-Transformers a battu la baseline BM25**, en obtenant une MSE inférieure de près de 45%. L'expérimentation a montré que l'agrégation des vecteurs au niveau de l'avis et l'utilisation de la distance euclidienne donnaient les meilleurs résultats. Cependant, les autres approches ont tout de même montré de meilleures performances que BM25.

#### · Interprétation des résultats
La supériorité du modèle d'embedding s'explique par sa capacité à capturer le **sens** et le **contexte** des avis, plutôt que de se limiter à la surface lexicale. Deux hôtels peuvent être jugés similaires s'ils évoquent des expériences similaires même s'ils n'utilisent pas exactement les mêmes mots.

***

### 💡 Ce que j'ai appris
#### · Compétences acquises ou renforcées
-   **Recherche d'Information :** Implémentation et évaluation d'un modèle de référence classique (BM25).
-   **Prétraitement de Texte :** Application de techniques de nettoyage de texte (lemmatisation, stopwords) adaptées à un corpus d'avis clients.
-   **NLP & Sémantique :** Utilisation de modèles de transformers pré-entraînés (`Sentence-Transformers`) et de modèles personnalisés (`Word2Vec`) pour générer des embeddings de texte et effectuer de la recherche par similarité sémantique.

