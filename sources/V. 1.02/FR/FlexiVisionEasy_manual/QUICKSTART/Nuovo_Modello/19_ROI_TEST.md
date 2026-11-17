(roitest)=
# **Définition ROI et tolérances**

Cette section permet de définir la Region Search (zone de recherche) et les tolérances de reconnaissance pour le modèle créé. Ces paramètres déterminent où et avec quelle précision FlexiVision One recherchera les composants pendant le fonctionnement.

**Qu'est-ce que la Region Search ?**  
La **Region Search** est la zone dans laquelle FlexiVision One recherchera et détectera les composants à prélever.

# Procédure

Après avoir cliqué sur «&nbsp;Next&nbsp;» sur la page de formation, la page **Define Robot Picking Limit Area Model** s'ouvre automatiquement.



## Étape 1 : Définition de la zone

:::{video} ../../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **1**
  - Sur la page **Define Robot Picking Limit Area Model**, modifier l'encadré pour délimiter la zone de recherche
* - **2**
  - Une fois que la Region Search est correctement dimensionnée, cliquer sur <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
* - **3**
  - S'ouvre la page **Locator Model 1 Cam 1**
```
```{tip}
Dimensionner la zone en fonction de l'espace de travail réel du robot, en évitant les zones inaccessibles.
```
:::{tip}
En cas de doutes lors de la configuration, consulter le bouton **INFO** présent sur la page actuelle.
:::

### *Aperçu de l'interface Locator Model*

![Page Locator Model](../../../../../_shared/media/images/pagina_locatormodel.png)
```{list-table}
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Description
* - **Test**
  - Effectue un test de reconnaissance en temps réel avec les paramètres actuels
* - **Accept Threshold**
  - Seuil de fidélité minimum (score) qu'un composant doit avoir pour être accepté
* - **Results Panel**
  - Panneau montrant tous les composants détectés avec des détails (Id, coordonnées, score)
```
### Tutoriel vidéo
Tutoriel vidéo expliquant les étapes 2 et 3 qui suivent : 
:::{video} ../../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
    :width: 100%
    :align: center
:::




## Étape 2 : Préparation de la scène
```{list-table}
:widths: 5 95

* - **4**
  - Placer **d'autres composants** dans la zone de visualisation de manière aléatoire autour du composant de référence afin de ne pas les confondre avec lui.
    
    :::{warning}
    Ne pas toucher au composant de référence utilisé pour le training ! Et ne pas le perdre de vue !
    :::
```

## Étape 3 : Exécution de Test et Accept Threshold
```{list-table}
:widths: 5 95

* - **5**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon"> pour effectuer la reconnaissance

* - **6**
  - Observer combien de composants sont détectés et avec quels scores

* - **7**
  - Modifier l'**Accept Threshold** en fonction des exigences de l'application
    
    :::{note}
    **Qu'est-ce que l'Accept Threshold ?**
    
    C'est le **degré minimal de fidélité** (score) qu'un composant détecté doit avoir par rapport au modèle de référence pour être accepté.
    
    - **Valeur 0,95** → N'accepte que les composants avec une fidélité ≥ 95 %
    - **Valeur 0,80** → Accepte les composants avec une fidélité ≥ 80 %
    - **Valeur plus élevée** → Plus restrictif (moins de faux positifs)
    - **Valeur plus basse** → Plus permissif (détecte également les composants moins similaires à celui de référence)
    :::
```
```{tip}

**Approche itérative recommandée :**

1. Commencer avec Accept Threshold = 0.85
2. Faire des tests et observer les résultats
3. Si **trop de pièces sont acceptées** (y compris les faux positifs) → Augmenter le seuil (par ex. : 0,90)
4. Si **trop peu de pièces sont détectées** (bonnes pièces écartées) → Diminuer le seuil (par ex. : 0,80)
5. Répéter jusqu'à trouver la valeur optimale pour l'application

**Objectif** : Trouver la valeur la plus élevée possible qui détecte toutes les bonnes pièces mais écarte les plus mauvaises.
```
:::{tip}
En cas de doutes lors de la configuration, consulter le bouton **INFO** présent sur la page actuelle.
:::

---

## Interprétation des résultats

### *Affichage des composants détectés*

Le panneau Results affiche tous les composants détectés qui respectent l'Accept Threshold :
```{list-table}
:header-rows: 1
:widths: 15 25 60

* - Champ
  - Type
  - Description
* - **Id**
  - Entier
  - Identifiant unique progressif (0, 1, 2, ...)
* - **X**
  - Millimètres
  - Coordonnée X du composant (référence origine de la grille d'étalonnage)
* - **Y**
  - Millimètres
  - Coordonnée Y du composant (référence origine de la grille d'étalonnage)
* - **Rotation**
  - Degrés
  - Angle de rotation du composant (0-360°)
* - **Score**
  - Pourcentage
  - Degré de fidélité par rapport au modèle de référence (0.00-1.00)
```
```{admonition} Système de priorité
:class: info
Par défaut, FlexiVision One trie automatiquement tous les composants reconnus par **score décroissant** :
- **Id 0** → Composant ayant le score le plus élevé (le plus similaire au modèle de référence)
- **Id 1** → Deuxième meilleur composant
- **Id 2** → Troisième meilleur composant
- Et ainsi de suite...
```
### *Exemple d'interprétation*

Supposons que ces résultats apparaissent après le test :

| Id | X | Y | Rotation | Score |
|----|-------|-------|----------|-------|
| 0 | 125.4 | -45.2 | 15.3° | 0.92 |
| 1 | -80.1 | 32.5 | 178.5° | 0.89 |
| 2 | 45.7 | 110.3 | 92.1° | 0.86 |
| 3 | -150.2 | -95.7 | 45.8° | 0.83 |

**Interprétation :**
- **Id 0** : Meilleure correspondance (92 %), sera prélevé en premier
- **Id 1** : Bonne correspondance (89 %), deuxième option
- **Id 2** : Correspondance satisfaisante (86 %), troisième option
- **Id 3** : Correspondance acceptable (83 %), quatrième option

Si Accept Threshold est à 0,85 :
- Id 0, 1, 2 seraient acceptés
- Id 3 serait rejeté (score 0.83 < 0.85)

---

# Finalisation

## Étape 4 : Nettoyage et suite
```{list-table}
* - **8**
  - Retirer **tous les composants** de la zone, **à l'exception du composant de référence** et des deux objets situés à ses côtés
    :::{danger}
      **Ne pas déplacer le composant de référence !**
      Même en nettoyant la scène, veillez à ne pas heurter ou déplacer le composant de référence. Ses coordonnées sont encore nécessaires pour l'étalonnage du robot dans la phase finale.
    :::
* - **9**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> → s'ouvre la page **Clearances**
```
```{seealso}
Passer à la [Configuration des Clearances](istogrammi) pour définir les zones libres.
```

