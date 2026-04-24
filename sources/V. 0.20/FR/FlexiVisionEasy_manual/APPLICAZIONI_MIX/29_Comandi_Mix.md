# **Commandes Application Mix**
```{note}
**Prérequis**

Avant de poursuivre avec cette section, s'assurer d'avoir compris le fonctionnement de l'Application Mix et d'avoir correctement configuré la recette avec les modèles des différents composants. Consulter [Vue d'Ensemble Application Mix](28_Panoramica_Mix.md).
```

---

## Différences côté robot

Dans une Application Mix, les commandes TCP/IP envoyées par le robot au système de vision changent par rapport à celles d'une application Standard.

La principale différence concerne la **famille de commandes de localisation**: les commandes qui, dans l'application Standard, ont le préfixe `start_` sont remplacées par la famille équivalente avec le préfixe `mix_`.

Cette variation permet au système de vision d'activer la logique de reconnaissance **multi-composant**, en renvoyant au robot non seulement les coordonnées de la pièce localisée, mais aussi l'**identifiant du modèle** reconnu, afin que le programme robot puisse sélectionner la stratégie de prise correcte pour chaque type de pièce.
```{important}
La valeur de retour des commandes Mix inclut toujours l'identifiant du pattern reconnu (`Pattern_n`). Le programme robot doit être prévu pour gérer les différents types de réponse et adopter la logique de prise appropriée en fonction du modèle identifié.
```

---

## Commandes disponibles en mode Mix

### Gestion des recettes

| Commande | Action | Valeur de Retour |
|---|---|---|
| `set_Recipe=nome_ricetta` | Charge la recette Mix spécifiée | Aucune |
| `get_Recipe` | Renvoie le nom de la recette actuellement chargée | `nome_ricetta` |
```{note}
Les commandes de gestion recette sont identiques entre les modes Standard et Mix.
```

### Commandes de localisation Mix

Les commandes de localisation Mix permettent au robot de demander les coordonnées d'un modèle spécifique à l'intérieur de la recette. Chaque commande est dédiée à un seul modèle et gère de manière autonome le cycle de recherche, y compris le mouvement du FlexiBowl® et l'activation du hopper si nécessaire.

Le comportement de `mix_Locator_n` est le suivant:

1. Le système acquiert une image et recherche le Modèle `n`.
2. Si le modèle n'est pas trouvé à la première acquisition, le FlexiBowl® est actionné automatiquement et la recherche reprend.
3. Le cycle continue jusqu'à ce que le Modèle `n` soit localisé ou que la commande `stop_Locator` soit envoyée.
4. Pendant toute la phase de recherche, le hopper est activé automatiquement si nécessaire.
```{important}
Chaque commande `mix_Locator_n` recherche **exclusivement** le modèle correspondant au numéro `n`.   
Cela signifie que, pour demander les coordonnées d'un modèle différent, il est nécessaire d'utiliser la commande spécifique à ce modèle (p. ex. `mix_Locator_2` pour le Modèle 2, `mix_Locator_3` pour le Modèle 3, et ainsi de suite).
```

| Commande | Action | Valeur de Retour |
|---|---|---|
| `mix_Locator_1` | Démarre la recherche du **Modèle 1**. S'il n'est pas trouvé, actionne le FlexiBowl® et répète automatiquement la recherche jusqu'à la détection ou jusqu'à `stop_Locator`. Active le hopper si nécessaire. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Comme ci-dessus, pour le **Modèle 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Comme ci-dessus, pour le **Modèle 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | Comme ci-dessus, pour le **Modèle 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | Si aucune pièce n'a été prise, fait tourner le FlexiBowl® et redémarre la recherche multi-composant | `Pattern_n;x;y;r` |
| `test_Locator` | Démarre la localisation multi-composant sans activer le FlexiBowl® (acquisition d'image uniquement) | `Pattern_n;x;y;r` / Aucune |
| `stop_Locator` | Interrompt toute recherche en cours | Aucune |
| `state_Locator` | Renvoie l'état diagnostique du localisateur | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
Le nombre maximal de modèles gérables dans une seule recette Mix est **8**, correspondant aux commandes `mix_Locator_1` … `mix_Locator_8`. Le programme robot peut demander les modèles dans n'importe quel ordre et combinaison, selon la logique applicative.
```

### Commandes FlexiBowl®

| Commande | Action | Valeur de Retour |
|---|---|---|
| `start_Empty` | Démarre la séquence de vidage rapide du FlexiBowl® | `start_Empty ended` |

### Signaux hopper optionnels
```{note}
Si le hopper doit être activé, nous recevrons la chaîne: `"Hopper;signalnumber;time"`
```

---

## Format de la valeur de retour

En mode Mix, la valeur de retour des commandes de localisation a le format suivant:
```
Pattern_n;x;y;r
```

| Champ | Description |
|---|---|
| `Pattern_n` | Identifiant du modèle reconnu (p. ex. `Pattern_1`, `Pattern_2`, …). Correspond au numéro du modèle demandé avec la commande `mix_Locator_n`. |
| `x` | Coordonnée X de la pièce dans la zone de travail (en mm, dans le système de référence du robot) |
| `y` | Coordonnée Y de la pièce dans la zone de travail (en mm, dans le système de référence du robot) |
| `r` | Angle de rotation de la pièce (en degrés) |
```{tip}
Le champ `Pattern_n` est le paramètre clé pour les applications Mix: le programme robot doit l'utiliser pour sélectionner la routine de prise correcte (position d'approche, ouverture pince, force de prise, etc.) en fonction du type de pièce identifié.
```

---


Pour des informations sur le protocole de communication et les paramètres de connexion TCP/IP, consulter:

**→ [Protocole de Communication Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
