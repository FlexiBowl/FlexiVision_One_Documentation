# **Setup Initial**
```{warning}
**Composants inaccessibles**

Si le FlexiBowl®, le robot ou la caméra ne sont pas accessibles :

1. Vérifier que tous les câbles Ethernet sont correctement connectés
2. Vérifier que l'interrupteur/routeur est sous tension
3. Vérifier les adresses IP de tous les appareils :
   - Elles doivent se trouver sur le même sous-réseau (par ex : 192.168.1.x)
   - Il ne doit pas y avoir de conflits d'IP (deux appareils avec la même IP)
4. Utiliser la commande `ping` du terminal pour tester l'accessibilité
5. Désactiver temporairement le pare-feu Windows sur le port/adaptateur utilisé pour les caméras GigE

Pour plus de détails sur la configuration du réseau, voir [Câblage et connexions](cablaggio).
```
(troubleshooting_cam_setup)=
## Dépannage pour la section Camera Setup

```{warning}
**Problèmes de netteté**

Si l'image apparaît floue :

1. Vérifier que la caméra est à la bonne distance de travail ([Calcul de la distance optimale](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Vérifier que l'objectif est vissé à fond
3. Vérifier qu'il n'y ait pas de saleté ou de traces de doigts sur l'objectif
4. Veiller à ce que la caméra soit montée parfaitement parallèle au plan de travail du FlexiBowl®

```
```{tip}
**Problèmes de luminosité**

Si l'image numérisée est trop sombre ou trop claire :

**Trop sombre** :
- Vérifier que le rétro-éclairage/l'éclairage supérieur est allumé (Config FlexiBowl®)
- Augmenter le temps d'exposition (paramètre Cam Exposure dans [Camera FLB])

**Trop claire (surexposée)** :
- Réduire le temps d'exposition (paramètre Cam Exposure dans [Camera FLB])
- Vérifier qu'il n'y ait pas de lumière ambiante excessive
- Ajuster l'ouverture du diaphragme dans le corps optique de la caméra 
  :::{warning}
  Faire très attention en manipulant l'appareil, car même un petit mouvement de l'appareil peut compromettre la fiabilité de l'étalonnage si celui-ci a déjà été effectué 
  :::
```
```{note}
**Performances d’acquisition**

Si l'acquisition de l'image est lente :
- Vérifier que le câble Ethernet est de type Gigabit (Cat6 supérieur)
- Vérifier que le commutateur réseau est de type Gigabit Ethernet (et non Fast Ethernet 100Mbps)
- Modifier le niveau de latence s'il n'y a pas de problèmes d'écrans bleus
- Réduire la taille des paquets à 1500-2000


La fréquence d'images maximale de la caméra est de 24 fps (images par seconde), ce qui est suffisant pour toutes les applications de prélèvement standard.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Image trop sombre**
  - • Exposition de la caméra trop faible
    
    • Toplight éteint ou en panne

    • Backlight éteint ou en panne

    • Toplight présentant une puissance insuffisante
    
    • Objectif avec capuchon de protection
  - • Augmenter l'exposition dans Camera Setup
    
    • Vérifier que le toplight est allumé 
    
    • Vérifier que la coche Light On est activée dans la configuration FlexiBowl®
    
    • Vérifier l'alimentation du toplight
    
    • Retirer le bouchon de protection de l'objectif
* - **Image trop claire (surexposée)**
  - • Exposition de la caméra trop élevée
    
    • Reflets sur la surface du FlexiBowl®
  - • Diminuer l'exposition dans Camera Setup
    
    • Remplacer la surface de préhension par une surface moins réfléchissante
* - **Image floue**
  - • L'objectif n'est pas au point 
    
    • L'objectif n'est pas complètement vissé
    
    • Lentille sale
    
    • Caméra en mouvement/vibrations
  - • Corriger la mise au point de la caméra
    
    • Visser la lentille jusqu'au contact métal-métal
    
    • Nettoyer la lentille avec un chiffon en microfibre
    
    • Mieux fixer la caméra et réduire les vibrations
* - **Image avec artefacts ou lignes**
  - • Interférences électromagnétiques
    
    • Câble de la caméra endommagé
    
    • Capteur de la caméra endommagé
  - • Éloigner le câble de la caméra des sources d'EMI, utiliser un câble blindé
    
    • Remplacer le câble Ethernet de la caméra
    
    • Remplacer la caméra
* - **La caméra n'acquiert pas pendant le cycle**
  - • Le déclencheur n'est pas configuré
    
  - • Configurer correctement le déclencheur d'acquisition
* - **La caméra ne traite pas pendant le cycle**
  - 
```
(scelta_camera)=
### *Procédure de configuration*

