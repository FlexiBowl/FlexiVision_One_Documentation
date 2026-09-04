(setupcomponenti)=
# **Initial System Configuration**

This section guides the user through the complete configuration of the hardware and software components of the FlexiVision One system. It is essential to follow the steps in the order indicated to ensure proper operation of the system.

```{note}
**Prerequisites**

Before starting the software configuration, make sure that:
- Mechanical installation of all components is completed ([Mechanical Installation](Installazione_Meccanica))
- All cables are correctly connected ([Wiring and Connections](cablaggio)) 
```
![WorkFlow](../../../../../_shared/media/images/workflow.png)
---

## Overview of the setup process

The initial setup process consists of seven main steps:

0. **Enter the Licence Key** supplied in the kit
1. **Login** - Access the software with user credentials
2. if Backlight included: **Configure** **FlexiBowl® IP Address** and **Switch on** **Backlight**
3. **Camera Setup**
4. **FlexiBowl** **Setup** - Connect and configure the FlexiBowl®
5. **Hopper Setup**
6. **Robot** **Setup** - Configure communication with the robot
7. **Protocol** Setup - Configure protocol parameters
8. **Rename and Save the Basic Recipe** - Application profile configuration



```{warning}
**Order of steps**

The order of the setups is important! Do not skip steps or change the sequence, as some setups depend on previous ones.
```

---

## Preliminary operations

:::{important}
The first step before starting the FlexiVision One software is to enter the license key supplied with the kit. 
:::

### *Login to the system*

When the FlexiVision One software is started, the Home page is displayed. 
```{list-table} 
   :widths: 10 90
   :header-rows: 0
   * - **0**
     - Click Setup 
   * - **1**
     - **Select the user ENGINEER** from the drop-down menu at the top right.
   * - **2**
     - **Enter the password** '3'.
   * - **3**
     - Click the **LOGIN** button to access the interface.
```

```{tip}
**User management**

FlexiVision One supports multiple user profiles with different permission levels:
- **ARS**
- **Engineer**
- **Technician**
- **Operator**
```
:::{important}
Se l'utente corrente non dispone del livello di accesso necessario per una funzione, il sistema mostra una message box che ne segnala l'impossibilità di esecuzione.
:::
---

### *Switch on  the Backlight if included*

After the first login, if you need to activate your FlexiVision One licence, follow these steps: 

```{list-table}
* - **4** 
  - From the software home page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **5**
  - On the SETUP page, identify and click the **FlexiBowl® Setup** icon
    ```{dropdown} Setup Page 
       ![Setup Page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **6**
  - The FlexiBowl® Setup screen opens
* - **7**
  - Enter the FlexiBowl® IP address (default: `192.168.1.10` )
* - **8**
  - After entering the IP, click the button **Connection Test**
* - **9**
  - The system performs a communication test (ping) to the FlexiBowl®
* - **10**
  - Observe the **Status** indicator:
    - 🟢 **Green:** Connection successful
    - 🔴 **Red:** Connection failed (check IP address and wiring)
* - **11** 
  - Click the button <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **12**
  - A window opens with the configurable parameters of the FlexiBowl®
* - **13**
  - Turn on the backlight by ticking the "Light ON" box
```

---

## Hardware components configuration

Once the preliminary steps have been completed, proceed to configure the hardware components in the following order.

All hardware setups are accessible from the software’s central **SETUP** page.


```{list-table} 
* - **14** 
  - From the main menu, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **15** 
  - Icons for the different components to be configured are displayed
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
15b_SaveRecipe.md
```

