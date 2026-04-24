# **Vue d'Ensemble Application Mix**
Cette section présente le concept d'**Application Mix** dans FlexiVision One, en expliquant en quoi elle se distingue d'une application standard et comment la configurer correctement au niveau de la recette et des modèles.

---

## Qu'est-ce qu'une Application Mix?

Une **Application Mix** est une configuration applicative dans laquelle, au sein d'une même recette, coexistent des modèles relatifs à **des composants complètement différents les uns des autres**.

Dans une application Mix, le robot est capable de reconnaître et de prendre **plusieurs types de pièces différents** présents simultanément dans la zone de travail, sans devoir changer de recette ni interrompre le cycle. La vision identifie chaque pièce présente sur le FlexiBowl® et renvoie au robot les coordonnées de la pièce préhensible la plus appropriée, indépendamment de son type.
```{tip}
**Exemple typique:** des vis, écrous et rondelles peuvent se trouver simultanément sur le FlexiBowl®. Le robot prend n'importe quelle pièce reconnue, optimisant le throughput sans interruptions.
```

---

## Application Standard vs Application Mix

| Caractéristique | Application Standard | Application Mix |
|---|---|---|
| **Types de pièces** | Un seul type de pièce  | Plusieurs types de pièces complètement différents les uns des autres |
| **Modèles dans la recette** | Tous les modèles se réfèrent au même composant | Les modèles peuvent également se référer à des composants distincts |
| **Comportement du robot** | Prend toujours la même pièce même dans des positions différentes (en créant plusieurs modèles)| Prend n'importe quelle pièce reconnue, indépendamment du type |
| **Configuration logicielle** | Aucune différence par rapport au mode Mix | Aucune différence par rapport au mode Standard |
| **Sélection du mode** | Non requise: dépend des modèles insérés dans la recette | Non requise: dépend des modèles insérés dans la recette |
| **Commandes robot** | Famille `start_..` | Famille `mix_..` |

```{note}
Au niveau logiciel, il n'existe pas de choix explicite entre mode Standard et Mix: la distinction est déterminée exclusivement par le **contenu de la recette**. Si tous les modèles présents se réfèrent à la même pièce (ou à ses différentes faces), il s'agit d'une application Standard. Si les modèles se réfèrent à des pièces différentes, il s'agit automatiquement d'une application Mix.
```

---

## Comment créer une recette Mix?

Le processus de création d'une recette Mix est **identique** à celui d'une recette Standard. Il n'est nécessaire de sélectionner aucune option préliminaire. Il est donc possible de suivre la procédure de [Création Recettes et Modèles - Vue d'ensemble](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md)

La différence se manifeste **dans la phase de création des modèles**:

- Dans une application **Standard**, tous les modèles insérés dans la recette représentent le même composant (par exemple: face A, face B, face C de la même pièce).
- Dans une application **Mix**, les modèles insérés représentent **des composants complètement différents** (par exemple: Pièce A, Pièce B, Pièce C — trois composants distincts avec des géométries différentes).
```{important}
Chaque modèle au sein d'une recette Mix doit être entraîné séparément avec sa propre pièce physique de référence, en suivant la procédure standard décrite dans [Créer un Nouveau Modèle](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Les clearances et les coordonnées robot pick doivent être calibrées individuellement pour chaque composant.
```

---

## Prochaines étapes

Une fois le concept d'Application Mix compris et la recette configurée avec les modèles des différents composants, l'étape suivante concerne l'adaptation des **commandes robot** nécessaires pour fonctionner en mode Mix:

**→ [Commandes Application Mix](29_Comandi_Mix.md)**

