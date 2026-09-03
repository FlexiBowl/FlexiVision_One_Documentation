(protocol_setup)=
# **Protocol Setup**

La page **Protocol Setup** permet de configurer les paramètres régissant le flux de communication et l'échange de données entre le système de vision FlexiVision One et le robot. Ces paramètres déterminent le nombre d'objets envoyés, la manière dont ils sont triés et la façon dont le système gère les statistiques et les états opérationnels.

---

## Accès à Protocol Setup

1. À partir du menu principal, accéder à la section dédiée au protocole de communication
2. Sélectionner **Protocol Setup**
3. L'interface s'ouvre avec les paramètres configurables


---

## Paramètres configurables

![Page Protocol Setup](../../../../../_shared/media/images/pagina_protocolsetup.png)

```{list-table}
:header-rows: 1

* - **Paramètre**
  - **Description et fonction**
* - [**Max Object Count Return**](maxobject)
  - Indique le nombre **maximum** d'objets (c'est-à-dire leur triade de coordonnées) que le système de vision peut renvoyer au robot en une seule fois. Si le système de vision détecte plus d'objets que cette limite, un maximum de ce nombre est envoyé, sélectionné en fonction des critères de tri configurés (Sorting Mode).
* - [**Min Object Count Return**](minobject)
  - Indique le nombre **minimum** d'objets qui doivent être renvoyés lors d'une exécution pour que le résultat soit considéré comme valide. Si le nombre est inférieur à ce seuil, l'exécution est considérée comme non valide.
* - [**Sorting Mode Results**](sortingmode)
  - Définit le **critère de** tri selon lequel la liste des objets renvoyés par la vision est triée. Ce paramètre détermine la priorité du prélèvement et les objets inclus dans le Max Object Count Return.
    
    *Option typique :* pour les scores décroissants.
* - [**Pickable parts by the robot detected by vision in each cycle**](pickableparts)
  - Indique le nombre de prélèvements effectués par le robot par cycle de vision. Par exemple, une prise double correspond à la valeur 2. Ne représente pas le nombre d'objets détectés par la vision, mais le nombre de prises du robot par cycle. Paramètre utilisé pour le calcul des statistiques.
* - **Maximum processing time per part with the robot (in seconds)**
  - Définit le temps maximum après lequel le système considère que le traitement/l'envoi de coordonnées pour une exécution est terminé et passe généralement de l'état RUN à l'état IDLE. Paramètre utilisé pour les **statistiques et la gestion des flux de travail**.

    :::{attention}
    **Il ne s'agit pas d'une erreur de délai d'attente du robot** mais une référence temporelle pour le calcul du cycle et les indicateurs de productivité.
    :::
```

---

## Configuration détaillée des paramètres

(maxobject)=
### *Max Object Count Return*

```{list-table}
 :class: align-top

* - **Fonction** :
  - Limite le nombre maximum de coordonnées envoyées au robot par cycle de vision.

* - **Valeurs typiques :**
  - 
    - **1** : Configuration la plus courante pour les robots à prélèvement unique
    - **2** : Configuration pour les robots à double prélèvement
    - **3** : Configuration pour les robots à triple prélèvement
    - **4-8 objets** : Pour les systèmes à suivi circulaire
    - **>8 objets** : Rarement nécessaire, peut saturer la communication

    :::{tip}
        **Comment choisir la valeur :**
        1. Tenir compte de la vitesse du robot (temps de prélèvement et de placement par pièce).
        2. Tenir compte du temps de cycle de vision + FlexiBowl®
        3. Formule approximative&nbsp;: `Max Count = (Temps de cycle vision+FB) / (Temps de prélèvement robot)`

        **Exemple pratique :**
        - Cycle Vision+FlexiBowl® : 3 secondes
        - Temps de prélèvement du robot : 2 secondes/pièce
        - Max Count optimal : 3/2 = 1,5 → Arrondir à 2 objets
    :::
```

(minobject)=
### *Min Object Count Return*

```{list-table}
* - **Fonction :**
  - Limite le nombre minimum de coordonnées envoyées au robot par cycle de vision.

* - **Valeurs typiques :**
  - 
    - **1**: Configuration la plus courante - même une seule pièce reconnue est acceptable
    - **>2** : Uniquement pour les applications spéciales avec multi-pick obligatoire

* - **Comportement du système :**
  - 
    - **Objets détectés ≥ Min Count** : coordonnées envoyées au robot
    - **Objets détectés < Min Count** : coordonnées non envoyées et exécution de la séquence du FlexiBowl®


* - **Impact sur la productivité**
  - 
    **Min Count = 1** (le plus permissif) :
    - ✓ Flexibilité maximale, le robot travaille même s'il n'y a qu'une seule pièce
    - ✗ Cycles à faible rendement possible (1 pièce toutes les N secondes)

    **Min Count = 3** (le plus restrictif) :
    - ✓ Garantit une efficacité minimale par cycle
    - ✗ Peut provoquer une attente si le remplissage est variable
```

