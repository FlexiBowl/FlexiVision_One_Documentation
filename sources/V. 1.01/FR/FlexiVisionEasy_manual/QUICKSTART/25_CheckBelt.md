# **Surveillance de la bande : Check Belt**

Cette section décrit la procédure permettant de vérifier l'état d'usure et de propreté de la bande du FlexiBowl® à l'aide de la fonction **Belt Check**.

**Qu'est-ce que le Belt Check ?**
Le **Belt Check** est un outil qui compare l'image actuelle de la bande avec une image de référence de la bande propre (**Clean Reference**), en calculant un indice de similarité. Cela permet de surveiller dans le temps le niveau de salissure ou d'usure de la bande, en identifiant à temps la nécessité d'un entretien.

:::{note}
**Prérequis**

Avant de continuer, s'assurer que :

- Le FlexiBowl® est connecté et configuré ([FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md))
- La bande est visible et correctement éclairée
:::

---

## Accès à la page Check Belt

| **1** | Depuis la page principale du logiciel, cliquer sur **Setup** |
| ----- | ------------------------------------------------------------ |
| **2** | Sur la page SETUP, repérer et cliquer sur l'icône **Check Belt** |
| **3** | La page de contrôle de la bande s'ouvre, avec un bloc pour chaque FlexiBowl® géré par le système |

---

## Aperçu de l'interface Check Belt

:::{image} ../../../_shared/media/images/beltcheck.png
:width: 100%
:align: center
:::

La page est divisée en un bloc pour chaque FlexiBowl® connecté, chacun composé de deux sections :

| Élément | Description |
| --- | --- |
| **Flb X Connected** | Indicateur d'état de connexion du FlexiBowl® correspondant (🟢 Vert = connecté, 🔴 Rouge = non connecté) |
| **Save Clean Reference** | Acquiert et enregistre l'image actuelle de la bande comme référence « propre », à utiliser comme terme de comparaison lors des contrôles suivants |
| **Delete Clean Reference** | Supprime l'image de référence enregistrée précédemment, afin de pouvoir en acquérir une nouvelle |
| **Aperçu caméra (avant/après)** | Les deux vignettes montrent respectivement l'image de référence enregistrée et l'image actuelle de la bande au moment du test |
| **Run Belt Check** | Lance la comparaison entre l'image de référence et l'image actuelle, en calculant l'état de la bande |
| **Belt Health Result** | Panneau affichant le résultat de la comparaison : barre graduée Clean → Dirty, indicateur coloré, état textuel et date du dernier contrôle |

---

## Procédure

### Étape 1 : Acquisition de la référence propre

:::{important}
Effectuer cette étape **uniquement lorsque la bande est réellement propre**. La précision de tous les contrôles futurs dépend de la qualité de cette image de référence.
:::

| **1** | S'assurer que la bande est propre et exempte de composants ou de résidus dans la zone cadrée |
| **2** | Cliquer sur **Save Clean Reference** |
| **3** | L'image est acquise et enregistrée comme référence ; elle apparaîtra dans la vignette de gauche |

:::{tip}
Si la bande est remplacée ou nettoyée en profondeur, répéter cette étape pour mettre à jour la référence.
:::

### Étape 2 : Exécution du Belt Check

| **4** | Cliquer sur **Run Belt Check** |
| **5** | Le système acquiert l'image actuelle de la bande (visible dans la vignette de droite) et la compare avec la référence enregistrée |
| **6** | Le résultat s'affiche dans le panneau **Belt Health Result** |

---

## Interprétation des résultats

Le panneau **Belt Health Result** affiche :

| Élément | Signification |
| --- | --- |
| **Barre graduée** | Représentation visuelle de la position de la valeur mesurée entre les deux extrêmes Clean (propre) et Dirty (sale) |
| **Indicateur coloré et texte** | État synthétique de la bande : |

| Couleur | Texte | Signification |
| --- | --- | --- |
| 🟢 Vert | **Good** | Bande en bon état |
| 🟡 Jaune | **Warning** | Bande à surveiller, nécessité possible de nettoyage prochainement |
| 🔴 Rouge | **Poor** | Bande sale ou usée, une intervention de nettoyage/entretien est recommandée |



:::{note}
*À confirmer* : les seuils de pourcentage exacts qui déterminent le passage de Good à Warning à Poor.
:::

---