(robotpick)=
# **Robot Pick Calibration**
In this page we will see how to link vision coordinates with robot coordinates to enable precise picking of components.


**What is Robot Pick?**
The **Robot Pick** function calculates the offset between the coordinates detected by FlexiVision One and the robot's actual coordinates, allowing the robot to pick the components in the correct position.
```{danger}
**Fundamental robot coordinates!**

This phase **MANDATORILY** requires the X, Y, Rz coordinates saved during the physical preparation of the setup (Step 1 of the Clearances section).

Without these coordinates, the calibration cannot be completed. If they are lost or forgotten, it will be necessary to repeat the entire physical preparation with the robot.
```
---

## Robot Pick Interface Overview

After clicking 'Next' on the Clearances page, the **Robot Model Pick** page opens.

![Robot Pick Page](../../../../../_shared/media/images/pagina_robotpick.png)

|Section | Parameter | Function |
|-----------|-----------|----------|
| Enable | **Enable Robot Pick** | Activates robot calibration |
|Vision Result| **X cord** | X coordinate detected by vision |
|Vision Result| **Y cord** | Y coordinate detected by vision |
|Vision Result| **RZ cord** | Z rotation detected by vision |
|Insert Robot Coordinate| **X cord** | Robot X coordinate (to be inserted) |
|Insert Robot Coordinate| **Y cord** | Robot Y coordinate (to be inserted) |
|Insert Robot Coordinate| **RZ cord** | Robot Z rotation (to be inserted) |


| Function | Description |
|----------|-------------|
| **Find Object** | Detects the component and shows vision coordinates |
| **Picking Offset** | Calculates the offset for the correct picking |

---

## Step 1: Component Activation and Detection

:::{video} ../../../../../_shared/media/videos/Step1_robot.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **1**
  - Click **Enable Robot Pick**
* - **2**
  - Click <img src="../../../../../_shared/media/images/tasto_FIND_OBJECT1.png" class="inline-icon">:
      - The system will detect the reference component
      - The coordinates will appear in the **Vision Result** section

      :::{note} Vision Result:
      These are the coordinates that FlexiVision One 'sees' in the image. They are not yet linked to the robot's coordinate system.
      :::
```
:::{tip}
If you have any doubts during configuration, please consult the **INFO** key on the current page.
:::

## Step 2: Robot Coordinate Insertion and Offset calculation

:::{video} ../../../../../_shared/media/videos/Step2_robot.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **3**
  - In the **Insert Robot Coordinates** box, enter the coordinates saved when creating the model:
      - **X cord** → X coordinate noted in step 1 of [Clearances Creation](setupclearances)
      - **Y cord** → Y coordinate noted in step 1 of [Clearances Creation](setupclearances)
      - **RZ cord** → Z rotation noted in step 1 of [Clearances Creation](setupclearances)

      :::{danger}
      Use the coordinates saved during model setup. Without these coordinates, the calibration will be incorrect!
      The coordinates must be entered with **the utmost precision**:
      - Copy the values exactly as written down (including decimals)
      - **DO NOT approximate** (e.g.: 450.23 ≠ 450.2 ≠ 450)
      - Make sure you haven't swapped X and Y
      - Check the sign (+ or -) of each coordinate

      **Errors at this phase cause completely incorrect robot offsets**, resulting in picking attempts in wrong positions (even tens of centimetres of error). Failure to comply with these two points could lead to robot collisions resulting in damage to the FlexiBowl®, components or the robot itself.
      :::
* - **4**
  - Click <img src="../../../../../_shared/media/images/tasto_GRIPPER_OFFSET.png" class="inline-icon">
      - The system will automatically calculate the transformation between vision coordinates and robot coordinates
      - This offset will be applied to all future readings
```
---
```{admonition} **How Does the Gripper Offset Work?**
:class: info
The system compares:
- **Vision Coordinates**: where FlexiVision One 'sees' the origin of the component
- **Robot Coordinates**: where the robot actually grasped the component

It calculates the difference and stores it as an **offset**. This offset will be applied to all detected components in the future, ensuring that the robot always picks in the correct position.
```
:::{tip}
If you have any doubts during configuration, please consult the **INFO** key on the current page.
:::
---

## Step 3: Finalising and Saving
```{list-table}
* - **5**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> to go back to the recipe page <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
* - **6**
  - Click <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon"> to save the entire configuration

      :::{admonition} Complete Saving
      :class: success
      Saving includes:
      - ✓ Model created
      - ✓ Work area (ROI)
      - ✓ Tolerances (Accept Threshold)
      - ✓ Configured clearances
      - ✓ Robot calibration (Gripper Offset)
      :::
```
:::{warning}
Se il Robot Pick Offset è stato abilitato ma il relativo valore non è stato calcolato correttamente, il sistema mostra una message box e impedisce di proseguire con Next.
:::
---

## Multiple Models - Adding More Models

### *Step 4: Additional Models (optional)*
```{list-table}
* - **7**
  - To create other models in the same recipe:
      - Go back to <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">
      - Select a new, not yet configured model
      - Repeat the entire procedure from [Model Creation](nuovomodello)

      :::{tip}
      Each model in the recipe can have different configurations (ROI, clearance, offset), allowing you to manage components with different features in the same application.
      :::
```

```{seealso}
For any issues with the steps just completed, refer to [Troubleshooting](troubleshooting)
```

---


