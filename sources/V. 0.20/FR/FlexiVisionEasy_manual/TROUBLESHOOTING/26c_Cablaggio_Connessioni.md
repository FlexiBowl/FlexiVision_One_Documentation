# **Câblage et connexions**
(troubleshooting_alimentazione)=
## Problèmes d'alimentation du FlexiBowl

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **La LED READY ne s'allume pas**  
  - • L'alimentation n'est pas bien branchée  
    
    • Interrupteur AC en position «&nbsp;O&nbsp;» au lieu de «&nbsp;I »  
    
    • Câble d’alimentation endommagé  
    
    • Fusibles grillés à l'intérieur du panneau avant  
  - • Vérifier la connexion électrique conformément au manuel FlexiBowl®  
    
    • Amener l’interrupteur en position «I» (ON)  
     
    • Inspecter le câble pour vérifier qu'il ne soit pas endommagé et le remplacer si nécessaire  
    
    • Contactez l’assistance technique pour le remplacement du fusible  
* - Le **FlexiBowl® s'éteint aléatoirement**  
  - • Connexion électrique desserrée  
    
    • Interférences électriques  
    
  - • Serrer les connexions électriques  
    
    • Brancher à une ligne dédiée avec filtre EMI  

```
(troubleshooting_ethernet)=
## Problèmes de connexion Ethernet

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **FlexiBowl® ne communique pas avec le VisionController**  
  - • FlexiBowl® n'est pas allumé (LED READY éteinte)  
    • Le câble Ethernet n'est pas correctement connecté au FlexiBowl® et/ou au VisionController  
    • Le câble Ethernet est endommagé  
    • Mauvaise adresse IP  
    • Le FlexiBowl® et le VisionController se trouvent sur des sous-réseaux différents  
    • Le pare-feu bloque la communication  
    • Le port Ethernet du VisionController est défectueux  
  - • Vérifier l’allumage de la LED READY sur le FlexiBowl®  
    • Vérifier la connexion physique du câble Ethernet des deux côtés  
    • Tester le câble avec un testeur de câble ou le remplacer  
    • Vérifier la configuration IP dans [FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md)  
    • Configurer le FlexiBowl® et le VisionController dans le même réseau (par exemple : 192.168.1.x)  
    • Désactiver temporairement le pare-feu pour les tests  
    • Essayer un autre port Ethernet du VisionController  
* - **Connexion intermittente**  
  - • Câble trop long (> 100 m)  
    • Connecteur RJ45 endommagé ou mal serti  
    • Interférences électromagnétiques  
  - • Réduire la longueur du câble en dessous de 100 m ou utiliser un interrupteur intermédiaire  
    • Remplacer les connecteurs ou le câble complet  
    • Utiliser un câble blindé (STP) loin des sources d'EMI  
```
(troubleshooting_pneumatica)=
## Problèmes pneumatiques (air comprimé)

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Le Flip ne fonctionne pas ou l'impulsion est très faible**  
  - • L'air comprimé n'est pas connecté  
    • Le tuyau pneumatique est endommagé ou obstrué  
    • Le régulateur de pression est fermé ou est au minimum  
    
    • Pression insuffisante (< 5 bar)  
    
    
    
    • Fuites dans le circuit pneumatique  
    
    
  - • Raccorder l'air comprimé à la connexion FlexiBowl® (voir manuel)  

    • Vérifier que le tuyau ne soit pas plié ou obstrué, le remplacer si nécessaire  
    • Ouvrir le régulateur de pression sur le panneau de contrôle  
    
    • Augmenter la pression à 5-6 bars  
    
    
    
    • Inspecter les raccords avec de l'eau savonneuse, les resserrer ou les remplacer  
    
    
* - **L'air-blow ne **fonctionne** pas**  
  - • Le FlexiBowl® n'est pas configuré avec l'option Air-Blow  

    • Déviateurs d’air non alimentés à l’extérieur  

    • Régulateurs de flux fermés  

    • Pression d’ait insuffisante  
  
    
    • Électrovanne défectueuse  
  - • Vérifier que le FlexiBowl® commandé comporte l'option Blow Test True dans la fiche de production  

    • Vérifier que l'alimentation pneumatique externe est présente (tuyau fourni)  

    • S'il y a plusieurs déviateurs d'air, vérifier que le régulateur de débit situé sur le côté du FlexiBowl® est réglé au-dessus de zéro  

    • Vérifier la pression d'air (5-6 bar)  

    
    • suivre les [instructions]  
