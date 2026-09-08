(protocollo)=
# **Robot-Vision Communication Protocol**

FlexiVision One communicates with the robot via **TCP/IP** protocol over an Ethernet network.

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

The system supports the following commands via text strings sent over the TCP/IP connection.

### *Recipe management*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `set_recipe=<name>`
  - Loads the specified recipe and starts synchronization of the connected FlexiBowl® units.
  - None
* - `get_recipe`
  - Returns the name of the currently loaded recipe.
  - `<recipe_name>`
```

Example:

```
set_recipe=MyRecipe
```

or:

```
get_recipe
→ MyRecipe
```

### *Locator commands*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `start_Locator`
  - Starts the part-locating process. If no pickable parts are present, it automatically calls the FlexiBowl® movement routine. If the Locator is already active, the command is ignored and the process is not restarted.
    :::{important}
    If no model is selected/enabled at the time the command is issued, the system returns an error message and the Locator does not start.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Stops the locating process.
  - None
* - `turn_Locator`
  - If no part has been picked, it requests a new FlexiBowl® movement and restarts the search process.
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Starts the locating process without activating the FlexiBowl®; only image acquisition and search are performed.
  - `Pattern_n;x;y;r` / None
* - `state_Locator`
  - Returns the diagnostic status of the locating process.
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
* - `mix_Locator_<models>`
    :::{tip}
    Weitere Informationen finden Sie im [Abschnitt zu den Mix-Befehlen](mix)
    :::
  - Dynamically selects one or more models and starts the Locator. Previously selected models are first disabled. Available numbers range from 1 to 8 (e.g. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
    :::{note}
    If the Locator is already running, the command is ignored and the current selection is not changed.
    :::
  - Normal Locator result / `#Error_mix_locator_not_valid` (if no valid model is found)
```

:::{note}
Other available string separators, besides `;`, are: `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

:::{note}
For `start_Locator` and `mix_Locator_<models>`, when the Locator is already running, no response is sent to the robot.
:::

### *FlexiBowl® commands – Emptying*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `start_Empty`
  - Starts the FlexiBowl® Quick-Emptying sequence. The command cannot be executed while the Locator is active.
  - `Start_Empty Started` / `Locator is Running` / `#Error_flexibowl_not_connect`
* - `stop_Empty`
  - Stops the FlexiBowl® emptying sequence.
  - `Stop_Empty Command Sent` / `#Error_flexibowl_not_connect`
* - `state_Empty`
  - Returns the current status of the emptying sequence.
  - `Emptying Running` / `Emptying Stopped` / `#Error_flexibowl_not_connect` / `#Error_invalid_emptying_state`
```

### *Optional hopper signals*

```{note}
If the hopper needs to be activated, the following string will be received: `"Hopper;signalnumber;time"`
```

## General errors

```{note}
**FlexiVision license**: if the software license is not active, robot commands are rejected and the following is returned:
`#Error_License_not_active`
```

---

## Advanced / Service Commands

The following commands are reserved for technical personnel.

### *FlexiBowl® connection*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return Value
* - `connect_flb`
  - Requests connection to the FlexiBowl®. If not connected, the related connection task is started.
  - `#Flb1_connected` / `#Flb1_Not_connected`
```


---

For detailed information on physical installation and electrical connections, proceed to the following sections:
- [Optimal Camera Distance Calculation](05_Calcolo_distanza_ottimale.md)
- [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
