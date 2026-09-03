(nuovomodello)=
# **Créer un nouveau modèle**

Sur cette page, nous verrons comment créer un modèle de référence pour la reconnaissance des composants.


## Étape 1 : Préparation de l'installation physique
Si elle n'a pas déjà été faite, suivre ces étapes :
````{list-table}
* - **1**
  - Retirer la grille d'étalonnage et rétablir la disposition initiale :
    - Repositionner la surface
    - Repositionner la bride centrale
    - Fixer la bride centrale avec ses quatre vis
* - **2**
  - Placer un objet au centre de la zone d'observation
````
---

## Étape 2 : Accès au modèle

Une fois la préparation physique terminée, procéder à l'acquisition de l'image et à la création du modèle
````{list-table}
* - **3**
  - À partir de la page «&nbsp;Recipes&nbsp;», une fois la bonne recette sélectionnée, cliquer sur <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">
* - **4**
  - Sélectionner le FlexiBowl® avec lequel vous travaillez
    :::{dropdown} **Choix du FlexiBowl®**
    ![Choix FB](../../../../../_shared/media/images/scelta_FB.png)
    :::
* - **5**
  - Les emplacements disponibles pour les modèles seront affichés (jusqu'à 8 modèles par recette)
* - **6**
  - Cliquer sur **Modèle 1** pour accéder à la page «&nbsp;Train Model 1 Cam 1&nbsp;»
````

### *Aperçu de l'interface Train Model*

![Page Train Model](../../../../../_shared/media/images/pagina_trainmodel.png)
````{list-table}
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Fonction
* - **Enable Model**
  - Active cette fente de modèle pour la rendre utilisable
* - **Grab Train Image**
  - Prend une image du composant de référence pour l'entraînement
* - **Score Threshold**
  - Règle le niveau de détail du modèle (de 0 = détail maximum à 1 = détail minimum)
* - **Train**
  - Génère réellement le modèle en traitant l'image capturée
* - **Model Name**
  - Champ de texte pour attribuer un nom descriptif au modèle
````
````{tip}
**Gestion de modèles multiples**

Dans cette phase, seul le premier modèle est activé. Après l'achèvement, il sera possible de :
- Activer des emplacements supplémentaires (Modèle 2, Modèle 3, etc.) pour des pièces différentes dans la même recette
- Modifier les modèles existants
- Désactiver les modèles qui ne sont plus nécessaires

Pour l'instant, se concentrer sur l'achèvement du premier modèle.
````
---

## Étape 3 : Procédure de formation
````{video} ../../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
:width: 100%
:align: center 
````
````{list-table}
:widths: 5 95

* - **7**
  - Cliquer sur **Enable Model** pour activer ce modèle. Le modèle est maintenant actif et prêt à être configuré.

* - **8**
  - Cliquer sur **Grab Train Image** pour prendre une photo du composant de référence qui a été placé sur le FlexiBowl®
    
    :::{warning}
    Le composant de référence doit rester immobile à cet endroit pendant tout le processus de création de l'application
    :::

* - **9**
  - Déplacer l'**encadré ROI** pour encadrer complètement le composant

* - **10**
  - Déplacer l'**origine** (point de référence) au centre de la zone de l'encadré
    
    :::{tip}
    **Où placer l'origine ?**
    
    L'origine est automatiquement placée au centre du composant.  
    Si le point de préhension ne coïncide pas avec le centre géométrique, déplacer l'origine vers :
    - **Point de préhension** : Pour les pièces asymétriques, placer là où la pince saisit
    
    *L'origine définit le point (0,0) du système de coordonnées du modèle.*
    :::

* - **11**
  - Utiliser le **Score Threshold** pour ajuster le niveau de détail souhaité
    
    ::::{note}
    **Score Threshold**
     
      ![Comparaison Score threshold](../../../../../_shared/media/images/confrontomodello.png)
    
    **Valeur proche de 0** → Détecte PLUS de détails (modèle plus précis)
    
    **Valeur proche de 1** → Détecte MOINS de détails (modèle plus simple)
    ::::
    
    :::{tip}
    **Comment choisir le Score Threshold optimal ?**
    
    **Utiliser une valeur BASSE (0.1-0.3) lorsque :**
    - La pièce présente de nombreux détails distinctifs (gravures, logos, textures)
    - Les pièces sont toujours très similaires les unes aux autres (tolérances étroites)
    - Une précision maximale est souhaitée, même avec des orientations difficiles
    
    **Utiliser une valeur ÉLEVÉE (0.4-0.6) lorsque :**
    - La pièce a une forme distinctive mais simple
    - Un équilibre entre précision et tolérance est souhaité
    - Première configuration d'un modèle (point de départ)
    
    **Utiliser une valeur TRÈS ÉLEVÉE (0.7-0.9) lorsque :**
    - Il existe des variations significatives entre les pièces (tolérances larges)
    - La surface de la pièce est très réfléchissante ou variable
    :::

* - **12**
  - Cliquer sur **Train**
````
:::{tip}
En cas de doutes lors de la configuration, consulter le bouton **INFO** présent sur la page actuelle.
:::
---

## Étape 4 : Inspection visuelle

Après avoir généré le modèle, il est essentiel de vérifier sa qualité avant de continuer.
````{list-table}

* - **13**
  - **Zoomer** sur l'image pour inspecter les détails du modèle créé et vérifier que le modèle est correct
    
    :::{tip}
      **Caractéristiques d'un modèle valide**  
      ✓ Avoir suffisamment de lignes pour reconnaître le composant  
      ✓ Ne pas inclure la texture de la surface arrière  
      ✓ Éviter les reflets de lumière  
    :::

    ![Comparaison de modèle](../../../../../_shared/media/images/confrontomodello2.png)
````
````{attention}
Si le modèle n'est pas satisfaisant :
- Modifier le **Score Threshold**
- Cliquer à nouveau sur **Train**
- Recommencer jusqu'à l'obtention d'un modèle optimal
````
````{tip}
**Stratégie d'optimisation**

**Problème : Le modèle inclut la texture de la surface**  
→ Solution : Augmenter Score Threshold ou la valeur Cam Exposure (SETUP > Camera Setup > Cam Exposure)

**Problème : Le modèle comporte trop peu de lignes et n'est pas distinctif**  
→ Solution : Diminuer Score Threshold 

**Problème : Le modèle comprend des reflets**  
→ Solution : Augmenter Score Threshold ou bien régler l'exposition de la caméra

Effectuer des changements progressifs (par étapes de 0,1 à 0,2) et les tester à chaque fois.
````
---

## Étape 5 : Sauvegarde
````{list-table}
* - **14**
  - Nommer le modèle avec un nom descriptif  
    :::{tip}
    **Éviter les noms génériques**

    ❌ Noms à éviter :
    - `Test`, `Prova`, `Modello1`, `Nuovo_Modello`

    ✓ Noms recommandés :
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    Un nom clair facilite la gestion lorsque vous avez plusieurs modèles différents.
    :::
* - **15**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> → s'ouvre la page **Define Robot Pick Area**  
````
````{seealso}
Passer à la [Définition ROI](roitest) pour continuer la configuration.
````