```
(troubleshooting_connessione_camera)=
## Problèmes de connexion de la caméra

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - La **caméra n'est pas détectée par le VisionController**  
  - • Le câble Ethernet de la caméra n'est pas connecté  
    
    • Caméra connectée au port non-POE du VisionController  
    

    
    • L'adresse IP de la caméra est en conflit avec celles d'autres appareils du même sous-réseau  
    • Port POE du VisionController défectueux  
  - • Vérifier la connexion physique du câble de la caméra  
    • Connecter la caméra UNIQUEMENT au port POE du VisionController  
    • Réinitialiser l'IP de la caméra ou configurer une IP statique unique  
    • Essayer un autre port POE du VisionController  
* - **Image de la caméra noire ou absente**  
  - • Dispositif d’éclairage éteint  
    • Exposition de la caméra trop faible  
    • Objectif avec capuchon de protection non retiré  
    • Objectif non installé  
    • Caméra non alimentée (POE non actif)  
    
     
    • Caméra défectueuse  
  - • Vérifier que le dispositif d’éclairage est allumé  
    • Augmenter l'exposition dans [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
    • Retirer le capuchon de protection de l'objectif  
    • Installer l'objectif avec la longueur focale correcte  
    • Vérifier que la LED de la caméra est allumée (indicateur POE actif)  
    • Remplacer la caméra

* - **La caméra se déconnecte de façon aléatoire**  
  - • Alimentation POE insuffisante (puissance < demande de la caméra)  
    
    • Câble endommagé  
    
    • Surchauffe de la caméra  
    
    • Port POE endommagé  
  - • Vérifier la puissance POE disponible  
    • Remplacer le câble Ethernet  
    
    • Améliorer la ventilation de la zone caméra  
    
    • Remplacer le commutateur POE ou le port du VisionController  
```
(troubleshooting_connessione_toplight)=
## Problèmes de connexion du Toplight
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Le toplight ne s'allume pas**
  - • L'alimentation 24V DC n'est pas connectée
    
    • Câble d’alimentation endommagé
    
    • Tension incorrecte (≠ 24V)
    
    • Toplight en panne
    
    • Fusible/protection déclenchée
  - • Vérifier la connexion de l'alimentation 24V DC
    
    • Inspecter le câble, le remplacer s'il est endommagé
    
    • Mesurer la tension à l'aide d'un multimètre, elle doit être de 24V DC (±10 %)
    
    • Remplacer le toplight
    
    • Vérifier les protections dans le tableau électrique
* - **Luminosité variable du toplight**
  - • Alimentation électrique instable
    
    • Connexions desserrées
    
    • Alimentation électrique sous-dimensionnée
    
    • Toplight en fin de vie
  - • Vérifier la stabilité de la tension d'alimentation
    
    • Serrer toutes les connexions électriques
    
    • Vérifier la consommation de courant par rapport à la capacité du bloc d’alimentation
    
    • Remplacer le toplight
* - **Toplight se surchauffe**
  - • Ventilation insuffisante
    
    • Courant excessif
    
    • Cycle de fonctionnement continu à 100 %
  - • Améliorer la circulation de l'air autour du toplight
    
    • Vérifier que la consommation de courant ne dépasse pas les spécifications
    
    • Mettre en œuvre un cycle de travail intermittent si possible
```
(troubleshooting_multi)=
## Problèmes de Configurations Multi-appareils
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions
* - **Système avec 2-3 FlexiBowl® : un seul communique**  
  - • FlexiBowl® éteint  
    • Adresses IP en double  
    • Câbles croisés  
  - • Vérifier que le FlexiBowl® est allumé  
    • Attribuer des IP uniques à chaque FlexiBowl® (par ex : 192.168.1.10, .11, .12)  
    • Vérifier le câblage en étoile (pas de guirlande)  
* - **Système avec 2-3 caméras : une seule acquiert**  
  - • Alimentation électrique insuffisante  
    • Adresses IP des caméras contradictoires  
  - • Vérifier que l'alimentation électrique est comprise entre 6 et 26 V  
    • Configurer une IP statique unique pour chaque caméra  
    • Activer toutes les caméras dans [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
* - **Système avec 2-3 trémies : contrôle incorrect**  
  - • Les trémies ne sont pas activées individuellement dans le logiciel  
    • Alimentation électrique incorrecte  
    • Contact robot incorrect  
  - • Activer chaque trémie dans [Hopper Setup](../QUICKSTART/SETUP/13b_Hopper_Setup.md)  
    • Vérifier l'alimentation électrique  
    • Vérifier le contact avec le robot  
```



