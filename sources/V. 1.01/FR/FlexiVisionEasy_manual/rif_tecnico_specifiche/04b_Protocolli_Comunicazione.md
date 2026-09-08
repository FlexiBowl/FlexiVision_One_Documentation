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
* - Caractère de terminaison
  - CHR(13) - Retour chariot
* - Format des données
  - Chaîne ASCII
* - Timeout
  - Configurable (par défaut : 5000 ms)
* - Encodage
  - UTF-8
```

## Commandes disponibles

Le système prend en charge les commandes suivantes via des chaînes de texte envoyées sur la connexion TCP/IP.

### *Gestion des recettes*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `set_recipe=<nom>`
  - Charge la recette indiquée et démarre la synchronisation des FlexiBowl® connectés.
  - Aucune
* - `get_recipe`
  - Renvoie le nom de la recette actuellement chargée.
  - `<nom_recette>`
```

Exemple :

```
set_recipe=MyRecipe
```

ou :

```
get_recipe
→ MyRecipe
```

### *Commandes de localisation*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `start_Locator`
  - Démarre le processus de localisation des pièces. Si aucune pièce n'est prélevable, la routine de mouvement du FlexiBowl® est automatiquement rappelée. Si le Locator est déjà actif, la commande est ignorée et le processus n'est pas redémarré.
    :::{important}
    Si aucun modèle n'est sélectionné/activé au moment de la commande, le système renvoie un message d'erreur et le Locator ne démarre pas.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Arrête le processus de localisation.
  - Aucune
* - `turn_Locator`
  - Si aucune pièce n'a été prélevée, demande un nouveau mouvement du FlexiBowl® et redémarre le processus de recherche.
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Démarre la localisation sans activer le FlexiBowl® ; seules l'acquisition d'image et la recherche sont effectuées.
  - `Pattern_n;x;y;r` / Aucune
* - `state_Locator`
  - Renvoie l'état de diagnostic du processus de localisation.
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
* - `mix_Locator_<modèles>`
    :::{tip}
    Pour plus d'informations, consultez la [section consacrée aux commandes de mixage](mix)
    :::
  - Sélectionne dynamiquement un ou plusieurs modèles et démarre le Locator. Les modèles précédemment sélectionnés sont d'abord désactivés. Les numéros disponibles vont de 1 à 8 (ex. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
    :::{note}
    Si le Locator est déjà en cours d'exécution, la commande est ignorée et la sélection actuelle n'est pas modifiée.
    :::
  - Résultat normal du Locator / `#Error_mix_locator_not_valid` (si aucun modèle valide n'est trouvé)
```

:::{note}
D'autres séparateurs de chaîne disponibles, en plus de `;`, sont : `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

:::{note}
Pour `start_Locator` et `mix_Locator_<modèles>`, lorsque le Locator est déjà en cours d'exécution, aucune réponse n'est envoyée au robot.
:::

### *Commandes FlexiBowl® – Emptying*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `start_Empty`
  - Démarre la séquence de vidage rapide (Quick-Emptying) du FlexiBowl®. La commande ne peut pas être exécutée tant que le Locator est actif.
  - `Start_Empty Started` / `Locator is Running` / `#Error_flexibowl_not_connect`
* - `stop_Empty`
  - Arrête la séquence de vidage du FlexiBowl®.
  - `Stop_Empty Command Sent` / `#Error_flexibowl_not_connect`
* - `state_Empty`
  - Renvoie l'état actuel de la séquence de vidage.
  - `Emptying Running` / `Emptying Stopped` / `#Error_flexibowl_not_connect` / `#Error_invalid_emptying_state`
```

### *Signaux trémie optionnels*

```{note}
Si la trémie doit être activée, la chaîne suivante sera reçue : `"Hopper;signalnumber;time"`
```

## Erreurs générales

```{note}
**Licence FlexiVision** : si la licence logicielle n'est pas active, les commandes du robot sont rejetées et le message suivant est renvoyé :
`#Error_License_not_active`
```

---

## Commandes Avancées / Service

Les commandes suivantes sont réservées au personnel technique.

### *Connexion FlexiBowl®*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Commande
  - Action
  - Valeur de retour
* - `connect_flb`
  - Demande la connexion au FlexiBowl®. S'il n'est pas connecté, la tâche de connexion correspondante est démarrée.
  - `#Flb1_connected` / `#Flb1_Not_connected`
```


---

Pour des informations détaillées sur l'installation physique et les raccordements électriques, poursuivez avec les sections suivantes :
- [Calcul de la Distance Optimale de la Caméra](05_Calcolo_distanza_ottimale.md)
- [Installation Mécanique](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Câblage et Connexions](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
