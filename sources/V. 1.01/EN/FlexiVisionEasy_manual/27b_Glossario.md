# **Glossary** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Term
  - Definition
* - **Accept Threshold**
  - Minimum similarity threshold (score 0.0-1.0) for a detected object to be accepted by pattern matching. Typical values: 0.70–0.90.
* - **Air-blow**
  - Optional pneumatic module for separating components on the disc by jets of compressed air. Requires supply at 5-6 bar.
* - **Artefact**
  - Defect in the captured image caused by electromagnetic interference, wiring problems or sensor malfunction.
* - **Camera Calibration**
  - Real pixel/coordinate correlation via calibration target with known pattern. It calculates the intrinsic and extrinsic parameters of the camera.
* - **Clearance**
  - Analysis of the distribution of greyscales over a defined area. Used to detect presence/absence of objects (gripper control, clear area).
* - **POE camera**
  - Industrial camera powered and connected via a single Ethernet cable. Standard: IEEE 802.3af (15.4W) or 802.3at (30W).
* - **CAPTURE**
  - Software command to acquire reference images of the empty and full disk, necessary for automatic calculation of hopper thresholds.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Geometrical categories of components in the FlexiBowl® Wizard. *FLAT*: flat shapes (washers, gaskets). *CYLINDRICAL*: cylindrical shapes (pins, screws). *COMPLEX*: irregular or asymmetrical geometries.
* - **Working Distance**
  - Ideal distance between lens and disk surface. Typically 950-1000mm in standard configurations.
* - **Optical Distortion**
  - Geometrical distortion of the image due to the lens. Automatically compensated during camera calibration.
* - **Exposure**
  - Light-gathering time of the camera sensor. Measured in μs or ms; directly affects image quality in production.
* - **Feature Threshold**
  - Feature extraction threshold (borders, lines) during model training. Typical values: 0.3–0.8.
* - **FlexiBowl®**
  - Vibrating rotating disc feeding system for random positioning and orientation of components for robotic picking.
* - **FlexiBowl® Wizard**
  - Wizard for automatic calculation of optimal FlexiBowl® parameters based on component geometry and behaviour.
* - **Flip**
  - Pneumatic impulse under the disc to reposition the components. Configurable via *Flip Count* (number of pulses) and *Flip Delay* (interval in ms between pulses).
* - **Grab Train Image**
  - Software command to acquire the image to be used in the training of a new model.
* - **Gripper Offset**
  - Correction vector (ΔX, ΔY, ΔRZ) that compensates for the offset between the optical centre of the vision system and the gripper TCP.
* - **Hotspot**
  - Zone of direct light reflection in the image. It appears as an overexposed area and may impair identification.
* - **Lens**
  - Optical component of the camera. It must be screwed until metal-to-metal contact; the focal length (e.g. 16mm, 25mm) determines the field of view at the working distance.
* - **Model**
  - Geometric template of the component created during the training phase. Each recipe supports up to 8 models per FlexiBowl®.
* - **Model Origin**
  - Reference point on the component used as the centre of the coordinate system to calculate positions. It typically corresponds to the pick TCP.
* - **Orthogonality**
  - Perpendicularity of the camera with respect to the disc (tolerance ±1°). Verifiable with precision level.
* - **Pattern Matching**
  - Algorithm that locates the components in the image by comparing them with the reference model recorded during training.
* - **Protocol**
  - Communication format between VisionController and robot. It defines message structure, coordinate order and units of measurement.
* - **Recipe**
  - XML file containing all system configuration parameters: models, thresholds, calibrations, FlexiBowl® and robot setup.
* - **Region Search**
  - Rectangular area in the image within which the pattern matching performs the search. It reduces processing time and increases accuracy.
* - **ROI (Region of Interest)**
  - Rectangular area delimiting the component in the image during model training.
* - **RZ / Rotation Z**
  - Angle of rotation around the Z axis communicated to the robot for component orientation. Expressed in degrees (0-360°).
* - **Score**
  - Similarity index (0.0-1.0) between the model and the detected object. It determines the trustworthiness of identification.
* - **Gripper Footprint Simulators**
  - Physical objects placed around the component during training to exclude from the model the areas engaged by the gripper during picking.
* - **Steps**
  - Number of movements of the FlexiBowl® required for components to reach the hopper unloading area from the vision area. 
* - **Subnet**
  - Subnet that FlexiBowl® and VisionController must share (e.g. 192.168.1.x) for TCP/IP communication.
* - **Synchronize Parameters**
  - Software command that transfers parameters to the FlexiBowl®. Mandatory after each change to make the settings effective.
* - **Timeout**
  - Maximum time to wait for a communication reply. An error is triggered when it is exceeded.
* - **Tilt**
  - Inclination of the camera with respect to the horizontal plane. Allowed value: 0° ± 1°.
* - **Toplight**
  - LED illuminator positioned above the disc for even illumination from above. Power supply: 24V DC.
* - **Training**
  - Process of creating the identification model by selecting the distinctive features of the component from a reference image.
* - **Trigger**
  - Image capture start signal. It can be software-related (timed) or hardware-related (external electrical signal).
* - **Vision Result**
  - Output of the vision system: coordinates (X, Y, RZ) and score of the detected component, transmitted to the robot for picking.
* - **VisionController**
  - Industrial computer that runs FlexiVision One, manages cameras, processes images and communicates with FlexiBowl® and robots.
```

