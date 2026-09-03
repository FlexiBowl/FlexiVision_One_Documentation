(Installazione_Meccanica)=
# **Installation mécanique du système**

Cette section décrit les exigences de montage et de positionnement des principaux composants du système de vision FlexiVision One.     L'installation ne doit être réalisée qu'après l'installation mécanique de base du FlexiBowl® et de la trémie, le cas échéant.

```{warning}
**Prérequis obligatoires**

Avant de procéder à l'installation des composants de vision, s'assurer que :

- Le FlexiBowl® a été monté et fixé à la structure de support (cellule robotisée)
- La trémie a été installée correctement
- La structure de support pour la caméra et le dispositif d'éclairage a été préparée

Pour l'installation du FlexiBowl®, veuillez vous référer au manuel dédié fourni.
```

```{note}
**Compétences requises**

L'installation mécanique demande des :
- Compétences de base en assemblage mécanique
- Utilisation d'instruments de mesure (jauge, niveau à bulle, mètre)
- Capacité à lire des dessins techniques
```

---

## Montage du VisionController

Le VisionController (PC industriel) assure le traitement des images et la communication avec le robot.   
En tant que composant électronique sensible, il doit être positionné avec soin pour assurer une ventilation adéquate et une protection contre les contaminants.

### *Spécifications techniques* 
```{figure} ../../../../_shared/media/images/Dim_PC.png
:alt: Dimensions du VisionController
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60
* - **Trous de vis**
  - M5
* - **Caractéristique**
  - **Valeur**
* - Largeur (totale avec supports)
  - 245.00 mm
* - Largeur (corps)
  - 227.00 mm
* - Largeur du panneau des connecteurs
  - 200.00 mm
* - Hauteur (totale avec supports)
  - 123.00 mm
* - Hauteur (corps)
  - 120.00 mm
* - Profondeur
  - 61.10 mm
```

### *Exigences de montage*

```{list-table}
:header-rows: 1
:widths: 35 65

* - Exigences
  - Spécifications
* - **Emplacement recommandé**
  - A l'intérieur du tableau électrique ou sur un panneau dédié près de la cellule robotisée
* - **Espace de ventilation**
  - Minimum 50 mm sur tous les côtés pour la circulation de l'air
* - **Fixation**
  - Rail DIN 35 mm ou vis M5 sur le panneau
* - **Température ambiante**
  - 1 °C ~ +50 °C (vérifier les spécifications complètes dans la section [Spécifications du VisionController](specifiche_VC))
* - **Protection**
  - IP40 minimum (montage dans un tableau électrique IP54 recommandé)
```

### *Procédure d'installation*

#### *Assemblage avec trous*

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Phase
     - Description opérationnelle
   * - **1. Préparation du support**
     - Percer les trous selon les instructions de la fiche technique 
   * - **2. Déballage**
     - Sortir le VisionController de son emballage en prenant soin de ne pas endommager les connecteurs. Vérifier l'intégrité du produit.
   * - **3. Fixation**
     - Fixer le VisionController avec des vis M5  
```

#### *Montage sur rail DIN*

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Phase
     - Description opérationnelle
   * - **1. Préparation du support**
     - vérifier que le rail est propre et bien fixé.
   * - **2. Déballage**
     - Sortir le VisionController de son emballage en prenant soin de ne pas endommager les connecteurs. Vérifier l'intégrité du produit.
   * - **3. Fixation**
     - Accrocher l'appareil en le faisant glisser sur le rail jusqu'à ce qu'il s'enclenche.  
```

```{warning}
**Ventilation**

Le VisionController génère de la chaleur pendant son fonctionnement. Veiller à ce qu'il y ait toujours au moins 50 mm d'espace libre autour de l'appareil.
Sinon, il y a un risque de :
- Surchauffe et arrêt automatique
- Baisse des performances
- Endommagement des composants internes
```

---

## Montage de la caméra

Le positionnement et l'alignement précis de la caméra sont des étapes critiques qui influent directement sur la précision de l'étalonnage et les performances du système de prélèvement.


### *Distance de travail optimale*

