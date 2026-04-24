# **Mix Application Commands**
```{note}
**Prerequisites**

Before proceeding with this section, make sure you understand how the Mix Application works and that you have correctly configured the recipe with the models of the different components. See [Mix Application Overview](28_Panoramica_Mix.md).
```

---

## Robot-side differences

In a Mix Application, the TCP/IP commands sent by the robot to the vision system change compared to those of a Standard application.

The main difference concerns the **localization command family**: the commands that have the `start_` prefix in the Standard application are replaced by the equivalent family with the `mix_` prefix.

This variation allows the vision system to activate **multi-component** recognition logic, returning to the robot not only the coordinates of the localized part, but also the **identifier of the recognized model**, so that the robot program can select the correct picking strategy for each part type.
```{important}
The return value of Mix commands always includes the identifier of the recognized pattern (`Pattern_n`). The robot program must be prepared to manage the different response types and adopt the appropriate picking logic based on the identified model.
```

---

## Commands available in Mix mode

### Recipe management

| Command | Action | Return Value |
|---|---|---|
| `set_Recipe=nome_ricetta` | Loads the specified Mix recipe | None |
| `get_Recipe` | Returns the name of the currently loaded recipe | `nome_ricetta` |
```{note}
Recipe management commands are identical between Standard and Mix modes.
```

### Mix localization commands

Mix localization commands allow the robot to request the coordinates of a specific model within the recipe. Each command is dedicated to a single model and independently manages the search cycle, including FlexiBowl® movement and hopper activation if necessary.

The behavior of `mix_Locator_n` is as follows:

1. The system acquires an image and searches for Model `n`.
2. If the model is not found on the first acquisition, the FlexiBowl® is actuated automatically and the search resumes.
3. The cycle continues until Model `n` is localized or the `stop_Locator` command is sent.
4. During the entire search phase, the hopper is activated automatically if necessary.
```{important}
Each `mix_Locator_n` command searches **exclusively** for the model corresponding to number `n`.   
This means that, to request the coordinates of a different model, the specific command for that model must be used (e.g. `mix_Locator_2` for Model 2, `mix_Locator_3` for Model 3, and so on).
```

| Command | Action | Return Value |
|---|---|---|
| `mix_Locator_1` | Starts the search for **Model 1**. If not found, it actuates the FlexiBowl® and automatically repeats the search until found or until `stop_Locator`. Activates the hopper if necessary. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | As above, for **Model 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | As above, for **Model 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | As above, for **Model 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | If no part has been picked, rotates the FlexiBowl® and restarts the multi-component search | `Pattern_n;x;y;r` |
| `test_Locator` | Starts multi-component localization without activating the FlexiBowl® (image acquisition only) | `Pattern_n;x;y;r` / None |
| `stop_Locator` | Stops any search currently in progress | None |
| `state_Locator` | Returns the diagnostic status of the locator | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
The maximum number of models manageable within a single Mix recipe is **8**, corresponding to the commands `mix_Locator_1` … `mix_Locator_8`. The robot program can request the models in any order and combination, depending on the application logic.
```

### FlexiBowl® commands

| Command | Action | Return Value |
|---|---|---|
| `start_Empty` | Starts the FlexiBowl® quick emptying sequence | `start_Empty ended` |

### Optional hopper signals
```{note}
If the hopper must be activated, we will receive the string: `"Hopper;signalnumber;time"`
```

---

## Return value format

In Mix mode, the return value of the localization commands has the following format:
```
Pattern_n;x;y;r
```

| Field | Description |
|---|---|
| `Pattern_n` | Identifier of the recognized model (e.g. `Pattern_1`, `Pattern_2`, …). Corresponds to the number of the model requested with the `mix_Locator_n` command. |
| `x` | X coordinate of the part in the work area (in mm, in the robot reference system) |
| `y` | Y coordinate of the part in the work area (in mm, in the robot reference system) |
| `r` | Rotation angle of the part (in degrees) |
```{tip}
The `Pattern_n` field is the key parameter for Mix applications: the robot program must use it to select the correct picking routine (approach position, gripper opening, gripping force, etc.) based on the identified part type.
```

---


For information on the communication protocol and TCP/IP connection parameters, see:

**→ [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
