(hoppersetup)=
# **Hopper Setup**

Cette section décrit la procédure de configuration de la trémie. La trémie est le composant qui alimente automatiquement le FlexiBowl® en pièces lorsque le niveau tombe en dessous d'un seuil minimum.

:::{important}  **Logique de fonctionnement**  

FlexiVision gère la logique d'activation de la trémie. Il enverra en effet la chaîne `Hopper;signalnumber;time` lorsqu'il jugera l'activation nécessaire. 
:::
```{note}
**Conditions préalables**

Avant de poursuivre, s'assurer que :
- La trémie a été installée mécaniquement
- Les branchements électriques sont terminés (signaux de contrôle et d'alimentation électrique)
- Le FlexiBowl® est déjà connecté
```
---
## Préparation de l'installation physique

````{list-table}
* - **0**
  - Retirer la grille d'étalonnage et rétablir la disposition initiale :
    - Repositionner la surface
    - Repositionner la bride centrale
    - Fixer la bride centrale avec ses quatre vis
````
---
## Accès à la configuration Hopper

```{list-table}
* - **1** 
  - Depuis la page principale du logiciel, cliquer sur <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Sur la page SETUP, identifier et cliquer sur l'icône **Hopper Setup**
    ```{dropdown} Page Setup 
       ![Page Setup](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3** 
  - La page de configuration du Hopper s'ouvre
```

---

## Aperçu de l'interface Hopper Setup

La page Hopper Setup comporte plusieurs sections permettant de configurer les paramètres de fonctionnement des différentes trémies :

![Page Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Enable Hopper**
  - Interrupteur pour activer/désactiver l'utilisation du Hopper dans le système
* - **Steps**
  - Nombre de séquences nécessaires pour que la section du disque qui se trouve actuellement dans la zone de visualisation parvienne sous la zone de déchargement de la trémie
* - **Time**
  - Durée de l'activation de la trémie en millisecondes
* - **Signal**
  - Numéro du signal numérique utilisé pour contrôler la trémie
* - **Config Hopper**
  - Bouton pour configurer la trémie (à utiliser ultérieurement)
```


---
(confighopper)=
# **Configuration de la trémie (Hopper)**

La configuration de la trémie permet le réapprovisionnement automatique des composants sur le disque FlexiBowl®. Le système utilise la vision pour déterminer si le niveau de remplissage est insuffisant et activer la trémie.

## Étape 1 : Accès à la configuration
```{list-table}
* - **1**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">.   
    La section **Hopper Setup** permet de visualiser et gérer les unités de charge connectées.
    
    :::{dropdown} Page Hopper Setup 
    ![Page Hooper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
    :::
* - **2**
  - Dans le champ **Signal**, entrer le numéro du signal numérique (DO - Digital Output) utilisé pour contrôler la trémie
    :::{warning}
      Il est essentiel d'entrer le bon numéro de signal :
      - Un numéro incorrect activera le mauvais signal (potentiellement dangereux)
      - Se reporter au schéma électrique réalisé lors de l'installation
      - En cas de doute, contacter la personne qui a réalisé le câblage
    :::
* - **3**
  - Cocher la case **Enable Hopper X** pour activer la trémie correspondante.
      :::{important}
      N'activer la trémie que si l'appareil est correctement installé
      :::
* - **4**
  - Cliquer sur le bouton **Config Hopper X** pour accéder à la configuration spécifique 
```
## Étape 2 : Définition de la zone de contrôle

:::{video} ../../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
    :width: 100%
    :align: center
:::

À ce stade, la partie du disque que la caméra doit surveiller pour le déchargement est définie.
```{list-table}
* - **5**
  - Modifier le cadre bleu de l'écran pour encadrer la zone où les composants seront détectés.
```
:::{tip}
En cas de doutes lors de la configuration, veuillez consulter le bouton **INFOS** sur la page actuelle.
:::

## Étape 3 : Définition des valeurs seuils

:::{video} ../../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
:width: 100%
:align: center
:::
```{list-table}
* - **6**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> pour accéder à la page **Define Value Hopper Cam**, où vous indiquez au système de faire la distinction entre un disque vide et un disque plein.
    :::{dropdown} Page Define Value Hopper Cam 
    ![Page Define Value Hopper Cam](../../../../../_shared/media/images/pagina_valuehopper.png)
    :::
* - **7**
  - Retirer tous les composants de la zone de visualisation et cliquer sur le premier bouton **CAPTURE**.
* - **8**
  - Placer le nombre minimum de composants à conserver dans la zone de visualisation. Si le nombre est inférieur à ce seuil, la trémie est activée.
* - **9**
  - Cliquer sur le deuxième bouton **CAPTURE**.
* - **10**
  - En cliquant sur <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> dans l'Expression Builder (générateur d'expression), le système calcule automatiquement les valeurs de **Mean** (moyenne) et **Standard Deviation**.
* - **11**
  - Enlever quelques pièces et cliquer sur <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">. 
* - **12**
  - Observer l'indicateur de résultat :
    - **Vert** 🟢: Niveau insuffisant, la trémie est activée (déchargement nécessaire)
    - **Rouge** 🔴: Niveau suffisant, la trémie NE S'ACTIVE PAS (OK)

      :::{warning}
      **Étalonnage insuffisant**

      Si le système ne détecte pas le niveau correctement :

      **Problème : Toujours vert (active toujours la trémie)**  
      → Seuil trop bas ou interférences dans la zone  
      → Solution : Augmenter le nombre de pièces lors de la deuxième acquisition, vérifier la propreté de la zone  

      **Problème : Toujours rouge (n'active jamais la trémie)**  
      → Seuil trop élevé ou zone de surveillance non représentative  
      → Solution : Réduire le nombre de pièces lors de la deuxième acquisition CAPTURE, répéter AUTO  

      **Problème : Comportement incorrect (alternance aléatoire vert/rouge)**  
      → Éclairage instable ou surface trop petite  
      → Solution : Vérifier la stabilité du rétroéclairage, agrandir la zone de surveillance, répéter l'étalonnage  
      :::
```
```{note}
**Hopper Fill Threshold**

Le paramètre **Hopper Fill Threshold** définit le seuil en pourcentage de remplissage en dessous duquel la trémie est automatiquement activée.

La valeur de 100 % correspond à la quantité de pièces acquises lors de la deuxième CAPTURE (surface complète). Par conséquent, un seuil de 50 % correspond à la moitié de cette quantité.

Le système fixe automatiquement la valeur initiale à **70 %**, ce qui constitue un bon équilibre pour la plupart des applications.

**Modification en cours**

Il est possible d'ajuster le seuil sans répéter la procédure d'acquisition :

- Pour décharger **moins de pièces** → réduire le pourcentage (par exemple 50 %) et cliquer sur **AUTO**
- Pour décharger **plus de pièces** → augmenter le pourcentage (par exemple 85 %) et cliquer sur **AUTO**

```

:::{tip}
En cas de doutes lors de la configuration, veuillez consulter le bouton **INFOS** sur la page actuelle.
:::

## Étape 4 : Paramètres opérationnels

Revenir à l'écran principal de Hopper Setup pour définir le comportement mécanique.
![Page Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
```{list-table} Paramètres de fonctionnement
:widths: 20 80
:header-rows: 1

* - **Paramètre**
  - **Description et procédure**
* - **Steps**
  - Nombre d'avancements du FlexiBowl® (séquences) nécessaires pour amener les pièces de la zone de visualisation à la zone de déchargement de la trémie.
* - **Time**
  - Millisecondes d'activation de la trémie.   Valeur recommandée : **100 – 1000 ms** (moyenne : **500 ms**). Ajuster de ±50 ms selon le débit désiré.
```
```{tip}
   Le temps d'activation dépend non seulement de la valeur réglée, mais aussi du volume des composants présents dans la cuve de la trémie. Il est essentiel de maintenir une charge constante pour obtenir un débit régulier.
```
```{tip}
La valeur Time est étroitement liée au volume de chargement de la trémie : 
- Avec une trémie pleine, il y aura plus de pièces dans la zone de déchargement 
- Avec une trémie à moitié pleine, il y aura moins de pièces dans la zone de déchargement 

```
:::{important}
En général, il est important de ne jamais dépasser la charge maximale de la trémie utilisée. 
:::

### *Calculer le paramètre Steps*

![Première page Steps](../../../../../_shared/media/images/Steps1.png)
![Deuxième page Steps](../../../../../_shared/media/images/Steps2.png)
![Troisième page Steps](../../../../../_shared/media/images/Steps3.png)
![Quatrième page Steps](../../../../../_shared/media/images/Steps4.png)

## Sauvegarde de la configuration
```{warning}
**Sauvegarde obligatoire de recette**

À la fin de la configuration de la trémie :

  :::{list-table}
    * - 1. 
      - Vérifier que tous les paramètres sont correctement configurés :
        - Zone de surveillance positionnée
        - Seuils calibrés (TEST fonctionnel)
        - Steps et Time réglés
    * - 2. 
      - Revenir à la page principale <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon icon-small">
    * - 3. 
      - Cliquer sur <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon icon-small">
    * - 4. 
      - Confirmer la sauvegarde
  :::
**IMPORTANT** : Toute modification apportée n'est enregistrée **QUE** si la recette est correctement sauvegardée avant de quitter ou de changer de page.

Sans sauvegarde, toutes les configurations de Hopper seront perdues à la fermeture de FlexiVision One !
```

---


## Étapes suivantes

Une fois que la configuration de la trémie est terminée (ou ignorée si elle n'est pas présente), passer à :

- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Sauvegarder la recette](ricettabase)



