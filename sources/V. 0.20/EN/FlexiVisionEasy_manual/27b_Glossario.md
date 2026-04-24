# **Glossary** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Term
  - Definition
* - **Accept Threshold**
  - Minimum similarity threshold (score 0.0–1.0) required for a detected object to be accepted by pattern matching. Typical values: 0.70–0.90.
* - **Air-blow**
  - Optional pneumatic module for separating components on the disk using compressed-air jets. Requires a 5–6 bar supply.
* - **Artifact**
  - Defect in the acquired image caused by electromagnetic interference, wiring problems, or sensor malfunctions.
* - **Camera Calibration**
  - Pixel/real-coordinate correlation using a calibration target with a known pattern. Calculates the intrinsic and extrinsic parameters of the camera.
* - **Clearance**
  - Analysis of the grayscale level distribution over a defined area. Used to detect the presence/absence of objects (gripper check, free area).
* - **POE Camera**
  - Industrial camera powered and connected through a single Ethernet cable. Standard: IEEE 802.3af (15.4W) or 802.3at (30W).
* - **CAPTURE**
  - Software command used to acquire the reference images of the empty and full disk, required for automatic calculation of the hopper thresholds.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Geometric categories of components in the FlexiBowl Wizard. *FLAT*: flat shapes (washers, gaskets). *CYLINDRICAL*: cylindrical shapes (pins, screws). *COMPLEX*: irregular or asymmetrical geometries.
* - **Working Distance**
  - Optimal distance between the lens and the disk surface. Typically 950–1000mm in standard configurations.
* - **Optical Distortion**
  - Geometric deformation of the image caused by the lens. Automatically compensated during camera calibration.
* - **Exposure**
  - Light collection time of the camera sensor. Measured in μs or ms; directly affects image quality in production.
* - **Feature Threshold**
  - Feature extraction threshold (edges, lines) during model training. Typical values: 0.3–0.8.
* - **FlexiBowl**
  - Vibrating rotary-disk feeding system for random positioning and orientation of components for robotic picking.
* - **FlexiBowl Wizard**
  - Guided procedure for automatic calculation of the optimal FlexiBowl parameters based on component geometry and behavior.
* - **Flip**
  - Pneumatic pulse under the disk used to reposition components. Configurable through *Flip Count* (number of pulses) and *Flip Delay* (interval in ms between pulses).
* - **Grab Train Image**
  - Software command used to acquire the image to be used for training a new model.
* - **Gripper Offset**
  - Correction vector (ΔX, ΔY, ΔRZ) that compensates for the offset between the optical center of the vision system and the gripper TCP.
* - **Hotspot**
  - Direct light reflection area in the image. Appears as an overexposed area and may compromise recognition.
* - **Lens**
  - Optical component of the camera. It must be screwed in until metal-to-metal contact; the focal length (e.g. 16mm, 25mm) determines the field of view at the working distance.
* - **Model (Model)**
  - Geometric template of the component created during training. Each recipe supports up to 8 models.
* - **Model Origin**
  - Reference point on the component used as the center of the coordinate system for position calculation. Typically corresponds to the picking TCP.
* - **Orthogonality**
  - Perpendicularity of the camera with respect to the disk (tolerance ±1°). Can be checked with a precision level.
* - **Pattern Matching**
  - Algorithm that locates components in the image by comparing them with the reference model recorded during training.
* - **Protocol (Protocol)**
  - Communication format between VisionController and robot. Defines message structure, coordinate order, and units of measurement.
* - **Recipe (Recipe)**
  - XML file containing all system configuration parameters: models, thresholds, calibrations, FlexiBowl setup, and robot setup.
* - **Region Search**
  - Rectangular area in the image within which pattern matching performs the search. Reduces processing time and increases accuracy.
* - **ROI (Region of Interest)**
  - Rectangular area that delimits the component in the image during model training.
* - **RZ / Rotation Z**
  - Rotation angle around the Z axis communicated to the robot for component orientation. Expressed in degrees (0–360°).
* - **Score**
  - Similarity index (0.0–1.0) between the model and the detected object. Determines recognition confidence.
* - **Gripper Clearance Simulators**
  - Physical objects placed around the component during training to exclude from the model the areas occupied by the gripper during picking.
* - **Steps**
  - Number of hopper vibration cycles required for the components to reach the picking area. Critical parameter for synchronization with the robot cycle.
* - **Subnet**
  - FlexiBowl and VisionController must share the same subnet (e.g. 192.168.1.x) for TCP/IP communication.
* - **Synchronize Parameters**
  - Software command that transfers parameters from the VisionController to the FlexiBowl. Required after each change to make the settings effective.
* - **Calibration Target**
  - Printed geometric pattern (circles or checkerboard) with known dimensions and a flat surface, used for camera calibration.
* - **Timeout**
  - Maximum waiting time for a communication response. An error is generated when it is exceeded.
* - **Tilt**
  - Inclination of the camera relative to the horizontal plane. Allowed value: 0° ± 1°.
* - **Toplight**
  - LED illuminator positioned above the disk that provides uniform top lighting. Power supply: 24V DC.
* - **Training**
  - Process of creating the recognition model by selecting the component's distinctive features from a reference image.
* - **Trigger**
  - Image acquisition start signal. It may be software-based (timed) or hardware-based (external electrical signal).
* - **Vision Result**
  - Vision system output: coordinates (X, Y, RZ) and score of the detected component, transmitted to the robot for picking.
* - **VisionController**
  - Industrial computer that runs FlexiVision One, manages the cameras, processes images, and communicates with FlexiBowl and the robot.
```