La caméra doit être montée de manière à ce que la face avant de l'objectif soit placée à une distance spécifique (distance de travail) de la surface de travail du FlexiBowl®.  
Pour un calcul détaillé de la distance optimale pour votre application, veuillez vous référer à la section dédiée : [Calcul de la distance optimale](distanza_lavoro)

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distance de travail
:width: 40%
:align: center
```

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

### *Positionnement et alignement*

L'alignement correct de la caméra est essentiel pour obtenir des images de qualité et garantir la précision du prélèvement.

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
**Configuration correcte.** La caméra doit être positionnée au centre de la zone de visualisation du FlexiBowl® (zone de rétro-éclairage). De cette manière, le champ de vision (en vert) couvre symétriquement l'ensemble de la zone de travail, ce qui garantit le bon fonctionnement du système de vision.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distance de travail
:width: 70%
:align: center
```

```{list-table}
* - **Centrage :**
  - 
    - La caméra doit être positionnée exactement au-dessus de la zone de visualisation du FlexiBowl®
    - Tolérance de centrage maximale : ±5 mm
* - **Orthogonalité :**
  - 
    - La caméra doit être montée parfaitement parallèlement à la surface de travail du FlexiBowl®
    - Aucune inclinaison latérale ni rotation par rapport à la verticale n'est autorisée
    - Tolérance d'inclinaison maximale : ±1°
```

```{tip}
Pour faciliter l'installation et permettre des ajustements ultérieurs, il est fortement recommandé de concevoir le support mécanique de la caméra avec la possibilité de micro-ajustements&nbsp;:
- **Axe Z (hauteur)** : -10 mm / +30 mm (pour le réglage de la distance de travail)
- **Axe X (gauche-droite)** : ±10 mm (pour un centrage précis)
- **Axe Y (avant-arrière)** : ±10 mm (pour un centrage précis)
Cette flexibilité est particulièrement utile lors de l'étalonnage initial et pour tout ré-étalonnage ultérieur.
```

### *Dimensions de la caméra* 
```{figure} ../../../../_shared/media/images/Dimensioni_Cam.png
:alt: Dimensions caméra CAM-CIC-5000-20G-1
:align: center
:width: 100%

Dimensions de la caméra CAM-CIC-5000-20G-1 (mm)
```
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Caractéristique**
  - **Valeur**
* - Largeur × Hauteur (corps)
  - 29 × 29 mm
* - Profondeur (corps)
  - 42.0 mm
* - Profondeur totale (y compris le connecteur arrière)
  - 48.9 mm
