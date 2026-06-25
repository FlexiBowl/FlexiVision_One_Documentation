# **Création de recettes et de modèles**

(troubleshooting_nuova_ricetta)=
## Dépannage pour la section Créer une nouvelle recette

```{warning}
**Erreur lors de la sauvegarde**

Si la sauvegarde de la recette échoue :
  - Vérifier qu'il y a suffisamment d'espace sur le disque
  - S'assurer que le nom ne contienne pas de caractères inadmissibles N`/ \ : * ? " < > |`)
  - Vérifier qu'une recette portant le même nom n'existe pas déjà
  - Vérifier d'avoir les droits d'écriture sur le dossier du logiciel
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Impossible de créer une nouvelle recette**
  - • Disque plein
    
    • Le nom de la recette contient des caractères inadmissibles
  - • Libérer de l'espace sur le disque
    
    • Éviter les caractères spéciaux dans le nom N/ \ : * ? " < > |)

* - **Recette sauvegardée mais configurations perdues**
  - • La sauvegarde n'a pas été confirmée correctement
    
    • Arrêt forcé du logiciel
    
    • Erreur d'écriture sur le disque
  - • Toujours cliquer sur «&nbsp;Save Recipe » et attendre la confirmation
    
    • Fermer correctement le logiciel
    
    • Vérifier le journal des erreurs Windows
* - **Impossible de charger la recette créée**
  - • Fichier de recette corrompu
    
    • Le parcours d'accès au fichier a changé
  - • Restaurer à partir d'une sauvegarde si elle est disponible
    
    • Vérifier le parcours du dossier de la recette dans la configuration
* - **La recette chargée a des configurations erronées**
  - • Mauvaise recette sélectionnée
    
    • Modifications non enregistrées précédemment
    
    • Conflit entre des recettes aux noms similaires
  - • Vérifier le nom de la recette dans la barre supérieure
    
    • Recharger la recette corrigée de la liste
    
    • Utiliser des conventions de dénomination non ambiguës
```

(troubleshooting_nuovo_modello)=
## Dépannage pour la section Créer un nouveau modèle

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions

* - **Grab Train Image capture une image noire**
  - • Caméra non connectée
    
    • Toplight éteint

    • Backlight éteint
    
    • Exposition trop basse
    
    • Objectif avec capuchon de protection
  - • Vérifier la connexion de la caméra dans Camera Setup
    
    • Allumer le toplight et vérifier l’alimentation

    • Contrôler que light on dans Configuration FlexiBowl® est coché
    
    • Augmenter l'exposition de la caméra
    
    • Retirer le bouchon de l'objectif
* - **Le ROI ne se déplace pas ou ne se redimensionne pas**
  - • L'image n'est pas acquise
    
    • Logiciel bloqué
  - • Exécuter Grab Train Image d’abord
    
    • Redémarrer le logiciel

* - **Apply Train ne génère pas de modèle**
  - • ROI trop faible
    
    • Image sans contraste suffisant
  
  - • Agrandir ROI pour inclure l'ensemble du composant
    
    • Améliorer le contraste/l'éclairage

* - **Le motif créé comprend la texture de la surface**
  - • Feature Threshold trop bas
    
    • Contraste composant-surface insuffisant
  - • Augmenter le Feature Threshold Nes : 0.3 à 0.6)
    
    • Améliorer l'éclairage pour augmenter le contraste
* - **Le modèle créé comporte trop peu de lignes**
  - • Feature Threshold trop élevé
    
    • Image floue

    • Image sans contraste suffisant
  - • Diminuer Feature Threshold Nes : 0.8 à 0.5)
    
    • Vérifier la mise au point de la caméra et la corriger si nécessaire

    • Améliorer le contraste/l'éclairage

* - **Le modèle comprend des reflets lumineux**
  - • Feature Threshold trop faible
    
    • Éclairage non uniforme
    
  - • Augmenter Feature Threshold
    
    • Ajuster la position/l'angle du toplight


* - **Impossible de nommer le modèle**
  - • Le nom contient des caractères inadmissibles
    
    • Longueur excessive du nom
  - • Utiliser uniquement des lettres, des chiffres, des traits de soulignement et des traits d'union
    
    • Limiter le nom à max 50 caractères
```

(troubleshooting_modelli_roi)=
## Dépannage pour la section Définition du ROI et tolérances

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions

