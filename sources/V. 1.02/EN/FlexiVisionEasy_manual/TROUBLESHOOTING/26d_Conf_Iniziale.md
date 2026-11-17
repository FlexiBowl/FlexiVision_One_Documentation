# **Initial Setup**
```{warning}
**Components not reachable**

If FlexiBowl®, robot or camera cannot be reached:

1. Check that all Ethernet cables are correctly connected
2. Check that switch/router is switched on
3. Check the IP addresses of all devices:
   - They must be on the same subnet (e.g: 192.168.1.x)
   - There must be no IP conflicts (two devices with the same IP)
4. Use the `ping` terminal command to test reachability
5. Temporarily disable the Windows firewall on the port/adapter used for the GigE cameras

For details on network configuration, see [Wiring and Connections](cablaggio).
```
(troubleshooting_cam_setup)=
## Troubleshooting for the Camera Setup section

```{warning}
**Focusing problems**

If the image is blurred:

1. Check that the camera is at the correct working distance ([Optimal Distance Calculation](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Check that the lens is screwed in all the way
3. Check that there is no dirt or fingerprints on the lens
4. Ensure that the camera is mounted perfectly parallel to the FlexiBowl® work surface

```
```{tip}
**Brightness problems**

If the scanned image is too dark or too light:

**Too dark**:
- Check that the backlight/toplight is switched on (Config FlexiBowl®)
- Increase shutter speed (Cam Exposure parameter in [Camera FLB])

**Too light (overexposed)**:
- Reduce the shutter speed (Cam Exposure parameter in [Camera FLB])
- Check that there is no excessive ambient light
- Adjust the aperture in the camera lens body 
  :::{warning}
  Take special care when handling the camera, as even a small movement of the camera can compromise the reliability of the calibration if it has already been carried out
  :::
```
```{note}
**Capture performance**

If image capture is slow:
- Check that the Ethernet cable is Gigabit (Cat6 upwards )
- Check that the network switch is Gigabit Ethernet (not Fast Ethernet 100Mbps)
- Change the Latency Level if there are no problems with blue screens
- Reduce the Packet Size to 1500-2000 


The maximum frame rate of the camera is 24 fps (frames per second), sufficient for all standard picking applications.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Image too dark**
  - • Camera exposure too low
    
    • Toplight off or faulty

    • Backlight off or faulty

    • Toplight not strong enough
    
    • Lens with protective cap
  - • Increase exposure in Camera Setup
    
    • Check that the toplight is switched on 
    
    • Check that the Light On tick is on in FlexiBowl® Configuration
    
    • Check toplight power supply
    
    • Remove lens cap
* - **Image too bright (overexposed)**
  - • Camera exposure too high
    
    • Reflections from FlexiBowl® surface
  - • Decrease exposure in Camera Setup
    
    • Replace grip surface with a less reflective one
* - **Blurred image**
  - • Lens not in focus 
    
    • Lens not screwed in all the way
    
    • Dirty lens
    
    • Camera in motion/vibration
  - • Correct camera focus
    
    • Screw lens until metal-to-metal contact
    
    • Clean lens with microfibre cloth
    
    • Improve camera fastening and reduce vibrations
* - **Image with artefacts or lines**
  - • Electromagnetic interference
    
    • Camera cable damaged
    
    • Camera sensor damaged
  - • Move camera cable away from EMI sources, use shielded cable
    
    • Replace camera Ethernet cable
    
    • Replace camera
* - **Camera does not capture during cycle**
  - • Trigger not configured
    
  - • Configure capture trigger correctly
* - **Camera does not process during cycle**
  - 
```
(scelta_camera)=
### *Configuration procedure*

