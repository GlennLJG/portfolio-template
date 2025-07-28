---
title: 'Computer vision : détection de défauts de soudure' 
publishDate: 2025-01-10 00:00:00
img: /assets/CV_welding.jpg
img_alt: Computer vision for detecting welding defects
description: |
tags:
  - Computer vision
  - YOLO
  - PowerBI
---

### 🎯 Contexte & Objectif
#### · Présentation du besoin métier
Dans les industries critiques comme le pétrole et le gaz, la qualité des soudures est primordiale pour garantir l'intégrité et la sécurité des infrastructures, notamment des pipelines. Les méthodes d'inspection manuelle sont non seulement longues et coûteuses, mais également sujettes à l'erreur humaine.
L'automatisation de la détection de défauts de soudure à l'aide de la vision par ordinateur permet d'améliorer la fiabilité, d'accélérer les processus de contrôle qualité et de réduire les coûts opérationnels.

#### · Objectif final à atteindre
L'objectif est d'entraîner et de comparer les performances de deux modèles de détection d'objets de pointe, **YOLO** et **DETR**, pour identifier avec précision les défauts de soudure. Le but est de déterminer lequel est le plus adapté à ce cas d'usage et de visualiser les résultats de manière interactive grace à PowerBI.

***

### 🧰 Données
#### · Source des données
Le projet utilise le jeu de données public "The Welding Defect Dataset - v2", qui contient des images de soudures avec différents types de défauts.
[Lien vers le dataset sur Kaggle](https://www.kaggle.com/datasets/sukmaadhiwijaya/welding-defect-object-detection/data)

#### · Volume et structure
Le dataset est divisé en ensembles d'entraînement, de validation et de test. Les annotations (bounding boxes) sont fournies au format YOLO (.txt), où chaque ligne contient la classe et les coordonnées de la boîte englobante.

#### · Type de variables (classes)
Le modèle a été entraîné pour détecter et classifier les soudures en trois catégories :
-   `bad weld` (mauvaise soudure)
-   `good weld` (bonne soudure)
-   `defect` (défaut spécifique)

***

### 🧪 Méthodologie
#### · Exploration et nettoyage des données
Pour identifier les potentiels biais lors de l'entainement, les caractéristiques des annotations ont été structuré dans un DataFrame pandas pour faciliter la comparaison. L'analyse s'est concentrée sur la répartition des annotations sur les images (centre, aire, etc...). 

#### · Modélisation (algorithmes, métriques utilisées)
Deux architectures de modèles ont été entraînées et comparées :
1.  **YOLO 11n:** Un modèle rapide et efficace, basé sur une approche à un seul passage (single-shot detector).
2.  **DETR (DEtection TRansformer) :** Un modèle basé sur une architecture de Transformer, qui traite la détection d'objets comme un problème de "set prediction".

#### · Entraînement des modèles
L’entraînement des modèles **YOLOv11n** et **DETR** a débuté par une phase de **préparation des données**.  
Les images et annotations ont été nettoyées, formatées (YOLO pour YOLOv11n, COCO pour DETR), puis réparties en trois ensembles :  
- **train**  
- **validation**  
- **test**

Les deux architectures ont ensuite été **configurées** avec des paramètres adaptés :  
- taille des images  
- nombre de classes  
- taux d’apprentissage  
- nombre d’épochs  
- batch size

Chaque modèle a été **entraîné séparément** sur les données d’apprentissage.

Pendant l'entraînement, les performances ont été suivies à l’aide de métriques telles que :  
- **loss** (perte)  
- **mAP** (mean Average Precision)  

L’ensemble de validation a permis de **surveiller l’overfitting** et d’ajuster les hyperparamètres si nécessaire.

Enfin, une fois l’entraînement terminé, les modèles ont été **évalués sur le jeu de test** pour permettre une comparaison objective de leurs performances.

#### · Comparaison des prédictions
La comparaison est au cœur du projet. Le notebook met en place une méthodologie rigoureuse :
1.  **Standardisation des prédictions :** Les prédictions des deux modèles sont converties et sauvegardées au format COCO JSON pour une évaluation standardisée.
2.  **Création d'un DataFrame comparatif :** Pour chaque boîte englobante de la vérité terrain, le script identifie la prédiction la plus proche (basée sur la distance euclidienne des centres) pour chaque modèl.
3.  **Exportation pour visualisation :** Un DataFrame final fusionne les informations de la vérité terrain avec les prédictions correspondantes de YOLO et DETR, incluant la classe, les coordonnées et l'aire des boîtes. Ce fichier est la source de données pour l'analyse visuelle.

#### · Mise en application
La finalité de l'analyse est un tableau de bord interactif. Les données comparatives préparées dans le notebook sont exportées pour être utilisées dans **Power BI**, permettant une exploration visuelle et approfondie des performances des deux modèles.

***

### 📊 Résultats
#### · Performances du ou des modèles

Pour fournir un premier niveau de comparaison entre YOLOv11n et DETR, les performances ont été évaluées à l’aide de **métriques standards en détection d’objets**. Ces mesures permettent d’analyser la qualité des prédictions à différents niveaux.

- **mAP50 (mean Average Precision à IoU 0.5)**  
  C’est la moyenne de la précision sur toutes les classes, en considérant une prédiction correcte si l’objet détecté recouvre au moins 50 % de l’objet réel. Cette métrique est souvent utilisée comme référence de base.

- **mAP50:95**  
  Cette version plus stricte du mAP prend en compte plusieurs seuils de recouvrement (IoU) entre 0.5 et 0.95. Elle permet de mieux évaluer la **qualité de localisation** des objets, et donne une vision plus complète des performances du modèle.

- **Précision (Precision)**  
  Mesure la proportion de bonnes détections parmi toutes les prédictions faites par le modèle. Une haute précision signifie que le modèle fait peu de fausses détections.

- **Rappel (Recall)**  
  Évalue la capacité du modèle à retrouver tous les objets présents dans l’image. Un bon rappel signifie que le modèle oublie peu d’objets.

En combinant ces métriques, on peut évaluer si un modèle est plutôt conservateur (précis mais peu sensible) ou plus sensible (bon rappel mais avec plus de fausses détections).  
Ces résultats permettent de mieux comprendre les **forces et faiblesses** de chaque modèle dans différents contextes.

#### · Comparaison des approches
L'analyse dans Power BI permet de comparer visuellement les modèles sur plusieurs axes :
-   Nombre de défauts correctement identifiés.
-   Taux de fausses détections.
-   Précision de la localisation des défauts (comparaison des aires et des coordonnées des boîtes).

#### · Interprétation des résultats
La visualisation des données via Power BI permet de tirer des conclusions claires sur les forces et faiblesses de chaque modèle dans le contexte spécifique de la détection de défauts de soudure, aidant à choisir la meilleure approche pour un déploiement industriel. Au terme de la comparaison, de meilleures performances ont été observée avec Yolo, que ce soit en terme de qualité des prédictions ou en terme de vitesse et simplicité d'entraînement.

***

### 💡 Ce que j’ai appris
#### · Compétences acquises ou renforcées
-   Entraînement et fine-tuning de modèles de détection d'objets (YOLO, DETR).
-   Mise en place d'un pipeline de comparaison de modèles de Computer Vision.
-   Manipulation de données géospatiales (bounding boxes) et conversion entre différents formats d'annotation (YOLO, COCO).
-   Utilisation de pandas pour structurer et fusionner des données complexes (vérité terrain et prédictions multiples).
-   **Data Visualization :** Création d'un tableau de bord avec Power BI pour présenter et analyser les résultats d'expériences de machine learning.