* - **Le test ne détecte aucun composant**
  - • Accept Threshold trop élevé
    
    • Composants en dehors de la Region Search
    
    • Modèle incorrect
    
    • Modification de l'éclairage par rapport à la formation
  - • Diminuer Accept Threshold Nes : de 0,90 à 0,75)
    
    • Élargir la Region Search pour inclure les composants
    
    • Répéter le training du modèle
    
    • Stabiliser l'éclairage
* - **Le test détecte trop de faux positifs**
  - • Accept Threshold trop bas
    
    • Modèle trop simple/générique
    
    • Il y a des composants très similaires mais qui présentent en même temps de nombreuses différences
  - • Augmenter Accept Threshold Nes : de 0,70 à 0,85)
    
    • Refaire le modèle avec un Feature Threshold plus bas (plus détaillé)
    
    • Séparer en différents modèles si nécessaire
* - **Le test détecte des composants mais les résultats sont trop faibles**
  - • Variabilité des composants réels par rapport au modèle training
    
    • Éclairage différent
    
    • Composants sales/endommagés
    
    • Modèle trop détaillé
  - • Vérifier la qualité des composants et les nettoyer si nécessaire
    
    • Normaliser l'éclairage
    
    • Écarter les composants endommagés
    
    • Refaire le modèle avec un Feature Threshold plus élevé (moins détaillé)

* - **Results Panel vide même avec des composants visibles**
  - • Aucun composant ne dépasse Accept Threshold
    
    • Region Search n’inclut pas de composants
    
    • Test non effectué
  - • Diminuer Accept Threshold
    
    • Vérifier et élargir la Region Search
    
    • Cliquer sur le bouton Test
* - **Coordonnées X,Y, Rotation incorrectes**
  - • L'étalonnage de la caméra n'a pas été effectué ou a été effectué de manière incorrecte
    
    • Système de référence erroné
    
    • La caméra s'est déplacée après l'étalonnage
  - • Effectuer un étalonnage complet de la caméra ou réviser l'étalonnage actuel
    
    • Vérifier l'origine du système de coordonnées
    
    • Répéter l'étalonnage de la caméra
```

(troubleshooting_istogrammi)=
## Dépannage pour la section Histogrammes

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Impossible d'activer l'histogramme**
  - • Modèle non reconnu
    
    • Limite maximale des histogrammes atteinte N8 par modèle)
    
    • Emplacement déjà occupé
  - • Compléter d'abord la configuration du modèle
    
    • Désactiver des histogrammes non utilisés
    
    • Sélectionner un emplacement libre

* - **AUTO ne calcule pas correctement**
  - • Surface d'histogramme trop petite
    
    • Histogramme en dehors de l'image
    
    • L'image n'est pas chargée
  - • Agrandir la surface de l'histogramme
    
    • Déplacer l'histogramme dans la zone visible
    
    • Acquérir une nouvelle image
* - **Test toujours ROUGE même avec une zone libre**
  - • Étalonnage AUTO effectué avec une surface occupée
    
    • Ombre ou reflet dans la zone
    
    • Bord FlexiBowl® inclus dans la surface
    
    • Saletés sur la surface
  - • Répéter AUTO lorsque la surface est complètement dégagée
    
    • Exclure les zones d'ombres/reflets
    
    • Réduire la surface en excluant les bords
    
    • Nettoyer la surface du FlexiBowl®
* - **Test toujours VERT même avec une zone occupée**
  - • Étalonnage AUTO effectué avec des composants déjà présents
    
    • Seuils mal calculés
    
    • Contraste insuffisant
  - • Répéter AUTO en veillant à ce que la zone soit complètement vide
    
    • Répéter l'étalonnage avec un éclairage stable
    
    • Améliorer le contraste de l'éclairage
* - **L'histogramme se déclenche de manière aléatoire**
  - • Une zone trop grande comprend des zones variables
    
    • Éclairage instable
    
    • Seuil trop étroit
  - • Réduire la zone au minimum nécessaire
    
    • Stabiliser l'éclairage
    
    • Répéter l'étalonnage AUTO
* - **L'histogramme ne se déclenche pas quand il le devrait**
  - • La zone trop petite n'inclut pas d’obstacle
    
    • Seuil trop permissif
    
  - • Agrandir la zone de l'histogramme
    
    • Répéter l'étalonnage AUTO avec un contraste plus élevé
    
* - **Impossible de créer un deuxième histogramme pour la pince**
  - • Mauvais emplacement d'histogramme sélectionné
  - • Revenir à la liste et sélectionner Histogramme 2
* - **Le test d'histogrammes multiples ne fonctionne pas**
  - • Tous les histogrammes ne sont pas activés
    
    • Configuration incomplète
    
    • Conflit entre les histogrammes
  - • Vérifier l'activation de tous les histogrammes nécessaires
    
    • Terminer la configuration AUTO pour chaque histogramme
    
    • Vérifier que les zones ne se chevauchent pas
```