```{list-table}
* - **Accès à la configuration**
  - 1. Cliquer sur le bouton **Config Camera X** (où X représente le numéro de la caméra)
    2. La première page de l'assistant d'étalonnage s'ouvre, laquelle permet de modifier le paramètre **Cam Exposure**

* - **Activation du mode avancé**
  - 3. Cliquer sur le bouton **Expert** (en bas à droite)
    4. Ce mode permet d'accéder à tous les paramètres avancés de la caméra nécessaires à la configuration initiale
* - **Configuration du dispositif d'acquisition d'images**
  - 5. Dans le panneau **Expert**, cliquer sur la section **Image Acquisition** à partir de **Settings**
    6. Cliquer sur **Image Acquisition Device**
    7. Un menu s'ouvre pour sélectionner les dispositifs d'acquisition disponibles
* -  **Identification de la caméra spécifique**
  - 8. Dans le menu des appareils, sélectionner la caméra souhaitée
        - Rechercher dans la liste le numéro de série ou le modèle de la caméra
        - Exemple : "CAM-CIC-5000-20G-XXXXX" (où XXXXX est le numéro de série)
    9. Cliquer sur la caméra pour la sélectionner 
```
:::{video} ../../../../_shared/media/videos/Step2_calib.mp4
  :width: 100%
  :align: center
:::

```{tip}
**Identification du numéro de série correct**

Si plusieurs pièces ou appareils sont répertoriés :
- Le numéro de série se trouve sur une étiquette apposée sur la caméra physique
- Comparer le dernier groupe de caractères du numéro de série pour identifier la bonne caméra
- En cas de doute, déconnecter physiquement les autres caméras pour identifier celle qui est utilisée
```


```{list-table} 
* - **Sélection du format vidéo**
  - 11. Cliquer sur **Video Formats** 
    12. Dans la liste des formats disponibles, sélectionner **Generic GigEVision**
    13. Sélectionner **Mono** (monochrome) en tant que type de capteur
```


```{warning}
**Format correct requis**

Il est essentiel de sélectionner **Generic GigEVision Mono** :
- D'autres formats peuvent ne pas fonctionner ou provoquer des erreurs
- Les formats de couleur ne sont pas compatibles avec cette caméra
- Si le format n'est pas disponible, il se peut que des pilotes ou des configurations système soient manquants
```

```{list-table}
* - **Activation du système d'acquisition**
  - 14. Après avoir sélectionné le format approprié, cliquer sur **Initialize Acquisition**  
    15. Attendre que l'initialisation soit terminée (quelques secondes)
* - **Vérification du fonctionnement de l'acquisition**
  - 16. Localiser le bouton **Run** en haut à gauche de l'interface (icône de lecture)
    17. Cliquer sur **Run** à plusieurs reprises (5 à 10 fois) pour acquérir des images de test
    18. Observer la zone d'affichage de l'image :
        - L'image de la caméra sur le FlexiBowl® devrait s'afficher
        - L'image devrait se mettre à jour à chaque clic sur Run
```

(schermo_blu)=
```{warning}
**Diagnostic écran complètement bleu**

Si l'image numérisée apparaît **complètement bleue** au moins une fois pendant le test :

**Cause** : Problème de communication GigE (latence du réseau ou taille sous-optimale des paquets)

**Solution** :

1. Dans le menu supérieur, sélectionner **GigE** (ou **GigE Vision Settings**)

2. Modifier les paramètres suivants :
   - **Latency Level** (Niveau de latence)
   - **Packet Size** (Taille du paquet)

Passer aux étapes suivantes pour une configuration optimale de ces paramètres.
```

---

#### *Latency Level (Niveau de latence)*

```{note}
**Réglage de la latency**

Le paramètre **Latency Level** contrôle le tampon de communication entre la caméra et le VisionController.

**Valeurs typiques** :
- Valeur par défaut : 0
- Gamme disponible : 0-3

**Comment l'ajuster** :

1. Augmenter progressivement la valeur
2. Après chaque changement, tester l'acquisition (bouton Run) 5-10 fois
3. Si aucun autre écran bleu ne se produit, la valeur est correcte
4. Si les écrans bleus persistent, augmenter encore la taille des paquets ou essayer de modifier ce paramètre
```

