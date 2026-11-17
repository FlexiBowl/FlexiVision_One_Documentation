(backup)=
# **BackUp Management**

## Aperçu

L'ensemble de la configuration de FlexiVision One — configuration du matériel, calibrages, modèles de pièces et paramètres de protocole — est contenu dans les fichiers de recette. C'est pourquoi les sauvegardes sont essentielles pour assurer la sécurité de toutes les données.

```{important}
Il est recommandé d'effectuer une sauvegarde après chaque création ou modification importante d'une recette, avant la mise à jour du logiciel FlexiVision et avant toute intervention matérielle sur le système.

**Règle minimale :** au moins une fois par semaine en fonctionnement normal.
```

---

## Procédure de sauvegarde

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Étape**
  - **Action**
* - Cliquer sur Sauvegarde
  - Dans le menu Recettes, cliquer sur le bouton Sauvegarde.
* - Choisir le dossier FlexiVision
  - Localiser le dossier d'exécution FlexiVision One sur le VisionController.
* - Choisir le dossier de destination
  - Sélectionner le dossier de destination de la sauvegarde.
* - Attribution d'un nom avec la date
  - Toujours attribuer un nom qui inclut la date, la version du logiciel et l'identifiant du système ou d'autres informations utiles telles que le nom du client. Exemples :
    
    - `FV_Recipes_LineA_20260402_SW1.2.xml`
    - `Backup_FlexiVision_ClientABC_Plant3_20260402.xml`
    - `Recipes_FB500_Commissioning_20260315_v1.zip`
    
    Inclure la version du logiciel (visible sur la page d'accueil) dans le nom ou dans un fichier texte joint.
```

---

## Procédure d'importation de la sauvegarde

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Étape**
  - **Action**
* - Cliquer sur Import Backup
  - Dans la section Recettes, cliquer sur Import Backup.
* - Sélectionner le dossier d'exécution de FlexiVision
  - **Sélectionner le dossier contenant l'installation de FlexiVision.**
* - Sélectionner le chemin d'accès à la sauvegarde
  - Définir le chemin d'accès au fichier de sauvegarde. FlexiVision va redémarrer pendant ce processus.
* - Contrôles après la récupération
  - Après la récupération, effectuer les contrôles suivants avant de redémarrer la production :

    1. Vérifier que toutes les recettes attendues sont répertoriées sur la page Recettes.
    2. Confirmer que la recette principale peut être chargée sans erreur.
    3. Vérifier que les FlexiBowl® et les tests de connexion de la caméra sont positifs (verts) dans la configuration de la caméra.
    4. Confirmer que le tableau de bord affiche les appareils correctement connectés.

    **Effectuer un cycle d'essai avec la recette de fonctionnement principale pour vérifier le bon fonctionnement.**
```

---

## Gestion correcte des recettes

```{list-table}
:header-rows: 1
:widths: 25 37 38

* - **Action**
  - **Méthode correcte**
  - **Méthode à éviter**
* - Renommer une recette
  - Page Recettes → fonction Renommer dans le logiciel.
  - Renommer le fichier XML via l'explorateur de fichiers.
* - Supprimer une recette
  - Page Recettes → bouton **Supprimer la recette**.
  - Supprimer manuellement le fichier XML.
* - Copier une recette vers un autre système
  - Page Recettes → Sauvegarde → Importation Sauvegarde sur l'autre système.
  - Copier et coller des fichiers XML entre deux dossiers Recipes.
* - Modifier un paramètre de recette
  - Ouvrir la recette en mode **Modification** dans le logiciel.
  - Modifier le fichier XML à l'aide d'un éditeur de texte.
```
