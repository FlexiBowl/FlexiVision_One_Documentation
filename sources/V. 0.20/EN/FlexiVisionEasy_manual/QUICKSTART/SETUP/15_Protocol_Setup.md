(protocol_setup)=
# **Step 7: Protocol Setup**

The **Protocol Setup** page allows configuration of the parameters that regulate communication flow and data exchange between the FlexiVision One vision system and the robot. These parameters determine how many objects are sent, how they are sorted, and how the system manages statistics and operating states.

```{note}
**Position of Protocol Setup in the workflow**

Protocol Setup is typically configured:
- **After**: robot calibration and model creation
- **Before**: continuous production monitoring

This is because:
- It requires understanding of robot behavior, such as speed and gripper type
- It affects the statistics shown in the Dashboard
- It is the last configuration step before real production

Once configured correctly, it rarely requires changes unless the robot or the operating mode changes.
```

---

## Accessing Protocol Setup

1. From the main menu, access the section dedicated to the communication protocol
2. Select **Protocol Setup**
3. The interface opens with the configurable parameters

---

## Configurable parameters

![Protocol Setup page](../../../../../_shared/media/images/pagina_protocolsetup.png)

```{list-table}
:header-rows: 1
:widths: 35 65

* - **Parameter**
  - **Description and function**
* - [**Max Object Count Return**](maxobject)
  - Indicates the **maximum** number of objects, meaning coordinate triplets, that the vision system can return to the robot in a single run. If vision detects more objects than this limit, no more than this number will be sent, selected according to the configured sorting criterion.
* - [**Min Object Count Return**](minobject)
  - Indicates the **minimum** number of objects that must be returned in one run for the result to be considered valid. If the number is below this threshold, the run is considered invalid.
* - [**Sorting Mode Results**](sortingmode)
  - Defines the **sorting criterion** used to order the list of objects returned by the vision system. This parameter determines pick priority and which objects are included in the Max Object Count Return.

    *Typical option:* descending score.
* - [**Pickable parts by the robot detected by vision in each cycle**](pickableparts)
  - Indicates how many picks the robot performs for each vision run. For example, a double pick corresponds to value `2`. It does not represent the number of objects detected by vision, but the number of robot picks per cycle. This parameter is used for statistical calculations.

* - [**Maximum processing time per part with the robot (in seconds)**](maxprocessingtime)
  - Defines the maximum reference time after which the system considers handling or transmission of the coordinates related to a run completed and typically switches from RUN to IDLE. This parameter is used for **statistics and workflow management**.

    :::{attention}
    **It is not a robot error timeout**, but a time reference used for cycle calculation and productivity metrics.
    :::
```

---

## Detailed parameter configuration

(maxobject)=
### Max Object Count Return

```{list-table}
 :class: align-top

* - **Function**:
  - Limits the maximum number of coordinates sent to the robot for each vision cycle.

* - **Typical values:**
  -
    - **1-3 objects**: most common configuration for robots with single, double, or triple picking
    - **4-8 objects**: for systems with a buffer or fast robots able to manage queues
    - **>8 objects**: rarely required and may saturate communication

    :::{tip}
    **How to choose the value:**
    1. Consider robot speed, meaning pick-and-place time per part
    2. Consider the vision plus FlexiBowl cycle time
    3. Approximate formula: `Max Count = (Vision+FlexiBowl cycle time) / (Robot pick time)`

    **Practical example:**
    - Vision plus FlexiBowl cycle: 3 seconds
    - Robot pick time: 2 seconds per part
    - Optimal Max Count: 3/2 = 1.5 -> round to 2 objects
    :::
```

(minobject)=
### Min Object Count Return

```{list-table}
* - **Function**:
  - Sets the minimum number of coordinates sent to the robot for each vision cycle.

* - **Typical values:**
  -
    - **1**: most common configuration, even a single recognized part is acceptable
    - **>2**: only for special applications with mandatory multi-pick

* - **System behavior:**
  -
    - **Detected objects >= Min Count**: coordinates are sent to the robot
    - **Detected objects < Min Count**: coordinates are not sent and the FlexiBowl sequence is executed

* - **Impact on productivity**
  -
    **Min Count = 1** (more permissive):
    - ✓ Maximum flexibility, the robot works even if only one part is available
    - ✗ Possible low-efficiency cycles, such as 1 part every several seconds

    **Min Count = 3** (more restrictive):
    - ✓ Ensures a minimum cycle efficiency
    - ✗ May cause waiting time if filling is variable
```

