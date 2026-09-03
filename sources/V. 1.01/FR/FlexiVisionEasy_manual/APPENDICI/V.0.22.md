# V. 0.22


```{note}
Cette page concerne la version **1.01** du présent manuel, compatible avec **FlexiVision Studio v0.21** et **v0.22**.
```

## **Nouvelles fonctionnalités**

### Applications Mix

- Ajout de la gestion combinée des commandes `mix_locator` pour Robot 1, Robot 2 et Robot 3 : il est désormais possible d'appeler plusieurs modèles simultanément au sein d'une même chaîne de caractères (par exemple `mix_locator_12`, `mix_locator_248`, `mix_locator_12345678`).
- Ajout d'un contrôle de validité sur les commandes `mix_locator` : si la chaîne reçue ne contient pas de modèles valides (de 1 à 8), le système renvoie une erreur spécifique.
- Ajout d'une protection sur les commandes `start_locator` et `mix_locator` : si un Locator est déjà en cours d'exécution, la commande est ignorée, ce qui évite les redémarrages indésirables de la tâche et les modifications imprévues des modèles actifs.

### Clearances (Histogrammes)

- Ajout de la prise en charge de trois types de régions pour les outils Histogramme — **Rectangle**, **Secteur annulaire** et **Cercle** — sélectionnables via un menu dédié sur la page de recette, pour tous les modèles et histogrammes disponibles.
- Mise à jour de la page « Test d'histogramme » pour afficher correctement les nouveaux types de zones, représentées en vert ou en rouge selon le résultat du contrôle.
- Ajout d'un affichage graphique de l'indice d'histogramme et des mesures principales de la zone sélectionnée.

### FlexiBowl®

- Ajout de la fonction **Belt Check** pour contrôler l'état d'usure et de propreté de la bande :
  - acquisition d'une image de référence de la bande propre à l'aide du bouton **Save Clean Reference** ;
  - comparaison automatique, à l'aide d'un histogramme, entre l'image de référence et l'image actuelle de la bande ;
  - classification automatique de la bande en **Light**, **Dark** ou **Medium** en fonction de la luminosité de l'image de référence ;
  - affichage de l'état de la bande avec une valeur en pourcentage, une couleur et une indication textuelle (**Good**, **Warning**, **Poor**) ;
  - affichage de la date du dernier contrôle Belt Check pour chaque FlexiBowl®.
- Ajout de l’assistant **Hopper Step Setup** pour calculer le nombre de séquences nécessaires pour atteindre la zone de la trémie, avec les fonctions **Reset Steps**, **Test Sequence** et **Save Hopper Step**, ainsi que l’indication correspondante de l’état d’étalonnage.
- Ajout de la possibilité de saisir manuellement les paramètres des FlexiBowl® à l’aide du clavier, en alternative au réglage via le curseur.
- Ajout d’un message d’avertissement non modal lorsque les paramètres d’un FlexiBowl® sont modifiés mais ne sont pas encore synchronisés avec l’appareil réel.
- Ajout de la fonction **Réinitialisation automatique FlexiBowl** : si une erreur est déjà présente au lancement d’une commande de mouvement, le système effectue automatiquement la réinitialisation avant de lancer la commande.

### Sécurité et accès

- Ajout d'un contrôle du niveau d'accès sur les boutons communs de l'interface : les fonctions protégées vérifient le niveau d'utilisateur actuel avant leur exécution et affichent un message en cas d'autorisations insuffisantes.

## **Améliorations**

### Assistant de création de recette

- Ajout d'une vérification du décalage de prélèvement (Picking Offset) au bouton **NEXT** : si le décalage est activé, il doit être calculé et valide avant de pouvoir poursuivre dans l'assistant.

### Interface de recette

- Correction du format d'affichage des décalages « Robot Pick » dans les pages de recette, en imposant le point comme séparateur décimal à la place de la virgule.

## **Problèmes résolus**

### Gestion des sauvegardes

- Correction d'une erreur survenant lors de la création d'une sauvegarde lorsque le chemin d'accès sur le PC contenait des espaces.

### Séquences

- Correction d'un problème d'affichage qui pouvait faire apparaître des commandes apparemment en double dans la liste des séquences.
