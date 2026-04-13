(nuovaricetta)=
# **Create a New Recipe**

This section describes how to create a new application recipe in FlexiVision One. A recipe is the main container that includes all part models, FlexiBowl or Hopper configurations, and robot parameters required for a complete picking application.

```{note}
**Create a new recipe when:**

- You are working with a **completely different part type**
- The **application** changes

**It is NOT necessary to create a new recipe when:**
- You add another face of the same part, in which case create a new model in the same recipe for the same part in different positions
- You make minor adjustments to existing parameters, such as camera exposure
- You modify only the accept threshold, score threshold, and similar values
```

---

## Interface overview

Before proceeding with model training, become familiar with the [Recipes](recipes) interface.

## Saving the base recipe

Before proceeding, make sure you have saved the base recipe created during initial setup:

:::{list-table}
  * - **1**
    - From the main page, click **Recipes**
  * - **2**
    - Verify that the current recipe is the base one, for example `"Base_Recipe"` created during setup
  * - **3**
    - Click **Save Recipe**
  * - **4**
    - Keep the same name in the save field, because you are overwriting the recipe with the updated configuration
  * - **5**
    - Confirm the save operation
:::

```{important}
**Why save the base recipe?**

The base recipe contains all hardware configurations completed during setup:
- FlexiBowl connection, including IP and parameters
- Hopper connection
- Robot connection, including TCP/IP port
- Camera calibration

Having a ready-made base recipe allows all these configurations to be reused without repeating them.
```

---

## Step 1: Duplicate the base recipe

To start creating the first model and therefore a new application, it is always recommended to duplicate the base recipe just saved.  
This is useful because it keeps all the setup values already configured stored separately. This is advantageous for two reasons:
- To start a new application on the same system, you do not need to repeat all the previous steps
- If only one element changes in the configuration, the setup of all the other components can remain valid

```{list-table}
* - **6**
  - From the main FlexiVision One page, click **Recipes**
* - **7**
  - The recipe management page opens with the list of all existing recipes
* - **8**
  - Select the Base Recipe
* - **9**
  - Duplicate the Base Recipe
* - **10**
  - Click **Load Recipe**
* - **11**
  - Verify in the top bar that the displayed name is the one of the new recipe
    :::{warning}
    **Always work on the correct recipe**

    When multiple recipes are present, always verify that the correct one is selected before making changes. Modifications applied to the wrong recipe require rework.
    :::
```

## Step 2: Name the recipe

Before clicking **Save Recipe**, choose a descriptive name.

```{list-table}
* - **12**
  - Rename the duplicated recipe  
    **Recommended naming conventions:**
    - Names that clearly identify the part or application
    - No spaces, use `_` or `-`
    - Include relevant information such as part type, size, or application

    :::{tip}
    **Avoid generic names**

    ❌ Names to avoid:
    - `Test`
    - `Trial`
    - `Recipe1`
    - `New_Recipe`

    ✓ Recommended names:
    - `Prod_M8_Steel_Screws`
    - `Assembly_Connectors_2024`
    - `QC_Gears_Series_X`

    **Suggested format**: `[LINE]_[PRODUCT]_[VARIANT]_[YEAR]`

    A clear name makes management easier when many different recipes are available.
    :::
```

```{warning}
**Recipe backup**

After creating and configuring a recipe:
- Use the software backup function ([Backup Management](backup))
- Export recipes periodically to external media
- Document critical parameters on paper or in digital form

A well-configured recipe represents many hours of work. Protecting it properly prevents data loss.
```

---

## Next steps

**-> [Create a Model](18_NuovoModello.md)**

```{tip}
**What is needed for the next step**

- Physical parts to recognize, at least 10 to 15 pieces
- Empty and clean FlexiBowl
- If the robot tool is a gripper, two objects different from the target part are also required to simulate the tool clearance
- A sheet to note robot coordinates, X, Y, RZ
```
