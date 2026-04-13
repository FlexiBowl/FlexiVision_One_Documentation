(hoppersetup)=
# **Step 5: Hopper Setup**

This section describes the procedure for configuring the hopper. The hopper is the component that automatically feeds parts onto the FlexiBowl when the fill level drops below a minimum threshold.

```{note}
**Prerequisites**

Before proceeding, make sure that:
- The Hopper has been installed mechanically
- Electrical connections have been completed, including control signals and power supply
- The FlexiBowl is already connected
```

---

## Accessing Hopper configuration

```{list-table}
* - **1**
  - From the main software page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - In the SETUP page, locate and click the **Hopper Setup** icon
    ```{dropdown} Setup page
       ![Setup page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - The Hopper configuration page opens
```

---

## Hopper Setup interface overview

The Hopper Setup page contains several sections for configuration of the operating parameters of the available hoppers:

![Hopper Setup page](../../../../../_shared/media/images/pagina_hoppersetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Enable Hopper**
  - Switch used to enable or disable Hopper usage in the system
* - **Steps**
  - Number of sequences required for the plate section currently in the viewing area to reach the hopper discharge area
* - **Time**
  - Hopper activation duration in milliseconds
* - **Signal**
  - Number of the digital signal used to control the Hopper
* - **Config Hopper**
  - Button used to configure the hopper in more detail later
```

---

## Configuration procedure

```{list-table}
:widths: 10 30 70
* - Step 1
  - Enable Hopper
  - Enable the **Enable Hopper** checkbox
* - Step 2
  - Configure Signal
  - In the **Signal** field, enter the digital output number used to control the Hopper
* - Step 3
  - Save and complete
  - Return to the main <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon"> page and continue with the next setup step
```

```{important}
Enable the Hopper only if the device is installed correctly.
```

```{warning}
It is essential to enter the correct signal number:
- A wrong number will activate the wrong signal, which can be dangerous
- Refer to the electrical diagram prepared during installation
- If in doubt, contact the person who performed the wiring
```

```{tip}
The parameters set at this stage are sufficient for initial system configuration.
The remaining aspects of hopper behavior will be defined later in the guided procedure.
```

---

(confighopper)=
# **Hopper Configuration**

Hopper configuration allows automatic replenishment of components onto the FlexiBowl® plate. The system uses vision to determine when the fill level is insufficient and when the hopper must be activated.

## **Step 1: Access the configuration**

```{list-table}
* - **1**
  - Click the <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon"> section
* - **2**
  - In the **Hopper Setup** section, connected loading units can be displayed and managed

    :::{dropdown} Hopper Setup page
    ![Hopper Setup page](../../../../../_shared/media/images/pagina_hoppersetup.png)
    :::
* - **3**
  - Select **Enable Hopper X** to activate the corresponding hopper
* - **4**
  - Click **Config Hopper X** to access the specific configuration
```

## **Step 2: Define the control area**

:::{video} ../../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
    :width: 100%
    :align: center
:::

In this phase, the portion of the plate that the camera must monitor for hopper discharge is defined.

```{list-table}
* - **5**
  - Modify the blue box on screen so it frames the area where the components will be detected.
   **Support tools**:
      * **Info**: click to display details about the page functions.
```

## **Step 3: Define the threshold values**

:::{video} ../../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
:width: 100%
:align: center
:::

```{list-table}
* - **6**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> to open the **Define Value Hopper Cam** page, where the system is instructed to distinguish between an empty plate and a full plate.
    :::{dropdown} Define Value Hopper Cam page
    ![Define Value Hopper Cam page](../../../../../_shared/media/images/pagina_valuehopper.png)
    :::
* - **7**
  - Remove all components from the viewing area and click the first **CAPTURE** button.
* - **8**
  - Position the minimum number of components that must remain in the viewing area. If the number drops below this threshold, the hopper will activate.
* - **9**
  - Click the second **CAPTURE** button.
* - **10**
  - By clicking <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> in the Expression Builder, the system automatically calculates **Mean** and **Standard Deviation** values.
* - **11**
  - Remove some parts and click <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">.
* - **12**
  - Observe the result indicator:
    - **Green** 🟢: insufficient level, Hopper activates, discharge required
    - **Red** 🔴: sufficient level, Hopper does not activate

      :::{warning}
      **Insufficient calibration**

      If the system does not detect the level correctly:

      **Problem: always green, Hopper always activates**  
      -> Threshold too low or interference in the area  
      -> Solution: increase the number of parts in the second acquisition and verify area cleanliness

      **Problem: always red, Hopper never activates**  
      -> Threshold too high or monitoring area not representative  
      -> Solution: reduce the number of parts in the second CAPTURE acquisition and repeat AUTO

      **Problem: incorrect behavior, random green-red alternation**  
      -> Unstable lighting or area too small  
      -> Solution: verify stable backlight, enlarge the monitoring area, and repeat calibration
      :::
```

```{note}
**Fill Hopper Threshold** = ...
```

## **Step 4: Operating parameters**

Return to the main Hopper Setup screen to define the mechanical behavior.

![Hopper Setup page](../../../../../_shared/media/images/pagina_hoppersetup.png)

```{list-table} Operating Parameters
:widths: 20 80
:header-rows: 1

* - **Parameter**
  - **Description and procedure**
* - **Steps**
  - Number of FlexiBowl advances, or sequences, needed to bring parts from the viewing area to the hopper discharge area.

    :::{note}
    **How to calculate it**

    :::::{list-table}

    * - 1.
      - Empty the FlexiBowl plate completely
    * - 2.
      - Leave one component in the center of the viewing area
    * - 3.
      - Execute FlexiBowl sequences until the component reaches the hopper discharge area and count how many advances were needed
    * - 4.
      - The resulting count is the value to enter in **Steps**
    :::::
    :::

* - **Time**
  - Hopper activation time in milliseconds. Recommended value: **100-1000 ms**, average **500 ms**. Adjust by about ±50 ms according to the desired flow.
```

```{tip}
Activation time depends not only on the configured value, but also on the volume of components currently present in the hopper bowl. Maintaining a constant load is essential for a uniform flow.
```

```{tip}
The **Time** value is strictly connected to hopper load volume:
- With a full hopper, more parts will reach the discharge area
- With a half-full hopper, fewer parts will reach the discharge area

An effective activation time depends on:
  :::{list-table}
  :header-rows: 1

  * - **Part weight** (*)
    - **Part behavior**
    - **Hopper load volume**
    - **Recommended Time**

  * - **Heavy parts**
    -
      - Tend to jam
      - Do not jam
    -
      - Less than 30%
      - Between 50% and 80%
    -
      - Time greater than 600 ms
      - Time greater than 600 ms

  * - **Light parts**
    -
      - Tend to jam
      - Do not jam
    -
      - Less than 30%
      - Between 50% and 80%
    -
      - Time between 100 and 500 ms
      - Time between 100 and 500 ms
  :::

 **General best practice**: keep the hopper constantly filled between 50% and 80% to obtain a uniform flow

 (*) **Part weight** is intended relative to the size of the hopper being used.
```

:::{important}
In general, it is important never to exceed the maximum load of the hopper being used.
:::

## Saving the configuration

```{warning}
**Saving the recipe is mandatory**

At the end of Hopper configuration:

  :::{list-table}
    * - 1.
      - Verify that all parameters are configured correctly:
        - monitoring area positioned
        - thresholds calibrated, TEST working
        - Steps and Time set
    * - 2.
      - Return to the main page <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon icon-small">
    * - 3.
      - Click <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon icon-small">
    * - 4.
      - Confirm the save
  :::
**IMPORTANT**: every change is stored **ONLY** if the recipe is saved correctly before exiting or changing page.

Without saving, all Hopper settings will be lost when FlexiVision One is closed.
```

---

## Hopper troubleshooting

### Common problems and solutions

```{warning}
**Hopper never activates**

**Symptoms**: the plate becomes empty but the Hopper does not discharge

**Possible causes:**
- Threshold configured too low, so the system always thinks the plate is full
- Monitoring area positioned incorrectly and not representative
- Enable Hopper disabled

**Solutions:**
1. Verify that Enable Hopper is active
2. Repeat threshold calibration using more parts in the second acquisition
3. Move the monitoring area to a more representative zone
4. Execute TEST manually to verify the trigger
```

```{warning}
**Hopper activates too frequently**

**Symptoms**: the Hopper discharges continuously and the plate becomes overfilled

**Possible causes:**
- Threshold configured too high
- Discharge time too long
- Monitoring area placed in a zone that is always empty

**Solutions:**
1. Reduce the threshold, meaning fewer parts in the second CAPTURE acquisition
2. Reduce **Time** by 100 to 200 ms
3. Verify monitoring area positioning
```

```{warning}
**Discharged parts do not arrive in time**

**Symptoms**: the robot still finds the plate empty immediately after Hopper activation

**Possible causes:**
- Steps too low, so parts do not have enough time to arrive
- FlexiBowl sequences not effective
- Obstruction in the discharge path

**Solutions:**
1. Increase **Steps** by 1 or 2 units
2. Verify FlexiBowl configuration parameters, such as speed and angle
3. Physically inspect the Hopper to plate discharge path
```

---

## Next steps

Once Hopper Setup is completed, or skipped if no hopper is present, continue with:

**[Step 6: Robot Setup](13c_Robot_Setup.md)** - configuration of robot communication
