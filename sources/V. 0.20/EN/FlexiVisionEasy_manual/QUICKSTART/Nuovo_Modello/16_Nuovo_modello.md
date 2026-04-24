# **Recipe and Model Creation - Overview**

This section guides the user through the complete process of creating an application recipe and the part models required for recognition and robotic picking.

```{note}
**Prerequisites**

Before proceeding with recipe and model creation, make sure that:
- All hardware setup has been completed ([Component Setup](setupcomponenti))
- Camera calibration has been successfully completed ([Camera Calibration](calibrazione))
- Robot calibration is completed
- Physical sample parts are available
```

---

## Recipe vs Model: fundamental differences

Before starting, it is important to understand the difference between a **Recipe** and a **Model**:

```{list-table}
   :widths: 50 50
   :header-rows: 1

   * - What is a Recipe?
     - What is a Model?
   * - The global container for the entire picking application.
     - The specific definition of one single component to be recognized.
   * - Includes up to 8 models, FlexiBowl parameters, Hopper settings, and communication logic.
     - Includes training images, ROI, visual features, filters, and robot offsets.
   * - Manages hardware parameters such as vibrations and speed, as well as network settings such as TCP/IP port and timeout.
     - Manages vision parameters such as thresholds and minimum score, plus pick coordinates for the gripper.
   * - Can handle multiple part types simultaneously in a multi-model application.
     - Focused on one specific visual pattern.
```

```{tip}
A recipe can contain up to 8 different models, allowing the robot to recognize and pick different part types from the same application without changing the overall configuration.
```

---

## Overview of the complete process

The process for creating a complete and working recipe is divided into several sequential stages:

```{figure} ../../../../../_shared/media/images/newmodel4.jpg
:alt: Recipe and model creation workflow
:width: 100%
:align: center

Complete recipe and model creation workflow
```

### Main stages

```{list-table}
:header-rows: 1
:widths: 10 30 60

* - Stage
  - Name
  - Description
* - **1**
  - Recipe Creation
  - Definition of the application recipe with name, type, and FlexiBowl used
* - **2**
  - Physical Preparation
  - Positioning of the reference part in the viewing area
* - **3**
  - Model Training
  - Image acquisition and creation of the recognition pattern
* - **4**
  - ROI Definition
  - Definition of the search area where parts will be detected
* - **5**
  - Filter Setup
  - Configuration of accept threshold and recognition tolerances
* - **6**
  - Physical Preparation
  - Picking simulation with the robot to position the objects used to simulate gripper clearance
* - **7**
  - Coordinate Saving
  - Saving robot coordinates in the picking position of the reference part
* - **8**
  - Clearance Creation
  - Definition of zones that must remain free, such as gripper area or obstacles
* - **9**
  - Robot Coordinates
  - Calculation of the gripper offset for correct picking
* - **10**
  - Test and Validation
  - Verification of full operation and recipe saving
```

---

## Navigation guide for the detailed sections

For complete information about each process stage, refer to the dedicated sections:

- **[Create a New Recipe](nuovaricetta)** - how to create and configure a new recipe
- **[Model Training](nuovomodello)** - image acquisition and pattern creation
- **[ROI and Filter Definition](roitest)** - configuration of search area and tolerances
- **[Clearance Creation](istogrammi)** - definition of zones that must remain free
- **[Robot Pick Coordinates](robotpick)** - calculation of the gripper offset

---

## Practical advice before starting

### Material preparation

```{tip}
**Preparation checklist**

Before starting model creation, prepare:

- At least 10 to 20 parts of the type to be recognized for testing
- Clean parts in good condition, representative of production
- Gripper-clearance simulators, which must **not** be parts of the same type, to avoid confusion with the reference component
- A sheet to note robot coordinates, X, Y, RZ
- Empty and clean FlexiBowl
- Backlight or TopLight switched on
```

### Optimal environment

```{note}
**Ideal training conditions**

- Stable lighting, avoiding variable direct sunlight
- FlexiBowl stopped
- Robot in a safe position and not interfering during acquisition
- FlexiVision One open with the base recipe loaded
```

### Common mistakes to avoid

```{error}
**Avoid these common errors**

❌ **Not saving robot coordinates** during physical preparation -> impossible to calculate gripper offset

❌ **Moving the part** after saving coordinates -> incorrect offset

❌ **Feature threshold too low** -> model becomes too detailed and starts recognizing the background surface texture

❌ **ROI too narrow** -> parts close to the edges are not detected

❌ **Clearances too small** -> gripper collisions with nearby parts

❌ **Not testing with multiple parts** -> issues are not discovered until production

Follow the detailed procedures in the next sections carefully to avoid these problems.
```

---

## Support and additional resources

```{note}
**INFO buttons**

- **Video tutorial**
- **Step-by-step explanation**
- **Technical support**: [support@arsautomation.com](mailto:support@arsautomation.com) for assistance

For specific issues during model creation, refer to [Troubleshooting](troubleshooting).
```

---

## Next steps

Once the process overview is clear, proceed with the actual creation:

**-> [Start with: Create a New Recipe](nuovaricetta)**

```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```
