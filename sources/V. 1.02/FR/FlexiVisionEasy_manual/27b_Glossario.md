# **Glossaire**

```{list-table}
:header-rows: 1
:widths: 25 75

* - Terme
  - Définition
* - **Accept Threshold**
  - Seuil de similarité minimum (score 0,0-1,0) pour qu'un objet détecté soit accepté par le pattern matching. Valeurs typiques : 0.70–0.90.
* - **Air-blow**
  - Module pneumatique optionnel permettant de séparer les composants du disque par des jets d'air comprimé. Nécessite une alimentation à 5-6 bars.
* - **Artefact**
  - Défaut dans l'image capturée causé par des interférences électromagnétiques, des problèmes de câblage ou un dysfonctionnement du capteur.
* - **Étalonnage de la caméra**
  - Corrélation entre les pixels et les coordonnées réelles par le biais d'une cible d’étalonnage avec un modèle connu. Il calcule les paramètres intrinsèques et extrinsèques de la caméra.
* - **Clearance**
  - Analyse de la distribution des niveaux de gris sur une zone définie. Utilisé pour détecter la présence/absence d'objets (contrôle de la pinces, de la zone libre).
* - **Caméra POE**
  - Caméra industrielle alimentée et connectée via un seul câble Ethernet. Standard : IEEE 802.3af (15.4W) ou 802.3at (30W).
* - **CAPTURE**
  - Commande logicielle permettant d'acquérir des images de référence du disque vide et du disque plein, nécessaires au calcul automatique des seuils de la trémie.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Catégories géométriques de composants dans l'assistant FlexiBowl®. *FLAT* : formes plates (rondelles, joints). *CYLINDRICAL* : formes cylindriques (broches, vis). *COMPLEX* : géométries irrégulières ou asymétriques.
* - **Distance de travail**
  - Distance optimale entre l'objectif et la surface du disque. Typiquement 950-1000 mm dans les configurations standards.
* - **Distorsion optique**
  - Déformation géométrique de l'image due à l'objectif. Compensation automatique lors de l'étalonnage de la caméra.
* - **Exposition**
  - Temps de collecte de la lumière par le capteur de la caméra. Mesuré en μs ou en ms ; influe directement sur la qualité de l'image en production.
* - **Feature Threshold**
  - Seuil d'extraction des caractéristiques (arêtes, lignes) lors du training du modèle. Valeurs typiques : 0.3–0.8.
* - **FlexiBowl®**
  - Système d'alimentation par disque rotatif vibrant pour le positionnement et l'orientation aléatoire des composants pour le prélèvement robotisé.
* - **FlexiBowl® Wizard**
  - Assistant pour le calcul automatique des paramètres optimaux de FlexiBowl® en fonction de la géométrie et du comportement des composants.
* - **Flip**
  - Impulsion pneumatique sous le disque pour repositionner les composants. Configurable par le biais du *Flip Count* (nombre d'impulsions) et du *Flip Delay* (intervalle en ms entre les impulsions).
* - **Grab Train Image**
  - Commande logicielle permettant d'acquérir l'image à utiliser au cours du training d'un nouveau modèle.
* - **Gripper Offset**
  - Vecteur de correction (ΔX, ΔY, ΔRZ) qui compense le décalage entre le centre optique du système de vision et le TCP de la pince.
* - **Hotspot**
  - Zone de réflexion directe de la lumière dans l'image. Elle apparaît comme une zone surexposée et peut compromettre la reconnaissance.
* - **Objectif**
  - Composant optique de la caméra. Il doit être vissé dans un contact métal sur métal ; la longueur focale (par exemple 16 mm, 25 mm) détermine le champ de vision à la distance de travail.
* - **Model (Modèle)**
  - Modèle géométrique du composant créé lors de la phase de training. Chaque recette prend en charge jusqu'à 8 modèles par FlexiBowl®.
* - **Origine du modèle**
  - Point de référence sur le composant utilisé comme centre du sistema di coordinate per il calcolo delle posizioni. Corrisponde generalmente al TCP di presa.
* - **Orthogonalité**
  - Perpendicularité de la chambre par rapport au disque (tolérance ±1°). Vérifiable à l'aide d'un niveau de précision.
* - **Pattern matching**
  - Algorithme qui localise les composants de l'image en les comparant au modèle de référence enregistré pendant le training.
* - **Protocol (Protocole)**
  - Format de communication entre le VisionController et le robot. Définit la structure des messages, l'ordre des coordonnées et les unités de mesure.
* - **Recipe (Recette)**
  - Fichier XML contenant tous les paramètres de configuration du système : modèles, seuils, étalonnages, configuration FlexiBowl® et robot.
* - **Region search**
  - Surface rectangulaire de l'image à l'intérieur de laquelle le pattern matching effectue la recherche. Il réduit le temps de traitement et augmente la précision.
* - **ROI (Region of Interest)**
  - Surface rectangulaire délimitant le composant dans l'image lors du training du modèle.
* - **RZ / Rotation Z**
  - Angle de rotation autour de l'axe Z communiqué au robot pour l'orientation du composant. Exprimé en degrés (0-360°).
* - **Score**
  - Indice de similarité (0,0-1,0) entre le modèle et l'objet détecté. Il détermine le degré de confiance de la reconnaissance.
* - **Simulateurs d’encombrement de pince**
  - Objets physiques placés autour du composant pendant le training afin d'exclure du modèle les zones occupées par la pince pendant le prélèvement.
* - **Steps**
  - Nombre de manutentions du FlexiBowl® nécessaires pour que les composants, de la zone de vision, atteignent la zone de déchargement de la trémie.
* - **Subnet**
  - Sous-réseau que le FlexiBowl® et le VisionController doivent partager (par exemple 192.168.1.x) pour la communication TCP/IP.
* - **Synchronize Parameters**
  - Commande logicielle qui transfère les paramètres au FlexiBowl®. Obligatoire après chaque modification pour que les configurations soient effectives.
* - **Timeout**
  - Temps d'attente maximum pour une réponse de communication. Une erreur est générée en cas de dépassement.
* - **Tilt**
  - Inclinaison de la caméra par rapport au plan horizontal. Valeur autorisée : 0° ± 1°.
* - **Toplight**
  - Éclairage LED positionné au-dessus du disque pour un éclairage homogène par le haut. Alimentation électrique : 24V DC.
* - **Training**
  - Processus de création du modèle de reconnaissance par la sélection des caractéristiques distinctives du composant à partir d'une image de référence.
* - **Trigger**
  - Signal de démarrage de l’acquisition d'image. Il peut être logiciel (temporisé) ou matériel (signal électrique externe).
* - **Vision Result**
  - Sortie du sistema di visione: coordinate (X, Y, RZ) e score del componente rilevato, trasmessi al robot per il prelievo.
* - **VisionController**
  - Ordinateur industriel qui fait fonctionner FlexiVision One, gère les caméras, traite les images et communique avec FlexiBowl® et les robots.
```

