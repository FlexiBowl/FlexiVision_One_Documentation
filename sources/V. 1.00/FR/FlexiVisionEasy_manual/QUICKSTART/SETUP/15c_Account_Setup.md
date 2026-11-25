# **Account Setup**

La page **Account Setup** permet de créer et de supprimer les comptes utilisateur de FlexiVision One. Un **niveau d'accès** est attribué à chaque compte ; il détermine les fonctions du logiciel que le compte peut utiliser.

```{note}
La gestion des comptes est réservée aux utilisateurs de niveau **5** (**Engineer**).
```

---

(accesso-alla-configurazione-account)=
## Accès à la configuration des comptes

:::{list-table}
:widths: 10 90

* - **1**
  - Ouvrir la page **Setup**.
* - **2**
  - Dans le menu déroulant **Name**, sélectionner **Engineer**.
* - **3**
  - Dans le champ **Password**, saisir `3`.
* - **4**
  - Appuyer sur **Login** et valider le message de connexion réussie avec **OK**.
* - **5**
  - Appuyer sur l'icône **Account Setup**.
:::

```{note}
La connexion n'est effective qu'après avoir appuyé sur **Login**. L'utilisateur actif et son niveau sont indiqués sous **Current User Name**.
```

---

## Aperçu de l'interface Account Setup

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Liste des comptes** (à gauche)
  - Affiche les comptes existants. **Delete Account** supprime le compte sélectionné.
* - **Nouveau compte** (à droite)
  - Champs **Account Name**, **Account Password**, **Account Level** et bouton **Create Account**.
:::

---

## Création d'un nouveau compte

### *Étape 1 : Saisie des données*

:::{list-table}
:widths: 10 90

* - **6**
  - Dans le champ **Account Name**, saisir le nom du nouveau compte.
* - **7**
  - Dans le champ **Account Password**, saisir le mot de passe du nouveau compte.
* - **8**
  - Dans le champ **Account Level**, saisir le niveau d'accès, de `1` à `5` (voir [Niveaux d'accès](#livelli-di-accesso)).
* - **9**
  - Appuyer sur **Create Account**. Le nouveau compte apparaît dans la liste de gauche.
:::

### *Étape 2 : Connexion avec le nouveau compte*

:::{list-table}
:widths: 10 90

* - **10**
  - Revenir à la page **Setup** et sélectionner le nouveau compte dans le menu déroulant **Name**.
* - **11**
  - Saisir le mot de passe et appuyer sur **Login**.
:::

La vidéo montre la création d'un compte de niveau 3, la connexion avec le nouveau compte et les messages affichés lorsque le niveau est insuffisant.

:::{video} ../../../../../_shared/media/videos/new_account.mp4
     :width: 100%
     :align: center
:::

---

## Suppression d'un compte

Effectuer les étapes 1 à 5 de la section [Accès à la configuration des comptes](#accesso-alla-configurazione-account), puis procéder comme suit.

:::{list-table}
:widths: 10 90

* - **6**
  - Dans la liste de gauche, sélectionner le compte à supprimer.
* - **7**
  - Appuyer sur **Delete Account**. Le compte est retiré de la liste et du menu déroulant de la page **Setup**.
:::

```{warning}
La suppression est immédiate et aucune confirmation n'est demandée. Vérifier le compte sélectionné avant d'appuyer sur **Delete Account**.
```

:::{video} ../../../../../_shared/media/videos/delete_account.mp4
     :width: 100%
     :align: center
:::

---

(livelli-di-accesso)=
## Niveaux d'accès

FlexiVision One dispose de trois profils prédéfinis. Un compte créé par l'utilisateur reçoit les autorisations correspondant au niveau attribué.

:::{list-table}
:header-rows: 1
:widths: 20 20 60

* - Niveau
  - Profil
  - Utilisation
* - 1 – 3
  - **Operator**
  - Fonctions de base : consultation de la page Home, chargement des recettes et sauvegarde.
* - 4
  - **Technician**
  - Fonctions Operator, plus les tests, la gestion des recettes, la configuration du système et la licence logicielle.
* - 5
  - **Engineer**
  - Fonctions Technician, plus **Protocol Setup** et **Account Setup**.
:::

### *Fonctions activées par profil*

:::{list-table}
:header-rows: 1
:widths: 16 33 17 17 17

* - Page
  - Fonction
  - Operator (1 – 3)
  - Technician (4)
  - Engineer (5)
* - Home
  - Contact Us
  - Oui
  - Oui
  - Oui
* - Home
  - Documentation
  - Oui
  - Oui
  - Oui
* - Home
  - Quick Start
  - Oui
  - Oui
  - Oui
* - Dashboard
  - Test
  - —
  - Oui
  - Oui
* - Recipes
  - Load Recipe
  - Oui
  - Oui
  - Oui
* - Recipes
  - Backup
  - Oui
  - Oui
  - Oui
* - Recipes
  - Import Backup
  - —
  - Oui
  - Oui
* - Recipes
  - New Recipe
  - —
  - Oui
  - Oui
* - Recipes
  - Save Recipe
  - —
  - Oui
  - Oui
* - Recipes
  - Edit Recipe
  - —
  - Oui
  - Oui
* - Recipes
  - Delete Recipe
  - —
  - Oui
  - Oui
* - Setup
  - Camera Setup
  - —
  - Oui
  - Oui
* - Setup
  - FlexiBowl® Setup
  - —
  - Oui
  - Oui
* - Setup
  - Hopper Setup
  - —
  - Oui
  - Oui
* - Setup
  - Robot Setup
  - —
  - Oui
  - Oui
* - Setup
  - License Software
  - —
  - Oui
  - Oui
* - Setup
  - Protocol Setup
  - —
  - —
  - Oui
* - Setup
  - Account Setup
  - —
  - —
  - Oui
* - Général
  - Fermeture de l'application
  - —
  - Oui
  - Oui
:::

En cas de tentative d'utilisation d'une fonction non activée, le message **Insufficient Access Level** apparaît ; il indique le niveau requis et celui de l'utilisateur actif.

### *Déconnexion automatique*

- **Technician** : déconnexion automatique après 5 minutes.
- **Engineer** : aucune déconnexion automatique.

```{tip}
Attribuer à chaque utilisateur le niveau le plus bas suffisant pour ses tâches, afin d'éviter des modifications accidentelles des recettes et des configurations.
```
