(roitest)=
# **ROI Definition and Tolerances**

In this section, the Region Search and identification tolerances for the created model are defined. These parameters determine where and with what precision FlexiVision One will search for components during operation.

**What is the Region Search?**
The **Region Search** is the area within which FlexiVision One will search and detect components to be picked.

# Procedure

After clicking 'Next' on the training page, the **Define Robot Picking Limit Area Model** page opens automatically.



## Step 1: Area Definition

:::{video} ../../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **1**
  - On the **Define Robot Picking Limit Area Model** page, edit the box to delimit the search area
* - **2**
  - Once the Region Search is correctly sized, click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
* - **3**
  - The **Locator Model 1 Cam 1** page will open
```
```{tip}
Size the area according to the robot's actual working space, avoiding unreachable areas.
```
:::{tip}
If you have any doubts during configuration, please consult the **INFO** key on the current page.
:::

### *Locator Model interface overview*

![Locator Model page](../../../../../_shared/media/images/pagina_locatormodel.png)
```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Description
* - **Test**
  - Performs a real-time identification test with the current parameters
* - **Accept Threshold**
  - Minimum fidelity threshold (score) that a component must have in order to be accepted
* - **Results Panel**
  - Panel showing all detected components with details (Id, coordinates, score)
```
### Video Tutorial
Video tutorial explaining the subsequent Step 2 and Step 3:
:::{video} ../../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
    :width: 100%
    :align: center
:::




## Step 2: Scene Preparation
```{list-table}
:widths: 5 95

* - **4**
  - Place **other components** in the vision area randomly around the reference component so as not to confuse them with it.
    
    :::{warning}
    Do not touch the reference component used for training! And don't lose sight of it!
    :::
```

## Step 3: Test Execution and Accept Threshold
```{list-table}
:widths: 5 95

* - **5**
  - Click <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon"> to run identification

* - **6**
  - Observe how many components are detected and with which scores

* - **7**
  - Change the **Accept Threshold** according to application needs
    
    :::{note}
    **What is the Accept Threshold?**
    
    It's the **minimum degree of fidelity** (score) that a detected component must have with respect to the reference model to be accepted.
    
    - **Value 0.95** → Accept only components with fidelity ≥ 95%
    - **Value 0.80** → Accept components with fidelity ≥ 80%
    - **Highest value** → More restrictive (fewer false positives)
    - **Lowest value** → More permissive (also detects components less similar to the reference model)
    :::
```
```{tip}

**Recommended iterative approach:**

1. Start with Accept Threshold = 0.85
2. Run Tests and see results
3. If **too many parts accepted** (including false positives) → Increase threshold (e.g: 0.90)
4. If **too few parts detected** (good pieces discarded) → Decrease threshold (e.g: 0.80)
5. Repeat until the optimum value for the application is found

**Goal**: Find the highest possible value that detects all the good parts but rejects the worst ones.
```
:::{tip}
If you have any doubts during configuration, please consult the **INFO** key on the current page.
:::

---

## Interpreting Results

### *Display of detected components*

The Results panel shows all detected components that meet the Accept Threshold criteria:
```{list-table}
:header-rows: 1
:widths: 15 25 60

* - Field
  - Type
  - Description
* - **Id**
  - Integer
  - Progressive unambiguous identifier (0, 1, 2, ...)
* - **X**
  - Millimetres
  - X-coordinate of the component (reference origin of the calibration grid)
* - **Y**
  - Millimetres
  - Y-coordinate of the component (reference origin of the calibration grid)
* - **Rotation**
  - Degrees
  - Angle of rotation of the component (0-360°)
* - **Score**
  - Percentage
  - Degree of fidelity compared to the reference model (0.00-1.00)
```
```{admonition} Priority System
:class: info
FlexiVision One by default automatically sorts all components identified by **decreasing score**:
- **Id 0** → Component with highest score (most similar to the reference model)
- **Id 1** → Second best component
- **Id 2** → Third best component
- And so on...
```
### *Interpretation example*

Let's suppose that these results appear after the Test:

| Id | X | Y | Rotation | Score |
|----|-------|-------|----------|-------|
| 0 | 125.4 | -45.2 | 15.3° | 0.92 |
| 1 | -80.1 | 32.5 | 178.5° | 0.89 |
| 2 | 45.7 | 110.3 | 92.1° | 0.86 |
| 3 | -150.2 | -95.7 | 45.8° | 0.83 |

**Interpretation:**
- **Id 0**: Best match (92%), will be picked first
- **Id 1**: Good match (89%), second option
- **Id 2**: Fair match (86%), third option
- **Id 3**: Acceptable match (83%), fourth option

If Accept Threshold were 0.85:
- Id 0, 1, 2 would be accepted
- Id 3 would be rejected (score 0.83 < 0.85)

---

# Finalisation

## Step 4: Cleaning and Continuation
```{list-table}
* - **8**
  - Remove **all components** from the area, **except the reference component** and the two objects at its sides
    :::{danger}
      **Do not move the reference component!**
      Even when cleaning the scene, take care not to bump or move the reference component. Its coordinates are still needed for robot calibration in the final phase.
    :::
* - **9**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> → the **Clearances** page will open
```
```{seealso}
Proceed to the [Clearances Configuration](istogrammi) to define the clear areas.
```

