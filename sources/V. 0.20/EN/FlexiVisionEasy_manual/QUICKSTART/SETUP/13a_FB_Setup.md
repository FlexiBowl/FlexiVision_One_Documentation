(fbsetup)=
# **Step 4: FlexiBowl Setup**

This section describes the procedure for connecting and configuring the FlexiBowl with the FlexiVision One system.

```{note}
**Prerequisites**

Make sure that:
- Mechanical installation of all components has been completed ([Mechanical Installation](Installazione_Meccanica))
- All cables are connected correctly ([Wiring and Connections](cablaggio))
```

---

## Accessing FlexiBowl configuration

```{list-table}
* - **1**
  - From the main software page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - In the SETUP page, locate and click the **FlexiBowl Setup** icon
    ```{dropdown} Setup page
       ![Setup page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - The FlexiBowl configuration screen opens
```

![FlexiBowl Setup page](../../../../../_shared/media/images/pagina_FBsetup.png)

---

## Connection procedure

### **Step 1: Configure the network address**

```{list-table}
* - **4**
  - Verify that the address is on the same subnet as the VisionController

* - **5**
  - In the **FlexiBowl IP** field, enter the FlexiBowl IP address
      - Format: `192.168.1.XXX`, or according to your network configuration
```

:::{tip}
For consistency and convenience, start from the first available FlexiBowl.
:::

:::{note}
The FlexiBowl is shipped with default IP address `192.168.1.10`
:::

### **Step 2: Test the connection**

```{list-table}
:widths: 5 95

* - **6**
  - After entering the IP address, click **Connection Test**

* - **7**
  - The system performs a communication test, or ping, toward the FlexiBowl

* - **8**
  - Check the **Status** indicator:
    - 🟢 **Green**: connection established correctly
    - 🔴 **Red**: connection failed, verify IP address and wiring
```

```{warning}
**Connection failed**

If the indicator remains red or an error message appears:

0. Verify that the FlexiBowl is powered on
1. Verify that the entered IP address is correct
2. Physically check the Ethernet cable and ensure it is fully inserted
3. If present, verify that the network switch or router is powered on
4. Make sure the FlexiBowl and VisionController are on the same subnet
5. Try pinging the FlexiBowl from a Windows terminal:
   - Open Command Prompt
   - Type: `ping 192.168.1.XXX`, replacing with the real IP
   - If ping fails, the issue is network-related

If the problem persists, refer to [Troubleshooting](troubleshooting).
```

---

## FlexiBowl parameter configuration

Once the connection has been established, continue with configuration of the operating parameters.

### **Step 3: Access the configuration**

```{list-table}
* - **9**
  - Click <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **10**
  - A window opens with the configurable FlexiBowl parameters
```

### **Step 5: Synchronize parameters**

```{list-table}

* - **12**
  - Click **Synchronize Parameters**
* - **13**
  - Return to the main SETUP page and continue with the next setup step
```

```{warning}
**Do not skip synchronization**

It is essential to click **Synchronize Parameters** after every modification. Without this step:
- Changes are not applied to the FlexiBowl
- The system may behave inconsistently
- Settings are not saved
```

---

(configfb)=
# **Guided Configuration: FlexiBowl® Wizard**

The **FlexiBowl® Wizard** interface is an interactive tool designed to guide the user through configuration of feeding parameters based on the specific product family to be handled.

## **Step 1: Access the Wizard**

To start the procedure:

```{list-table}
:widths: 5 95

* - **1**
  - Go to the <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon"> section of the FlexiVision One software

* - **2**
  - Click **FlexiBowl Setup**. A page opens showing all FlexiBowls managed by FlexiVision One

    :::{dropdown} FlexiBowl Setup page
    ![FlexiBowl Setup page](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **3**
  - Click <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl">. A page opens with all movements available for the selected FlexiBowl

    :::{dropdown} FlexiBowl Configuration page
    ![FlexiBowl Config page](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **4**
  - Click **FlexiBowl X Wizard** to open the Wizard welcome page

* - **5**
  - Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">

    :::{note}
    Click <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> on each Wizard page to move forward through the guided configuration.
    :::
```

## **Step 2: Select model and rotation**

In this phase, the hardware characteristics of the system are defined:

```{list-table}
* - **6**
  - Select the device size, for example 200, 350, 500, and so on.
* - **7**
  - Define the plate rotation direction, **Clockwise** or **CounterClockwise**.
```

## **Step 3: Component characterization**

The system requires information about part morphology to optimize separation.

```{list-table}
* - **8**
  - Select the geometry that best describes the component:
      * **FLAT**: flat components
      * **CYLINDRICAL**: cylindrical components
      * **COMPLEX**: articulated or irregular geometries
* - **9**
  - Define how the components interact with each other on the surface:
      * **Overlapping**: parts tend to overlap
      * **Not Overlapping**: parts do not overlap
      * **Tangling / Stacking**: parts tend to hook or stack together
      * **Not Tangling / Not Stacking**: parts remain separated and do not interlock
```

## **Step 4: Accessory tests**

```{list-table}
* - **10**
  - Select from the dropdown menu whether the FlexiBowl® is equipped with the **Air-blow** module
* - **11**
  - Click **TEST Air-blow** to verify operation
* - **12**
  - Select **USE** to enable it in the current application, otherwise click **DON'T USE**
* - **13**
  - Click **TEST FLIP** to verify actual striker activation.  
      Flip is the unit that generates the mechanical impulse used to turn parts over. It is essential for separating, disentangling, or overturning components during the feeding cycle.

      :::{important}
      If the impulse is not noticeable, verify that compressed air is connected and adjust the mechanical pressure regulator located on the control panel.
      :::
* - **14**
  - At the end of the Wizard, by clicking **FINISH**, the system automatically calculates:
    - movement parameters, speed, acceleration, angle
    - shake parameters
    - accessory timings, flip and blow
* - **15**
  - These values can then be fine-tuned in the summary dashboard
```

```{list-table} Parameter Overview
   :widths: 20 30 50
   :header-rows: 1

   * - Group
     - Parameter
     - Description
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Main plate movement parameters
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Timing management for accessory activation
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Shake vibration parameters for part separation
```

## **Step 5: Validate the sequence**

Use **Test Sequence** to verify that the cycle meets the following efficiency criteria:

```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronization**
  - The Flip impulse must end exactly when the movement, or *Move*, ends. Adjust *Flip Count* and *Delay* values to align them.

* - **Image stability**
  - Components must be still at the moment the camera captures the image.
    - If the parts move, reduce speed or acceleration, or add a pause such as `pause 200ms`
```

:::{warning}
Always click **Synchronize Parameters** after every manual change so the variations become active in the controller.
:::

## FlexiBowl parameter overview

```{list-table}
:header-rows: 1
:widths: 5 25 70

* - ID
  - Element
  - Description
* - 1
  - MOVE - Acceleration
  - Acceleration value used for each MOVE command
* - 2
  - MOVE - Deceleration
  - Deceleration value used for each MOVE command
* - 3
  - MOVE - Speed
  - Speed value in rpm used for each MOVE command
* - 4
  - MOVE - Angle
  - Angle used by FlexiBowl® for each MOVE command
* - 5
  - SHAKE - Acceleration
  - Acceleration value used for each SHAKE command
* - 6
  - SHAKE - Deceleration
  - Deceleration value used for each SHAKE command
* - 7
  - SHAKE - Speed
  - Speed value in rpm used for each SHAKE command
* - 8
  - SHAKE - Angle CW
  - Clockwise angle used by FlexiBowl® for each SHAKE command
* - 9
  - SHAKE - Angle CCW
  - Counterclockwise angle used by FlexiBowl® for each SHAKE command
* - 10
  - OPTION - Flip Count
  - Number of Flip activations to be executed
* - 11
  - OPTION - Flip Delay
  - Time in milliseconds between one flip activation and the next deactivation
* - 12
  - OPTION - Blow Time
  - Time in milliseconds for blow activation
* - 13
  - OPTION - Light ON
  - Press to enable or disable the backlight
```

## Next steps

Once FlexiBowl configuration is complete, continue with:

**-> [Hopper Configuration](../23_Config_Hopper.md)** - if an external hopper is present

**-> [Verify Results](../24_Verifica_Risultati.md)** - monitor the complete application

```{tip}
**Production test**

Before going into production:
1. Run 50 to 100 test cycles to verify consistency
2. Monitor the plate fill rate, which should remain constant
3. Verify that there are no abnormal accumulations or persistent empty zones
4. Increase gradually toward production speed

The optimal configuration may require two or three fine-tuning sessions with the real part in significant quantity.
```

## Next steps

Once FlexiBowl Setup is completed, proceed with:

- [Step 5: Hopper Setup](13b_Hopper_Setup.md)
- [Step 6: Robot Setup](13c_Robot_Setup.md)
