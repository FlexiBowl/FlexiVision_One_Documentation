(robotsetup)=
# **Step 6: Robot Setup**

This section describes the procedure to configure TCP/IP communication between the FlexiVision One system and the industrial robot. Correct communication is essential to allow the exchange of coordinates and commands between the two systems.

```{note}
**Prerequisites**

Before proceeding, make sure that:
- The robot is powered on and operational
- The Ethernet cable between VisionController and robot is connected
- The robot is configured to accept TCP/IP connections, refer to the robot manual
- The communication port configured in the robot code is known
```

---

## Accessing Robot configuration

```{list-table}

* - **1**
  - From the main software page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - In the SETUP page, locate and click the **Robot Setup** icon
    ```{dropdown} Setup page
       ![Setup page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - The robot communication configuration page opens
```

---

## Robot Setup interface overview

The Robot Setup page includes several sections used to configure and test communication:

![Robot Setup page](../../../../../_shared/media/images/pagina_robotsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Port**
  - TCP/IP port used by the robot to communicate, configured on the robot controller
* - **Reconfigure Server**
  - Button used to reconfigure the communication server with the new parameters
* - **Server Online**
  - FlexiVision One server status indicator, green means server active and reachable
* - **Client Connect**
  - Robot client status indicator, green means robot connected
* - **Robot-FlexiVision One messages**
  - Log windows showing the messages exchanged between robot and FlexiVision One, used for debugging:
      - the first, smaller window shows the messages sent by FlexiVision One or by the operator
      - the second window shows the messages received by FlexiVision One
```

---

## Configuration procedure

### Step 1: Enter the communication port

The TCP/IP port is the critical parameter and must match on both the robot and FlexiVision One sides:

```{list-table}
* - **4**
  - In the **Port** field, enter the TCP/IP port number used by the robot to communicate
```

```{note}
Default value: standard FlexiVision One port.  
The port number must:
   - match the one configured in the robot program
   - be between 1024 and 65535, user port range
   - not conflict with other services on the network
```

```{warning}
It is **essential** that the port number is identical on both sides:
- **FlexiVision One**: port configured in this page
- **Robot**: port configured in the robot program

If the numbers do not match, the connection will always fail.

Example:
- ❌ WRONG: FlexiVision One port 2000, Robot port 2001 -> no communication
- ✅ CORRECT: FlexiVision One port 2000, Robot port 2000 -> communication works
```

### Step 2: Reconfigure the server

After setting the correct port, the communication server must be restarted:

```{list-table}
* - **5**
  - Click **Reconfigure Server**
* - **6**
  - Wait a few seconds for reconfiguration to complete
```

```{note}
It is necessary to click **Reconfigure Server** whenever:
- The port number is changed
- The server must be restarted after an error
- The network configuration of the VisionController has been changed
- Existing connections must be closed forcibly

The server starts automatically when FlexiVision One opens, but it requires manual reconfiguration after changes.
```

### Step 3: Verify server status

After reconfiguration, verify that the server is active:

```{list-table}

* - **7**
  - Check the **Server Online** indicator:
   - **Green**: server active
     **Red**: server not active
* - **8**
  - After starting the robot program, check the **Client Online** indicator:
   - **Green**: robot connected
     **Red**: robot not connected

```

```{note}
If the indicators are green, the system is connected correctly.

If one of the indicators is red, verify:
   - that the program on the robot has been started
   - that the IP addresses are on the same subnet
   - that the port is not already in use by another program
   - the system logs for error messages
```

### Step 4: Save and complete

```{list-table}
:header-rows: 0
:widths: 10 90

* - **9**
  - Verify that robot to FlexiVision One communication is stable

* - **10**
  - Communication parameters are saved automatically

* - **11**
  - Return to the main **SETUP** page
```

---

## Next steps

Once Robot Setup is completed, continue with:

**[Step 7: Camera Setup](13d_Camera_Setup.md)** - configure and test camera acquisition
