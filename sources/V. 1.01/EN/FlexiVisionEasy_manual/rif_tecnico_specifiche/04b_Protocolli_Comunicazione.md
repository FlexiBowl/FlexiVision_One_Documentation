(protocollo)=
# **Robot-Vision Communication Protocol**

FlexiVision One dialogues with the robot via **TCP/IP** protocol over an Ethernet network.

## Protocol specifications

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parameter
  - Value
* - Protocol
  - TCP/IP
* - Port
  - Configurable (default: FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Termination character
  - CHR(13) - Carriage Return
* - Data format
  - ASCII string
* - Timeout
  - Configurable (default: 5000 ms)
* - Encoding
  - UTF-8
```

## Available commands

The system supports the following commands via text strings sent over the TCP/IP connection:

### *Recipe management*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `set_Recipe=nome_ricetta`
  - Uploads the recipe matching the specified "recipe_name"
  - None
* - `get_Recipe`
  - Returns the name of the currently uploaded recipe
  - `nome_ricetta`
```

### *Tracking commands*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `start_Locator`
  - It starts the part tracking process. If there are no parts that can be picked up, it automatically retrieves the FlexiBowl® movement routine.
    :::{important}
    Se al momento del comando non risulta selezionato/abilitato alcun modello, il sistema restituisce un messaggio di errore e il Locator non viene avviato.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - It stops the tracking process
  - None
* - `turn_Locator`
  - If no parts have been picked up, it rotates the FlexiBowl® and restarts the search
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - It starts tracking without activating the FlexiBowl® (image acquisition only)
  - `Pattern_n;x;y;r`/ None
* - `state_Locator`
  - It returns the diagnostic status of the locator
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```
:::{note}
Other string separators available, in addition to `;`, are: `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

### *FlexiBowl® Commands*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `start_Empty`
  - It starts the FlexiBowl® Quick-Emptying sequence
  - `start_Empty ended`
```


### *Optional hopper signals*

```{note}
If the hopper needs to be switched on, we will receive the string: `"Hopper;signalnumber;time"`

```



For detailed information on physical installation and electrical connections, go to the following sections:
- [Ideal Camera Distance Calculation](05_Calcolo_distanza_ottimale.md)
- [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

