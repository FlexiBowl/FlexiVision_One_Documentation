(setupcomponenti)=
# **Initial System Configuration**

This section guides the user through the complete setup of the FlexiVision One hardware and software components. It is essential to follow the steps in the indicated order to ensure correct system operation.

```{note}
**Prerequisites**

Before starting software configuration, make sure that:
- Mechanical installation of all components has been completed ([Mechanical Installation](Installazione_Meccanica))
- All cables are connected correctly ([Wiring and Connections](cablaggio))
```

---

## Setup process overview

The initial configuration process consists of eight main steps:

0. **Enter the license key** supplied with the kit
1. **Login** - access the software using user credentials
2. If a backlight illuminator is present: **Configure the FlexiBowl IP address** and **turn on the backlight**
3. **Camera Setup** - configure the camera
4. **FlexiBowl Setup** - connection and configuration of the FlexiBowl
5. **Hopper Setup** - configuration of the hopper
6. **Robot Setup** - configuration of communication with the robot
7. **Protocol Setup** - configuration of protocol parameters
8. **Rename and save the base recipe** - configuration of the application profile

:::{note}
The complete setup flow diagram is not yet available as an exported image in this repository. Refer to the guided sequence described below.
:::

```{warning}
**Step order**

The setup sequence is important. Do not skip steps or change the order, because some configurations depend on previous ones.
```

---

## Preliminary operations

:::{important}
Before starting FlexiVision One, the first operation is entering the license key supplied with the kit.
:::

### Step 1: Login to the system

When FlexiVision One starts, the Home page is displayed.

```{list-table}
   :widths: 10 90
   :header-rows: 0
   * - **0**
     - Click **Setup**
   * - **1**
     - **Select user ARS** from the dropdown menu at the top right.
   * - **2**
     - **Enter password** `ArS2025`.
       *(Note: the field is case-sensitive).*
   * - **3**
     - Click **LOGIN** to access the interface.
```

```{tip}
**User management**

FlexiVision One supports multiple user profiles with different permission levels:
- **ARS**
- **Engineer**
- **Technician**
- **Operator**
```

---

### Step 2: Turn on the backlight if present

After the first login, if it is necessary to activate the FlexiVision One license, follow these steps:

```{list-table}
* - **1**
  - From the main software page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - In the SETUP page, identify and click the **FlexiBowl Setup** icon
    ```{dropdown} Setup page
       ![Setup page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - The FlexiBowl configuration screen opens
* - **4**
  - Enter the FlexiBowl IP address, default `192.168.1.10`
* - **5**
  - After entering the IP address, click **Connection Test**
* - **6**
  - The system performs a communication test, or ping, to the FlexiBowl
* - **7**
  - Check the **Status** indicator:
    - 🟢 **Green**: connection established correctly
    - 🔴 **Red**: connection failed, verify IP address and wiring
* - **8**
  - Click <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **9**
  - A window opens with the configurable FlexiBowl parameters
* - **10**
  - Turn on the backlight by enabling the `"Light ON"` checkbox
```

---

### Recommended setup sequence

```{list-table}
:header-rows: 1
:widths: 15 35 50

* - Step
  - Component
  - Description
* - **3**
  - [Camera Setup](camerasetup)
  - Configure image acquisition and test the camera
* - **4**
  - [FlexiBowl Setup](fbsetup)
  - Connect and test communication with the FlexiBowl
* - **5**
  - [Hopper Setup](hoppersetup)
  - Configure the external hopper if present
* - **6**
  - [Robot Setup](robotsetup)
  - Configure the TCP/IP port and test communication with the robot
* - **7**
  - [Protocol Setup](protocol_setup)
  - Configure data exchange parameters and operating statistics
```

```{warning}
**Sequence importance**

Following the indicated order is important because the camera requires the FlexiBowl to be configured in order to test illumination, and some parameters depend on previous configurations.
```

(ricettabase)=
### Step 8: Save and rename the base recipe

Before configuring the hardware components, it is necessary to create a base recipe defining the system parameters.

````{list-table}
:header-rows: 0
:widths: 10 90

* - **8**
  - Open the |tasto_recipes| section from the top button

* - **9**
  - Enter the recipe name.

    Use a descriptive name, for example `"Base_Recipe"`.

    Avoid special characters or spaces, and use underscores ``_`` instead of spaces.

* - **12**
  - Click **Save Recipe** to save the recipe
````

```{tip}
**Recipe organization**

FlexiVision One allows multiple recipes to be created for different part types or configurations. Recommended naming convention:

- Use names that clearly identify the part, for example `"Zincated_M6_Screw"`

For more details about recipe management, refer to [Create a new recipe](nuovaricetta).
```

---

## Hardware component configuration

Once the preliminary operations are completed, proceed with hardware configuration in the following order.

All hardware setup sections are accessible from the central **SETUP** page of the software.

```{list-table}
* - **14**
  - From the main menu, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **15**
  - The icons of the various components to configure are displayed
* - **16**
  - Click the icon of the desired component to access its specific configuration
```

---

```{toctree}
:hidden:
13d_Camera_Setup.md
14_calibrazione_camera.md
13a_FB_Setup.md
13b_Hopper_Setup.md
13c_Robot_Setup.md
15_Protocol_Setup.md
```
