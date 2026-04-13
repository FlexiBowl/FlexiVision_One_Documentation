(protocollo)=
# **Robot-Vision Communication Protocol**

FlexiVision One communicates with the robot through the **TCP/IP** protocol over Ethernet.

## Protocol specifications

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parameter
  - Value
* - Protocol
  - TCP/IP
* - Port
  - Configurable (default: FB1 -> 4001 ; FB2 -> 4002 ; FB3 -> 4003)
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

The system supports the following commands through text strings sent over the TCP/IP connection:

### Recipe management

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return value
* - `set_Recipe=recipe_name`
  - Loads the recipe corresponding to the specified `recipe_name`
  - None
* - `get_Recipe`
  - Returns the name of the currently loaded recipe
  - `recipe_name`
```

### Locator commands

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return value
* - `start_Locator`
  - Starts the part localization process. If no pickable parts are available, it automatically calls the FlexiBowl movement routine.
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Stops the localization process
  - None
* - `turn_Locator`
  - If no part has been picked, rotates the FlexiBowl and restarts the search
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Starts localization without activating the FlexiBowl (image acquisition only)
  - `Pattern_n;x;y;r` / None
* - `state_Locator`
  - Returns the locator diagnostic status
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

### FlexiBowl commands

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Command
  - Action
  - Return value
* - `start_Empty`
  - Starts the FlexiBowl quick-emptying sequence
  - `start_Empty ended`
```

### Optional hopper signals

```{note}
If the hopper must be activated, the following string will be received: `"Hopper;signalnumber;time"`
```

For detailed information about physical installation and electrical connections, continue with the following sections:
- [Optimal Camera Working Distance Calculation](05_Calcolo_distanza_ottimale.md)
- [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
