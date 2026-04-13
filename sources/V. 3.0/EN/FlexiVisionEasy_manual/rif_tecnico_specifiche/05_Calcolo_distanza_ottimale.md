(distanza_lavoro)=
# **Optimal Working Distance Calculation**

This section defines the recommended working distance between the camera and the FlexiBowl plate, together with the corresponding lens selection required to ensure the correct Field of View (FOV).

The correct choice of working distance and lens is essential to:
- ensure that the entire useful FlexiBowl surface is visible
- obtain the resolution required to detect the parts
- minimize optical distortion
- simplify system calibration

---

## Recommended working distances and lens selection

Lens selection is strictly linked to the recommended mounting distance between the camera and the FlexiBowl plate surface. Maintaining the standard working distance ensures the correct FOV and minimizes optical distortion issues.

```{note}
**Lens already included**

The lens appropriate for the FlexiBowl model specified in the order is always included in the FlexiVision One package and is supplied in a separate package from the camera. It does not need to be purchased separately.
```

### Distance and field-of-view diagram

The following diagram shows the relationship between working distance, lens focal length, and resulting viewing area for the different FlexiBowl models.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Working Distance
:width: 40%
:align: center
```

**Diagram legend:**
- **Working Distance**: vertical distance between the front face of the lens and the FlexiBowl plate surface
- **Viewing area**: portion of the FlexiBowl surface covered by the camera field of view

### Summary table by model

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - FlexiBowl model
  - Recommended working distance
  - Lens included in the kit (focal length)
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

- **Distance too short**: insufficient FOV, so part of the FlexiBowl is not visible
- **Distance too long**: insufficient resolution for detecting small parts, or blurred images

Always comply with the distances listed in the table during mechanical camera installation.
```

### Camera positioning

**Correct configuration.** The camera must be positioned centrally and with the same angular orientation as the FlexiBowl viewing area (backlight zone). In this way, the field of view (shown in green) symmetrically covers the entire working area, ensuring correct operation of the vision system.

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Correct camera positioning
:width: 70%
:align: center
```

**Incorrect configurations.** The images below show examples of improper camera positioning: the field of view (shown in red) is off-center with respect to the viewing area, covering only part of the working area or including areas outside it. These configurations compromise part recognition and the operation of the vision system.

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Incorrect camera positioning
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Incorrect camera positioning
:width: 60%
:align: center
```

---

## TopLight positioning

If the system includes a TopLight, it must have the same angular orientation as the camera to guarantee uniform illumination. It must be installed on a mechanically independent support from the camera support, so that removing or replacing the lighting system does not require loosening or dismantling the camera.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Recommended value
* - **Distance from the FlexiBowl surface**
  - Similar to the camera working distance (+/-100 mm)
* - **Position relative to the camera**
  - Concentric (same optical axis as the camera)
* - **Orientation**
  - Parallel to the FlexiBowl surface and with the same angular orientation as the camera (long side of viewing area - long side of illumination)
* - **Relative camera-TopLight height**
  - Vision optics flush with the upper surface of the TopLight (leave free access to the adjustment rings of the vision optics)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Camera and TopLight position
    :width: 80%
    :align: center
    :::
```

```{tip}
To obtain the best illumination uniformity, follow the guidelines above.
```

```{warning}
**Avoid direct reflections**

When positioning the TopLight, make sure that:

- light does not reflect directly from the FlexiBowl surface into the camera, causing glare
- there are no shadows caused by mechanical components
- illumination is as uniform as possible across the entire useful surface
```

---

## Related references

To complete system installation and configuration:

- **Mechanical camera installation**: [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Camera technical specifications**: [FlexiVision One Specifications](04_Specifiche_FlexiVision.md)
- **System calibration**: [Camera Calibration](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Electrical wiring**: [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
