(cablaggio)=
# **Câblage et connexions**
  
![Pan Coll](../../../../_shared/media/images/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **De**
  - **Vers**
  - **Branchement**

* - Réseau électrique
  - FlexiBowl®
  - Alimentation 110/220 Vdc

* - Réseau électrique
  - Robot
  - Alimentation conformément aux spécifications du robot en votre possession

* - Réseau électrique
  - Caméra
  - Alimentation 24 Vdc

* - Réseau électrique
  - Dispositif d'éclairage (lumière)
  - Alimentation 24 Vdc

* - Réseau électrique
  - Contrôleur de trémie
  - Alimentation 110/220 Vdc

* - Contrôleur de trémie
  - Trémie
  - Alimentation et signal

* - Robot
  - Contrôleur de trémie
  - E/S numériques

* - VisionController
  - Caméra
  - Ethernet TCP

* - VisionController
  - FlexiBowl®
  - Ethernet TCP

* - VisionController
  - Robot
  - Ethernet TCP
```

## Assistant de câblage

```{list-table} 
:header-rows: 1

* - **Étape**
  - **Action**
* - 1
  - Brancher l'alimentation électrique du FlexiBowl®.  
    [🔗 Reportez-vous au manuel pour connaître les spécifications de l'alimentation électrique](https://www.flexibowl.com/wp-content/uploads/2026/04/Manuale-Utente-Flexibowl_IT_Rev2.9.pdf)
* - 2
  - Brancher le [câble d'alimentation Hirose 24V](cavo) à la caméra.
* - 3
  - Connecter le FlexiBowl® au VisionController à l'aide d'un câble Ethernet.
* - 4
  - Connecter la caméra au VisionController (PC) à l'aide d'un câble Ethernet.
* - 5
  - Connecter le robot au VisionController à l'aide d'un câble Ethernet.
* - 6
  - Raccorder l'air comprimé au FlexiBowl®.  
    [🔗 Se référer au manuel pour les spécifications pneumatiques](https://www.flexibowl.com/wp-content/uploads/2026/04/Manuale-Utente-Flexibowl_IT_Rev2.9.pdf)
* - 7
  - Si présent, brancher la trémie à son contrôleur
* - 8
  - Si présent, brancher le robot au contrôleur de la trémie (E/S numériques)
* - 9 
  - Si présent, alimenter le contrôleur de la trémie (110/220 V selon l'option choisie lors de l'achat de la base vibrante de la trémie)
* - 10
  - Allumer l'interrupteur AC du FlexiBowl® (position « I »). Le voyant READY est **allumé**.
* - 11
  - Allumer tous les autres appareils
```
(cablaggio_illuminatore)=
## Câblage du dispositif d'éclairage

![Pin Toplight](../../../../_shared/media/images/pin_toplight1.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Paramètre
  - Exigence / Action
* - **Tension**
  - 24V DC (±10 %). Tension minimale de fonctionnement : 20V DC sur l'entrée lumière.
* - **Connecteur**
  - M12 mâle. 
    :::{note}
      Pour connecter le toplight, il est également possible d'acheter son [câble d'alimentation](cavoalimtoplight). 
    :::
* - **Brochage du connecteur**
  - Broche 1 : +24V (marron) — Broche 3 : GND (bleu) — Broche 4 : STROBE PNP (noir)
* - **Mode STROBE (PNP)**
  - De 5V à 24V pour une activation à 100 %. De 0V à 1V pour une extinction à 100 %.
* - **Mode CONTINU**
  - Broche 1 (+24V) et Broche 3 (GND) connectées ; Broche 4 (PNP) connectée à la Broche 1.
* - **Chute de tension (câble M12, 10 m)**
  - 1,15V @ 5A — 2,3V @ 10A — 3,5V @ 15A — 4,6V @ 20A (max 20A)
* - **Blindage**
  - Utiliser des câbles blindés pour réduire les interférences électromagnétiques (EMI).
```
```{warning}
**Sécurité électrique**

- Respecter les tensions d'alimentation et les bornes de raccord indiquées.
- Ne pas modifier ou démonter le produit.
- Ne pas brancher ou nettoyer l'appareil lorsqu'il est sous tension.
- Ne pas regarder directement la source lumineuse.
```



