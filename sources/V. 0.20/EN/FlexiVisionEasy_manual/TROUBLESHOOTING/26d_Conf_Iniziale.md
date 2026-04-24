# **Initial Setup**

```{warning}
**Components not reachable**

If the FlexiBowl, robot, or camera cannot be reached:

1. Verify that all Ethernet cables are connected correctly
2. Check that switches or routers are powered on
3. Verify the IP addresses of all devices:
   - They must be on the same subnet, for example `192.168.1.x`
   - There must be no IP conflicts, meaning no two devices with the same IP
4. Use the `ping` command from a terminal to test connectivity
5. Temporarily disable the Windows firewall on the port or adapter used for GigE cameras

For network configuration details, refer to [Wiring and Connections](cablaggio).
```

(troubleshooting_fb_setup)=
## Troubleshooting for Step 4: FlexiBowl Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **FlexiBowl does not respond to software commands**
  - • IP address not configured or incorrect

    • FlexiBowl not connected to the network

    • Firewall blocking communication

    • FlexiBowl powered off
  - • Verify and configure the correct IP in FlexiBowl Setup

    • Test the connection using ping from the VisionController

    • Temporarily disable the firewall for testing

    • Verify that the READY LED is on
* - **Impossible to save FlexiBowl configuration**
  - • Disk full

  - • Free disk space

* - **FlexiBowl parameters are not applied**
  - • `"Synchronize Parameters"` button not pressed

    • FlexiBowl connection lost

    • FlexiBowl in error state
  - • Always click `"Synchronize Parameters"` after modifications

    • Verify Ethernet connection stability

    • Restart the FlexiBowl
* - **FlexiBowl Wizard calculates wrong parameters**
  - • Incorrect component characterization, geometry or behavior

    • Wrong FlexiBowl model selected

    • Rotation direction set incorrectly
  - • Review geometry selection, FLAT, CYLINDRICAL, or COMPLEX

    • Verify installed FlexiBowl size against the selected one

    • Verify actual physical rotation direction and compare it with the configured setting
```

(troubleshooting_hopper_setup)=
## Troubleshooting for Step 5: Hopper Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Hopper never activates automatically**
  - • Hopper not enabled in the software  
    • Wrong Signal field
    • Control area not defined

    • Thresholds not calibrated

    • Hopper not connected electrically
  - • Enable the `"Enable Hopper X"` checkbox  
    • Verify that the **Signal** number matches the physically connected digital output
    • Define the control area in `"Define Area Check"`

    • Run threshold calibration with empty and full CAPTURE

    • Verify electrical connections
* - **Hopper activates continuously**
  - • Thresholds calibrated incorrectly

    • Vibration time too short, too few parts discharged

    • `"Steps"` parameter incorrect
  - • Repeat calibration by removing all parts for the empty CAPTURE

    • Increase `"Time"` parameter, for example from `500 ms` to `700 ms`

    • Recalculate `"Steps"` by counting real cycles
* - **Hopper test always red, does not activate**
  - • Too many components in the area during calibration

    • Lighting changed between calibration and test

    • Reflections or shadows in the control area
  - • Repeat calibration with the correct minimum number of parts

    • Run calibration and test under stable lighting

    • Reposition the area excluding reflective zones
* - **Hopper test always green, always activates**
  - • Control area includes irrelevant zones

    • Empty calibration performed with parts still present

    • Expression Builder not calculated correctly
  - • Redefine a tighter control area

    • Repeat empty CAPTURE ensuring the area is completely clear

    • Click AUTO again to recalculate Mean and Std Dev
* - **Part flow not uniform**
  - • Incorrect vibration time calculation

    • Initial load too high and above payload
  - • Review the vibration calculation according to the initial fill level

    • Verify that the load does not exceed hopper payload
```

(troubleshooting_robot_setup)=
## Troubleshooting for Step 6: Robot Setup

```{warning}
**Failed connection diagnosis**

If the robot cannot establish the connection:

**Basic checks**:
1. FlexiVision One server online, green indicator
2. Correct IP address in the robot program
3. Correct port in the robot program, same as FlexiVision One
4. Ethernet cable connected correctly

**Network checks**:
1. Ping from the VisionController to the robot:
   - Open Command Prompt on the VisionController
   - `ping <ROBOT_IP>`, for example `ping 192.168.1.10`
   - If it fails, the issue is physical networking or IP configuration

2. Ping from the robot to the VisionController, if the robot supports ping

3. Verify that robot and VisionController are on the same subnet

**Firewall checks**:
1. Temporarily disable Windows firewall for testing
2. If it works, the firewall is the issue, configure an exception

**Robot checks**:
1. Verify the TCP/IP connection command syntax, refer to the robot manual
2. Check connection timeout and increase it if needed
3. Verify network permissions on the robot controller
```

