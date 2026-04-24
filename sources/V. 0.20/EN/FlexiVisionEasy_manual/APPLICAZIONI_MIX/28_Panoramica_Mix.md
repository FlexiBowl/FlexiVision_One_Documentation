# **Mix Application Overview**
This section introduces the concept of a **Mix Application** in FlexiVision One, explaining how it differs from a standard application and how to configure it correctly at recipe and model level.

---

## What is a Mix Application?

A **Mix Application** is an application configuration in which models relating to **completely different components** coexist within the same recipe.

In a Mix application, the robot can recognize and pick **multiple different part types** present simultaneously in the work area, without having to change recipe or interrupt the cycle. The vision system identifies each part present on the FlexiBowl® and returns to the robot the coordinates of the most suitable pickable part, regardless of its type.
```{tip}
**Typical example:** screws, nuts, and washers may be present simultaneously on the FlexiBowl®. The robot picks any recognized part, optimizing throughput without interruptions.
```

---

## Standard Application vs Mix Application

| Feature | Standard Application | Mix Application |
|---|---|---|
| **Part types** | Only one part type  | Multiple completely different part types |
| **Models in the recipe** | All models refer to the same component | Models may also refer to distinct components |
| **Robot behavior** | Always picks the same part even in different positions (creating multiple models)| Picks any recognized part, regardless of type |
| **Software configuration** | No difference compared to Mix mode | No difference compared to Standard mode |
| **Mode selection** | Not required: depends on the models entered in the recipe | Not required: depends on the models entered in the recipe |
| **Robot commands** | `start_..` family | `mix_..` family |

```{note}
At software level, there is no explicit choice between Standard and Mix mode: the distinction is determined exclusively by the **contents of the recipe**. If all the models present refer to the same part (or to its different faces), it is a Standard application. If the models refer to different parts, it is automatically a Mix application.
```

---

## How is a Mix recipe created?

The process of creating a Mix recipe is **identical** to that of a Standard recipe. No preliminary option needs to be selected. You can therefore follow the [Recipe and Model Creation - Overview](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md) procedure.

The difference appears **during the model creation phase**:

- In a **Standard** application, all models entered in the recipe represent the same component (for example: face A, face B, face C of the same part).
- In a **Mix** application, the entered models represent **completely different components** (for example: Part A, Part B, Part C — three distinct components with different geometries).
```{important}
Each model within a Mix recipe must be trained separately using its own physical reference part, following the standard procedure described in [Create a New Model](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Clearances and robot pick coordinates must be calibrated individually for each component.
```

---

## Next steps

Once the concept of Mix Application has been understood and the recipe has been configured with the models of the different components, the next step concerns adapting the **robot commands** required to operate in Mix mode:

**→ [Mix Application Commands](29_Comandi_Mix.md)**

