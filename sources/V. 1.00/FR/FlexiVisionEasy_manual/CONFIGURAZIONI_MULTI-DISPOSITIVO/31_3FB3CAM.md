# **3 FlexiBowl® et 3 Caméras**

Cette section décrit les configurations disponibles lorsque vous souhaitez faire fonctionner **trois FlexiBowl®** et **trois caméras** au sein d'un même îlot de prélèvement, géré par un seul VisionController FlexiVision One.

---

## Aperçu de la configuration

Dans une configuration **3 FlexiBowl® + 3 caméras**, le système comprend trois stations d'alimentation et de vision indépendantes, toutes contrôlées par le même VisionController. Chaque station est composée des éléments suivants&nbsp;:

* 1 FlexiBowl®
* 1 Caméra avec optique dédiée
* 1 Trémie (optionnelle, si présente)

Les trois stations communiquent avec le VisionController par l'intermédiaire d'un **commutateur de réseau**.
```{important}
Le **Switch** est un composant **obligatoire** dans toutes les configurations multi-appareils. Sans lui, il n'est pas possible de connecter simultanément plusieurs FlexiBowl® et plusieurs caméras au VisionController. Pour les spécifications techniques et les codes de commande, consultez la section [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Cette configuration permet trois variantes de fonctionnement, en fonction du nombre de robots disponibles dans l'usine :

| | **Variante A** | **Variante B** | **Variante C** |
|---|---|---|---|
| **Robot** | 1 | 2 | 3 |
| **FlexiBowl®** | 3 | 3 | 3 |
| **Caméras** | 3 | 3 | 3 |
| **Logique de fonctionnement** | Le robot atteint les trois stations | Premier robot sur un FlexiBowl®, deuxième robot sur deux FlexiBowl® | Chaque robot est dédié à une station |
| **Commutateur requis** | Oui | Oui | Oui |
---

## Variante A — 1 Robot, 3 FlexiBowl®

![Aperçu du système 3FB3CAM1Robot](../../../../_shared/media/images/3FB3CAM1R.png)

Un **seul robot** opère sur les trois stations. Le robot doit être positionné de manière à pouvoir atteindre la zone de prélèvement de chaque FlexiBowl®. Le VisionController gère les trois stations de manière indépendante, chacune ayant sa propre recette et son propre canal de communication TCP/IP.

Chaque station prend en charge les applications **Standard** ou **Mix**.

| Paramètre | Valeur |
|---|---|
| FlexiBowl® | 3 |
| Caméras | 3 |
| Robot | 1 |
| Commutateur requis | **Oui** |


```{important}
**Recette de base et gestion des recettes**

