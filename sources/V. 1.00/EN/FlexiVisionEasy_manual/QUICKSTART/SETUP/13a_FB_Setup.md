(fbsetup)=
# **FlexiBowl® Setup**

This section describes the procedure for connecting and configuring the FlexiBowl® with the FlexiVision One system. 

```{note}
**Prerequisites**

Make sure that:
- Mechanical installation of all components is completed ([Mechanical Installation](Installazione_Meccanica))
- All cables are correctly connected ([Wiring and Connections](cablaggio)) 
```

---

## Access the FlexiBowl® Setup
```{list-table}
* - **1** 
  - From the software home page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - On the SETUP page, identify and click the **FlexiBowl® Setup** icon
    ```{dropdown} Setup page 
       ![Setup Page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - The FlexiBowl® Setup screen opens
```
![FlexiBowl® Setup Page](../../../../../_shared/media/images/pagina_FBsetup.png)
---

## Connection procedure

### *Step 1: Network address configuration*

```{list-table}
* - **4**
  - Make sure that the address is on the same subnet as the VisionController
  
* - **5**
  - In the field **FlexiBowl® IP**, enter the IP address of the FlexiBowl®
      - Format: `192.168.1.XXX` (or depending on your network configuration)
```
:::{tip}
For the sake of convenience and consistency, start with the first FlexiBowl® available 
:::
:::{note}
The FlexiBowl® is shipped with a default IP address `192.168.1.10`
:::
:::{important}
For instructions on how to change the IP address of your FlexiBowl®, please refer to the manual available in the [Download](https://www.flexibowl.it/downloads) section.
:::

### *Step 2: Connection test*

```{list-table}
:widths: 5 95

* - **6**
  - After entering the IP, click the **Connection Test** button

* - **7**
  - The system performs a communication test (ping) to the FlexiBowl®

* - **8**
  - Watch the **Status** indicator:
    - 🟢 **Green**: Connection successful
    - 🔴 **Red**: Connection failed (check IP address and wiring)
```

```{warning}
**Connection failed**

If the indicator remains red or an error message appears:

0. Check that you have switched on the FlexiBowl®
1. Check that the IP address entered is correct
2. Physically check the Ethernet cable (it must be fully inserted)
3. If present, check that the network switch/router is on
4. Ensure that FlexiBowl® and VisionController are on the same subnet
5. Try pinging the FlexiBowl® from a Windows terminal:
   - Open Command Prompt
   - Type: `ping 192.168.1.XXX` (replace with actual IP)
   - If the ping fails, it is a network problem

If the problem persists, see [Troubleshooting](troubleshooting).
```

---

## FlexiBowl® parameter configuration

Once the connection is established, proceed to set the operating parameters.

### *Step 3: Configuration access*

```{list-table}
* - **9** 
  - Click the button <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **10**
  - A window opens with the configurable parameters of the FlexiBowl®
```


### *Step 4: Parameter synchronisation*

```{list-table}

* - **12**
  - Click **Synchronize Parameters**
* - **13**
  - Go back to the main SETUP page to proceed with the next setup 
```

```{warning}
**Do not skip the synchronisation**

It is essential to click **Synchronize Parameters** after any change is made. Without this step:
- The changes are not applied to the FlexiBowl® 
- The system may behave inconsistently
- The settings are not saved 
```
---
(configfb)=
# **Guided configuration: FlexiBowl® Wizard**


The **FlexiBowl® Wizard** interface is an interactive tool designed to guide the user in configuring feed parameters according to the specific product family to be managed.

## Step 1: Accessing the Wizard

To start the procedure:
```{list-table}
:widths: 5 95

* - **1**
  - Go to the <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon"> section of the FlexiVision One software

* - **2**
  - Click the **FlexiBowl® Setup** button. This will open a page with all the FlexiBowl® devices that can be managed with FlexiVision One

    :::{dropdown} FlexiBowl® Setup Page  
    ![FlexiBowl® Setup Page](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **3**
  - Click the button <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl"> to open a page with all available movements for the selected FlexiBowl

    :::{dropdown} FlexiBowl® Configuration Page  
    ![FlexiBowl® Config page](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **4**
  - Click the **FlexiBowl® X Wizard** button; the Wizard welcome page opens

* - **5**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">
    
    :::{note}
    Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> on each page of the wizard to move forward in the guided setup
    :::
```

## Step 2: Model Selection and Rotation

In this step, the hardware features of the system are defined:
```{list-table}
* - **6**
  - Select the size of the device (e.g. 200, 350, 500, etc.).
* - **7**
  - Define the direction of disc rotation (**Clockwise** or **CounterClockwise**).
```
## Step 3: Component Characterisation

The system requires information on the morphology of the parts to optimise separation.
````{list-table}
* - **8**
  - Select component size:**

    **For FlexiBowl Models 200, 350, 500, 650:**

    :::{card}
    <= 150mm
    :::

    :::{card}
    &gt; 150mm
    :::

    **For FlexiBowl Models 800 and 1200:**

    :::{card}
    <= 250mm
    :::

    :::{card}
    &gt; 250mm
    :::

* - **9**
  - Select the geometry that best describes the component:
      * **FLAT**: Flat components.
      * **CYLINDRICAL**: Cylindrical components.
      * **COMPLEX**: Articulated or irregular geometries

      ![Flat Cylindrical or Complex](../../../../../_shared/media/images/flatorcomplex.png)

      *Examples of geometries: Flat, Cylindrical and Complex.*

* - **10**
  - Define how the components interact with each other on the surface:
      * **Overlapping**: The pieces tend to overlap.
      * **Not Overlapping**: The pieces do not overlap.
      * **Tangling / Stacking**: The pieces tend to hook together or stack.
      * **Not Tangling / Not Stacking**: The pieces remain separate and do not interlock.

      ![Overlapping](../../../../../_shared/media/videos/overlapping.gif)

      *Not Overlapping: the pieces do not overlap on the surface.*

      ::::{grid} 2
      :::{grid-item}
      ![Stacking](../../../../../_shared/media/videos/stacking.gif)

      *Stacking: the pieces stack up.*
      :::
      :::{grid-item}
      ![Tangling](../../../../../_shared/media/videos/tangling.gif)

      *Tangling: the pieces get entangled with each other.*
      :::
      ::::
````
## Step 4: Testing of Accessories
```{list-table}
* - **11**
  - Select from the drop-down menu whether the FlexiBowl® is equipped with the **Air-blow** module.
* - **12**
  - Click **TEST Air-blow** to check that it works properly.
* - **13**
  - Select **USE** to enable it in the current application, otherwise click **DON'T USE**.
* - **14**
  - Click **TEST FLIP** to check the actual activation of the flip unit.
      The 'Flip' is the unit that generates the mechanical impulse to flip parts; it is essential for separating, untangling or flipping components during the feeding cycle.
 
      :::{important}
      If the pulse is not noticeable, verify that compressed air is connected and adjust the mechanical pressure regulator on the control panel.
      :::
* - **15**
  - At the end of the Wizard, clicking **FINISH**, the system will automatically calculate the parameters: 
    - Motion parameters (speed, acceleration, angle)
    - Shake parameters (shake)
    - Accessory timings (flip, blow)
* - **16**
  - They can then be fine-tuned in the summary dashboard.
```
```{list-table} Parameter Overview
   :widths: 20 30 50
   :header-rows: 1

   * - Group
     - Parameter
     - Description
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Main disc movement parameters.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Management of accessory activation timing.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Shake (separation) vibration parameters.
```

## Step 5: Sequence Validation

Use the **Test Sequence** function to check that the cycle meets the following efficiency criteria:
```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronisation**
  - The Flip impulse must end at exactly the same time as the movement (*Move*). Adjust the *Flip Count* and *Delay* values to align them.

* - **Image Stability**
  - The components must be still when the camera takes the picture.
    - If the pieces are moving, decrease speed/acceleration or insert a pause (e.g. `pause 200ms`).

* - **Positioning of pieces during the sequence**
  - During the movement, the pieces must be conveyed towards the centre of the FlexiBowl® range to maximise the effectiveness of the flip. At the end of the sequence, the pieces should practically be arranged in the centre of the vision area.
```

:::{warning}
Always click **Synchronize Parameters** after any manual change to activate the changes in the controller.
:::

## Overview of FlexiBowl® Parameters
```{list-table}
:header-rows: 1
:widths: 5 25 70

* - ID
  - Element
  - Description
* - 1
  - MOVE – Acceleration
  - Acceleration value used at each MOVE command
* - 2
  - MOVE – Deceleration
  - Deceleration value used at each MOVE command
* - 3
  - MOVE – Speed
  - Speed value (rpm) used at each MOVE command
* - 4
  - MOVE – Angle
  - Angle at which FlexiBowl® moves at each MOVE command
* - 5
  - SHAKE – Acceleration
  - Acceleration value used at each SHAKE command
* - 6
  - SHAKE – Deceleration
  - Deceleration value used at each SHAKE command
* - 7
  - MOVE – Speed
  - Speed value (rpm) used at each SHAKE command
* - 8
  - MOVE – CW angle
  - Clockwise angle at which FlexiBowl® moves at each SHAKE command
* - 9
  - MOVE – CCW angle
  - Counterclockwise angle at which FlexiBowl® moves at each SHAKE command
* - 10
  - OPTION – Flip count
  - Number of times Flip will be activated
* - 11
  - OPTION – Flip Delay
  - Time (in milliseconds) between an activation and a deactivation of the flip
* - 12
  - OPTION – Blow Time
  - Time (in milliseconds) for activating the blow
* - 13
  - OPTION – Light on
  - Press to enable/disable the backlight
```

```{tip}
**Production test**

Before using in production:
1. Run 50-100 test cycles to check consistency
2. Monitor disk fill rate (it must be constant)
3. Check that there are no abnormal accumulations or persistent empty zones
4. Gradually increase to production speed

The ideal configuration may require 2-3 fine-tuning sessions with the actual part in significant quantities.
```

## Next steps

Once the FlexiBowl® Setup is complete, proceed with:

- [Hopper Setup](13b_Hopper_Setup.md)
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Save Recipe](ricettabase)




