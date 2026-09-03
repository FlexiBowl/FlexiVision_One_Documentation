# **Creating Recipes and Models - Overview**

This section guides the user through the complete process of creating an application recipe and the part models required for robot identification and picking.

```{note}
**Prerequisites**

Before proceeding with the creation of recipes and models, make sure that:
- All hardware setups are completed ([Component Setup](setupcomponenti))
- Camera calibration has been successful ([Camera Calibration](calibrazione))
- Robot calibration is completed
- Physical parts to be identified are available
```

---

## Recipe vs. Model: Fundamental differences

Before starting, it is important to understand the difference between **Recipe** and **Model**:

```{list-table}
   :widths: 50 50
   :header-rows: 1

   * - What is a Recipe?
     - What is a Model?
   * - The global container of the entire picking application.
     - The specific definition of a single component to be identified.
   * - It includes up to 8 models, FlexiBowl®, Hopper parameters and communication logics.
     - It includes training images, ROI, visual features, filters and robot offsets.
   * - It manages hardware parameters (vibration, speed) and network parameters (TCP/IP port, timeout).
     - It manages vision parameters (threshold, minimum score) and picking coordinates (gripper).
   * - It can manage several types of parts simultaneously (multi-model).
     - Focused on one specific visual pattern.
```


```{tip}
A recipe can contain up to 8 different models, allowing the robot to identify and pick different types of parts from the same application without changing configuration.
```


---

## Complete process overview

The process of creating a complete and functioning recipe consists of several sequential steps:

```{figure} ../../../../../_shared/media/images/newmodel4.jpg
:alt: Recipe and model creation workflow
:width: 100%
:align: center

Complete outline of the recipe and model creation process
```

### *Main Phases*

```{list-table}
:header-rows: 1
:widths: 10 30 60

* - Phase
  - Name
  - Description
* - **1**
  - Recipe creation
  - Definition of application recipe with name, type and FlexiBowl® used
* - **2**
  - Physical Preparation
  - Positioning of the reference part in the vision area
* - **3**
  - Pattern Training
  - Image capture and creation of the identification pattern
* - **4**
  - ROI Definition
  - Definition of the search area where to search for parts
* - **5**
  - Filter Setting
  - Configuration of accept threshold and identification tolerances
* - **6**
  - Physical preparation
  - Picking simulation with robot to position the objects that will simulate the gripper footprint
* - **7**
  - Saving coordinates
  - Saving robot coordinates at the picking position of the reference component
* - **8**
  - Creating clearances
  - Defining areas that are to remain clear (gripper area obstacles)
* - **9**
  - Robot coordinates
  - Calculation of gripper offset for correct picking
* - **10**
  - Testing and Validation
  - Complete operating check and recipe saving
```

---

## Navigation guide to detailed sections

For complete information on each phase of the process, please refer to the dedicated sections:

- **[Creating a New Recipe](nuovaricetta)** - How to create and configure a new recipe
- **[Model Training](nuovomodello)** - Image capture and model creation
- **[ROI definition and filters](roitest)** - Configuring search area and tolerances
- **[Creating Clearances](istogrammi)** - Definition of Clearance Areas
- **[Robot Pick Coordinates](robotpick)** - Gripper offset calculation

---

## Practical advice before starting

### *Material preparation*

```{tip}
**Preparation Checklist**

Before starting to create models, you must prepare:

-  At least 10-20 parts to be identified (for testing purposes)
-  Clean parts in good condition (representative of production)
-  Gripper footprint simulators (must NOT be parts of the same type, as it is important not to get them mixed up with the reference part.)
-  Sheet for writing down robot coordinates (X, Y, RZ)
-  FlexiBowl® empty and clean
-  Backlight/Toplight switched on
```

### *Ideal environment*

```{note}
**Ideal conditions for training**

- Stable lighting (avoid variable direct sunlight)
- FlexiBowl® stationary
- Robot in safe position (it must not interfere during captures)
- FlexiVision One software open and basic recipe uploaded
```

### *Common mistakes to avoid*

```{error}
**Avoid these common mistakes**

❌ **Do not save robot coordinates** during physical preparation → impossible to calculate gripper offset 

❌ **Moving the part** after saving the coordinates → wrong offset

❌ **Feature threshold too low** → model too detailed, identifies surface texture

❌ **ROI too narrow** → parts at the edges are not detected

❌ **Clearances too small** → gripper collisions with adjacent parts

❌ **Do not test with multiple parts** → problems not detected until production

Carefully follow the procedures detailed in the following sections to avoid these issues.
```

---

## Support and additional resources

```{note}
**The INFO keys**  
In each of the operating sections, an INFO key is available at the top right.
This button has an explanation of the Step By Step procedure. The same procedure can be seen in the video tutorial.

- [**Full video tutorials**](vidtutcompleti) 
- **Technical support**: [support@arsautomation.com](mailto:support@arsautomation.com) for service

For specific problems when creating models, see [Troubleshooting](troubleshooting).
```

---

## Next steps

Once the overview of the process is understood, proceed with the actual creation:

**→ [Start: Creating a New Recipe](nuovaricetta)**


```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```