(sortingmode)=
### *Sorting Mode Results*


```{list-table}
:header-rows: 1
:widths: 30 70

* - Mode Sorting
  - Description et cas d'utilisation
* - **By score (Descending)**
  - Tri par score du plus élevé au plus bas. Les objets qui correspondent le mieux au modèle sont envoyés en premier.
    **Plus fréquent et recommandé** : Il garantit toujours le prélèvement des pièces avec une reconnaissance plus fiable.
* - **By score (Ascending)**
  - Trie par score du plus faible au plus élevé. Les objets qui correspondent le moins bien au modèle sont envoyés en premier.
    **NON RECOMMANDÉ** : NE garantit PAS toujours la sélection des pièces avec une reconnaissance plus fiable.
* - **By X Coordinate (Ascending)**
  - Trier par coordonnée X croissante. Utile si le robot a une préférence de prélèvement séquentiel le long d'un axe.
* - **By X Coordinate (Descending)**
  - Trier par coordonnée X décroissante.
* - **By Y Coordinate (Ascending)**
  - Trier par coordonnée Y croissante.
* - **By Y Coordinate (Descending)**
  - Trier par coordonnée Y décroissante.
* - **X Alternating**
  - Le système alterne la sélection du composant entre le premier et le dernier détecté sur l'axe X. Les deux composants sélectionnés étant éloignés l'un de l'autre, le risque que le prélèvement précédent ait déplacé des pièces à proximité est réduit, ce qui garantit un prélèvement plus sûr et plus fiable.
* - **Y Alternating**
  - Le système alterne la sélection du composant entre le premier et le dernier détecté sur l'axe Y. Même principe que le X Alternating : la distance entre les deux points de prélèvement minimise l'interférence causée par le mouvement accidentel des pièces adjacentes.
```

```{tip}
**Choix optimal du Sorting Mode**

**Recommandé dans la plupart des cas : By Score (Descending)**

**Avantages** :
  - Fiabilité maximale : le robot prélève toujours les pièces les mieux reconnues
  - Réduction du risque de prélèvement incorrect
  - Indépendant de la position physique
```

```{note}
Le mode de tri interagit avec Max Object Count. Les 15 premiers objets (selon les critères) sont envoyés.
```
(pickableparts)=
### *Pickable parts by the robot*

**Fonction**

Paramètre statistique indiquant le nombre de pièces **effectivement prélevées** par le robot par cycle de vision.

**Valeurs typiques**

  - **1** : robot avec pince simple, saisit 1 pièce à la fois
  - **2** : robot avec pince double ou ventouse double
  - **>2** : robot avec pince ou ventouse multi-pick

```{important}
Cette valeur représente les **prises physiques**, et non pas les objets détectés par la vision.
```

**Exemple de clarification**

Scénario : double pince, la vision détecte 5 objets.

  - Si je veux envoyer au robot un maximum de 2 objets, je règle `Max Object Count = 2`.
  - Si je veux que le robot prenne au moins 2 objets à la fois, je règle `Min Object Count = 2`.
  - Dans ce cas, je règle `Pickable Parts by the robot = 2`.
  - Si, en revanche, je souhaite également autoriser le prélèvement d'un seul objet, je règle `Max Object Count = 2`, `Min Object Count = 1` et `Pickable Parts by the robot = 2`.

**Impact sur les statistiques Dashboard**

Ce paramètre est crucial pour le calcul précis des **Parts Per Minute (PPM).**

  - Formule : `PPM = (Pickable parts x 60) / Temps de cycle total en secondes`
  - En cas de réglage incorrect, le PPM affiché ne correspond pas à la réalité



---

## Sauvegarde de configuration

```{warning}
**Sauvegarde obligatoire**

Après avoir configuré les paramètres de Protocol Setup :

1. Vérifier que toutes les valeurs sont réglées correctement
2. Cliquer sur Recipes > Save Recipe
3. Les paramètres sont sauvegardés dans la configuration du système
```

---

## Étapes suivantes

Une fois le Protocol Setup terminé, le système est entièrement configuré pour fonctionner :

- [Sauvegarder la recette](ricettabase)





