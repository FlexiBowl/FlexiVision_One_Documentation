(protocollo)=
# **Protocole de Communication Robot-Vision**

FlexiVision One communique avec le robot via le protocole **TCP/IP** sur réseau Ethernet. 

## Spécifications du protocole

```{list-table}
:header-rows: 1
:widths: 35 65

* - Paramètre
  - Valeur
* - Protocole
  - TCP/IP
* - Port
  - Configurable (par défaut: FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Caractère de terminaison
  - CHR(13) - Carriage Return
* - Format des données
  - Chaîne ASCII
* - Timeout
  - Configurable (par défaut: 5000 ms)
* - Encoding
  - UTF-8
```

## Commandes disponibles

Le système prend en charge les commandes suivantes via des chaînes de texte envoyées sur la connexion TCP/IP:

### Gestion des recettes

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de Retour
* - `set_Recipe=nome_ricetta`
  - Charge la recette correspondant au "nome_ricetta" spécifié
  - Aucune
* - `get_Recipe`
  - Renvoie le nom de la recette actuellement chargée
  - `nome_ricetta`
```

### Commandes de localisation

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de Retour
* - `start_Locator`
  - Démarre le processus de localisation des pièces. Si aucune pièce préhensible n'est présente, il appelle automatiquement la routine de mouvement du FlexiBowl.
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Arrête le processus de localisation
  - Aucune
* - `turn_Locator`
  - Si aucune pièce n'a été prise, fait tourner le FlexiBowl et redémarre la recherche
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Démarre la localisation sans activer le FlexiBowl (acquisition d'image uniquement)
  - `Pattern_n;x;y;r`/ Aucune
* - `state_Locator`
  - Renvoie l'état diagnostique du localisateur
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

### Commandes FlexiBowl

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de Retour
* - `start_Empty`
  - Démarre la séquence de vidage rapide (Quick-Emptying) du FlexiBowl
  - `start_Empty ended`
```


### Signaux hopper optionnels

```{note}
Si le hopper doit être activé, nous recevrons la chaîne: `"Hopper;signalnumber;time"`

```



Pour des informations détaillées sur l'installation physique et les connexions électriques, passer aux sections suivantes:
- [Calcul Distance Optimale Caméra](05_Calcolo_distanza_ottimale.md)
- [Installation Mécanique](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Câblage et Connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

