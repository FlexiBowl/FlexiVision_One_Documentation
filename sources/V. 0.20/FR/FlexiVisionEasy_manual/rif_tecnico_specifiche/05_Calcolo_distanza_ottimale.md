(distanza_lavoro)=
# **Calcul de la Distance de Travail Optimale**

Cette section définit la distance de travail (Working Distance) recommandée entre la caméra et le plateau FlexiBowl, ainsi que la sélection des objectifs nécessaires qui en découle pour garantir le Champ de Vision correct (Field of View, FOV).

Le choix correct de la distance de travail et de l'objectif est fondamental pour:
- Garantir que toute la surface utile du FlexiBowl est visible
- Obtenir la résolution nécessaire pour détecter les pièces
- Minimiser les distorsions optiques
- Faciliter la calibration du système

---

## Distances de travail recommandées et sélection des objectifs

Le choix de l'objectif dépend strictement de la distance de montage recommandée entre la caméra et la surface du plateau FlexiBowl. Le maintien de la distance de travail standard garantit le FOV correct et minimise les problèmes de distorsion optique.


```{note}
**Objectif déjà inclus**

L'objectif approprié pour le modèle FlexiBowl spécifié dans la commande est toujours inclus dans le pack FlexiVision One et est fourni dans un emballage séparé de celui de la caméra. Il n'est pas nécessaire de l'acheter séparément.
```

### Schéma des distances et du champ de vision

Le diagramme suivant illustre la relation entre distance de travail, longueur focale de l'objectif et zone de vision résultante pour les différents modèles de FlexiBowl.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distance De Travail
:width: 40%
:align: center
```

**Légende du schéma:**
- **Distance de Travail**: Distance verticale entre la face frontale de l'objectif et la surface du plateau FlexiBowl
- **Zone de vision**: Zone de la surface du FlexiBowl couverte par le champ de vision de la caméra

### Tableau récapitulatif par modèle

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modèle FlexiBowl
  - Distance de Travail Recommandée (Working Distance)
  - Objectif Inclus dans le Kit (Longueur Focale)
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

Des écarts significatifs par rapport à la distance de travail recommandée peuvent provoquer:

- **Distance trop courte**: FOV insuffisant (une partie du FlexiBowl non visible).
- **Distance trop longue**: Résolution insuffisante pour détecter les petites pièces, flou

Toujours respecter les distances indiquées dans le tableau pendant le montage mécanique de la caméra.
```
### Positionnement Caméra 

**Configuration correcte.** La caméra doit être positionnée au centre et avec la même orientation angulaire que la zone de vision du FlexiBowl (zone backlight). De cette façon, le champ de vision (indiqué en vert) couvre symétriquement toute la zone de travail, garantissant le bon fonctionnement du système de vision.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distance De Travail
:width: 70%
:align: center
```

**Configurations incorrectes.** Les images montrent des exemples de positionnement incorrect de la caméra: le champ de vision (indiqué en rouge) est décentré par rapport à la zone de vision, ne couvrant que partiellement la zone de travail ou incluant des zones extérieures à celle-ci. Ces configurations compromettent la reconnaissance des pièces et le fonctionnement du système de vision.  

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Distance De Travail
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Distance De Travail
:width: 60%
:align: center
```
---

## Positionnement TopLight 

Si le système inclut un TopLight (illuminateur par le haut), son positionnement doit avoir la même orientation angulaire que la caméra afin de garantir un éclairage uniforme. Il doit être installé sur un support mécaniquement indépendant du support de la caméra, de sorte que le retrait ou le remplacement du système d'éclairage ne nécessite pas de desserrer ou de démonter la caméra.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Valeur Conseillée
* - **Distance de la surface FlexiBowl**
  - Similaire à la Working Distance de la caméra (±100 mm)
* - **Position par rapport à la caméra**
  - Concentrique (même axe optique que la caméra)
* - **Orientation**
  - Parallèle à la surface du FlexiBowl et même orientation angulaire que la caméra (côté long zone de vision - côté long d'éclairage)
* - **Hauteur relative caméra-TopLight**
  - Optique de vision affleurante à la surface supérieure Top Light (laisser libre l'accès aux bagues de réglage de l'optique de vision)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Distance De Travail
    :width: 80%
    :align: center
    :::
```

```{tip}
Pour obtenir la meilleure uniformité d'éclairage, suivre les indications qui viennent d'être fournies 
```

```{warning}
**Éviter les réflexions directes**

Lors du positionnement du TopLight, s'assurer que:

- La lumière ne se réfléchit pas directement de la surface du FlexiBowl vers la caméra (provoquant un éblouissement)
- Il n'y a pas d'ombres causées par des composants mécaniques
- L'éclairage est aussi uniforme que possible sur toute la surface utile

```

---

## Références associées

Pour compléter l'installation et la configuration du système:

- **Installation mécanique caméra**: [Installation Mécanique](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Spécifications techniques caméra**: [Spécifications FlexiVision One](04_Specifiche_FlexiVision.md)
- **Calibration système**: [Calibration de la Caméra](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Câblage électrique**: [Câblage et Connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

