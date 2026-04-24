# **2 FlexiBowl® et 2 Caméras**

Cette section décrit les configurations disponibles lorsque l'on souhaite fonctionner avec **deux FlexiBowl®** et **deux caméras** gérés par un seul VisionController FlexiVision One.

---

## Vue d'ensemble de la configuration

Dans une configuration **2 FlexiBowl® + 2 Caméras**, le système comprend deux stations d'alimentation et de vision indépendantes, toutes deux gérées par le même VisionController. Chaque station est composée de:

* 1 FlexiBowl®
* 1 Caméra avec optique dédiée
* 1 Hopper (optionnel, si présent)

Les deux stations communiquent avec le VisionController via un **Switch réseau**.

```{important}
Le **Switch** est un composant **obligatoire** dans toutes les configurations multi-dispositif. Sans lui, il n'est pas possible de connecter simultanément plusieurs FlexiBowl® et plusieurs caméras au VisionController. Pour les spécifications techniques et les codes de commande, consulter la section [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Cette configuration prend en charge deux variantes opérationnelles, selon le nombre de robots disponibles dans l'installation:
| | **Variante A** | **Variante B** |
|---|---|---|
| **Robot** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Caméras** | 2 | 2 |
| **Logique opérationnelle** | Le robot atteint les deux stations | Chaque robot est dédié à une station |
| **Switch requis** | Oui | Oui |


---

## Variante A — 1 Robot, 2 FlexiBowl®

![Vue d'ensemble Système 2FB2CAM1Robot](../../../../_shared/media/images/2FB2CAM1R.png)

Dans cette variante, un **seul robot** opère sur les deux stations. Le robot est positionné de manière à pouvoir atteindre la zone de picking de chaque FlexiBowl®, en alternant la prise entre les deux stations sur la base des commandes reçues.

Chaque station gère sa propre recette indépendante. Sur chaque station, il est possible de configurer une application de type **Standard** ou **Mix**, avec des modèles de composants différents au sein de la même recette.

| Paramètre | Valeur |
|---|---|
| FlexiBowl® | 2 |
| Caméras | 2 |
| Robot | 1 |
| Switch requis | **Oui** |

```{important}
**Recette de base et gestion des recettes**

