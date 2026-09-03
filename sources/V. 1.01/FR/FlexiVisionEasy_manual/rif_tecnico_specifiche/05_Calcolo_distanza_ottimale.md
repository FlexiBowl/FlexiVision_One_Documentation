(distanza_lavoro)=
# **Calcul de la distance optimale de travail**

Cette section définit la distance de travail (Working Distance) recommandée entre la caméra et la surface de travail du FlexiBowl, ainsi que la sélection des objectifs nécessaires pour garantir un champ de vision (Field of View, FOV) correct.

Le bon choix de la distance de travail et de l'objectif est crucial pour :
- S'assurer que toute la surface utile du FlexiBowl® est visible
- Obtenir la résolution nécessaire à la détection des pièces
- Minimiser les distorsions optiques
- Faciliter l'étalonnage du système

---

## Distances de travail recommandées et choix des objectifs

Le choix de l'objectif dépend strictement de la distance de montage recommandée entre la caméra et la surface de travail du FlexiBowl®. Le respect de la distance de travail standard permet d'obtenir un champ de vision correct et de minimiser les problèmes de distorsion optique.


```{note}
**Objectif déjà inclus**

L'objectif approprié pour le modèle FlexiBowl® spécifié dans la commande est toujours inclus avec le FlexiVision One et est fourni dans un emballage séparé de la caméra. Il n'est pas nécessaire de l'acheter séparément.
```

### *Schéma des distances et du champ de vision*

Le diagramme suivant illustre la relation entre la distance de travail, la longueur focale de l'objectif et la zone de visualisation résultante pour les différents modèles FlexiBowl®.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distance de travail
:width: 40%
:align: center
```

**Légende du schéma :**
- **Distance de travail** : Distance verticale entre l'objectif de la caméra et la surface de travail du FlexiBowl®
- **Zone de visualisation** : Surface du FlexiBowl® couverte par le champ de vision de la caméra

### *Tableau récapitulatif par modèle*

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modèle FlexiBowl®
  - Distance de travail recommandée (Working Distance)
  - Objectif inclus dans le kit (longueur focale)
* - **FB 200**
  - 800 mm 
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

```{warning}
**Importance de la distance correcte**

Des écarts importants par rapport à la distance de travail recommandée peuvent entraîner :

- **Distance trop courte** : FOV insuffisant (partie du FlexiBowl® non visible).
- **Distance trop longue** : Résolution insuffisante pour détecter les petites pièces, flou

Toujours respecter les distances indiquées dans le tableau lors du montage mécanique de la caméra.
```
### *Positionnement de la caméra*

**Configuration correcte.** La caméra doit être positionnée au centre et avec la même orientation angulaire que la zone de visualisation du FlexiBowl® (zone de rétro-éclairage). De cette manière, le champ de vision (indiqué en vert) couvre symétriquement l'ensemble de la zone de travail, ce qui garantit le bon fonctionnement du système de vision.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distance de travail
:width: 70%
:align: center
```

**Configurations incorrectes.** Les images montrent des exemples de positionnement incorrect de la caméra : le champ de vision (indiqué en rouge) est décentré par rapport à la zone de visualisation, ne couvre qu'une partie de la zone de travail ou inclut des zones situées en dehors de la zone de travail. Ces configurations compromettent la reconnaissance des pièces et le fonctionnement du système de vision.  

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Distance de travail
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Distance de travail
:width: 60%
:align: center
```
---

## Positionnement du TopLight 

Si le système comprend un TopLight (éclairage par le haut), son positionnement doit avoir la même orientation angulaire que la caméra afin de garantir un éclairage uniforme. Il doit être installé sur un support mécaniquement indépendant du support de la caméra, de sorte qu'il ne soit pas nécessaire de desserrer ou de démonter la caméra pour retirer ou remplacer le système d'éclairage.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Valeur recommandée
* - **Distance de la surface du FlexiBowl®**
  - Similaire à la distance de travail de la caméra (±100 mm)
* - **Position par rapport à la caméra**
  - Concentrique (même axe optique que la caméra)
* - **Orientation**
  - Parallèle à la surface du FlexiBowl® et même orientation angulaire que la caméra (côté long de la zone d'observation - côté long de l'éclairage)
* - **Hauteur relative caméra-TopLight**
  - Optique de visualisation affleurant la surface supérieure du Top Light (laisser libre accès aux anneaux de réglage de l'optique de visualisation)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Distance de travail
    :width: 80%
    :align: center
    :::
```

```{tip}
Pour obtenir une uniformité d'éclairage optimale, suivre les instructions qui viennent d'être données.
```

```{warning}
**Éviter les reflets directs**

En positionnant le TopLight, veiller à ce que :

- La lumière ne soit pas réfléchie directement de la surface du FlexiBowl® vers la caméra (ce qui provoque un éblouissement)
- Il n'y ait pas d'ombres causées par les composants mécaniques
- L'éclairage soit aussi uniforme que possible sur l'ensemble de la surface utile

```

---

## Références connexes

Pour terminer l'installation et la configuration du système :

- **Installation mécanique de la caméra** : [Installation mécanique](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Spécifications techniques de la caméra** : [Spécifications de FlexiVision One](04_Specifiche_FlexiVision.md)
- **Étalonnage du système** : [Étalonnage de la caméra](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Câblage électrique** : [Câblage et connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