* - Saillie avant (raccord de l'objectif)
  - 12.60 mm
* - Entraxe des trous de fixation latéraux (M2)
  - 20.0 × 23.7 mm
* - Trous de fixation avant
  - 2× M2 profondeur 3 mm
* - Trous de fixation latéraux
  - 4× M2 profondeur 3,5 mm + 3× M3 profondeur 3,5 mm
* - Poids
  - 88 g
```
```{warning}
**Fixation :**
- Utiliser les 4 trous de fixation M3 sur le corps de la caméra
- Vis recommandées : M3 A2 / M3 8.8
- Couple de serrage : 0.5 Nm (ne pas trop serrer pour éviter les déformations)
```
```{tip}
**Réglage de la position de la chambre**

Pour permettre des ajustements ultérieurs et éviter les problèmes d'alignement, le support mécanique doit être conçu avec des possibilités de micro-ajustement sur tous les axes :

- **Axe Z (hauteur)** : -10 mm / +30 mm
- **Axe X (gauche-droite)** : ±10 mm
- **Axe Y (avant-arrière)** : ±10 mm

Un support avec des vis serrées en permanence sans possibilité de réglage rend impossible la correction de la position de la caméra après le montage initial.
```
### *Vérification du montage de l'objectif*

```{warning}
Avant de procéder à la fixation finale&nbsp;:
1. Vérifier visuellement que l'objectif est installé.
2. Vérifiez que la distance focale est correcte pour votre modèle FlexiBowl® (étiquette sur l'objectif ou documentation de commande).
3. Vérifier que l'objectif est bien vissé (contact métal sur métal entre l'objectif et le boîtier de la caméra).
4. NE PAS retirer ni desserrer l'objectif s'il est déjà correctement monté.
```
### *Installation de la caméra*
Pour garantir le bon fonctionnement du système de vision, la caméra doit être installée sur un support rigide et stable.
Le système FlexiBowl® ne génère pas de vibrations ; cependant, d'autres sources de vibrations sont présentes dans les lignes automatisées (robots industriels, systèmes de manutention, autres machines sur la ligne).

Si ces vibrations sont transmises à la caméra, l'image capturée peut être instable et les coordonnées calculées par le système de vision peuvent ne pas être fiables, ce qui compromet la précision du prélèvement robotisé.

![Installation de la caméra](../../../../_shared/media/images/installazionecamera.png)

:::{tip}
Pour cette raison, il est recommandé de :

- installer la caméra sur une structure rigide et stable

- éviter les supports soumis aux vibrations provenant de robots ou d'autres machines

- utiliser de préférence une structure indépendante de la machine
:::

```{warning}
**Vis de fixation de la caméra : prévention du desserrage**

Les vis de fixation de la caméra peuvent se desserrer avec le temps pour les raisons suivantes :

- **Couple de serrage excessif (> 0,5 Nm)** : peut provoquer des déformations du corps de la caméra et un desserrage ultérieur. Toujours serrer avec un couple maximal de **0,5 Nm**.
- **Vibrations transmises par la ligne** : utiliser un **frein filet moyen** sur toutes les vis de fixation.
- **Vis inadaptées** : vérifier l'utilisation de vis **M3 × 8 mm inox** comme recommandé.
```

### *Réglage de la position de la caméra :*

Le support de la caméra doit permettre d'ajuster la position pour permettre un alignement correct avec la zone de prélèvement du FlexiBowl®.

![Réglages caméra](../../../../_shared/media/images/regolazionicamera.png)

:::{note}
En partant d'un positionnement nominal avec inclinaison, hauteur et positionnement corrects au centre de la zone rétroéclairée, il est recommandé de prévoir les réglages suivants :

Réglage X/Y → ± 50 mm
Réglage Z → ± 50 mm
Rotation θ → ± 10°
:::

```{caution}
**Caméra endommagée pendant le montage**

Pour éviter d'endommager la caméra pendant l'installation et le réglage :

- **Couple de serrage excessif** : ne pas dépasser **0,5 Nm** de couple sur les vis M3. Le dépassement de cette valeur peut entraîner une déformation irréversible du corps optique.
- **Manipulation incorrecte** : toujours manipuler la caméra avec précaution, en évitant toute pression directe sur le corps optique et le capteur.
- **Chocs pendant l'installation** : protéger la caméra lors de travaux mécaniques environnants (perçage, fraisage, serrage des structures).
```
---

## Montage du Toplight

Si la commande comprend un Toplight (dispositif d'éclairage par le haut), celui-ci doit être monté sur la même structure de support que la caméra afin d'assurer un éclairage uniforme de la surface de travail.

:::{attention}
Lors du montage, l'appareil doit être éteint et débranché.
:::
### *Dimensions du Toplight* 
![Dimensioni Toplight](../../../../_shared/media/images/toplight_dim.JPG)

| Longueur x largeur (mm) | Hauteur (mm) | Hauteur avec plaque de fixation (mm) | Diamètre du trou central | Surface utile maximale [A x B] | Périmètre utile maximal |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **A x B** | **C** | **±10 mm** | **D** | **–** | **–** |
| 500x300 | 45 | 55 | 65 | 0,15 m² | 1,6 m |
| 700x300 | 45 | 55 | 65 | 0,21 m² | 2 m |
| 700x500 | 45 | 55 | 65 | 0,35 m² | 2,4 m |
| 900x600 | 45 | 55 | 65 | 0,54 m² | 3 m |

### *Positionnement du Toplight* 
Le toplight doit être positionné au centre de la surface utile du panneau lumineux,
avec l'optique de la caméra montée à l'intérieur du trou central, au ras de la surface supérieure du toplight.   
Les flèches rouges indiquent les vis de fixation des bagues de l'objectif, l'une pour le réglage de la mise au point et l'autre pour le réglage de l'ouverture. Comme le montre la figure, le toplight doit être monté de manière à ce que les deux vis restent accessibles par le haut. 

![Position TopLight et Cam](../../../../_shared/media/images/posizione_cam_TPL_B.png)

Le champ de vision de la caméra et le faisceau lumineux du toplight (en vert) doivent être alignés de manière concentrique et perpendiculaire à la zone de visualisation du FlexiBowl®.    
Comme le montrent les trois vues (frontale, supérieure et axonométrique), le toplight doit éclairer exactement la zone encadrée par la caméra, les deux composants étant centrés sur l'axe optique vertical du système.  

![Position Toplight Cam + FB](../../../../_shared/media/images/posizioneTPL_giusta.png)

Un mauvais positionnement se produit lorsque le toplight et la caméra ne sont pas centrés sur la zone de visualisation du FlexiBowl®.   
Comme illustré (en rouge), les deux erreurs typiques sont les suivantes :  
- se déplacer vers l'avant ou vers l'arrière par rapport à la zone de visualisation.  
- faire pivoter le toplight par rapport à cette dernière.   
  
Dans les deux cas, l'éclairage est décalé et non perpendiculaire, ce qui compromet la qualité de l'acquisition.

![Position erronée Toplight Cam + FB](../../../../_shared/media/images/posizioneTPL_sbagliata.png)

### *Procédure d'installation*
```{list-table}
:header-rows: 1
:widths: 35 65

* - **Phase**
  - **Instructions d'utilisation**
* - **1. Positionnement**
  - Fixer le Toplight sur la structure de support dans une position concentrique par rapport à la caméra.
* - **2. Distance de la surface**
  - Positionner le dispositif d'éclairage à une distance de la surface du FlexiBowl® similaire à celle de la caméra pour :
    
    * Minimiser les ombres projetées par les pièces
    * Maximiser l'uniformité de la lumière
    * Éviter les réflexions directes vers la caméra
* - **3. Orientation**
  - Veiller à ce que la surface d'émission du Toplight soit parallèle à la surface de travail du FlexiBowl®.
* - **4. Angle d'éclairage**
  - Perpendiculaire à la surface (inclinaison de 0°).
* - **5. Fixation**
  - Selon les spécifications du mode choisi (voir section suivante).
```

### *Modes de fixation*

Le Toplight peut être fixé de deux manières : sur l'[angle](angolo) ou sur le [côté](lato).

:::{note}
Les composants de fixation **ne sont pas inclus** dans l'approvisionnement du Toplight. L'assemblage peut donc être personnalisé en fonction des besoins d'installation.

- Fixation sur le côté (rainure) : écrous M4 **fournis**
- Fixation sur l'angle : vis CHC M4x20 **non fournies**

Dans les deux cas, l'utilisation d'un **frein filet** (non fourni) est recommandée pour éviter le desserrage au fil du temps. Le couple de serrage recommandé est compris entre **0,5 et 1,5 Nm.**
:::

(angolo)=
#### *1. Fixation sur l'angle*

La fixation sur l'angle se fait à l'aide de vis CHC M4x20 (non fournies) appliquées dans les trous situés aux quatre coins du Toplight.
```{figure} ../../../../_shared/media/images/fissaggio_angolo.png
:alt: Fixation du Toplight sur l'angle avec vis CHC M4x20
:align: center
:width: 60%

Fixé à l'angle à l'aide d'une vis CHC M4x20 (non fournie).
```

(lato)=
#### *2. Fixation sur le côté (rainure)*

La fixation sur le côté nécessite 4 écrous M4 (fournis) à insérer dans la rainure latérale du profilé du Toplight.  
   La profondeur maximale d'insertion de l'écrou dans la rainure est de **5 mm.**  
     Les vis recommandées sont de type M4x8.

```{figure} ../../../../_shared/media/images/fissaggio_lato.JPG
:alt: Fixation du Toplight sur le côté 
:align: center
:width: 100%

Fixation sur le côté
```
(montaggio_staffa)=
##### Fixation sur le côté avec des supports 
Si le Toplight est fixé avec des supports : 

:::{error}
![montaggio Laterale](../../../../_shared/media/images/errorimontaggiolaterale.png)
:::

:::{tip}
![montaggio Laterale](../../../../_shared/media/images/montaggiolaterale.png)
:::

:::{card}
  Pour le montage latéral, il est possible d'acheter **séparément** la [staffa](staffa) appropriée.
:::



### *Câblage de l'illuminateur*


![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Exigence / Action
* - **Tension**
  - 24V DC (±10 %). Tension minimale de fonctionnement : 20V DC sur l'entrée de la lumière.
* - **Connecteur**
  - M12 à 5 broches (codage en T).
* - **Brochage du connecteur**
  - Broche 1 : +24V (marron) — Broche 3 : GND (bleu) — Broche 4 : STROBE PNP (noir)
* - **Mode STROBE (PNP)**
  - De 5V à 24V pour un allumage à 100 %. De 0V à 1V pour une extinction à 100 %.
* - **Mode CONTINU**
  - Broche 1 (+24V) et Broche 3 (GND) connectées ; Broche 4 (PNP) connectée à la Broche 1.
* - **Chute de tension (câble M12, 10 m)**
  - 1,15V @ 5A — 2,3V @ 10A — 3,5V @ 15A — 4,6V @ 20A (max 20A)
* - **Blindage**
  - Utiliser des câbles blindés pour réduire les interférences électromagnétiques (EMI).
```
```{warning}
**Sécurité électrique**

- Respecter les tensions d'alimentation et les bornes de raccord indiquées.
- Ne pas modifier ou démonter le produit.
- Ne pas brancher ou nettoyer l'appareil lorsqu'il est sous tension.
- Ne pas regarder directement la source lumineuse.
```
```{note}
Pour plus de détails sur les connexions électriques, consultez la section [Câblage et connexions](10_Cablaggio_Connessioni.md).
```
---

## Plan complet

```{raw} html
<div style="
    border: 2px solid #0d6efd;
    border-radius: 8px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
    background-color: #f0f6ff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
">
    <div>
        <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem;">📐 Flexibowl General Layout.STEP</div>
        <div style="font-size: 0.95rem; color: #444;">Fichier CAO avec la disposition complète entre FlexiBowl®, Toplight et Caméra. À utiliser pour l'intégration mécanique du système.</div>
    </div>
    <a href="https://arsautomationsrl-my.sharepoint.com/:f:/g/personal/documentation_arsautomation_com/IgBMPLcyTzL8TbeSdjCwp6miAZlpuvrhEkqWnkK4AxLJEHU?e=gXEc2x" target="_blank" style="
        display: inline-block;
        padding: 0.7rem 1.4rem;
        background-color: #0d6efd;
        color: white !important;
        font-weight: 600;
        font-size: 1rem;
        border-radius: 6px;
        text-decoration: none !important;
        white-space: nowrap;
        flex-shrink: 0;
    ">⬇ Télécharger</a>
</div>
```
---
(luce_ambientale)=
## Blindage contre la lumière ambiante

La stabilité du système de vision dépend fortement de la constance des conditions d'éclairage. Les variations de la lumière ambiante peuvent entraîner des lectures incohérentes.

Le système de vision fonctionne en comparant chaque image acquise à un modèle de référence. Si les conditions d'éclairage varient d'une numérisation à l'autre, le système peut avoir des difficultés à reconnaître correctement les pièces. La lumière ambiante - solaire, artificielle ou réfléchie - qui pénètre dans la cellule est la principale cause d'instabilité des performances dans les applications réelles.

![Blindage contre la lumière ambiante](../../../../_shared/media/images/LIGHTSHIELDING.png)

### *Symptômes typiques d'une lumière ambiante incontrôlée*

- **Reconnaissance instable** : le système fonctionne bien à certains moments et se dégrade à d'autres, par exemple lorsque la lumière du soleil pénètre dans la cellule.
- **Score de reconnaissance variable** : les pièces sont détectées avec des scores très différents d'un cycle à l'autre, même si elles sont physiquement identiques.
- **Faux positifs** : les pièces dont la fiabilité est faible sont reconnues avec des scores élevés et vice versa.

### *Meilleures pratiques d'installation*

- Blinder les côtés de la cellule exposés à un éclairage irrégulier par des panneaux opaques.
- Éviter les éclairages artificiels variables (lampes à variateur, fluorescents clignotants) au-dessus ou à proximité de la cellule.
- Préférer un éclairage à flux constant dans la zone entourant la cellule.
- Vérifier le blindage avant de calibrer et de créer le modèle.

```{warning}
**Protection contre les sources lumineuses externes**

Les conditions d'étalonnage doivent être les mêmes qu'en fonctionnement normal. Il est fortement recommandé de blinder la cellule robotisée contre les éléments suivants :
- Lumière directe ou indirecte du soleil
- Éclairage artificiel variable (par exemple, lampes avec variateur)
- Reflets des surfaces brillantes environnantes
- Éclairs ou lumières clignotantes dans la zone
```
---

## Références connexes

Pour plus d'informations sur l'installation mécanique :

- **Calcul de la distance optimale de la caméra** : [Calcul de la distance optimale](distanza_lavoro)
- **Spécifications techniques complètes** : [Spécifications FlexiVision One](specifiche_tecniche)
- **Prochaine étape - Branchements électriques** : [Câblage et connexions](cablaggio)
- **Étalonnage de la caméra** : [Étalonnage de la caméra](calibrazione)

