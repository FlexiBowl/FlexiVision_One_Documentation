(cablaggio)=
# **Câblage et Connexions**
image d'ensemble des connexions électriques 
type:  
![Pan Coll](../../../../_shared/media/images/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **De**
  - **À**
  - **Connexion**

* - Réseau électrique
  - FlexiBowl
  - Alimentation 110/220 Vdc

* - Réseau électrique
  - Robot
  - Alimentation selon les spécifications du robot en votre possession

* - Réseau électrique
  - Caméra
  - Alimentation 24 Vdc

* - Réseau électrique
  - Illuminateur (lumière)
  - Alimentation 24 Vdc

* - Réseau électrique
  - Contrôleur Hopper
  - Alimentation 110/220 Vdc

* - Contrôleur Hopper
  - Hopper
  - Alimentation et signal

* - Robot
  - Contrôleur Hopper
  - I/O Numériques

* - VisionController
  - Caméra
  - Ethernet TCP

* - VisionController
  - FlexiBowl
  - Ethernet TCP

* - VisionController
  - Robot
  - Ethernet TCP
```

## Procédure guidée de câblage

```{list-table} 
:header-rows: 1

* - **Étape**
  - **Action**
* - 1
  - Connecter l'alimentation du FlexiBowl®.  
    [🔗 Se référer au manuel pour les spécifications d'alimentation](http://link-al-manuale.com)
* - 2
  - Connecter le [câble d'alimentation Hirose 24V](cavo) à la Caméra.
* - 3
  - Connecter le FlexiBowl® au VisionController avec un câble Ethernet.
* - 4
  - Connecter la Caméra au VisionController (PC) avec un câble Ethernet.
* - 5
  - Connecter le Robot au VisionController avec un câble Ethernet.
* - 6
  - Connecter l'air comprimé au FlexiBowl®.  
    [🔗 Se référer au manuel pour les spécifications pneumatiques](http://link-al-manuale.com)
* - 7
  - Si présent, connecter le hopper à son contrôleur
* - 8
  - Si présent, connecter le robot au contrôleur du hopper (I/O Numériques)
* - 9 
  - Si présent, alimenter le contrôleur du hopper (110/220 V selon l'option choisie lors de l'achat de la base vibrante du hopper)
* - 10
  - Allumer l'interrupteur AC du FlexiBowl® (position "I"). La LED READY est **ON**.
* - 11
  - Allumer tous les autres dispositifs
```
(cablaggio_illuminatore)=
## Câblage illuminateur

![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Exigence / Action
* - **Tension**
  - 24V DC (±10%). Tension minimale de fonctionnement: 20V DC sur l'entrée lumière.
* - **Connecteur**
  - M12 Male. 
    :::{note}
      Pour connecter le toplight, il est également possible d'acheter son [câble d'alimentation](cavoalimtoplight). 
    :::
* - **Pinout connecteur**
  - Pin 1: +24V (marron) — Pin 3: GND (bleu) — Pin 4: STROBE PNP (noir)
* - **Mode STROBE (PNP)**
  - De 5V à 24V pour allumage à 100%. De 0V à 1V pour extinction à 100%.
* - **Mode CONTINU**
  - Pin 1 (+24V) et Pin 3 (GND) connectés; Pin 4 (PNP) connecté à Pin 1.
* - **Chute de tension (câble M12, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Blindage**
  - Utiliser des câbles blindés pour réduire les interférences électromagnétiques (EMI).
```
```{warning}
**Sécurité électrique**

- Respecter les tensions d'alimentation et les bornes de connexion indiquées.
- Ne pas modifier ni démonter le produit.
- Ne pas connecter ou nettoyer l'appareil lorsqu'il est sous tension.
- Ne pas regarder directement la source lumineuse.
```