Comme pour la configuration simple, dans une configuration 3FB + 3CAM, le processus commence par la création d'une **recette de base unique**, qui contient la configuration matérielle et l'étalonnage de la caméra pour l'ensemble du système. Cette recette de base est ensuite **dupliquée** pour chaque station : chaque duplicata constitue la recette de fonctionnement de cette station, à l'intérieur de laquelle les modèles de pièces (jusqu'à 8 par station) sont créés.

Il est donc essentiel que l'association entre les appareils soit configurée correctement dès le départ :

* **Caméra 1** → FlexiBowl® 1 (+ Trémie 1, si présente)
* **Caméra 2** → FlexiBowl® 2 (+ Trémie 2, si présente)
* **Caméra 3** → FlexiBowl® 3 (+ Trémie 3, si présente)

Une association incorrecte lors de la configuration affecterait toutes les recettes dérivées, compromettant la reconnaissance des pièces et le bon fonctionnement de l'ensemble du système.
```
---

## Variante B — 2 Robots, 3 FlexiBowl®

![Aperçu du système 3FB3CAM2Robot](../../../../_shared/media/images/3FB3CAM2R.png)

Dans cette variante, **deux robots** se partagent les trois stations. Le premier robot fera le prélèvement sur un seul FlexiBowl®, le second sur les deux autres FlexiBowl®. La répartition de la charge entre les robots est définie par la logique du programme du robot et la disposition physique de l'usine. 

Chaque station prend en charge les applications **Standard** ou **Mix**.

| Paramètre | Valeur |
|---|---|
| FlexiBowl® | 3 |
| Caméras | 3 |
| Robot | 2 |
| Commutateur requis | **Oui** |

```{important}
**Recette de base et gestion des recettes**

Comme pour la configuration simple, dans une configuration 3FB + 3CAM, le processus commence par la création d'une **recette de base unique**, qui contient la configuration matérielle et l'étalonnage de la caméra pour l'ensemble du système. Cette recette de base est ensuite **dupliquée** pour chaque station : chaque duplicata constitue la recette de fonctionnement de cette station, à l'intérieur de laquelle les modèles de pièces (jusqu'à 8 par station) sont créés.

Il est donc essentiel que l'association entre les appareils soit configurée correctement dès le départ :

* **Caméra 1** → FlexiBowl® 1 (+ Trémie 1, si présente)
* **Caméra 2** → FlexiBowl® 2 (+ Trémie 2, si présente)
* **Caméra 3** → FlexiBowl® 3 (+ Trémie 3, si présente)

Une association incorrecte lors de la configuration affecterait toutes les recettes dérivées, compromettant la reconnaissance des pièces et le bon fonctionnement de l'ensemble du système.
```
---

## Variante C — 3 Robots, 3 FlexiBowl®

![Aperçu du système 3FB3CAM3Robot](../../../../_shared/media/images/3FB3CAM3R.png)

Chaque robot est dédié à une seule station : productivité maximale avec les trois cellules fonctionnant en parallèle et de manière totalement indépendante.

Chaque station prend en charge les applications **Standard** ou **Mix**.

| Paramètre | Valeur |
|---|---|
| FlexiBowl® | 3 |
| Caméras | 3 |
| Robot | 3 |
| Commutateur requis | **Oui** |

```{tip}
La variante C garantit les meilleures performances globales. Chaque cellule est totalement autonome et ne dépend pas de la disponibilité des autres.
```
```{important}
**Recette de base et gestion des recettes**

Comme pour la configuration simple, dans une configuration 3FB + 3CAM, le processus commence par la création d'une **recette de base unique**, qui contient la configuration matérielle et l'étalonnage de la caméra pour l'ensemble du système. Cette recette de base est ensuite **dupliquée** pour chaque station : chaque duplicata constitue la recette de fonctionnement de cette station, à l'intérieur de laquelle les modèles de pièces (jusqu'à 8 par station) sont créés.

Il est donc essentiel que l'association entre les appareils soit configurée correctement dès le départ :

* **Caméra 1** → FlexiBowl® 1 (+ Trémie 1, si présente)
* **Caméra 2** → FlexiBowl® 2 (+ Trémie 2, si présente)
* **Caméra 3** → FlexiBowl® 3 (+ Trémie 3, si présente)

Une association incorrecte lors de la configuration affecterait toutes les recettes dérivées, compromettant la reconnaissance des pièces et le bon fonctionnement de l'ensemble du système.
```
---

## Composants nécessaires

### *Kit de base FlexiVision One*

Le **kit de base FlexiVision One** (fourni avec le système) comprend déjà tout ce qui est nécessaire pour la **première station** (caméra, optique, câbles, grille d'étalonnage), y compris le VisionController. Il n'est pas nécessaire d'acheter un deuxième kit complet pour les stations supplémentaires.

### *Kit de caméra supplémentaire (× 2)*

Pour les stations 2 et 3, il est nécessaire d'acheter **deux kits de caméras supplémentaires**, un pour chaque station, en sélectionnant le code correspondant à la taille du FlexiBowl® de chaque station. Le kit comprend :

* 1 Caméra
* 1 Optique dédiée à la taille FlexiBowl®
* 1 Grille d'étalonnage
* 1 Câble d'alimentation de la caméra
* 2 Câbles Ethernet

Sélectionner le kit en fonction de la taille du FlexiBowl® de chaque station supplémentaire :

| Taille FlexiBowl® | Code Kit de caméra supplémentaire | Optique incluse |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optique |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optique |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optique |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optique |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optique |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optique |

```{note}
Si les stations supplémentaires utilisent des FlexiBowl® de tailles différentes, acheter un kit pour chaque taille.  
 Par exemple, pour une configuration avec FB500 + FB650 + FB800, le kit de base couvre la première station, tandis que pour la deuxième et la troisième station, il faut commander respectivement GM002004 et GM002006.
```

### *Switch*

Le Switch est toujours nécessaire dans les configurations multi-appareils. Pour le code, les spécifications électriques et physiques, voir la section dédiée :

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Câblage

Dans la **variante A** (1 robot), tous les appareils de terrain (FlexiBowl®, caméras, robot) se connectent au **Switch**, et le Switch se connecte au **VisionController** via un seul port Ethernet. Le nombre total de connexions est compris dans les 8 ports disponibles sur le Switch.

À partir de la **variante B**, le nombre total d'appareils dépasse les ports disponibles sur le Switch.   
Dans ces cas, un port du VisionController est utilisé pour le connecter au Switch, tandis que les ports libres restants du VisionController accueillent les appareils qui ne trouvent pas leur place sur le Switch :

- Dans la **variante B** (2 robots), le **FlexiBowl® 3** se connecte directement à un port libre du VisionController.
- Dans la **variante C** (3 robots), le **FlexiBowl® 3** et la **Caméra 3** se connectent directement aux ports libres du VisionController.

```{important}
Le Switch dispose de **8 ports Ethernet**. À partir de la variante B, il n'est plus possible de connecter tous les appareils exclusivement via le Switch : les appareils supplémentaires doivent être connectés directement aux ports Ethernet libres du VisionController, comme indiqué dans les tableaux ci-dessous.
```
:::{note}
Il est possible de choisir librement quels appareils connecter au VisionController. L'important est de toujours laisser un port libre pour connecter le VisionController au Switch
:::

### *Schéma de connexion*

| Appareil | Variante A (1 Robot) | Variante B (2 Robots) | Variante C (3 Robots) |
|---|---|---|---|
| FlexiBowl® 1 | → Switch | → Switch | → Switch |
| FlexiBowl® 2 | → Switch | → Switch | → Switch |
| FlexiBowl® 3 | → Switch | **→ VisionController (port libre)** | **→ VisionController (port libre)**  |
| Caméra 1 | → Switch | → Switch | → Switch |
| Caméra 2 | → Switch | → Switch | → Switch |
| Caméra 3 | → Switch | → Switch | **→ VisionController (port libre)**  |
| Robot 1 | → Switch | → Switch | → Switch |
| Robot 2 | — | → Switch | → Switch |
| Robot 3 | — | — | → Switch |
| **Switch** | **→ VisionController** | **→ VisionController** | **→ VisionController** |

:::{note}
Il est possible de choisir librement quels appareils connecter au VisionController. L'important est de toujours laisser un port libre pour connecter le VisionController au Switch
:::

```{tip}
Veiller à ce qu'une adresse IP unique soit attribuée à chaque appareil dans le même sous-réseau.  
 Les ports TCP/IP utilisés par le VisionController pour les trois stations sont configurables : par défaut **FB1 → 4001**, **FB2 → 4002**, **FB3 → 4003**.  
 Consultez la section [Protocole de communication Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) pour plus de détails.
```
### *Ports Switch occupés par variante*

| Port Switch | Variante A (1 Robot) | Variante B (2 Robots) | Variante C (3 Robots) |
|---|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | FlexiBowl® 3 | Caméra 1 | Caméra 1 |
| 4 | Caméra 1 | Caméra 2 | Caméra 2 |
| 5 | Caméra 2 | Caméra 3 | Robot 1 |
| 6 | Caméra 3 | Robot 1 | Robot 2 |
| 7 | Robot 1 | Robot 2 | Robot 3 |
| 8 | VisionController | VisionController | VisionController |

### *Ports VisionController occupés par variante*

| Port VisionController | Variante A (1 Robot) | Variante B (2 Robots) | Variante C (3 Robots) |
|---|---|---|---|
| 1 | Switch | Switch | Switch |
| 2 | — | FlexiBowl® 3 | FlexiBowl® 3 |
| 3 | — | — | Caméra 3 |

:::{note}
Il est possible de choisir librement quels appareils connecter au VisionController. L'important est de toujours laisser un port libre pour connecter le VisionController au Switch
:::

```{note}
Dans la **variante B**, les ports du Switch sont tous occupés (7 appareils + VisionController) : le FlexiBowl® 2 se connecte directement au VisionController. Dans la **variante C**, la Caméra 3 se connecte également directement au VisionController, occupant le troisième port disponible.
```
```{note}
**Câblage des composants individuels**

Les procédures de branchement physique de chaque composant (FlexiBowl®, caméra, trémie, robot) sont décrites en détail dans la section [Câblage et connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md).  
 Dans une configuration 3FB + 3CAM, il suffit d'effectuer **trois fois** les mêmes opérations — une fois pour chaque station — à la seule différence que chaque appareil se connecte au **Switch** plutôt que directement au VisionController, à l'exception du **FlexiBowl® 2** (variantes B et C) et de la **Caméra 3** (variante C), qui se connectent directement aux ports Ethernet libres du VisionController.
```
```{important}
**Association de dispositifs dans le logiciel**

FlexiVision One peut gérer toutes les stations simultanément, mais il est indispensable que l'association entre les appareils soit correctement configurée dans le logiciel. Veiller à associer :

* **Caméra 1** → FlexiBowl® 1 (+ Trémie 1, si présente)
* **Caméra 2** → FlexiBowl® 2 (+ Trémie 2, si présente)
* **Caméra 3** → FlexiBowl® 3 (+ Trémie 3, si présente)

Une association incorrecte compromettrait l'emplacement des pièces et le bon fonctionnement de l'ensemble du système.
```

**→ [Configuration initiale du système](../QUICKSTART/SETUP/13_setup.md)**

