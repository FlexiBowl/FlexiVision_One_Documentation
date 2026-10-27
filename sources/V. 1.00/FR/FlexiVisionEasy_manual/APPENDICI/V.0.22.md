# V. 0.22


## **Nouvelles fonctionnalités**

### Applications Mix

- Ajout de la gestion combinée des commandes `mix_Locator` pour le Robot 1, le Robot 2 et le Robot 3 : il est désormais possible d'appeler plusieurs modèles simultanément au sein d'une seule chaîne (par ex. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
- Ajout d'un contrôle de validité sur les commandes `mix_Locator` : si la chaîne reçue ne contient aucun modèle valide (de 1 à 8), le système renvoie une erreur dédiée.
- Ajout d'une protection sur les commandes `start_Locator` et `mix_Locator` : si un Locator est déjà en cours d'exécution, la commande est ignorée, ce qui évite les redémarrages indésirables de la tâche et les modifications imprévues des modèles actifs.

### Clearances (Histogrammes)

- Ajout de la prise en charge de trois types de région pour les outils Histogram — **Rectangle**, **Secteur annulaire** et **Cercle** — sélectionnables via un menu dédié dans la page recette, pour tous les modèles et histogrammes disponibles.
- Mise à jour de la page Test Histogram pour afficher correctement les nouveaux types de région, dessinés en vert ou en rouge selon le résultat du contrôle.
- Ajout de l'affichage graphique de l'indice Histogram et des principales mesures de la région sélectionnée.

### FlexiBowl®

- Ajout de la fonction **Belt Check** pour le contrôle de l'état d'usure et de propreté de la bande :
  - acquisition d'une image de référence de la bande propre via le bouton **Save Clean Reference** ;
  - comparaison automatique, via Histogram, entre l'image de référence et l'image actuelle de la bande ;
  - classification automatique de la bande en **Light**, **Dark** ou **Medium** selon la luminosité de la référence ;
  - affichage de l'état de la bande avec valeur en pourcentage, couleur et indication textuelle (**Good**, **Warning**, **Poor**) ;
  - affichage de la date du dernier Belt Check pour chaque FlexiBowl®.
- Ajout de la procédure guidée **Hopper Step Setup** pour calculer le nombre de séquences nécessaires pour atteindre la zone de la trémie, avec les fonctions **Reset Steps**, **Test Sequence** et **Save Hopper Step**, et l'indication correspondante de l'état d'étalonnage.
- Ajout de la possibilité de saisir manuellement au clavier les paramètres des FlexiBowl®, comme alternative au réglage par curseur.
- Ajout d'un message d'avertissement non modal lorsque les paramètres d'un FlexiBowl® sont modifiés mais pas encore synchronisés avec le dispositif réel.
- Ajout de l'**Auto Reset FlexiBowl** : si une erreur est déjà présente au démarrage d'une commande de mouvement, le système effectue automatiquement la réinitialisation avant de lancer la commande.

### Sécurité et accès

- Ajout du contrôle du niveau d'accès sur les boutons communs de l'interface : les fonctions protégées vérifient le niveau utilisateur actuel avant l'exécution et affichent un message en cas de droits insuffisants.

## **Améliorations**

### Assistant de création de recette

- Ajout d'un contrôle sur le Picking Offset au bouton **NEXT** : si l'offset est activé, il doit être calculé et valide avant de pouvoir poursuivre dans l'assistant.

### Interface recette

- Correction du format d'affichage des offsets Robot Pick dans les pages recette, en forçant le point comme séparateur décimal à la place de la virgule.

## **Problèmes résolus**

### Gestion des sauvegardes (BackUp)

- Correction d'une erreur lors de la création de la sauvegarde qui se produisait lorsque le chemin sur le PC contenait des espaces.

### Séquences

- Résolution d'un problème d'affichage qui pouvait montrer des commandes apparemment en double dans la liste des séquences.