```{list-table}
* - **Configuration access**
  - 1. Click the button **Config Camera X** (where X is the camera number)
    2. The first page of the calibration wizard opens, where you can change the parameter **Cam Exposure**

* - **Activating advanced mode**
  - 3. Click the **Expert** button (bottom right)
    4. This mode provides access to all advanced camera settings required for initial configuration
* - **Configuration of image acquisition device**
  - 5. In the **Expert** panel, click the **Image Acquisition** section from **Settings**
    6. Click **Image Acquisition Device**
    7. A menu opens to select available acquisition devices
* -  **Specific camera identification**
  - 8. From the device menu, select the required camera
        - Search for the serial number or camera model in the list
        - Example: "CAM-CIC-5000-20G-XXXXX" (where XXXXX is the serial number)
    9. Click on the camera to select it 
```
:::{video} ../../../../_shared/media/videos/Step2_calib.mp4
  :width: 100%
  :align: center
:::

```{tip}
**Identification of the correct serial number**

If multiple cameras or devices are listed:
- The serial number can be found on a label on the physical camera
- Compare the last group of characters of the serial number to identify the correct camera
- If in doubt, physically disconnect the other cameras to identify the one in use
```


```{list-table} 
* - **Video format selection**
  - 11. Click **Video Formats** 
    12. From the list of available formats, select **Generic GigEVision**
    13. Select **Mono** (monochrome) as a sensor type
```


```{warning}
**Correct format required**

It is essential to select **Generic GigEVision Mono**:
- Other formats may not work or cause errors
- Colour formats are not compatible with this camera
- If the format is not available, drivers or system configurations may be missing
```

```{list-table}
* - **Acquisition system activation**
  - 14. After selecting the correct format, click **Initialize Acquisition**  
    15. Wait for the initialisation to complete (a few seconds)
* - **Check acquisition operation**
  - 16. Locate the **Run** button at the top left of the interface ("play" icon)
    17. Click **Run** repeatedly (05-10 times) to capture test images
    18. Observe the image display area:
        - It should show the camera view on the FlexiBowl®
        - The image should update each time you click Run
```

(schermo_blu)=
```{warning}
**Completely blue screen diagnosis**

If the captured image appears **completely blue** at least once during testing:

**Cause**: GigE communication problem (network latency or packet size not ideal)

**Solution**:

1. From the top menu, select **GigE** (or **GigE Vision Settings**)

2. Edit the following parameters:
   - **Latency Level**
   - **Packet Size**

Proceed to the next steps for the optimal configuration of these parameters.
```

---

#### *Latency Level*

```{note}
**Latency adjustment**

The **Latency Level** parameter controls the communication buffer between the camera and VisionController.

**Typical values**:
- Default value: 0
- Range available: 0-3

**How to adjust**:

1. Gradually increase the value 
2. After each change, test the acquisition (Run button) 5-10 times
3. If no more blue screens occur, the value is correct
4. If blue screens persist, increase further or try to change the Packet Size parameter
```

#### *Packet Size*

```{note}
**Packet size adjustment**

The **Packet Size** parameter defines the size of data packets transmitted over the Ethernet network.

**Typical values**:
- Default value: 8164 bytes

**How to adjust**:

1. Gradually reduce (8000, 7000, etc.)
2. After each change, test the acquisition (Run button) 5-10 times
3. If no more blue screens occur, the value is correct
4. If blue screens persist, decrease further or try to change the Latency Level parameter
```


---

```{list-table}
* - **Final check and save**
  - 19. Click **Run** at least 2-3 times consecutively  
    20. Check that:  
      - No image appears completely blue or black
      - Images are updated regularly
      - The surface of the FlexiBowl® is clearly visible
      - The lighting is uniform
    21. If all tests pass, the configuration is correct
```

(troubleshooting_calib_cam)=
## Camera Calibration

### *Pattern not detected*

```{warning}
**Error: "Unable to detect calibration pattern"**

Cause: The software cannot identify the grid pattern.

**Solutions**:
- Increase contrast (adjust exposure or lighting)
- Check that the entire grid is visible in the image
- Improve focus
- Clean the surface of the grid (dust or fingerprints may interfere)
- Check that the grid is correct (squares, not circles or other patterns)
```

### *Calibration always "Bad" or "Acceptable"*

```{warning}
**Insufficient calibration quality**

If, despite adjustments, calibration remains less than 'Excellent':

1. Check the camera-FlexiBowl® working distance (it must be as calculated)
2. Check that the camera is parallel to the plane of the FlexiBowl® (it must be perfectly horizontal)
3. Make sure the camera is stable (no vibrations while capturing)
4. Check that the lens is screwed in all the way 

If the problem persists, there may be a mechanical problem in the assembly. Consult [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md) for review.
```