Comme pour la configuration simple, dans une configuration 2FB + 2CAM le processus part également de la création d'une **recette de base unique**, qui contient les setup hardware et la calibration de la caméra pour l'ensemble du système. Cette recette de base est ensuite **dupliquée** pour chaque station: chaque duplicata constitue la recette opérationnelle de cette station, dans laquelle sont créés les modèles des pièces (jusqu'à 8 par station).

Pour cette raison, il est fondamental que l'association entre les dispositifs soit configurée correctement dès le début:

* **Caméra 1** → FlexiBowl® 1 (+ Hopper 1, si présent)
* **Caméra 2** → FlexiBowl® 2 (+ Hopper 2, si présent)

Une association incorrecte en phase de setup se répercuterait sur toutes les recettes dérivées, compromettant la reconnaissance des pièces et le bon fonctionnement de l'ensemble du système.
```
---

## Variante B — 2 Robots, 2 FlexiBowl®

![Vue d'ensemble Système 2FB2CAM2Robot](../../../../_shared/media/images/2FB2CAM2R.png)

Dans cette variante, chaque robot est dédié à une seule station: le **Robot 1** effectue le picking sur le FlexiBowl® 1, le **Robot 2** effectue le picking sur le FlexiBowl® 2. Les deux cellules sont indépendantes et ne se chevauchent pas.

Dans cette variante également, chaque station prend en charge des applications de type **Standard** et **Mix**.

| Paramètre | Valeur |
|---|---|
| FlexiBowl® | 2 |
| Caméras | 2 |
| Robot | 2 |
| Switch requis | **Oui** |

```{tip}
Cette variante garantit une productivité maximale, avec les deux cellules qui fonctionnent en parallèle et de manière complètement autonome.
```

```{important}
**Recette de base et gestion des recettes**

Comme pour la configuration simple, dans une configuration 2FB + 2CAM le processus part également de la création d'une **recette de base unique**, qui contient les setup hardware et la calibration de la caméra pour l'ensemble du système. Cette recette de base est ensuite **dupliquée** pour chaque station: chaque duplicata constitue la recette opérationnelle de cette station, dans laquelle sont créés les modèles des pièces (jusqu'à 8 par station).

Pour cette raison, il est fondamental que l'association entre les dispositifs soit configurée correctement dès le début:

* **Caméra 1** → FlexiBowl® 1 (+ Hopper 1, si présent)
* **Caméra 2** → FlexiBowl® 2 (+ Hopper 2, si présent)

Une association incorrecte en phase de setup se répercuterait sur toutes les recettes dérivées, compromettant la reconnaissance des pièces et le bon fonctionnement de l'ensemble du système.
```

---

## Composants nécessaires

### Kit de base FlexiVision One

Le **kit de base FlexiVision One** (fourni avec le système) inclut déjà tout le nécessaire pour la **première station** (caméra, optique, câbles, grille de calibration). Il n'est pas nécessaire d'acheter un second kit complet pour la deuxième station.

### Kit Caméra Supplémentaire

Pour la deuxième station, il suffit d'acheter le **Kit Caméra Supplémentaire**, disponible dans une version spécifique pour chaque taille de FlexiBowl®. Le kit inclut:

* 1 Caméra
* 1 Optique dédiée à la taille FlexiBowl®
* 1 Grille de calibration
* 1 Câble alimentation caméra
* 2 Câbles Ethernet

Sélectionner le kit en fonction de la taille du **deuxième** FlexiBowl®:

| Taille FlexiBowl® | Code Kit Caméra Supplémentaire | Optique incluse |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |
```{note}
Si les deux stations utilisent des FlexiBowl® de **tailles différentes**, le Kit Caméra Supplémentaire doit être sélectionné en fonction de la taille du FlexiBowl® de la deuxième station. La première station est déjà couverte par le kit de base.
```

### Switch

Le Switch est toujours nécessaire dans les configurations multi-dispositif. Pour le code, les spécifications électriques et physiques, consulter la section dédiée:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Câblage

Le schéma de câblage est identique pour les deux variantes: tous les dispositifs de terrain (FlexiBowl®, caméras, robots) se connectent au **Switch**, et le Switch se connecte au **VisionController** via un seul port Ethernet. La différence entre la Variante A et la Variante B concerne exclusivement le nombre de robots connectés au Switch.
```{important}
Le Switch dispose de **8 ports Ethernet**. Vérifier que le nombre total de dispositifs à connecter ne dépasse pas la capacité disponible, en tenant compte de tous les FlexiBowl®, caméras et robots présents.
```

### Schéma de connexion

| Dispositif | Connexion |
|---|---|
| FlexiBowl® 1 | Port Ethernet → Switch |
| FlexiBowl® 2 | Port Ethernet → Switch |
| Caméra 1 | Câble Ethernet → Switch |
| Caméra 2 | Câble Ethernet → Switch |
| Robot 1 | Port Ethernet → Switch |
| Robot 2 *(seulement Variante B)* | Port Ethernet → Switch |
| **Switch** | **Port Ethernet → VisionController** |
```{tip}
Vérifier qu'une adresse IP unique est attribuée à chaque dispositif dans le même subnet. Les ports TCP/IP utilisés par le VisionController pour les deux stations sont configurables: par défaut **FB1 → 4001**, **FB2 → 4002**. Consulter la section [Protocole de Communication Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) pour les détails.
```

### Ports Switch occupés par variante

| Port Switch | Variante A (1 Robot) | Variante B (2 Robots) |
|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | Caméra 1 | Caméra 1 |
| 4 | Caméra 2 | Caméra 2 |
| 5 | Robot 1 | Robot 1 |
| 6 | VisionController | Robot 2 |
| 7 | — | VisionController |
| 8 | — | — |

```{note}
**Câblage des composants individuels**

Les procédures de connexion physique de chaque composant (FlexiBowl®, caméra, hopper, robot) sont décrites intégralement dans la section [Câblage et Connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md). Dans une configuration 2FB + 2CAM, les mêmes opérations doivent simplement être exécutées **deux fois** — une pour chaque station — avec pour seule différence que chaque dispositif se connecte au **Switch** au lieu d'être directement connecté au VisionController.
```
```{important}
**Association dispositifs dans le logiciel**

FlexiVision One est capable de gérer simultanément toutes les stations, mais il est fondamental que l'association entre les dispositifs soit configurée correctement dans le logiciel. S'assurer d'associer:

* **Caméra 1** → FlexiBowl® 1 (+ Hopper 1, si présent)
* **Caméra 2** → FlexiBowl® 2 (+ Hopper 2, si présent)

Une association incorrecte compromettrait la localisation des pièces et le bon fonctionnement de l'ensemble du système.
```

**→ [Configuration Initiale du Système](../QUICKSTART/SETUP/13_setup.md)**

