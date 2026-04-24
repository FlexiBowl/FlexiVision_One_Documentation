# **Mechanical Installation**

(troubleshooting_vision_controller)=
## VisionController issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **VisionController overheats and shuts down automatically**
  - • Insufficient ventilation or clearance below 50 mm

    • Ambient temperature above 50°C

  - • Verify at least 50 mm of free space on all sides

    • Move the unit to a cooler environment or add cabinet cooling

* - **VisionController does not lock correctly onto the DIN rail**
  - • DIN rail not compliant, not 35 mm

    • Locking mechanism damaged

    • Rail not firmly secured
  - • Verify that the rail is standard 35 mm DIN

    • Inspect the locking mechanism for damage

    • Secure the DIN rail more firmly to the panel
* - **VisionController becomes loose on the panel during screw mounting**
  - • Tightening torque too low

    • Incorrect screws, not M4

    • Incorrect panel drilling pattern
  - • Tighten the 4 M4 screws to 1.2 Nm

    • Use M4 screws as specified

    • Verify the drilling pattern against the technical drawings
* - **Insufficient IP protection**
  - • Installed outside the electrical cabinet

    • Cabinet with IP rating lower than 40

    • Presence of dust or humidity
  - • Install inside an IP54 electrical cabinet

    • Verify a minimum protection rating of IP40

    • Improve the cabinet sealing
```

(troubleshooting_camera)=
## Camera issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Image out of focus**
  - • Incorrect working distance for the FlexiBowl model

    • Lens not fully screwed in

  - • Measure and correct the distance according to [Optimal Working Distance Calculation](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md)

    • Fully screw in the lens until metal-to-metal contact

* - **Distorted image or incorrect perspective**
  - • Camera not centered on the FlexiBowl viewing area, error greater than ±5 mm

    • Camera tilted relative to the surface, tilt greater than ±1°

  - • Measure the centering with a ruler or caliper and correct it

    • Verify orthogonality with a precision level
```

(troubleshooting_toplight)=
## TopLight issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Non-uniform lighting with visible shadows**
  - • TopLight distance from the surface is incorrect

    • TopLight not parallel to the FlexiBowl plate

    • Lighting angle not perpendicular, tilt not equal to 0°
  - • Position the TopLight at a distance similar to the camera distance

    • Verify parallelism with a level

    • Correct the orientation to 0° tilt
* - **Indirect reflections toward the camera**
  - • Surface not compatible with the illuminator

  - • Check compatibility with the inspected surface
```

(troubleshooting_luce_ambientale)=
## Ambient light shielding issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Inconsistent detections at different times of day**
  - • Variable direct or indirect sunlight

    • Windows not shielded

    • Artificial lighting with dimmers
  - • Install blackout curtains or opaque panels

    • Fully shield windows inside the cell

    • Use fixed, non-adjustable lighting
* - **Reflections from surrounding surfaces**
  - • Reflective surfaces nearby, such as machines or panels

  - • Cover reflective surfaces with opaque material

    • Reposition reflective elements

    • Paint surfaces with matte paint
```
