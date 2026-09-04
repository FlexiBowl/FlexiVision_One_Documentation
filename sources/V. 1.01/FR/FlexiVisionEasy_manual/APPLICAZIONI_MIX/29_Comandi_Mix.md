# **Commandes de l'Application Mix**
```{note}
**Conditions préalables**

Avant de poursuivre cette section, assurez-vous d'avoir compris le fonctionnement de l'application Mix et d'avoir correctement configuré la recette avec les modèles des différents composants. Consultez [Vue d'ensemble de l'Application Mix](28_Panoramica_Mix.md).
```

---

## Différences du côté du robot

Dans une application Mix, les commandes TCP/IP envoyées par le robot au système de vision changent par rapport à celles d'une application Standard.

La principale différence concerne la **famille des commandes de localisation** : les commandes qui, dans l'application standard, portent le préfixe `start_` sont remplacées par la famille équivalente portant le préfixe `mix_`.

Cette variation permet au système de vision d'activer la logique de reconnaissance **multi-composants**, en renvoyant au robot non seulement les coordonnées de la pièce localisée, mais aussi l'**identifiant du modèle** reconnu, de sorte que le programme du robot puisse sélectionner la stratégie de prélèvement correcte pour chaque type de pièce.
```{important}
La valeur de retour des commandes Mix comprend toujours l'identifiant du modèle reconnu (`Pattern_n`). Le programme du robot doit être configuré pour gérer les différents types de réponse et adopter la logique de prélèvement appropriée en fonction du modèle identifié.
```
:::{tip}
La nouvelle version permet de gérer de manière combinée les commandes `mix_Locator_n` pour les robots 1, 2 et 3.
:::
---

## Commandes disponibles en mode Mix

### *Gestion des recettes*

| Commande | Action | Valeur de retour |
|---|---|---|
| `set_Recipe=nome_ricetta` | Charge la recette Mix spécifiée | Aucun |
| `get_Recipe` | Restitue le nom de la recette actuellement chargée | `nome_ricetta` |
```{note}
Les commandes de gestion de la recette sont identiques entre les modes Standard et Mix.
```

### *Commandes de localisation Mix*

Les commandes de localisation Mix permettent au robot de demander les coordonnées d'un modèle spécifique dans la recette. Chaque commande est dédiée à un seul modèle et gère de manière autonome le cycle de recherche, y compris la manutention du FlexiBowl® et l'activation de la trémie si nécessaire.

Le comportement de `mix_Locator_n` est le suivant :

1. Le système acquiert une image et cherche le Modèle `n`.
2. Si le modèle n'est pas trouvé lors de la première acquisition, le FlexiBowl® est automatiquement actionné et la recherche reprend.
3. Le cycle se poursuit jusqu'à ce que le Modèle `n` soit localisé ou que la commande `stop_Locator` soit envoyée.
4. Pendant toute la phase de recherche, la trémie est automatiquement activée si nécessaire.
```{important}
Chaque commande `mix_Locator_n` recherche **exclusivement** le modèle correspondant au numéro `n`.   
Cela signifie que pour demander les coordonnées d'un modèle différent, il faut utiliser la commande spécifique à ce modèle (par ex. `mix_Locator_2` pour le Modèle 2, `mix_Locator_3` pour le Modèle 3, et ainsi de suite).
```

| Commande | Action | Valeur de retour |
|---|---|---|
| `mix_Locator_1` | Lance la recherche du **Modèle 1**. S'il n'est pas trouvé, actionne le FlexiBowl® et répète la recherche automatiquement jusqu'à sa localisation ou jusqu'à `stop_Locator`. Active la trémie si nécessaire. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Comme ci-dessus, pour le **Modèle 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Comme ci-dessus, pour le **Modèle 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | Comme ci-dessus, pour le **Modèle 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | Si aucune pièce n'a été prélevée, fait tourner le FlexiBowl® et relance la recherche multi-composants | `Pattern_n;x;y;r` |
| `test_Locator` | Lance la localisation multi-composants sans activer le FlexiBowl® (acquisition d'image uniquement) | `Pattern_n;x;y;r` / Aucun |
| `stop_Locator` | Interrompt toute recherche en cours | Aucun |
| `state_Locator` | Renvoie l'état de diagnostic du localisateur | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
Le nombre maximal de modèles pouvant être gérés dans une seule recette Mix est de **8**, correspondant aux commandes `mix_Locator_1` … `mix_Locator_8`. Le programme du robot peut demander les modèles dans n'importe quel ordre et combinaison, en fonction de la logique de l'application.
```
:::{tip}
La nouvelle version permet de créer des commandes de type `mix_Locator` multi-modèles, c'est-à-dire qui font appel à plusieurs modèles simultanément. Par exemple, la commande `mix_Locator12` fait appel aux modèles 1 et 2.
:::

### *Commandes FlexiBowl®*

| Commande | Action | Valeur de retour |
|---|---|---|
| `start_Empty` | Démarre la séquence de vidage rapide du FlexiBowl® | `start_Empty ended` |

### *Signaux trémie optionnels*
```{note}
Si la trémie doit être activée, la chaîne suivante est renvoyée : `"Hopper;signalnumber;time"`
```

---

## Format de la valeur de retour

En mode Mix, la valeur de retour des commandes de localisation a le format suivant :
```
Pattern_n;x;y;r
```

| Champ | Description |
|---|---|
| `Pattern_n` | Identifiant du modèle reconnu (par ex. `Pattern_1`, `Pattern_2`, …). Correspond au numéro de modèle demandé par la commande `mix_Locator_n`. |
| `x` | Coordonnée X de la pièce dans la zone de travail (en mm, dans le système de référence du robot) |
| `y` | Coordonnée Y de la pièce dans la zone de travail (en mm, dans le système de référence du robot) |
| `r` | Angle de rotation de la pièce (en degrés) |
```{tip}
Le champ `Pattern_n` est le paramètre clé pour les applications Mix : le programme du robot doit l'utiliser pour sélectionner la routine de prélèvement correcte (position d'approche, ouverture de la pince, force de préhension, etc.) en fonction du type de pièce identifiée.
```

---


Pour plus d'informations sur le protocole de communication et les paramètres de connexion TCP/IP, voir :

**→ [Protocole de communication robot-vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