### *Errors after lighting change*

```{tip}
**Re-calibration after backlight/toplight change**

When switching from backlight to toplight (or vice versa):

1. The geometric calibration remains valid (no need to redo it)
2. It is only necessary to adjust the camera exposure for the new lighting type
3. Capture a test image to verify that the pattern is still clearly visible

In general, it is advisable to decide from the outset on the type of lighting to be used and to maintain that configuration.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Calibration fails (software error)**
  - • Calibration grid not correctly detected
    
    • Insufficient/excessive lighting
    
    • Damaged or dirty calibration grid
    
  - • Position target flat and clearly visible
    
    • Adjust camera exposure to get a good view of the target
    
    • Use clean and intact calibration grid
    
* - **Calibration error too high**
  - • Camera not perfectly perpendicular to the surface
    
    • Calibration grid not level
    
    • Excessive optical distortion
    
  - • Check camera squareness with spirit level (tolerance ±1°)
    
    • Place target on a hard, flat surface
    
    • Check optical lens quality, clean or replace
    
* - **Actual coordinates do not match measured coordinates**
  - • Incorrect scale factor (Tile Size incorrect)
    
    • Camera moved after calibration
    
  - • Repeat full calibration
    
    • Securely fasten camera to keep it from moving
    
    • Check calibration target size according to documentation
* - **Calibration valid only at image centre**
  - • Peripheral optical distortion
    
    • Calibration with too few points
  - • Use a higher quality lens with low distortion
    
    • Check that the working distance is correct
```



(troubleshooting_fb_setup)=
## Troubleshooting for the FlexiBowl® Setup section

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **FlexiBowl® does not respond to software commands**
  - • IP address not configured or incorrect
    
    • FlexiBowl® not networked
    
    • Firewall blocks communication
    
    • FlexiBowl® not switched on
  - • Check and correctly configure IP in FlexiBowl® Setup
    
    • Test connection with ping from VisionController
    
    • Disable firewall temporarily for testing
    
    • Check READY LED on FlexiBowl®
* - **Unable to save FlexiBowl® configuration**
  - • Full disk

  - • Free up disk space
 
* - **FlexiBowl® parameters do not apply**
  - • 'Synchronize Parameters' button not pressed
    
    • Lost FlexiBowl® connection
    
    • FlexiBowl® in error
  - • Always click 'Synchronize Parameters' after changes
    
    • Check Ethernet connection stability
    
    • Restart FlexiBowl® 
* - **Wizard FlexiBowl® calculates incorrect parameters**
  - • Incorrect component characterisation (geometry/behaviour)
    
    • Incorrect FlexiBowl® model selected
    
    • Incorrect direction of rotation
  - • Review geometry selection (FLAT/CYLINDRICAL/COMPLEX)
    
    • Check FlexiBowl® size installed vs. selected
    
    • Check physical direction of rotation and compare with setting
```

(troubleshooting_hopper_setup)=
## Troubleshooting for the Hopper Setup section

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Hopper never switches on automatically**
  - • Hopper not enabled in software    
    • Wrong Signal field  
    • Control area not defined  
    
    • Thresholds not calibrated  
    
    • Hopper not electrically connected
  - • Enable "Enable Hopper X" checkbox  
    • Check that the **Signal** number corresponds to the physically connected DO
    • Define control area in "Define Area Check"
    
    • Perform threshold calibration with CAPTURE empty/full
    
    • Check electrical connections 
* - **Hopper switches on constantly**
  - • Incorrectly calibrated thresholds
    
    • Insufficient vibration time (unloads too few pieces)
    
    • Parameter "Steps" incorrect
  - • Repeat calibration by removing ALL parts for empty CAPTURE
    
    • Increase 'Time' parameter (e.g. from 500ms to 700ms)
    
    • Recalculate 'Steps' by counting actual cycles
* - **Test hopper always red (it does not switch on)**
  - • Too many components in the area during calibration
    
    • Lighting changed between calibration and testing
    
    • Reflections/shadows in the control area
  - • Repeat calibration with correct minimum number of pieces
    
    • Perform calibration and testing with stable lighting
    
    • Reposition area excluding zones with reflections
* - **Test hopper always green (it always switches on)**
  - • Control area includes irrelevant areas
    
    • Empty CAPTURE performed with parts present
    
    • Expression Builder not calculated correctly
  - • Redefine narrower control area
    
    • Repeat empty CAPTURE ensuring completely clean area
    
    • Click AUTO again to recalculate Mean and Std Dev
* - **Non-uniform component flow**
  - • Incorrect vibration time calculation  
    
    • Initial load too high beyond payload
  - • Review vibration calculation based on initial filling 
    
    • Check that the load does not exceed the hopper payload 
```