(sortingmode)=
### Sorting Mode Results

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sorting mode
  - Description and when to use it
* - **By Score (Descending)**
  - Sorts by score from highest to lowest. Objects with the best match to the model are sent first.  
    **Most common and recommended**: ensures picking starts from the most reliably recognized parts.
* - **By Score (Ascending)**
  - Sorts by score from lowest to highest. Objects with the weakest match to the model are sent first.  
    **NOT RECOMMENDED**: does not ensure picking starts from the most reliable detections.
* - **By X Coordinate (Ascending)**
  - Sorts by increasing X coordinate. Useful if the robot prefers sequential picking along one axis.
* - **By X Coordinate (Descending)**
  - Sorts by decreasing X coordinate.
* - **By Y Coordinate (Ascending)**
  - Sorts by increasing Y coordinate.
* - **By Y Coordinate (Descending)**
  - Sorts by decreasing Y coordinate.
* - **X Alternating**
  - Alternates ordering along the X axis.
* - **Y Alternating**
  - Alternates ordering along the Y axis.
```

```{tip}
**Choosing the optimal sorting mode**

**Recommended in most cases: By Score (Descending)**

**Advantages**:
- Maximum reliability: the robot always picks the best recognized parts first
- Reduces the risk of incorrect picks
- Independent of physical position
```

```{note}
Sorting mode interacts with Max Object Count. The first objects according to the selected criterion are the ones returned.
```

(pickableparts)=
### Pickable parts by the robot - **Robot picks per vision cycle**

**Function**

Statistical parameter indicating how many parts are **actually picked** by the robot for each vision cycle.

**Typical values**

- **1**: robot with a single gripper, picks one part at a time
- **2**: robot with a double gripper or double suction cup
- **>2**: robot with a multi-pick gripper or suction tool

```{important}
This value represents the **physical picks**, not the number of objects detected by the vision system.
```

**Clarifying example**

Scenario: double gripper, vision detects 5 objects.

- If you want to send a maximum of 2 objects to the robot, set `Max Object Count = 2`.
- If you want the robot to pick at least 2 objects at a time, set `Min Object Count = 2`.
- In this case, set `Pickable Parts by the robot = 2`.
- If you also want to allow picking only one object, set `Max Object Count = 2`, `Min Object Count = 1`, and `Pickable Parts by the robot = 2`.

**Impact on Dashboard statistics**

This parameter is crucial for accurate **Parts Per Minute (PPM)** calculation.

- Formula: `PPM = (Pickable parts x 60) / Total cycle time in seconds`
- If set incorrectly, the displayed PPM will not reflect reality

(maxprocessingtime)=
### Maximum processing time per part

```{list-table}
* - **Function**:
  - Reference time in seconds used by the system to determine when a cycle is considered complete and when to switch from RUN to IDLE.

* - **Typical values:**
  -
    - Set the value slightly above the real robot handling time per part
    - Increase it if the robot performs complex movements or waiting phases

* - **How to calculate it**:
  -
    - Measure the average handling time per part, from coordinate receipt to completed pick
    - Add a small safety margin to cover normal variability

* - **Impact on Dashboard processing time**
  -
    - Influences productivity metrics and displayed cycle statistics
    - If set too low, cycles may appear artificially short
    - If set too high, cycle closure may appear delayed in statistics
```

---

## Saving the configuration

```{warning}
**Saving is mandatory**

After configuring the Protocol Setup parameters:

1. Verify that all values are set correctly
2. Click **Recipes > Save Recipe**
3. The parameters are saved in the system configuration
```

---

## Next steps

Once Protocol Setup is complete, the system is fully configured for operation:

**-> [Verify Results (Dashboard)](../24_Verifica_Risultati.md)** - production monitoring and configuration validation
