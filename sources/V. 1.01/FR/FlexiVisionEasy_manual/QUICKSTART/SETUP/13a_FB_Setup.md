(fbsetup)=
# **FlexiBowl® Setup**

Cette section décrit la procédure de connexion et de configuration du FlexiBowl® avec le système FlexiVision One. 

```{note}
**Prérequis**

Veiller à ce que :
- L'installation mécanique de tous les composants est terminée ([Installation mécanique](Installazione_Meccanica))
- Tous les câbles sont correctement connectés ([Câblage et connexions](cablaggio)) 
```

---

## Accès à la configuration de FlexiBowl®
```{list-table}
* - **1** 
  - Sur la page principale du logiciel, cliquer sur <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Sur la page SETUP, identifier et cliquer sur l'icône **FlexiBowl® Setup**
    ```{dropdown} Page Setup 
       ![Page Setup](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - L'écran de configuration des FlexiBowl® s'ouvre
```
![Page FlexiBowl® Setup](../../../../../_shared/media/images/pagina_FBsetup.png)
---

## Procédure de connexion

### *Étape 1 : Configuration de l'adresse réseau*

```{list-table}
* - **4**
  - Vérifier que l'adresse se trouve sur le même sous-réseau que le VisionController
  
* - **5**
  - Dans le champ **FlexiBowl® IP**, saisir l'adresse IP du FlexiBowl®
      - Format : `192.168.1.XXX` (ou selon la configuration de votre réseau)
```
:::{tip}
Pour plus de commodité et de constance, commencer par le premier FlexiBowl® disponible 
:::
:::{note}
Le FlexiBowl® est livré avec une adresse IP par défaut `192.168.1.10`
:::
:::{important}
Pour savoir comment modifier l'adresse IP de votre FlexiBowl®, veuillez consulter le manuel disponible dans la section [Télécharger](https://www.flexibowl.it/downloads).
:::

### *Étape 2 : Test de connexion*

```{list-table}
:widths: 5 95

* - **6**
  - Après avoir saisi l'IP, cliquer sur le bouton **Connection Test**

* - **7**
  - Le système effectue un test de communication (ping) vers le FlexiBowl®

* - **8**
  - Observer l'indicateur de **Status** :
    - 🟢 **Vert** : Connexion établie avec succès
    - 🔴 **Rouge :** Échec de la connexion (vérifier l'adresse IP et le câblage)
```

```{warning}
**Échec de la connexion**

Si l'indicateur reste rouge ou si un message d'erreur apparaît :

0. Vérifier d'avoir allumé le FlexiBowl®
1. Vérifier que l'adresse IP saisie est correcte
2. Vérifier physiquement le câble Ethernet (il doit être complètement inséré)
3. Si c'est le cas, vérifier que le commutateur/routeur réseau est allumé
4. S'assurer que FlexiBowl® et VisionController se trouvent sur le même sous-réseau
5. Essayer d'envoyer un ping au FlexiBowl® à partir d'un terminal Windows :
   - Ouvrir Prompt des commandes
   - Taper : `ping 192.168.1.XXX` (remplacer par l'IP réelle)
   - Si le ping échoue, il s'agit d'un problème de réseau

Si le problème persiste, consulter [Troubleshooting](troubleshooting).
```

---

## Configuration des paramètres du FlexiBowl®

Une fois la connexion établie, passer à la configuration des paramètres opérationnels.

### *Étape 3 : Accès à la configuration*

```{list-table}
* - **9** 
  - Cliquer sur le bouton <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **10**
  - Une fenêtre s'ouvre avec les paramètres configurables du FlexiBowl®
```


### *Étape 4 : Synchronisation des paramètres*

```{list-table}

* - **12**
  - Cliquer sur **Synchronize Parameters**
* - **13**
  - Revenir à la page principale SETUP pour procéder à la configuration suivante 
```
:::{important}
I parametri possono essere regolati tramite slider oppure inseriti manualmente da tastiera nel relativo campo numerico.
:::

```{warning}
**Ne pas ignorer la synchronisation**

Il est indispensable de cliquer sur **Synchronize Parameters** après chaque modification. Sans cette étape :
- Les modifications ne sont pas appliquées au FlexiBowl® 
- Le système peut se comporter de manière incohérente
- Les configurations ne sont pas sauvegardées 
```
---
(configfb)=
# **Assistant de configuration : FlexiBowl® Wizard**


L'interface **FlexiBowl® Wizard** est un outil interactif conçu pour guider l'utilisateur dans la configuration des paramètres d'alimentation en fonction de la famille de produits spécifique à gérer.

## Étape 1 : Accès à l'assistant

Pour lancer la procédure :
```{list-table}
:widths: 5 95

* - **1**
  - Aller à <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon"> dans le logiciel FlexiVision One

* - **2**
  - Cliquer sur le bouton **FlexiBowl® Setup**, cela ouvrira une page avec tous les FlexiBowl® qui peuvent être gérés avec FlexiVision One

    :::{dropdown} Page FlexiBowl® Setup  
    ![Page FlexiBowl® Setup](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **3**
  - Cliquer sur le bouton <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl">, une page s'ouvrira avec tous les mouvements disponibles pour le FlexiBowl sélectionné

    :::{dropdown} Page de configuration du FlexiBowl®  
    ![Page FlexiBowl® Config](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **4**
  - Cliquer sur le bouton **FlexiBowl® X Wizard**, une page de bienvenue sur l'assistant s'ouvre.

* - **5**
  - Cliquer sur <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">
    
    :::{note}
    Cliquer <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> sur chaque page de l'assistant pour avancer dans la configuration guidée
    :::
```

## Étape 2 : Sélection de modèle et rotation

Au cours de cette phase, les caractéristiques matérielles du système sont définies :
```{list-table}
* - **6**
  - Sélectionner la taille de l'appareil (par exemple 200, 350, 500, etc.).
* - **7**
  - Définir le sens de rotation du disque (**Clockwise** ou **CounterClockwise**).
```
## Étape 3 : Caractérisation du composant

Le système a besoin d'informations sur la morphologie des pièces pour optimiser la séparation.
````{list-table}
* - **8**
  - Sélectionner la taille du composant:**

    **Pour les modèles FlexiBowl 200, 350, 500, 650 :**

    :::{card}
    <= 150mm
    :::

    :::{card}
    &gt; 150mm
    :::

    **Pour les modèles FlexiBowl 800 et 1200 :**

    :::{card}
    <= 250mm
    :::

    :::{card}
    &gt; 250mm
    :::

* - **9**
  - Sélectionner la géométrie qui décrit le mieux le composant :
      * **FLAT** : Composants plats.
      * **CYLINDRICAL** : Composants cylindriques.
      * **COMPLEX** : Géométries articulées ou irrégulières

      ![Flat Cylindrical or Complex](../../../../../_shared/media/images/flatorcomplex.png)

      *Exemples de géométries : Flat, Cylindrical et Complex.*

* - **10**
  - Définir comment les composants interagissent entre eux sur la surface :
      * **Overlapping** : Les pièces ont tendance à se chevaucher.
      * **Not Overlapping** : Les pièces ne se chevauchent pas.
      * **Tangling / Stacking** : Les pièces ont tendance à s'accrocher ou à s'empiler.
      * **Not Tangling / Not Stacking** : Les pièces restent séparées et ne s'emboîtent pas.

      ![Overlapping](../../../../../_shared/media/videos/overlapping.gif)

      *Not Overlapping : les pièces ne se chevauchent pas sur la surface.*

      ::::{grid} 2
      :::{grid-item}
      ![Stacking](../../../../../_shared/media/videos/stacking.gif)

      *Stacking : les pièces s'empilent.*
      :::
      :::{grid-item}
      ![Tangling](../../../../../_shared/media/videos/tangling.gif)

      *Tangling : les pièces s'enchevêtrent les unes dans les autres.*
      :::
      ::::
````
## Étape 4 : Test des accessoires
```{list-table}
* - **11**
  - Sélectionner dans le menu déroulant si le FlexiBowl® est équipé du module **Air-blow**.
* - **12**
  - Cliquer sur **TEST Air-blow** pour vérifier le fonctionnement.
* - **13**
  - Sélectionner **USE** pour l'activer dans l'application en cours, sinon cliquer sur **DON'T USE**.
* - **14**
  - Cliquer sur **TEST FLIP** pour vérifier l'activation réelle du percuteur.
      Le « Flip » est l'unité qui génère l'impulsion mécanique pour retourner les pièces ; il est essentiel pour séparer, démêler ou retourner les pièces pendant le cycle d'alimentation.
 
      :::{important}
      Si l'impulsion n'est pas perceptible, vérifier que l'air comprimé est connecté et agir sur le régulateur de pression mécanique situé sur le panneau de commande.
      :::
* - **15**
  - À la fin de l'assistant, en cliquant sur **FINISH**, le système calculera automatiquement les paramètres : 
    - Paramètres de mouvement (vitesse, accélération, angle)
    - Paramètres de secouement (shake)
    - Temporisations des accessoires (flip, blow)
* - **16**
  - Il sera ensuite possible de les affiner dans le tableau de bord récapitulatif.
```
```{list-table} Aperçu des paramètres
   :widths: 20 30 50
   :header-rows: 1

   * - Groupe
     - Paramètre
     - Description
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Paramètres du mouvement principal du disque.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Gestion des temps d'activation des accessoires.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Paramètres de la vibration du secouement (séparation).
```

## Étape 5 : Validation de la séquence

La fonction **Test Sequence** permet de vérifier que le cycle répond aux critères d'efficacité suivants :
```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronisation**
  - L'impulsion du Flip doit se terminer exactement au même moment que le mouvement (*Move*). Régler les valeurs de *Flip Count* et *Delay* pour les aligner.

* - **Stabilité de l'image**
  - Les composants doivent être immobiles lorsque la caméra se déclenche.
    - Si les pièces se déplacent, diminuer la vitesse/accélération ou saisir une pause (par exemple `pause 200ms`).

* - **Positionnement des pièces lors de la séquence**
  - Lors du mouvement, les pièces doivent être acheminées vers le centre du rayon du FlexiBowl® afin de maximiser l'efficacité du Flip. À la fin de la séquence, les pièces doivent être disposées approximativement au centre de la surface de vision.
```

:::{warning}
Cliquer toujours sur **Synchronize Parameters** après chaque modification manuelle pour activer les modifications dans le contrôleur.
:::
:::{important}
Nel caso in cui i parametri venissero modificati ma non sincronizzati, apparirà un messaggio di avviso. 
:::

## Aperçu des paramètres du FlexiBowl®
```{list-table}
:header-rows: 1
:widths: 5 25 70

* - ID
  - Élément
  - Description
* - 1
  - MOVE – Accélération
  - Valeur d'accélération utilisée à chaque commande MOVE
* - 2
  - MOVE – Décélération
  - Valeur de décélération utilisée à chaque commande MOVE
* - 3
  - MOVE – Vitesse
  - Valeur de vitesse (tr/min) utilisée à chaque commande MOVE
* - 4
  - MOVE – Angle
  - Angle avec lequel FlexiBowl® se déplace à chaque commande MOVE
* - 5
  - SHAKE – Accélération
  - Valeur d'accélération utilisée à chaque commande SHAKE
* - 6
  - SHAKE – Décélération
  - Valeur de décélération utilisée à chaque commande SHAKE
* - 7
  - MOVE – Vitesse
  - Valeur de vitesse (tr/min) utilisée à chaque commande SHAKE
* - 8
  - MOVE – Angle CW
  - Angle horaire avec lequel FlexiBowl® se déplace à chaque commande SHAKE
* - 9
  - MOVE – Angle CCW
  - Angle antihoraire avec lequel FlexiBowl® se déplace à chaque commande SHAKE
* - 10
  - OPTION – Comptage Flip
  - Nombre d'activations Flip qui seront exécutées
* - 11
  - OPTION – Retard Flip
  - Temps (en millisecondes) entre une activation et une désactivation du flip
* - 12
  - OPTION – Temps Blow
  - Temps (en millisecondes) d'activation du blow
* - 13
  - OPTION – Lumière allumée
  - Appuyer pour activer/désactiver le rétro-éclairage
```

```{tip}
**Test de production**

Avant de l'utiliser en production :
1. Effectuer 50 à 100 cycles d'essai pour vérifier la cohérence
2. Surveiller le taux de remplissage du disque (il doit être constant)
3. Vérifier qu'il n'y ait pas d'accumulations anormales ou de zones vides persistantes
4. Augmenter progressivement vers la vitesse de production

La configuration optimale peut nécessiter 2 à 3 séances de mise au point avec la pièce réelle en quantités significatives.
```

## Étapes suivantes

Après le FlexiBowl® Setup, passer à :

- [Hopper Setup](13b_Hopper_Setup.md)
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Sauvegarder la recette](ricettabase)




