# V. 0.24

## **Nouvelles fonctionnalités**

### Caméras de contrôle

- Ajout de la gestion de **3 caméras de contrôle** indépendantes, associées respectivement à FLB1, FLB2 et FLB3.
- Implémentation de la commande robot `start_control_` avec prise en charge de paramètres personnalisés, transmis aux scripts VisionPro.
- Ajout de la gestion de scripts VisionPro personnalisables, avec sortie textuelle et images `CogRecord` incluant les résultats graphiques.
- Implémentation de Main Tasks dédiées aux caméras de contrôle, avec gestion des erreurs, journalisation et envoi des résultats au robot.
- Activation de l'exécution des contrôles même sans robot connecté, pour réaliser des tests locaux depuis la HMI.
- Ajout de pages HMI partagées pour la configuration de la caméra, la configuration de VisionPro et l'affichage runtime des trois caméras de contrôle.

## **Améliorations**

### Clearances (Histogrammes)

- Mise à jour de la gestion des régions pour les 8 modèles, les 8 Histogram et les 3 caméras, en préservant la position, les dimensions et la géométrie des ROI enregistrées.

## **Problèmes résolus**

### Recettes

- Correction de la réinitialisation des ROI des Histogram lors du changement de recette.
