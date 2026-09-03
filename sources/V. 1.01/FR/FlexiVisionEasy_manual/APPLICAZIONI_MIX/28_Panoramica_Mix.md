# **Vue d'ensemble de l'Application Mix**
Cette section présente le concept d'**Application Mix** dans FlexiVision One, en expliquant en quoi elle diffère d'une application standard et comment la configurer correctement au niveau de la recette et des modèles.

---

## Qu'est-ce qu'une Application Mix ?

Une **application Mix** est une configuration d'application dans laquelle des modèles de **composants complètement différents** coexistent dans la même recette.

Dans une application Mix, le robot est capable de reconnaître et de prélever simultanément **plusieurs types de pièces différentes** dans la zone de travail, sans avoir à changer de recette ou à interrompre le cycle. La vision identifie chaque pièce sur le FlexiBowl® et renvoie au robot les coordonnées de la pièce à saisir la plus appropriée, quel que soit son type.

![Application Mix](../../../../_shared/media/videos/video_applicazionemix.gif)  
*Exemple d'application Mix*

```{tip}
**Exemple typique&nbsp;:** il se peut qu'il y ait simultanément des vis, des écrous et des rondelles sur le FlexiBowl®. Le robot ramasse toute pièce reconnue, optimisant ainsi le débit sans interruption.
```

---

## Application standard comparée à une application Mix

| Caractéristique | Application standard | Application Mix |
|---|---|---|
| **Types de pièces** | Un seul type de pièce  | Plusieurs types de pièces complètement différents |
| **Modèles dans la recette** | Tous les modèles se réfèrent au même composant | Les modèles peuvent également faire référence à des composants distincts |
| **Comportement du robot** | Ramasse toujours la même pièce, même dans des positions différentes (en créant plusieurs modèles)| Ramasse toute pièce reconnue, quel qu'en soit le type |
| **Configuration du logiciel** | Pas de différence avec le mode Mix | Pas de différence avec le mode standard |
| **Sélection du mode** | Pas nécessaire : dépend des modèles inclus dans la recette | Pas nécessaire : dépend des modèles inclus dans la recette |
| **Commandes du robot** | Famille `start_..` | Famille `mix_..` |

```{note}
Au niveau logiciel, il n'y a pas de choix explicite entre le mode Standard et le mode Mix&nbsp;: la distinction est déterminée exclusivement par le **contenu de la recette**. Si tous les modèles présents se réfèrent à la même pièce (ou à ses différentes faces), il s'agit d'une application standard. Si les modèles font référence à des pièces différentes, il s'agit automatiquement d'une application Mix.
```

---

## Comment créer une recette Mix ?

Le processus de création d'une recette mixte est **identique** à celui d'une recette standard. Aucune option préalable ne doit être sélectionnée. Il est donc possible de suivre la procédure de [Création de recettes et de modèles - Vue d'ensemble](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md)

La différence se manifeste **au stade de la création des modèles&nbsp;**:

- Dans une application **standard**, tous les modèles saisis dans la recette représentent le même composant (par exemple, face A, face B, face C de la même pièce).
- Dans une application **Mix**, les modèles saisis représentent des **composants complètement différents** (par ex. : Pièce A, Pièce B, Pièce C — trois composants distincts avec des géométries différentes).
```{important}
Chaque modèle d'une recette de mélange doit être formé séparément avec sa propre pièce de référence physique, en suivant la procédure standard décrite dans la section [Création d'un nouveau modèle](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Les clearances et les coordonnées de prélèvement du robot doivent être calibrés individuellement pour chaque composant.
```

---

## Étapes suivantes

Une fois que le concept d'application Mix a été compris et que la recette a été configurée avec les modèles des différents composants, l'étape suivante consiste à adapter les **commandes du robot** nécessaires pour fonctionner en mode Mix :

**→ [Commandes de l'application Mix](29_Comandi_Mix.md)**