(troubleshooting_robot_setup)=
## Troubleshooting for the Robot Setup section

```{warning}
**Connection failure diagnosis**

If the robot cannot establish the connection:

**Basic checks**:
1. FlexiVision One server online (green indicator)
2. Correct IP address in robot program
3. Correct port in robot program (same as FlexiVision One)
4. Ethernet cable correctly connected

**Network checks**:
1. Ping from the VisionController to the robot:
   - Open Command Prompt at VisionController
   - `ping <IP_ROBOT>` (e.g: `ping 192.168.1.10`)
   - If it fails: physical network/IP configuration problem

2. Ping from robot to VisionController (if ping function available on robot)

3. Check that robot and VisionController are on the same subnet

**Firewall checks**:
1. Temporarily disable Windows firewall for testing
2. If it works, firewall problem → configure exception

**Robot verifications**:
1. Check correct TCP/IP connection command syntax (see robot manual)
2. Check connection timeout (increase if necessary)
3. Check network permissions on the robot controller
```

```{note}
**Connection stabilisation**

If the connection is frequently interrupted:

1. Check Ethernet cable quality (use Cat6 upwards)
2. Avoid excessively long cables 
3. Check that there is no excessive network traffic on the same subnet, you can use programs such as Wireshark or TCP dump 
4. Check stable power supply of the VisionController
5. Check Windows logs for network errors

If the problem persists, contact technical support for in-depth analysis.
```
```{warning}
**Incorrect command syntax**

If FlexiVision One responds with 'Invalid command':

1. Check the exact syntax of the command (case-sensitive, underscore, etc.)
2. Be sure to send the terminator character CHR(13) after each command
3. Do not add extra spaces at the beginning or end of the command
4. Check the message log in the Robot Setup section for the command that FlexiVision One received 

Correct vs. incorrect examples:
- ✅ `start_Locator` (with underscore, lower case)
- ❌ `Start_Locator` (incorrect upper case)
- ❌ `start Locator` (space instead of underscore)
- ❌ `startLocator` (missing underscore)

See [TCP/IP Protocol](protocollo) for a complete and correct list of commands.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Robot does not connect to FlexiVision One**
  - • Robot IP address not on same subnet as VisionController
    
    • TCP/IP port not configured
    
    • VisionController firewall blocks communication
    
  - • Check and configure correct subnet in Robot Setup
    
    • Configure TCP/IP port (typically 5000 or according to robot)
    
    • Disable firewall for testing
    
    • Select protocol compatible with robot in [Protocol Setup](../QUICKSTART/SETUP/15_Protocol_Setup.md)
* - **Robot goes to wrong positions**
  - • Robot calibration not performed or not performed correctly
    
    • Incorrect robot Frame/Tool
    
    • Incorrect gripper offset
    
    • Coordinates saved incorrectly during model setup
  - • Perform full robot calibration
    
    • Check Frame and Tool selected on the robot
    
    • Repeat Robot Pick calibration with correct coordinates
    
    • Re-train model by saving precise coordinates
* - **Unable to connect to robot**
  - • Robot switched off 
    
    • Ethernet cable not connected
    
    • Robot and VisionController on different subnets

  - • Switch on robot and set at automatic
    
    • Verify physical Ethernet robot-VisionController connection
    
    • Configure robot and VisionController on same network
```

