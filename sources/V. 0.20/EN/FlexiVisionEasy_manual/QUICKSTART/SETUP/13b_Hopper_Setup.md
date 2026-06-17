(hoppersetup)=
# **Hopper Setup**

This section describes the procedure for configuring the hopper. The Hopper is the component that automatically feeds parts to the FlexiBowl® when the level drops below a minimum threshold.

:::{important}  **Operating logic**

FlexiVision manages the hopper activation logic. It will in fact send the string `Hopper;signalnumber;time` when it considers activation necessary.
:::
```{note}
**Prerequisites**

Before proceeding, make sure that:
- The Hopper has been mechanically installed
- The electrical connections have been made (control and power signals)
- The FlexiBowl® is already connected
```
---
## Preparing the Physical Setup

````{list-table}
* - **0**
  - Remove the calibration grid and restore the initial layout:
    - Reposition the surface
    - Reposition the central flange
    - Fix the central flange with its four screws
````
---
## Accessing Hopper configuration

```{list-table}
* - **1** 
  - From the software main page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - On the SETUP page, locate and click the **Hopper Setup** icon
    ```{dropdown} Setup Page
       ![Setup Page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3** 
  - The Hopper configuration page opens
```

---

## Hopper Setup Interface Overview

The Hopper Setup page has several sections for configuring the operating parameters of the various hoppers:

![Hopper Setup Page](../../../../../_shared/media/images/pagina_hoppersetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Enable Hopper**
  - Switch to enable/disable the use of the Hopper in the system
* - **Steps**
  - Number of required sequences with which the section of the disc that is currently in the vision area arrives below the hopper unloading area
* - **Time**
  - Duration of hopper activation in milliseconds
* - **Signal**
  - Number of the digital signal used to control the Hopper
* - **Config Hopper**
  - Button to configure the hopper (to be used later)
```


---
(confighopper)=
# **Hopper configuration**

The hopper configuration allows you to manage the automatic filling of components on the FlexiBowl® disc. The system uses the vision to determine when the filling level is insufficient and to activate the hopper.

## Step 1: Accessing the Configuration
```{list-table}
* - **1**
  - Click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">.
    From the **Hopper Setup** section, you can view and manage the connected load units.
    
    :::{dropdown} Hopper Setup Page
    ![Hopper Setup Page](../../../../../_shared/media/images/pagina_hoppersetup.png)
    :::
* - **2**
  - In the **Signal** field, enter the number of the digital signal (DO - Digital Output) used to control the Hopper
    :::{warning}
      It is essential to enter the correct signal number:
      - An incorrect number will activate the wrong signal (potentially dangerous)
      - See the wiring diagram made during installation
      - If in doubt, contact the person who did the wiring
    :::
* - **3**
  - Tick the **Enable Hopper X** box to activate the corresponding hopper.
      :::{important}
      Only enable the Hopper if the device is correctly installed
      :::
* - **4**
  - Click the **Config Hopper X** button to access the specific configuration
```
## Step 2: Defining the Control Area

:::{video} ../../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
    :width: 100%
    :align: center
:::

In this step, the portion of the disc that the camera needs to monitor for unloading is defined.
```{list-table}
* - **5**
  - Change the blue box on the screen to frame the area where the components will be detected.
```
:::{tip}
If you have any doubts during configuration, please consult the **INFO** key on the current page.
:::

## Step 3: Definition of Threshold Values

:::{video} ../../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
:width: 100%
:align: center
:::
```{list-table}
* - **6**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> to access the **Define Value Hopper Cam** page, where the system learns how to distinguish between an empty and a full disk.
    :::{dropdown} Define Value Hopper Cam Page
    ![Define Value Hopper Cam Page](../../../../../_shared/media/images/pagina_valuehopper.png)
    :::
* - **7**
  - Remove all components from the vision area and click the first **CAPTURE** button.
* - **8**
  - Position the minimum number of components you wish to keep in the vision area. If the number drops below this threshold, the hopper will be activated.
* - **9**
  - Click the second **CAPTURE** button.
* - **10**
  - By clicking <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> in the Expression Builder, the system automatically calculates the **Mean** and **Standard Deviation** values.
* - **11**
  - Remove some pieces and click <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">.
* - **12**
  - Look at the result indicator:
    - **Green** 🟢: Insufficient level, Hopper is activated (unloading necessary)
    - **Red** 🔴: Sufficient level, Hopper is NOT ACTIVATED (OK)

      :::{warning}
      **Insufficient calibration**

      If the system does not detect the level correctly:

      **Problem: Always green (always activates Hopper)**
      → Threshold too low or interference in the area
      → Solution: Increase number of pieces in second capture, check that area is clean

      **Problem: Always red (never activates Hopper)**
      → Threshold too high or monitoring area not representative
      → Solution: Reduce number of pieces in second CAPTURE, repeat AUTO

      **Problem: Incorrect behaviour (green/red toggle randomly)**
      → Unstable lighting or area too small
      → Solution: Check stable backlight, enlarge monitoring area, repeat calibration
      :::
```
```{note}
**Hopper Fill Threshold**

The **Hopper Fill Threshold** parameter defines the filling percentage threshold of the vision area below which the hopper is automatically activated.

The value of 100% corresponds to the amount of pieces acquired during the second CAPTURE (full area). Consequently, a 50% threshold corresponds to half of that amount.

The system automatically sets the initial value to **70%**, which is a good balance for most applications.

**Ongoing modification**

It is possible to adjust the threshold without repeating the capture procedure:

- To unload **fewer pieces** → reduce the percentage (e.g. 50%) and click **AUTO**
- To unload **more pieces** → increase the percentage (e.g. 85%) and click **AUTO**

```

:::{tip}
If you have any doubts during configuration, please consult the **INFO** key on the current page.
:::

## Step 4: Operational Parameters

Return to the main Hopper Setup screen to define the mechanical behaviour.
![Hopper Setup Page](../../../../../_shared/media/images/pagina_hoppersetup.png)
```{list-table} Operating Parameters
:widths: 20 80
:header-rows: 1

* - **Parameter**
  - **Description and Procedure**
* - **Steps**
  - Number of FlexiBowl® feeds (sequences) required to bring parts from the vision area to the hopper unloading area.
* - **Time**
  - Milliseconds of hopper activation.   Recommended value: **100 – 1000 ms** (Average: **500 ms**). Adjust by ±50 ms according to the desired flow.
```
```{tip}
   The activation time depends not only on the set value, but also on the volume of components currently in the hopper tank. It is essential to maintain a constant load for an even flow.
```
```{tip}
The Time value is closely related to the hopper loading volume:
- With the hopper full, there will be more parts in the unloading area
- With the hopper half-full, there will be fewer parts in the unloading area

```
:::{important}
In general, it is important never to exceed the maximum load of the hopper used.
:::

### *Calculate the Steps Parameter*

![First Steps Page](../../../../../_shared/media/images/Steps1.png)
![Second Steps Page](../../../../../_shared/media/images/Steps2.png)
![Third Steps Page](../../../../../_shared/media/images/Steps3.png)
![Fourth Steps Page](../../../../../_shared/media/images/Steps4.png)

## Saving Configuration
```{warning}
**Saving recipe mandatory**

At the end of the Hopper configuration:

  :::{list-table}
    * - 1. 
      - Verify that all parameters are configured correctly:
        - Monitoring area positioned
        - Thresholds calibrated (TEST working)
        - Steps and Time set
    * - 2. 
      - Return to the main page <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon icon-small">
    * - 3. 
      - Click <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon icon-small">
    * - 4. 
      - Confirm saving
  :::
**IMPORTANT**: Any changes made are stored **ONLY** if the recipe is saved correctly before exiting or changing page.

Without saving, all Hopper setups will be lost when FlexiVision One is closed!
```

---


## Next steps

Once the Hopper Setup is complete (or skipped if not present), proceed with:

- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Save Recipe](ricettabase)



