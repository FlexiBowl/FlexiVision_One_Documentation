(roitest)=
# **ROI Definition and Tolerances**

In this section, the Region Search and recognition tolerances for the created model are defined. These parameters determine where FlexiVision One will search for components during operation and how strict detection will be.

**What is the Region Search?**  
The **Region Search** is the area within which FlexiVision One searches for and detects the components to be picked.

# Procedure

After clicking **Next** on the training page, the **Define Robot Picking Limit Area Model** page opens automatically.

![Define Robot Pick Area page](../../../../../_shared/media/images/pagina_definerobotpickarea.png)

## **Step 1: Define the area**

:::{video} ../../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **1**
  - In the **Define Robot Picking Limit Area Model** page, modify the rectangle to delimit the search area
* - **2**
  - Once the Region Search is correctly sized, click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
* - **3**
  - The **Locator Model 1 Cam 1** page opens
```

```{tip}
Size the area according to the actual robot working space, avoiding unreachable zones.
```

### Locator Model interface overview

![Locator Model page](../../../../../_shared/media/images/pagina_locatormodel.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Description
* - **Test**
  - Executes a real-time recognition test using the current parameters
* - **Accept Threshold**
  - Minimum score that a component must achieve to be accepted
* - **Results Panel**
  - Panel showing all detected components with details such as ID, coordinates, and score
```

### **Video tutorial**

Video tutorial explaining the following Step 2 and Step 3:

:::{video} ../../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
    :width: 100%
    :align: center
:::

## **Step 2: Prepare the scene**

```{list-table}
:widths: 5 95

* - **4**
  - Place **additional components** randomly within the viewing area around the reference component, making sure they cannot be confused with it.

    :::{warning}
    Do not touch the reference component used for training, and never lose sight of it.
    :::
```

## **Step 3: Run the test and set Accept Threshold**

```{list-table}
:widths: 5 95

* - **5**
  - Click <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon"> to run recognition

* - **6**
  - Observe how many components are detected and with which scores

* - **7**
  - Adjust the **Accept Threshold** according to application needs

    :::{note}
    **What is Accept Threshold?**

    It is the **minimum score** that a detected component must have compared to the reference model in order to be accepted.

    - **Value 0.95** -> accepts only components with score >= 95%
    - **Value 0.80** -> accepts components with score >= 80%
    - **Higher value** -> more restrictive, fewer false positives
    - **Lower value** -> more permissive, also detects components less similar to the reference one
    :::
```

```{tip}
**Recommended iterative approach**

1. Start with `Accept Threshold = 0.85`
2. Run **Test** and observe the results
3. If **too many parts are accepted**, including false positives, increase the threshold, for example to `0.90`
4. If **too few parts are detected**, meaning good parts are rejected, decrease the threshold, for example to `0.80`
5. Repeat until the optimal value for the application is found

**Goal**: find the highest possible value that still detects all good parts while rejecting the poorer ones.
```

---

## Result interpretation

### Display of detected components

The Results panel shows all detected components that meet the Accept Threshold:

```{list-table}
:header-rows: 1
:widths: 15 25 60

* - Field
  - Type
  - Description
* - **Id**
  - Integer
  - Progressive unique identifier, such as 0, 1, 2, and so on
* - **X**
  - Millimeters
  - X coordinate of the component, referenced to the calibration grid origin
* - **Y**
  - Millimeters
  - Y coordinate of the component, referenced to the calibration grid origin
* - **Rotation**
  - Degrees
  - Rotation angle of the component, 0 to 360 degrees
* - **Score**
  - Percentage
  - Similarity level with respect to the reference model, from 0.00 to 1.00
```

```{admonition} Priority System
:class: info
By default, FlexiVision One automatically sorts all recognized components by **descending score**:
- **Id 0** -> component with the highest score, most similar to the reference model
- **Id 1** -> second best component
- **Id 2** -> third best component
- and so on
```

### Example interpretation

Assume that after the test the following results appear:

| Id | X | Y | Rotation | Score |
|----|-------|-------|----------|-------|
| 0 | 125.4 | -45.2 | 15.3° | 0.92 |
| 1 | -80.1 | 32.5 | 178.5° | 0.89 |
| 2 | 45.7 | 110.3 | 92.1° | 0.86 |
| 3 | -150.2 | -95.7 | 45.8° | 0.83 |

**Interpretation:**
- **Id 0**: best match, 92%, and it will be picked first
- **Id 1**: good match, 89%, second option
- **Id 2**: fair match, 86%, third option
- **Id 3**: acceptable match, 83%, fourth option

If Accept Threshold were `0.85`:
- Id 0, 1, and 2 would be accepted
- Id 3 would be rejected because `0.83 < 0.85`

---

# Finalization

## **Step 4: Clean up and continue**

```{list-table}
* - **8**
  - Remove **all components** from the area, **except the reference component** and the two objects at its sides
    :::{danger}
      **Do not move the reference component**
      Even while cleaning the scene, take care not to hit or move the reference component. Its coordinates are still required for robot calibration in the final phase.
    :::
* - **9**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> -> the **Clearances** page opens
```

```{seealso}
Proceed to [Clearance Configuration](istogrammi) to define free areas.
```
