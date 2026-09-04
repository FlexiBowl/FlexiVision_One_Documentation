# **Mix Application Commands**
```{note}
**Prerequisites**

Before proceeding with this section, make sure you understand how the Mix Application works and that you have correctly configured the recipe with the models of the different components. See [Mix Application Overview](28_Panoramica_Mix.md).
```

---

## Robot side differences

In a Mix application, the TCP/IP commands sent by the robot to the vision system change compared to those in a Standard application.

The main difference concerns the **family of tracking commands**: the commands that in the Standard application have the prefix `start_` are replaced by the equivalent family with the prefix `mix_`.

This variation allows the vision system to activate the **multi-component** identification logic, returning to the robot not only the coordinates of the part located, but also the recognised **model identifier**, so that the robot program can select the correct picking strategy for each type of part.
```{important}
The return value of Mix commands always includes the recognised pattern identifier (`Pattern_n`). The robot program must be set up to manage the different response types and adopt the appropriate picking logic according to the identified model.
```
:::{tip}
The new version allows you to manage the `mix_Locator_n` commands for robots 1, 2, and 3 in a combined manner.
:::

---

## Commands available in Mix mode

### *Recipe management*

| Command | Action | Return Value |
|---|---|---|
| `set_Recipe=nome_ricetta` | Upload the specified Mix recipe | None |
| `get_Recipe` | Returns the name of the currently uploaded recipe | `nome_ricetta` |
```{note}
The recipe management commands for Standard and Mix modes are identical.
```

### *Mix tracking commands*

Mix tracking commands allow the robot to request the coordinates of a specific model within the recipe. Each command is dedicated to a single model and autonomously manages the search cycle, including moving the FlexiBowl® and activating the hopper if necessary.

The `mix_Locator_n` acts as follows:

1. The system captures an image and searches for the Model `n`.
2. If the model is not found at the first capture, the FlexiBowl® is automatically activated and the search resumes.
3. The cycle continues until the Model `n` is located or the command `stop_Locator` is sent.
4. During the entire search phase, the hopper is automatically switched on if necessary.
```{important}
Each `mix_Locator_n` command **only** searches for the model corresponding to the number `n`.
This means that to request the coordinates of a different model, the specific command for that model must be used (e.g. `mix_Locator_2` for Model 2, `mix_Locator_3` for Model 3, and so on).
```

| Command | Action | Return Value |
|---|---|---|
| `mix_Locator_1` | Start searching for **Model 1**. If not found, activate the FlexiBowl® and repeat the search automatically until found or at `stop_Locator`. Activate the hopper if necessary. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | As above, for **Model 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | As above, for **Model 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | As above, for **Model 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | If no part has been picked, rotate the FlexiBowl® and restart the multi-component search | `Pattern_n;x;y;r` |
| `test_Locator` | This starts multi-component tracking without activating the FlexiBowl® (image capture only) | `Pattern_n;x;y;r` / None |
| `stop_Locator` | It interrupts any search in progress | None |
| `state_Locator` | It returns the diagnostic status of the locator. | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
The maximum number of models that can be managed within a single Mix recipe is **8**, corresponding to the commands `mix_Locator_1` … `mix_Locator_8`. The robot program can request the models in any order and combination, depending on the application logic.
```
:::{tip}
The new version allows you to create `mix_Locator` commands that span multiple models—that is, commands that call multiple models simultaneously. For example, the `mix_Locator12` command calls models 1 and 2.
:::

### *FlexiBowl® Commands*

| Command | Action | Return Value |
|---|---|---|
| `start_Empty` | It starts the FlexiBowl® quick emptying sequence. | `start_Empty ended` |

### *Optional hopper signals*
```{note}
If the hopper needs to be switched on, we will receive the string: `"Hopper;signalnumber;time"`
```

---

## Return value format

In Mix mode, the return value of tracking commands has the following format:
```
Pattern_n;x;y;r
```

| Field | Description |
|---|---|
| `Pattern_n` | Identifier of the recognised model (e.g. `Pattern_1`, `Pattern_2`, ...). It corresponds to the model number requested with the command `mix_Locator_n`. |
| `x` | X coordinate of the part in the working area (in mm, in the robot reference system) |
| `y` | Y coordinate of the part in the working area (in mm, in the robot reference system) |
| `r` | Angle of rotation of the part (in degrees) |
```{tip}
The field `Pattern_n` is the key parameter for Mix applications: the robot program must use it to select the correct picking routine (approach position, gripper opening, picking force, etc.) according to the type of part identified.
```

---


For information on the communication protocol and TCP/IP connection parameters, see:

**→ [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
