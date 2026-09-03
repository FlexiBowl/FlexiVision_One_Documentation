(robotpick)=
# **Étalonnage du Robot Pick**
Sur cette page, nous verrons comment relier les coordonnées de la vision à celles du robot pour permettre un prélèvement précis des composants.


**Qu'est-ce que le Robot Pick ?**  
La fonction **Robot Pick** calcule le décalage entre les coordonnées détectées par FlexiVision One et les coordonnées réelles du robot, ce qui permet au robot de prélever les composants dans la bonne position.
```{danger}
**Coordonnées fondamentales du robot !**

Cette étape nécessite **OBLIGATOIREMENT** les coordonnées X, Y, Rz enregistrées lors de la préparation physique du réglage (étape 1 de la section Clearances).

Sans ces coordonnées, l'étalonnage ne peut être effectué. En cas de perte ou d'oubli, il faudra recommencer toute la préparation physique avec le robot.
```
---

## Aperçu de l'interface Robot Pick

Après avoir cliqué sur « Next » à la page Clearance, la page **Robot Model Pick** s'ouvre.

![Page Robot Pick](../../../../../_shared/media/images/pagina_robotpick.png)

|Section | Paramètre | Fonction |
|-----------|-----------|----------|
| Enable | **Enable Robot Pick** | Active l'étalonnage du robot |
|Vision Result| **X cord** | Coordonnée X détectée par la vision |
|Vision Result| **Y cord** | Coordonnée Y détectée par la vision |
|Vision Result| **RZ cord** | Rotation Z détectée par la vision |
|Insert Robot Coordinate| **X cord** | Coordonnées X du robot (à saisir) |
|Insert Robot Coordinate| **Y cord** | Coordonnées Y du robot (à saisir) |
|Insert Robot Coordinate| **RZ cord** | Rotation Z du robot (à saisir) |


| Fonction | Description |
|----------|-------------|
| **Find Object** | Détecte le composant et affiche les coordonnées de vision |
| **Picking Offset** | Calcule le décalage pour un prélèvement correct |

---

## Étape 1 : Activation et détection du composant

:::{video} ../../../../../_shared/media/videos/Step1_robot.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **1**
  - Cliquer sur **Enable Robot Pick**
* - **2**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_FIND_OBJECT1.png" class="inline-icon">:
      - Le système détecte le composant de référence
      - Les coordonnées apparaissent dans la section **Vision Result**

      :::{note} Vision Result:
      Ce sont les coordonnées que FlexiVision One « voit » dans l'image. Elles ne sont pas encore connectées au système de coordonnées du robot.
      :::
```
:::{tip}
En cas de doutes lors de la configuration, veuillez consulter le bouton **INFO** sur la page en cours.
:::

## Étape 2 : Saisie des coordonnées du robot et calcul du décalage

:::{video} ../../../../../_shared/media/videos/Step2_robot.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **3**
  - Dans la case **Insert Robot Coordinates**, entrer les coordonnées enregistrées lors de la création du modèle :
      - **X cord** → coordonnée X notée à l'étape 1 de la [Création Clearances](setupclearances)
      - **Y cord** → coordonnée Y notée à l'étape 1 de la [Création Clearances](setupclearances)
      - **RZ cord** → rotation Z notée à l'étape 1 de la [Création Clearances](setupclearances)

      :::{danger}
      Utiliser les coordonnées enregistrées lors de la configuration du modèle. Sans ces coordonnées, l'étalonnage sera incorrect !  
      Les coordonnées doivent être saisies avec une **précision maximale** :
      - Copier les valeurs exactement telles qu'elles sont écrites (y compris les décimales)
      - **NE PAS approximer** (ex. : 450,23 ≠ 450,2 ≠ 450)
      - Vérifier de ne pas avoir inversé X et Y
      - Vérifier le signe (+ ou -) de chaque coordonnée

      Les **erreurs commises à ce stade entraînent des décalages complètement erronés du robot**, ce qui se traduit par des tentatives de prélèvement dans des positions erronées (même des dizaines de centimètres d'erreur). Le non-respect de ces deux points peut entraîner des collisions avec le robot et endommager le FlexiBowl®, les composants ou le robot lui-même.  
      :::
* - **4**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_GRIPPER_OFFSET.png" class="inline-icon">
      - Le système calcule automatiquement la transformation entre les coordonnées de la vision et les coordonnées du robot
      - Ce décalage sera appliqué à tous les relevés ultérieurs
```
---
```{admonition} **Comment fonctionne le Gripper Offset ?**
:class: info
Le système compare :
- **Coordonnées Vision** : là où FlexiVision One « voit » l'origine du composant
- **Coordonnées Robot** : là où le robot a effectivement saisi le composant

Il calcule la différence et l'enregistre en tant que **décalage**. Ce décalage sera appliqué à tous les composants détectés à l'avenir, afin de garantir que le robot ramasse toujours dans la bonne position.
```
:::{tip}
En cas de doutes lors de la configuration, veuillez consulter le bouton **INFO** sur la page en cours.
:::
---

## Étape 3 : Finalisation et sauvegarde
```{list-table}
* - **5**
  - En cliquant sur <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">, retour à la page des recettes <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
* - **6**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon"> pour sauvegarder l'ensemble de la configuration

      :::{admonition} Sauvegarde complète
      :class: success
      La sauvegarde comprend :
      - ✓ Modèle créé
      - ✓ Zone de travail (ROI)
      - ✓ Tolérances (Accept Threshold)
      - ✓ Clearances configurées
      - ✓ Calibrage du robot (Gripper Offset)
      :::
```

---

## Modèles multiples - Ajouter d'autres modèles

### *Étape 4 : Modèles supplémentaires (optionnel)*
```{list-table}
* - **7**
  - Pour créer des modèles supplémentaires dans la même recette :
      - Revenir à <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">
      - Sélectionner un nouveau modèle non encore configuré 
      - Répéter toute la procédure depuis la [Création de modèle](nuovomodello)

      :::{tip}
      Chaque modèle de la recette peut avoir différentes configurations (ROI, clearance, offset), ce qui permet de gérer des composants aux caractéristiques différentes dans la même application.
      :::
```

```{seealso}
Pour tout problème rencontré lors des étapes qui viennent d'être effectuées, consulter [Résolution des problèmes](troubleshooting)
```

---


