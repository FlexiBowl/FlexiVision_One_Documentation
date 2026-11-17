# V. 0.23

## **Améliorations**

### Intégration robot

- Suppression du serveur TCP dédié au Laser : toutes les commandes et communications Laser sont désormais acheminées via le client TCP du Robot.

## **Problèmes résolus**

### Wizard Test Air Blow et Test Flip

- Correction du Wizard pour les tests **Flip** et **Blow** : ajout du contrôle de l'état du moteur avec activation automatique, vérification ultérieure et gestion de l'erreur en cas d'échec de l'activation.