#### *Packet Size (Taille du paquet)*

```{note}
**Réglage packet size**

Le paramètre **Packet Size** définit la taille des paquets de données transmis sur le réseau Ethernet.

**Valeurs typiques** :
- Valeur par défaut : 8164 octets

**Comment l'ajuster** :

1. Réduire progressivement 08000, 7000, etc.
2. Après chaque changement, tester l'acquisition (bouton Run) 5-10 fois
3. Si aucun autre écran bleu ne se produit, la valeur est correcte
4. Si les écrans bleus persistent, diminuer davantage ou essayer de modifier le paramètre Latency Level
```


---

```{list-table}
* - **Vérification finale et sauvegarde**
  - 19. Cliquer sur **Run** au moins 2 à 3 fois de suite  
    20. Vérifier que :  
      - Aucune image n'apparaît entièrement bleue ou noire
      - Les images sont mises à jour régulièrement
      - La surface du FlexiBowl® est clairement visible
      - L'éclairage est uniforme
    21. Si tous les tests sont positifs, la configuration est correcte
```

(troubleshooting_calib_cam)=
## Calibrage de la caméra

### *Motif non détecté*

```{warning}
**Erreur : « Unable to detect calibration pattern »**

Cause : Le logiciel ne peut pas identifier le motif de la grille.

**Solutions** :
- Augmenter le contraste (ajuster l'exposition ou l'éclairage)
- Vérifier que toute la grille est visible dans l'image
- Améliorer la mise au point
- Nettoyer la surface de la grille (la poussière ou les empreintes digitales peuvent interférer)
- Vérifier que la grille est correcte (carrés, pas de cercles ou d'autres motifs)
```

### *L'étalonnage est toujours «&nbsp;Bad » ou «&nbsp;Acceptable »*

```{warning}
**Qualité d'étalonnage insuffisante**

Si, malgré les réglages, l'étalonnage reste inférieur à «&nbsp;Excellent » :

1. Vérifier la distance de travail caméra-FlexiBowl® (elle doit être conforme aux calculs)
2. Vérifier que la caméra est parallèle au plan du FlexiBowl® (elle doit être parfaitement horizontale)
3. S’assurer que la caméra est stable (pas de vibrations pendant l'acquisition)
4. Vérifier que l'objectif est vissé à fond

Si le problème persiste, il peut s'agir d'un problème mécanique dans l'assemblage. Voir [Installation_Mécanique]009_Installation_Mécanique.md) pour examen.
```

### *Erreurs après un changement d'éclairage*

```{tip}
**Recalibrage après changement de backlight/toplight**

Si l'on passe du rétroéclairage à l'éclairage supérieur (ou vice versa) :

1. L'étalonnage géométrique reste valable (il n'est pas nécessaire de le refaire)
2. Il suffit de régler l'exposition de la caméra pour le nouveau type d'éclairage
3. Acquérir une image test pour vérifier que le motif est toujours clairement visible

D'une manière générale, il est conseillé de décider dès le départ du type d'éclairage à utiliser et de maintenir cette configuration.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **L'étalonnage échoue (erreur logicielle)**
  - • La grille d'étalonnage n'est pas correctement détectée
    
    • Éclairage insuffisant/excessif
    
    • Grille d'étalonnage endommagée ou sale
    
  - • Positionner la cible à plat et bien visible
    
    • Ajuster l'exposition de la caméra pour obtenir une bonne vue de la cible
    
    • Utiliser une grille d'étalonnage propre et en bon état
    
* - **Erreur de calibrage trop importante**
  - • La caméra n'est pas parfaitement orthogonale à la surface
    
    • Grille d'étalonnage non plate
    
    • Distorsion optique excessive
    
  - • Vérifier l'équerrage de la caméra à l'aide d'un niveau à bulle (tolérance ±1°)
    
    • Placer la cible sur une surface dure et plate
    
    • Vérifier la qualité de la lentille optique, la nettoyer ou la remplacer
    
* - **Les coordonnées réelles ne correspondent pas aux coordonnées mesurées**
  - • Facteur d’échelle erroné (Tile Size erroné)
    
    • Caméra déplacée après l'étalonnage
    
  - • Répéter l'étalonnage complet
    
    • Fixer solidement la caméra pour éviter tout déplacement
    
    • Vérifier les dimensions de la cible d'étalonnage conformément à la documentation
* - **L'étalonnage n'est valable qu'au centre de l'image**
  - • Distorsion optique périphérique
    
    • Étalonnage avec trop peu de points
  - • Utiliser un objectif de meilleure qualité avec une faible distorsion
    
    • Vérifier que la distance de travail est correcte
```



