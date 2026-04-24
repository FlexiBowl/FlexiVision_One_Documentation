(distanza_lavoro)=
# **Optimal Working Distance Calculation**

This section defines the recommended working distance between the camera and the FlexiBowl plate, together with the resulting selection of lenses required to ensure the correct Field of View (FOV).

The correct choice of working distance and lens is essential to:
- Ensure that the entire usable surface of the FlexiBowl is visible
- Obtain the resolution required to detect parts
- Minimize optical distortion
- Facilitate system calibration

---

## Recommended working distances and lens selection

Lens selection strictly depends on the recommended mounting distance between the camera and the surface of the FlexiBowl plate. Maintaining the standard working distance ensures the correct FOV and minimizes optical distortion problems.


```{note}
**Lens already included**

The lens appropriate for the FlexiBowl model specified in the order is always included in the FlexiVision One package and is supplied in separate packaging from the camera. It does not need to be purchased separately.
```

### Distance and field-of-view diagram

The following diagram illustrates the relationship between working distance, lens focal length, and resulting viewing area for the different FlexiBowl models.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Working Distance
:width: 40%
:align: center
```

**Diagram legend:**
- **Working Distance**: Vertical distance between the front face of the lens and the surface of the FlexiBowl plate
- **Viewing area**: Area of the FlexiBowl surface covered by the camera field of view

### Summary table by model

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - FlexiBowl Model
  - Recommended Working Distance
  - Lens Included in the Kit (Focal Length)
* - **FB 200**
  - 800 mm 
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

```{warning}
**Importance of the correct distance**

Significant deviations from the recommended working distance may cause:

- **Distance too short**: Insufficient FOV (part of the FlexiBowl not visible).
- **Distance too long**: Insufficient resolution to detect small parts, blurring

Always respect the distances indicated in the table during mechanical camera mounting.
```
### Camera Positioning 

**Correct configuration.** The camera must be positioned centrally and with the same angular orientation as the FlexiBowl viewing area (backlight zone). In this way, the field of view (shown in green) symmetrically covers the entire work area, ensuring correct operation of the vision system.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Working Distance
:width: 70%
:align: center
```

**Incorrect configurations.** The images show examples of incorrect camera positioning: the field of view (shown in red) is offset with respect to the vision area, covering the work area only partially or including areas outside it. These configurations compromise part recognition and operation of the vision system.  

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Working Distance
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Working Distance
:width: 60%
:align: center
```
---

## TopLight Positioning 

If the system includes a TopLight (top illuminator), it must have the same angular orientation as the camera to ensure uniform illumination. It must be installed on a support that is mechanically independent from the camera support, so that removing or replacing the lighting system does not require loosening or disassembling the camera.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Recommended Value
* - **Distance from the FlexiBowl surface**
  - Similar to the camera Working Distance (±100 mm)
* - **Position relative to the camera**
  - Concentric (same optical axis as the camera)
* - **Orientation**
  - Parallel to the FlexiBowl surface and with the same angular orientation as the camera (long side of viewing area - long side of illumination)
* - **Relative camera-TopLight height**
  - Vision optics flush with the upper surface of the Top Light (leave free access to the adjustment rings of the vision optics)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Working Distance
    :width: 80%
    :align: center
    :::
```

```{tip}
To obtain the best lighting uniformity, follow the instructions just provided 
```

```{warning}
**Avoid direct reflections**

When positioning the TopLight, make sure that:

- Light does not reflect directly from the FlexiBowl surface toward the camera (causing glare)
- There are no shadows caused by mechanical components
- Illumination is as uniform as possible over the entire usable surface

```

---

## Related references

To complete system installation and configuration:

- **Mechanical camera installation**: [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Camera technical specifications**: [FlexiVision One Specifications](04_Specifiche_FlexiVision.md)
- **System calibration**: [Camera Calibration](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Electrical wiring**: [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