(troubleshooting_robot_pick)=
## Dépannage pour la section Étalonnage Robot Pick 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Coordonnées du robot non disponibles Perdues/oubliées)**
  - • Non notées lors de la préparation physique
    
    • Feuille de notes perdue
    
    • Coordonnées écrasées
  - • **OBLIGATOIRE** : Répéter l'ensemble de la préparation physique du point 1 au point 9 de [Création de Modèle](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md)
    
    • Enregistrer les coordonnées dans des fichiers numériques et sur papier
    
    • Photographier l'écran du pupitre d’apprentissage du robot
* - **Find Object ne détecte pas de composant**
  - • Le composant de référence a été déplacé
    
    • Accept Threshold trop élevé
    
    • Composant en dehors de la Region Search
  - • Vérifier la position du composant de référence
    
    • Abaisser momentanément l’Accept Threshold
    
    • Vérifier que la Region Search inclut un composant
* - **Vision Result indique des coordonnées erronées**
  - • L'étalonnage de la caméra n'a pas été effectué
    
    • Système de coordonnées non configuré
    
    • La caméra s'est déplacée après l'étalonnage
  - • Effectuer un étalonnage avant Robot Pick
    
    • Vérifier l'origine du système de référence
    
    • Répéter l'étalonnage de la caméra
* - **Impossible d'entrer les coordonnées du robot**
  - • Champs bloqués
    
    • Enable Robot Pick non activé
    
    • Format des numéros incorrect
  - • Cliquer d'abord sur Enable Robot Pick
    
    • Activer les champs en cliquant dessus
    
    • Utiliser le point comme séparateur décimal
* - **Gripper Offset calcule des valeurs absurdes**
  - • Coordonnées du robot mal saisies
    
    • X et Y échangés
    
    • Signe +/- erroné
    
    • Décimales incorrectes ou approximatives
  - • **CRITIQUE** : Vérifier soigneusement chaque coordonnée
    
    • Contrôler l’ordre X, Y, RZ
    
    • Vérifier les signes des coordonnées
    
    • Copier les valeurs exactement comme indiqué sans approximations
* - **Le robot prélève dans des positions erronées après l'étalonnage**
  - • Les coordonnées du robot indiquées sont erronées
    
    • Cadre/outil robot modifié après l'annotation
    
    • Le composant de référence a été déplacé pendant l'annotation
    
    • Le Gripper Offset n'est pas enregistré
  - • Répéter la préparation physique en vérifiant que le cadre/l'outil sont corrects
    
    • Assurer le même cadre/outil pour l'annotation et le retrait
    
    • Répéter le réglage avec le composant correctement positionné
    
    • Sauvegarder la recette après le calcul Gripper Offset
* - **Offset robot valable uniquement pour le composant de référence**
  - • Distorsion optique élevée
    
    • Calibrage imprécis de la caméra
    
    • Region search trop grande par rapport à l'étalonnage
  - • Améliorer l'étalonnage de la caméra
    
    • Utiliser un objectif à faible distorsion
    
    • Réduire la Region Search si possible
* - **Impossible de sauvegarder le Gripper Offset**
  - • Recette non chargée
    
    • Permis insuffisants
    
    • Disque plein
  - • Vérifier que la recette a été correctement chargée
    
    • Vérifier les droits d'écriture
    
    • Libérer de l’espace disque
* - **Rotation RZ du robot toujours erronée**
  - • Le robot RZ n'était pas à 0° pendant le réglage
    
    • Dernier axe du robot incorrect
    
    • Système de coordonnées tourné
  - • Répéter le réglage en amenant le dernier axe du robot à RZ=0°
    
    • Vérifier que l'outil sélectionné est correct
    
    • Vérifier l'orientation du système de coordonnées
```



