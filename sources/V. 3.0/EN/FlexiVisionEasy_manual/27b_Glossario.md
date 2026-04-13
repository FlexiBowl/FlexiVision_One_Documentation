# **Glossary**

```{list-table}
:header-rows: 1
:widths: 25 75

* - Term
  - Definition
* - **Accept Threshold**
  - Minimum similarity threshold (score 0.0-1.0) required for a detected object to be accepted by pattern matching. Typical values: 0.70-0.90.
* - **Air-blow**
  - Optional pneumatic module used to separate components on the disk through compressed air jets. Requires a 5-6 bar air supply.
* - **Artifact**
  - Defect in the acquired image caused by electromagnetic interference, wiring issues, or sensor malfunction.
* - **Camera Calibration**
  - Correlation between pixels and real coordinates through a calibration target with a known pattern. It calculates the intrinsic and extrinsic camera parameters.
* - **Clearance**
  - Analysis of grayscale level distribution within a defined area. Used to detect object presence/absence (gripper check, free-area verification).
* - **PoE Camera**
  - Industrial camera powered and connected through a single Ethernet cable. Standard: IEEE 802.3af (15.4W) or 802.3at (30W).
* - **CAPTURE**
  - Software command used to acquire reference images of the empty and full disk, required for automatic hopper threshold calculation.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Geometric categories of components in the FlexiBowl Wizard. *FLAT*: flat shapes (washers, gaskets). *CYLINDRICAL*: cylindrical shapes (pins, screws). *COMPLEX*: irregular or asymmetrical geometries.
* - **Working Distance**
  - Optimal distance between the lens and the disk surface. Typically 950-1000 mm in standard configurations.
* - **Optical Distortion**
  - Geometric deformation of the image caused by the lens. It is automatically compensated for during camera calibration.
* - **Exposure**
  - Light collection time of the camera sensor. Measured in us or ms; it directly affects image quality in production.
* - **Feature Threshold**
  - Threshold for extracting features (edges, lines) during model training. Typical values: 0.3-0.8.
* - **FlexiBowl**
  - Vibrating rotating-disk feeding system used for the random positioning and orientation of components for robotic picking.
* - **FlexiBowl Wizard**
  - Guided procedure for automatically calculating the optimal FlexiBowl parameters based on component geometry and behavior.
* - **Flip**
  - Pneumatic pulse beneath the disk used to reposition components. Configurable through *Flip Count* (number of pulses) and *Flip Delay* (interval in ms between pulses).
* - **Grab Train Image**
  - Software command used to acquire the image that will be used when training a new model.
* - **Gripper Offset**
  - Correction vector (DeltaX, DeltaY, DeltaRZ) used to compensate for the offset between the optical center of the vision system and the gripper TCP.
* - **Hotspot**
  - Area of direct light reflection in the image. It appears as an overexposed zone and may compromise recognition.
* - **Lens**
  - Optical component of the camera. It must be screwed in with metal-to-metal contact; the focal length (for example 16 mm, 25 mm) determines the field of view at the working distance.
* - **Model**
  - Geometric template of the component created during the training phase. Each recipe supports up to 8 models.
* - **Model Origin**
  - Reference point on the component used as the center of the coordinate system for position calculation. It typically matches the picking TCP.
* - **Orthogonality**
  - Perpendicularity of the camera relative to the disk (tolerance +/-1 degree). It can be checked with a precision level.
* - **Pattern Matching**
  - Algorithm that locates components in the image by comparing them with the reference model recorded during training.
* - **Protocol**
  - Communication format between the VisionController and the robot. It defines message structure, coordinate order, and measurement units.
* - **Recipe**
  - XML file containing all system configuration parameters: models, thresholds, calibrations, FlexiBowl setup, and robot setup.
* - **Region Search**
  - Rectangular area in the image within which pattern matching performs the search. It reduces processing times and increases accuracy.
* - **ROI (Region of Interest)**
  - Rectangular area that encloses the component in the image during model training.
* - **RZ / Rotation Z**
  - Rotation angle around the Z axis sent to the robot for component orientation. Expressed in degrees (0-360 degrees).
* - **Score**
  - Similarity index (0.0-1.0) between the model and the detected object. It determines recognition confidence.
* - **Gripper Clearance Simulators**
  - Physical objects placed around the component during training to exclude from the model the areas occupied by the gripper during picking.
* - **Steps**
  - Number of hopper vibration cycles required for components to reach the picking area. Critical parameter for synchronization with the robot cycle.
* - **Subnet**
  - FlexiBowl and VisionController must share the same subnet (for example 192.168.1.x) for TCP/IP communication.
* - **Synchronize Parameters**
  - Software command that transfers parameters from the VisionController to the FlexiBowl. Mandatory after each change to make the settings effective.
* - **Calibration Target**
  - Printed geometric pattern (circles or chessboard) with known dimensions and a flat surface, used for camera calibration.
* - **Timeout**
  - Maximum waiting time for a communication response. When exceeded, an error is generated.
* - **Tilt**
  - Camera inclination relative to the horizontal plane. Allowed value: 0 degrees +/-1 degree.
* - **Toplight**
  - LED illuminator placed above the disk to provide uniform top-down lighting. Power supply: 24 V DC.
* - **Training**
  - Process of creating the recognition model by selecting the distinctive features of the component from a reference image.
* - **Trigger**
  - Signal that starts image acquisition. It can be software-based (timed) or hardware-based (external electrical signal).
* - **Vision Result**
  - Output of the vision system: coordinates (X, Y, RZ) and score of the detected component, transmitted to the robot for picking.
* - **VisionController**
  - Industrial computer that runs FlexiVision One, manages the cameras, processes images, and communicates with FlexiBowl and the robot.
```
