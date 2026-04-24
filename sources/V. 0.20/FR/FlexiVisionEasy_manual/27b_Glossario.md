# **Glossaire** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Terme
  - Définition
* - **Accept Threshold**
  - Seuil minimal de similarité (score 0.0–1.0) pour qu'un objet détecté soit accepté par le pattern matching. Valeurs typiques: 0.70–0.90.
* - **Air-blow**
  - Module pneumatique optionnel pour la séparation des composants sur le disque au moyen de jets d'air comprimé. Nécessite une alimentation à 5–6 bar.
* - **Artefact**
  - Défaut dans l'image acquise causé par des interférences électromagnétiques, des problèmes de câblage ou des dysfonctionnements du capteur.
* - **Calibration Caméra**
  - Corrélation pixels/coordonnées réelles au moyen d'une cible de calibration avec un motif connu. Calcule les paramètres intrinsèques et extrinsèques de la caméra.
* - **Clearance**
  - Analyse de la distribution des niveaux de gris sur une zone définie. Utilisée pour détecter la présence/absence d'objets (contrôle de pince, zone libre).
* - **Caméra POE**
  - Caméra industrielle alimentée et connectée par un seul câble Ethernet. Standard: IEEE 802.3af (15.4W) ou 802.3at (30W).
* - **CAPTURE**
  - Commande logicielle permettant d'acquérir les images de référence du disque vide et plein, nécessaires au calcul automatique des seuils du hopper.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Catégories géométriques des composants dans le FlexiBowl Wizard. *FLAT*: formes plates (rondelles, joints). *CYLINDRICAL*: formes cylindriques (goupilles, vis). *COMPLEX*: géométries irrégulières ou asymétriques.
* - **Distance de Travail**
  - Distance optimale entre l'objectif et la surface du disque. Typiquement 950–1000mm dans les configurations standard.
* - **Distorsion Optique**
  - Déformation géométrique de l'image due à l'objectif. Compensée automatiquement pendant la calibration caméra.
* - **Exposition**
  - Temps de collecte de lumière du capteur caméra. Mesuré en μs ou ms; influence directement la qualité de l'image en production.
* - **Feature Threshold**
  - Seuil d'extraction des caractéristiques (bords, lignes) pendant le training du modèle. Valeurs typiques: 0.3–0.8.
* - **FlexiBowl**
  - Système d'alimentation à disque rotatif vibrant pour le positionnement et l'orientation aléatoire des composants en vue de la prise robotisée.
* - **FlexiBowl Wizard**
  - Procédure guidée pour le calcul automatique des paramètres optimaux du FlexiBowl en fonction de la géométrie et du comportement des composants.
* - **Flip**
  - Impulsion pneumatique sous le disque pour repositionner les composants. Configurable via *Flip Count* (nombre d'impulsions) et *Flip Delay* (intervalle en ms entre les impulsions).
* - **Grab Train Image**
  - Commande logicielle permettant d'acquérir l'image à utiliser pour le training d'un nouveau modèle.
* - **Gripper Offset**
  - Vecteur de correction (ΔX, ΔY, ΔRZ) qui compense le décalage entre le centre optique du système de vision et le TCP du gripper.
* - **Hotspot**
  - Zone de réflexion directe de la lumière dans l'image. Elle apparaît comme une zone surexposée et peut compromettre la reconnaissance.
* - **Objectif**
  - Composant optique de la caméra. Il doit être vissé jusqu'au contact métal-métal; la focale (p. ex. 16mm, 25mm) détermine le champ de vision à la distance de travail.
* - **Model (Modèle)**
  - Gabarit géométrique du composant créé pendant le training. Chaque recette prend en charge jusqu'à 8 modèles.
* - **Origine Modèle**
  - Point de référence sur le composant utilisé comme centre du système de coordonnées pour le calcul des positions. Correspond généralement au TCP de prise.
* - **Orthogonalité**
  - Perpendicularité de la caméra par rapport au disque (tolérance ±1°). Vérifiable avec un niveau de précision.
* - **Pattern Matching**
  - Algorithme qui localise les composants dans l'image en les comparant au modèle de référence enregistré pendant le training.
* - **Protocol (Protocole)**
  - Format de communication entre VisionController et robot. Définit la structure des messages, l'ordre des coordonnées et les unités de mesure.
* - **Recipe (Recette)**
  - Fichier XML contenant tous les paramètres de configuration du système: modèles, seuils, calibrations, setup FlexiBowl et robot.
* - **Region Search**
  - Zone rectangulaire dans l'image dans laquelle le pattern matching effectue la recherche. Réduit les temps de traitement et augmente la précision.
* - **ROI (Region of Interest)**
  - Zone rectangulaire qui délimite le composant dans l'image pendant le training du modèle.
* - **RZ / Rotation Z**
  - Angle de rotation autour de l'axe Z communiqué au robot pour l'orientation du composant. Exprimé en degrés (0–360°).
* - **Score**
  - Indice de similarité (0.0–1.0) entre le modèle et l'objet détecté. Détermine la confiance de la reconnaissance.
* - **Simulateurs d'Encombrement de Pince**
  - Objets physiques placés autour du composant pendant le training pour exclure du modèle les zones occupées par la pince lors de la prise.
* - **Steps**
  - Nombre de cycles de vibration du hopper nécessaires pour que les composants atteignent la zone de prise. Paramètre critique pour la synchronisation avec le cycle robot.
* - **Subnet**
  - FlexiBowl et VisionController doivent partager le même subnet (p. ex. 192.168.1.x) pour la communication TCP/IP.
* - **Synchronize Parameters**
  - Commande logicielle qui transfère les paramètres du VisionController au FlexiBowl. Obligatoire après chaque modification pour rendre les réglages effectifs.
* - **Cible de Calibration**
  - Motif géométrique imprimé (cercles ou damier) avec dimensions connues et surface plane, utilisé pour la calibration caméra.
* - **Timeout**
  - Temps maximal d'attente d'une réponse en communication. En cas de dépassement, une erreur est générée.
* - **Tilt**
  - Inclinaison de la caméra par rapport au plan horizontal. Valeur admise: 0° ± 1°.
* - **Toplight**
  - Illuminateur LED positionné au-dessus du disque, qui garantit un éclairage uniforme par le haut. Alimentation: 24V DC.
* - **Training**
  - Processus de création du modèle de reconnaissance par sélection des caractéristiques distinctives du composant à partir d'une image de référence.
* - **Trigger**
  - Signal de démarrage de l'acquisition d'image. Il peut être logiciel (temporisé) ou matériel (signal électrique externe).
* - **Vision Result**
  - Sortie du système de vision: coordonnées (X, Y, RZ) et score du composant détecté, transmis au robot pour la prise.
* - **VisionController**
  - Ordinateur industriel qui exécute FlexiVision One, gère les caméras, traite les images et communique avec FlexiBowl et le robot.
```

