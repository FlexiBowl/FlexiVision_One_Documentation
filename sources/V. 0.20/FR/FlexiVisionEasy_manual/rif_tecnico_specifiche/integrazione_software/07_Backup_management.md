(backup)=
# **BackUp Management**

## **Vue d'ensemble**

Le backup de FlexiVision One consiste à copier le dossier `Recipes` présent sur le VisionController. Ce dossier contient toutes les recettes configurées dans le système — y compris modèles, paramètres de reconnaissance et réglages associés — et représente la seule donnée utilisateur à préserver.

Comme aucun outil dédié n'est nécessaire, le processus de backup se réduit à une simple opération de copier-coller via l'Explorateur de fichiers.
```{important}
Il est recommandé d'effectuer un backup chaque fois qu'une recette est créée ou modifiée, et dans tous les cas avant toute mise à jour logicielle ou intervention de maintenance sur le VisionController.
```

---

## **Contenu du Backup**

La structure suivante est présente dans le dossier d'installation de FlexiVision One:
```
C:\FlexiVision One\
├── Data\
├── Languages\
├── Recipes\          ← unica cartella da includere nel backup
├── Flexivision_Smart_018
└── Package.dat
```

Le seul dossier qui contient des données utilisateur est `Recipes\`. Les autres dossiers et fichiers présents appartiennent à l'installation du logiciel et ne doivent pas être inclus dans le backup.
```{note}
Le chemin exact du dossier d'installation peut varier selon la configuration du système. En cas de doute, vérifier le chemin dans les paramètres du logiciel.
```

---

## **Procédure de Backup**
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Étape**
  - **Action**
* - 1
  - S'assurer que le logiciel FlexiVision One est **fermé**.
* - 2
  - Ouvrir l'Explorateur de fichiers sur le VisionController et naviguer jusqu'à `C:\FlexiVision One\`.
* - 3
  - Faire un clic droit sur le dossier `Recipes` et sélectionner **Copier**.
* - 4
  - Naviguer vers la destination de backup souhaitée (clé USB, dossier réseau, NAS, etc.).
* - 5
  - Coller le dossier dans la destination. Il est conseillé de le renommer en incluant la date, par exemple: `Recipes_backup_2025-06-01`.
```
```{warning}
Ne pas effectuer le backup pendant que le logiciel FlexiVision One est en cours d'exécution. La copie de fichiers ouverts peut être incomplète ou corrompue.
```

---

## **Procédure de Restauration (Restore)**

En cas de perte des données ou de remplacement du VisionController, il est possible de restaurer les recettes précédentes en suivant ces étapes:
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Étape**
  - **Action**
* - 1
  - S'assurer que FlexiVision One est installé sur le VisionController et **fermé**.
* - 2
  - Ouvrir l'Explorateur de fichiers et naviguer jusqu'à `C:\FlexiVision One\`.
* - 3
  - Renommer le dossier `Recipes` existant (p. ex. `Recipes_old`) à titre de précaution.
* - 4
  - Copier le dossier de backup à l'emplacement `C:\FlexiVision One\` et le renommer `Recipes`.
* - 5
  - Démarrer FlexiVision One: toutes les recettes précédemment enregistrées seront à nouveau disponibles.
```
```{important}
La version du logiciel installée sur le VisionController doit être compatible avec celle utilisée au moment du backup. En cas de mise à jour logicielle, contacter le support technique avant de procéder à la restauration.
```

---

## **Recommandations**

- Conserver au moins **deux copies du backup** dans des emplacements physiques distincts (p. ex. une clé USB locale et un dossier réseau distant).
- Toujours étiqueter les backups avec **date et version logicielle** afin de faciliter leur identification dans le temps.
- Ne pas modifier manuellement le contenu du dossier `Recipes`: les recettes doivent être gérées exclusivement via l'interface de FlexiVision One.
```{tip}
Pour les environnements avec plusieurs VisionController, il est conseillé de centraliser les backups dans un dossier réseau partagé, organisé par nom de machine et date.
```
