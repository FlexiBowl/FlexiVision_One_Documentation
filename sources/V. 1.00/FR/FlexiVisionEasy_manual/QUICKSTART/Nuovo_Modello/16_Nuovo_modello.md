# **Création de recettes et de modèles - Aperçu**

Cette section guide l'utilisateur tout au long du processus de création d'une recette d'application et des modèles de pièces nécessaires à la reconnaissance et au prélèvement par le robot.

```{note}
**Pré-requis**

Avant de passer à la création de recettes et de modèles, s’assurer que :
  - Toutes les configurations matérielles sont terminées [(Configuration des composants)](setupcomponenti)
  - L'étalonnage de la caméra a été effectué avec succès[(Étalonnage de la caméra](calibrazione))
  - L'étalonnage du robot est terminé
  - Les pièces physiques à reconnaître sont disponibles
```

---

## Recette par rapport au modèle : Différences fondamentales

Avant de commencer, il est important de comprendre la différence entre **recette** et **modèle :**

```{list-table}
   :widths: 50 50
   :header-rows: 1

* - Qu'est-ce qu'une recette ?
     - Qu'est-ce qu'un modèle ?
* - Le conteneur global de l'ensemble de l'application de prélèvement.
     - La définition spécifique d'un composant unique à reconnaître.
* - Il comprend jusqu'à 8 modèles, paramètres FlexiBowl®, trémies et logiques de communication.
     - Il inclut des images d'apprentissage, ROI, des caractéristiques visuelles, des filtres et des décalages de robot.
* - Il gère les paramètres matériels (vibrations, vitesse) et réseau (port TCP/IP, délai d'attente).
     - Il gère les paramètres de vision (seuil, score minimum) et les coordonnées de prélèvement (gripper).
* - Il peut traiter plusieurs types de pièces simultanément (multi-modèle).
     - Axé sur un seul modèle visuel spécifique.
```


```{tip}
Une recette peut contenir jusqu'à 8 modèles différents, permettant au robot de reconnaître et de sélectionner différents types de pièces à partir d'une même application sans modification de configuration.
```


---

## Aperçu du processus complet

Le processus de création d'une recette complète et opérationnelle consiste en plusieurs étapes séquentielles :

```{figure} ../../../../../_shared/media/images/newmodel4.jpg
:alt: Workflow creazione ricetta e modelli
:width: 100%
:align: center

Schéma complet du processus de création de recettes et de modèles
```

### *Principales étapes*

```{list-table}
:header-rows: 1
:widths: 10 30 60

* - Étape
  - Nom
  - Description
* - **1**
  - Création de recette
  - Définition de la recette d'application avec nom, type et FlexiBowl® utilisé
* - **2**
  - Préparation physique
  - Positionnement de la pièce de référence dans la zone de vision
* - **3**
  - Apprentissage du modèle
  - Acquisition d'images et création du modèle de reconnaissance
* - **4**
  - Définition du ROI
  - Définition de la zone de recherche où rechercher les pièces
* - **5**
  - Configuration des filtres
  - Configuration du seuil d'acceptation et des tolérances de reconnaissance
* - **6**
  - Préparation physique
  - Simulation de prélèvement avec le robot pour positionner les objets qui simuleront l'empreinte de la pince
* - **7**
  - Sauvegarde des coordonnées
  - Sauvegarder les coordonnées du robot à la position de prélèvement du composant de référence
* - **8**
  - Création de Clearances
  - Définition des zones qui doivent rester dégagées (surface de la pince, obstacles)
* - **9**
  - Coordonnées du robot
  - Calcul du décalage du préhenseur pour un prélèvement correct
* - **10**
  - Test et validation
  - Vérification du fonctionnement complet et sauvegarde de la recette
```

---

## Guide de navigation des sections détaillées

Pour des informations complètes sur chaque étape du processus, veuillez vous référer aux sections correspondantes :

  - **[Création d'une nouvelle recette](nuovaricetta)** - Comment créer et configurer une nouvelle recette
  - **[Training Modèle](nuovomodello)** - Acquisition d'image et création de motifs
  - **[Définition ROI et filtres](roitest)** - Configuration de la zone de recherche et des tolérances
  - **[Création Clearances](istogrammi)** - Définition des zones à laisser libres
  - **[Coordonnées Robot Pick](robotpick)**  - Calcul du gripper offset

---

## Conseils pratiques avant de commencer

### *Préparation du matériel*

```{tip}
**Liste de vérification de préparation**

Avant de commencer à créer des modèles, préparer :

  - Au moins 10 à 20 pièces du type à reconnaître (à des fins d'essai)
  - Pièces propres et en bon état (représentatives de la production)
  - Simulateurs de taille de pinces (il ne doit PAS s'agir de pièces du même type, car il est important de ne pas les confondre avec la pièce de référence)
  - Feuille pour noter les coordonnées du robot (X, Y, RZ)
  - FlexiBowl® vide et propre
  - Backlight/Toplight allumé
```

### *Environnement optimal*

```{note}
**Conditions idéales pour le training**

  - Éclairage stable (éviter les rayons directs du soleil)
  - FlexiBowl® immobile
  - Robot en position de sécurité (ne doit pas interférer pendant les acquisitions)
  - Logiciel FlexiVision One ouvert et base de recettes chargée
```

### *Erreurs courantes à éviter*

```{error}
**Éviter ces erreurs fréquentes**

❌ **Ne pas sauvegarder les coordonnées du robot** pendant la préparation physique → impossible de calculer le décalage du préhenseur

❌ **Déplacer la pièce** après avoir enregistré les coordonnées → mauvais décalage

❌ **Feature threshold** (**Seuil des caractéristiques) trop bas** → modèle trop détaillé, reconnaît la texture de la surface

❌ **ROI trop étroit** → les pièces situées sur les bords ne sont pas détectées

❌ **Clearances (Dégagements) trop petits** → collisions de la pince avec des pièces adjacentes

❌ **Ne pas tester avec plusieurs pièces** → les problèmes ne sont détectés qu'au moment de la production

Pour éviter ces problèmes, il convient de suivre attentivement les procédures décrites dans les sections suivantes.
```

---

## Assistance et ressources supplémentaires

```{note}
**Les boutons** **INFOS**
Dans chacune des sections de fonctionnement, un bouton INFOS est disponible en haut à droite.
Une explication de la procédure étape par étape est disponible dans ce bouton, la même procédure peut être vue dans le tutoriel vidéo.

  - [**Tutoriels vidéo complets**](vidtutcompleti)
  - **Assistance technique**: [support@arsautomation.com](mailto:support@arsautomation.com) pour obtenir une assistance

Pour les problèmes spécifiques liés à la création de modèles, voir la section [Dépannage](troubleshooting).
```

---

## Étapes suivantes

Une fois que la vue d'ensemble du processus est comprise, il faut passer à la création proprement dite :

**→ [Commencer : Création d'une nouvelle recette](nuovaricetta)**


```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```
