(protocollo)=
# **Protocole de Communication Robot-Visione**

FlexiVision One communique avec le robot via le protocole **TCP/IP** sur un réseau Ethernet.

## Spécifications du protocole

```{list-table}
:header-rows: 1
:widths: 35 65

* - Paramètre
  - Valeur
* - Protocole
  - TCP/IP
* - Port
  - Configurable (par défaut : FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Caractère de fin
  - CHR(13) - Carriage Return
* - Format des données
  - Chaîne ASCII
* - Timeout
  - Configurable (par défaut : 5000 ms)
* - Encodage
  - UTF-8
```

## Commandes disponibles

Le système prend en charge les commandes suivantes par le biais de chaînes de texte envoyées via la connexion TCP/IP :

### *Gestion des recettes*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `set_Recipe=nome_ricetta`
  - Charger la recette correspondant au «&nbsp;nom_recette&nbsp;» spécifié
  - Aucun
* - `get_Recipe`
  - Restitue le nom de la recette actuellement chargée
  - `nome_ricetta`
```

### *Commandes de localisation*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `start_Locator`
  - Lance le processus de localisation des pièces. Si aucune pièce ne peut être prélevée, il appelle automatiquement la routine de manutention du FlexiBowl®.
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Arrête le processus de localisation
  - Aucun
* - `turn_Locator`
  - Si aucune pièce n'a été prélevée, fait tourner le FlexiBowl® et relance la recherche
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Démarre la localisation sans activer le FlexiBowl® (acquisition d'images uniquement)
  - `Pattern_n;x;y;r`/ Aucun
* - `state_Locator`
  - Renvoie l'état de diagnostic du localisateur
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```
:::{note}
Outre ` ; ` , les autres séparateurs de chaîne disponibles sont : `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

### *Commandes du FlexiBowl®*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `start_Empty`
  - Démarre la séquence de vidage rapide (Quick-Emptying) du FlexiBowl®
  - `start_Empty ended`
```


### *Signaux de trémie en option*

```{note}
Si la trémie doit être activée, nous recevrons la chaîne : `"Hopper;signalnumber;time"`

```



Pour des informations détaillées sur l'installation physique et les branchements électriques, voir les sections suivantes :
- [Calcul de la distance optimale de la Caméra](05_Calcolo_distanza_ottimale.md)
- [Installation mécanique](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Câblage et connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