(troubleshooting_fb_setup)=
## Dépannage pour la section FlexiBowl® Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Le FlexiBowl® ne répond pas aux commandes du logiciel**
  - • Adresse IP non configurée ou erronée
    
    • FlexiBowl® non connecté en réseau
    
    • Le pare-feu bloque la communication
    
    • Le FlexiBowl® n'est pas allumé
  - • Vérifier et configurer correctement l'IP dans FlexiBowl® Setup
    
    • Tester la connexion par ping à partir du VisionController
    
    • Désactiver temporairement le pare-feu pour effectuer des tests
    
    • Vérifier la LED READY sur le FlexiBowl®
* - **Impossible de sauvegarder la configuration du FlexiBowl®**
  - • Disque plein

  - • Libérer de l'espace disque
 
* - **Les paramètres FlexiBowl® ne s'appliquent pas**
  - • Le bouton «&nbsp;Synchronize Parameters » n'a pas été pressé
    
    • Connexion FlexiBowl® perdue
    
    • FlexiBowl® en erreur
  - • Toujours cliquer sur «&nbsp;Synchronize Parameters » après les modifications
    
    • Vérifier la stabilité de la connexion Ethernet
    
    • Redémarrer FlexiBowl®
* - **L'assistant FlexiBowl® calcule des paramètres incorrects**
  - • Caractérisation incorrecte du composant (géométrie/comportement)
    
    • Modèle FlexiBowl® sélectionné erroné
    
    • Sens de rotation mal réglé
  - • Revoir la sélection de la géométrie (FLAT/CYLINDRICAL/COMPLEX)
    
    • Vérifier la taille du FlexiBowl® installée par rapport à celle choisie
    
    • Vérifier le sens de rotation physique et le comparer au réglage
```

(troubleshooting_hopper_setup)=
## Dépannage pour la section Hopper Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **La trémie ne s'active jamais automatiquement**
  - • La trémie n'est pas activée dans le logiciel
    • Mauvais champ de signal
    • Zone de contrôle non définie
    
    • Seuils non calibrés
    
    • Trémie non connectée électriquement
  - • Activer la case à cocher «&nbsp;Enable Hopper X »
    • Vérifier que le numéro de **signal** correspond à l'OD physiquement connecté
    • Définir la zone de contrôle dans «&nbsp;Define Area Check »
    
    • Effectuer un étalonnage des seuils avec CAPTURE vide/plein
    
    • Vérifier les branchements électriques
* - **La trémie s'active en permanence**
  - • Seuils mal calibrés
    
    • Temps de vibration insuffisant (décharge trop peu de pièces)
    
    • Paramètre «&nbsp;Steps » incorrect
  - • Répéter l'étalonnage en enlevant TOUTES les pièces pour une CAPTURE vide
    
    • Augmenter le paramètre «&nbsp;Time » (par exemple de 500 ms à 700 ms)
    
    • Recalculer les «&nbsp;Steps » en comptant les cycles réels
* - **Test hopper toujours rouge (ne s'active pas)**
  - • Trop de composants dans la zone pendant l'étalonnage
    
    • L'éclairage a changé entre l'étalonnage et le test
    
    • Reflets/ombres dans la zone de contrôle
  - • Répéter l'étalonnage avec le nombre minimum correct de pièces
    
    • Effectuer l'étalonnage et les tests avec un éclairage stable
    
    • Repositionner la zone en excluant les zones avec des reflets
* - **Test hopper toujours vert (toujours activé)**
  - • La zone de contrôle inclut des zones non pertinentes
    
    • Étalonnage du vide effectué avec les pièces présentes
    
    • Expression Builder n'est pas calculé correctement
  - • Redéfinir une zone de contrôle plus étroite
    
    • Répéter l'opération CAPTURE vide en veillant à ce que la zone soit complètement propre
    
    • Cliquer à nouveau sur AUTO pour recalculer la moyenne et l'écart-type
* - **Flux de composants non uniforme**
  - • Calcul incorrect du temps de vibration
    
    • Charge initiale trop élevée dépassant la charge utile
  - • Revoir le calcul des vibrations sur la base du remplissage initial
    
    • Vérifier que la charge ne dépasse pas la charge utile de la trémie
```

