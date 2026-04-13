# **Mix Application Overview**
This section introduces the concept of a **Mix Application** in FlexiVision One, explains how it differs from a standard application, and shows how to configure it correctly at recipe and model level.

---

## What is a Mix Application?

A **Mix Application** is an application configuration in which models related to **completely different components** coexist within the same recipe.

In a Mix Application, the robot can recognize and pick **multiple different part types** present at the same time in the work area, without changing recipe or interrupting the cycle. The vision system identifies every part present on the FlexiBowl(R) and returns to the robot the coordinates of the most suitable pickable part, regardless of its type.
```{tip}
**Typical example:** screws, nuts, and washers may be present simultaneously on the FlexiBowl(R). The robot picks any recognized part, optimizing throughput without interruptions.
```

---

## Standard Application vs Mix Application

| Feature | Standard Application | Mix Application |
|---|---|---|
| **Part types** | Only one type of part | Multiple completely different part types |
| **Models in the recipe** | All models refer to the same component | Models may also refer to distinct components |
| **Robot behavior** | It always picks the same part, even from different positions (by creating multiple models) | It picks any recognized part, regardless of type |
| **Software configuration** | No difference compared to Mix mode | No difference compared to Standard mode |
| **Mode selection** | Not required: it depends on the models included in the recipe | Not required: it depends on the models included in the recipe |
| **Robot commands** | `start_..` family | `mix_..` family |

```{note}
At software level there is no explicit selection between Standard mode and Mix mode: the distinction is determined exclusively by the **content of the recipe**. If all models refer to the same part (or its different sides), it is a Standard application. If the models refer to different parts, it automatically becomes a Mix application.
```

---

## How is a Mix recipe created?

The process for creating a Mix recipe is **identical** to that of a Standard recipe. No preliminary option needs to be selected. You can therefore follow the procedure described in [Recipe and Model Creation - Overview](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md)

The difference appears **during model creation**:

- In a **Standard** application, all models included in the recipe represent the same component (for example: side A, side B, side C of the same part).
- In a **Mix** application, the models included represent **completely different components** (for example: Part A, Part B, Part C - three distinct components with different geometries).
```{important}
Each model within a Mix recipe must be trained separately using its own physical reference part, following the standard procedure described in [Create a New Model](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Clearances and robot pick coordinates must be calibrated individually for each component.
```

---

## Next steps

Once you understand the Mix Application concept and have configured the recipe with the models of the different components, the next step is to adapt the **robot commands** required to operate in Mix mode:

**-> [Mix Application Commands](29_Comandi_Mix.md)**