```{note}
**Connection stabilization**

If the connection drops frequently:

1. Verify Ethernet cable quality, use Cat6 or better
2. Avoid excessively long cables
3. Verify that there is no excessive network traffic on the same subnet, tools such as Wireshark or TCP dump can help
4. Verify stable VisionController power supply
5. Check Windows logs for network errors

If the problem persists, contact technical support for deeper analysis.
```

```{warning}
**Incorrect command syntax**

If FlexiVision One responds with `"Invalid command"`:

1. Verify the exact command syntax, case-sensitive, underscore, and so on
2. Make sure you send the CHR(13) termination character after every command
3. Do not add extra spaces at the beginning or end of the command
4. In the Robot Setup message log, verify which command FlexiVision One actually received

Correct vs incorrect examples:
- ✅ `start_Locator`, lowercase, with underscore
- ❌ `Start_Locator`, wrong uppercase
- ❌ `start Locator`, space instead of underscore
- ❌ `startLocator`, missing underscore

Refer to [TCP/IP Protocol](protocollo) for the complete and correct command list.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Robot does not connect to FlexiVision One**
  - • Robot IP address not on the same subnet as the VisionController

    • TCP/IP port not configured

    • VisionController firewall blocking communication

  - • Verify and configure the correct subnet in Robot Setup

    • Configure the TCP/IP port, typically `5000` or according to the robot

    • Disable the firewall for testing

    • Select a robot-compatible protocol in [Protocol Setup](../QUICKSTART/SETUP/15_Protocol_Setup.md)
* - **Robot moves to the wrong positions**
  - • Robot calibration not performed or not performed correctly

    • Wrong robot Frame or Tool

    • Incorrect gripper offset

    • Wrong coordinates saved during model setup
  - • Perform a complete robot calibration

    • Verify the Frame and Tool selected on the robot

    • Repeat Robot Pick calibration with the correct coordinates

    • Redo model training and save precise coordinates
* - **Impossible to connect to the robot**
  - • Robot powered off

    • Ethernet cable not connected

    • Robot and VisionController on different subnets

  - • Power on the robot and switch it to automatic mode

    • Verify the physical Ethernet connection between robot and VisionController

    • Configure robot and VisionController on the same network
```

(troubleshooting_cam_setup)=
## Troubleshooting for Step 7: Camera Setup

```{warning}
**Focus issues**

If the image appears blurred:

1. Verify that the camera is at the correct working distance ([Optimal Working Distance Calculation](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Check that the lens is fully screwed in
3. Verify that there is no dirt or fingerprints on the lens
4. Make sure the camera is mounted perfectly parallel to the FlexiBowl plate
```

```{tip}
**Brightness issues**

If the acquired image is too dark or too bright:

**Too dark**:
- Verify that the backlight or TopLight is on, Config FlexiBowl
- Increase exposure time, parameter Cam Exposure in [Camera FLB]

**Too bright, overexposed**:
- Reduce exposure time, parameter Cam Exposure in [Camera FLB]
- Verify that ambient light is not excessive
- Adjust the aperture ring on the camera lens
  :::{warning}
  Handle the camera with extreme care because, if calibration has already been performed, even a very small movement of the camera may compromise calibration reliability.
  :::
```

```{note}
**Acquisition performance**

If image acquisition is slow:
- Verify that the Ethernet cable is Gigabit, Cat6 or better
- Check that the network switch is Gigabit Ethernet and not Fast Ethernet 100 Mbps
- Change the Latency Level if there are no blue-screen image issues
- Reduce Packet Size to `1500-2000`

The maximum camera frame rate is `24 fps`, images per second, which is sufficient for all standard picking applications.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Image too dark**
  - • Camera exposure too low

    • TopLight off or faulty

    • Backlight off or faulty

    • TopLight power insufficient

    • Lens protective cap still on
  - • Increase exposure in Camera Setup

    • Verify that the TopLight is on

    • Verify that Light On is enabled in FlexiBowl Configuration

    • Verify TopLight power supply

    • Remove the lens protective cap
* - **Image too bright, overexposed**
  - • Camera exposure too high

    • Reflections from the FlexiBowl surface
  - • Reduce exposure in Camera Setup

    • Replace the grip surface with a less reflective one
* - **Blurred image**
  - • Lens out of focus

    • Lens not fully screwed in

    • Dirty lens

    • Camera moving or vibrating
  - • Correct camera focus

    • Screw the lens in until metal-to-metal contact

    • Clean the lens with a microfiber cloth

    • Improve camera fixing and reduce vibration
* - **Image with artifacts or lines**
  - • Electromagnetic interference

    • Damaged camera cable

    • Damaged camera sensor
  - • Move the camera cable away from EMI sources and use a shielded cable

    • Replace the camera Ethernet cable

    • Replace the camera
* - **Camera does not acquire during the cycle**
  - • Trigger not configured

  - • Configure acquisition trigger correctly
* - **Camera does not process during the cycle**
  -
```