(troubleshooting_robot_setup)=
## Dépannage pour la section Robot Setup

```{warning}
**Diagnostic de panne de connexion**

Si le robot ne parvient pas à établir la connexion :

**Contrôles de base** :
1. Serveur FlexiVision One en ligne (voyant vert)
2. Adresse IP correcte dans le programme du robot
3. Port correct dans le programme du robot (identique à FlexiVision One)
4. Câble Ethernet correctement connecté

**Contrôles du réseau** :
1. Ping du VisionController au robot :
   - Ouvrir Prompt comandi sur VisionController
   - `ping <IP_ROBOT>` (ex : `ping 192.168.1.10`)
   - En cas d'échec : problème de configuration physique du réseau/IP

2. Ping du robot vers le VisionController (si la fonction ping est disponible sur le robot)

3. Vérifier que le robot et le VisionController sont sur le même sous-réseau

**Contrôles du pare-feu** :
1. Désactiver temporairement le pare-feu de Windows pour les tests
2. Si cela fonctionne, problème de pare-feu → configurer l'exception

**Vérifications des robots** :
1. Vérifier la syntaxe correcte de la commande de connexion TCP/IP (voir le manuel du robot)
2. Vérifier le délai de connexion (l'augmenter si nécessaire)
3. Vérifier les autorisations réseau sur le contrôleur du robot
```

```{note}
**Stabilisation de la connexion**

Si la connexion est fréquemment interrompue :

1. Vérifier la qualité du câble Ethernet (utiliser Cat6 à partir de)
2. Éviter les câbles trop longs
3. Vérifier qu'il n'y a pas de trafic réseau excessif sur le même sous-réseau, utiliser des programmes tels que Wireshark ou TCP dump
4. Vérifier la stabilité de l'alimentation électrique du VisionController
5. Vérifier les journaux Windows pour les erreurs de réseau

Si le problème persiste, contacter le support technique pour une analyse approfondie.
```
```{warning}
**Syntaxe des commandes incorrecte**

Si le FlexiVision One répond par «&nbsp;Invalid command » :

1. Vérifier la syntaxe exacte de la commande (sensible à la casse, soulignement, etc.)
2. Veiller à envoyer le caractère de terminaison CHR(13) après chaque commande
3. Ne pas ajouter d'espaces supplémentaires au début ou à la fin de la commande
4. Vérifier dans le journal des messages de la section Robot Setup la commande reçue par le FlexiVision One

Exemples corrects ou incorrects :
- ✅ `start_Locator` (avec trait de soulignement, minuscule)
- ❌ `Start_Locator` (majuscule incorrecte)
- ❌ `start Locator` (espace au lieu du trait de soulignement)
- ❌ `startLocator` (trait de soulignement manquant)

Voir le [protocole TCP/IP](protocollo) pour une liste complète et correcte des commandes.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Le robot ne se connecte pas à FlexiVision One**
  - • L'adresse IP du robot n'est pas sur le même sous-réseau que le VisionController
    
    • Port TCP/IP non configuré
    
    • Le pare-feu du VisionController bloque la communication
    
  - • Vérifier et configurer le sous-réseau correct dans Robot Setup
    
    • Configurer le port TCP/IP (typiquement 5000 ou second robot)
    
    • Désactiver le pare-feu pour effectuer des tests
    
    • Sélectionner le protocole compatible avec le robot dans [Protocol Setup](../QUICKSTART/SETUP/15_Protocol_Setup.md)
* - **Le robot se met dans de mauvaises positions**
  - • L'étalonnage du robot n'a pas été effectué ou n'a pas été effectué correctement
    
    • Frame/Tool robot incorrect
    
    • Offset gripper erroné
    
    • Les coordonnées ont été enregistrées de manière incorrecte lors de la configuration du modèle
  - • Effectuer un étalonnage complet du robot
    
    • Vérifier Frame et Tool sélectionnés sur le robot
    
    • Répéter l'étalonnage de Robot Pick avec les coordonnées correctes
    
    • Réapprentissage du modèle en sauvegardant des coordonnées précises
* - **Impossible de se connecter au robot**
  - • Robot éteint
    
    • Câble Ethernet pas connecté
    
    • Robot et VisionController sur des sous-réseaux différents

  - • Mettre le robot en marche et l'amener en mode automatique
    
    • Vérifier la connexion physique Ethernet robot-VisionController
    
    • Configurer le robot et le VisionController sur le même réseau
```

