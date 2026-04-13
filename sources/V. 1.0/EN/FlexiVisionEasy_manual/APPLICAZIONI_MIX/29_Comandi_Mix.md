# **Mix Application Commands**
```{note}
**Prerequisites**

Before proceeding with this section, make sure you understand how a Mix Application works and that you have correctly configured the recipe with the models of the different components. See [Mix Application Overview](28_Panoramica_Mix.md).
```

---

## Robot-side differences

In a Mix Application, the TCP/IP commands sent by the robot to the vision system differ from those used in a Standard application.

The main difference concerns the **localization command family**: commands that in a Standard application use the `start_` prefix are replaced by the equivalent `mix_` command family.

This variation allows the vision system to activate **multi-component** recognition logic, returning to the robot not only the coordinates of the located part but also the **identifier of the recognized model**, so that the robot program can select the correct picking strategy for each part type.
```{important}
The return value of Mix commands always includes the identifier of the recognized pattern (`Pattern_n`). The robot program must be designed to handle the different response types and apply the correct picking logic based on the identified model.
```

---

## Commands available in Mix mode

### Recipe management

| Command | Action | Return Value |
|---|---|---|
| `set_Recipe=recipe_name` | Loads the specified Mix recipe | None |
| `get_Recipe` | Returns the name of the currently loaded recipe | `recipe_name` |
```{note}
Recipe management commands are identical in Standard and Mix modes.
```

### Mix localization commands

Mix localization commands allow the robot to request the coordinates of a specific model within the recipe. Each command is dedicated to a single model and autonomously manages the search cycle, including FlexiBowl(R) movement and hopper activation if required.

The behavior of `mix_Locator_n` is as follows:

1. The system acquires an image and searches for Model `n`.
2. If the model is not found in the first acquisition, the FlexiBowl(R) is automatically actuated and the search starts again.
3. The cycle continues until Model `n` is localized or the `stop_Locator` command is sent.
4. Throughout the entire search phase, the hopper is automatically activated if needed.
```{important}
Each `mix_Locator_n` command searches **only** for the model corresponding to number `n`.
This means that to request the coordinates of a different model, you must use the specific command for that model (for example `mix_Locator_2` for Model 2, `mix_Locator_3` for Model 3, and so on).
```

| Command | Action | Return Value |
|---|---|---|
| `mix_Locator_1` | Starts the search for **Model 1**. If not found, the FlexiBowl(R) is actuated and the search is automatically repeated until the model is found or `stop_Locator` is sent. Activates the hopper if required. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Same as above, for **Model 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Same as above, for **Model 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| ... | ... | ... |
| `mix_Locator_8` | Same as above, for **Model 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | If no part has been picked, rotates the FlexiBowl(R) and restarts the multi-component search | `Pattern_n;x;y;r` |
| `test_Locator` | Starts multi-component localization without actuating the FlexiBowl(R) (image acquisition only) | `Pattern_n;x;y;r` / None |
| `stop_Locator` | Stops any ongoing search | None |
| `state_Locator` | Returns the locator diagnostic state | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
The maximum number of models that can be managed within a single Mix recipe is **8**, corresponding to commands `mix_Locator_1` ... `mix_Locator_8`. The robot program can request models in any order and combination, depending on the application logic.
```

### FlexiBowl(R) commands

| Command | Action | Return Value |
|---|---|---|
| `start_Empty` | Starts the rapid emptying sequence of the FlexiBowl(R) | `start_Empty ended` |

### Optional hopper signals
```{note}
If the hopper must be activated, the returned string will be: `"Hopper;signalnumber;time"`
```

---

## Return value format

In Mix mode, the return value of localization commands has the following format:
```
Pattern_n;x;y;r
```

| Field | Description |
|---|---|
| `Pattern_n` | Identifier of the recognized model (for example `Pattern_1`, `Pattern_2`, ...). It matches the number of the model requested with the `mix_Locator_n` command. |
| `x` | X coordinate of the part in the work area (in mm, in the robot reference system) |
| `y` | Y coordinate of the part in the work area (in mm, in the robot reference system) |
| `r` | Rotation angle of the part (in degrees) |
```{tip}
The `Pattern_n` field is the key parameter for Mix applications: the robot program must use it to select the correct picking routine (approach position, gripper opening, gripping force, etc.) based on the identified part type.
```

---

For information on the communication protocol and TCP/IP connection parameters, see:

**-> [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
