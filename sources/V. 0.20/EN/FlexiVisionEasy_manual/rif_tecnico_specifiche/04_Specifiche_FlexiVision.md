(specifiche_tecniche)=
# **Detailed FlexiVision One Specifications**

This section provides the complete technical specifications of the FlexiVision One system, including details about the industrial camera, VisionController, calibration grid, communication interfaces, and hardware configurations.

---

(specifiche_camera)=
## Camera

```{figure} ../../../../_shared/media/images/Camera2.png
:alt: FlexiVision One camera CAM-CIC-5000-20G-1
:align: center
:width: 50%
```

The FlexiVision One system uses high-resolution cameras with Gigabit Ethernet interface to guarantee fast image acquisition and accurate component recognition.

### Electrical specifications

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Feature**
  - **Specification**
* - Model
  - CAM-CIC-5000-20G-1
* - Effective Pixels
  - 5 MP, `2448 × 2048`
* - SNR
  - `>38 dB`
* - Dynamic Range
  - `70 dB`
* - GPIO
  - 6-pin Hirose connector: 1 opto-isolated input, 1 opto-isolated output, 1 configurable I/O without optical isolation
* - Image Format
  - Mono8 / 10 / 10Packed
* - Binning
  - Supported
* - Gain
  - X1 ~ X32
* - Gamma
  - From 0 to 4, LUT supported
* - Exposure Time
  - `34.23 μs ~ 1 s`
* - Trigger Mode
  - Software / Hardware / Free run
* - Image Buffer
  - 256 MB
* - User Settings
  - Supports two sets of user-defined configuration
* - Power Supply
  - PoE or DC through Hirose connector, `12 V` or `24 V`
* - Power Consumption
  - `12V ≈ 3.2 W`
* - Lens Mount
  - C-mount
* - Operating Temperature
  - `-30°C ~ +50°C`
* - Storage Temperature
  - `-30°C ~ +80°C`
* - Certifications
  - CE, UL, FCC, RoHS
* - Resolution
  - `2448 x 2048`
* - Pixel Size
  - `3.45 × 3.45 μm`
* - Sensor
  - IMX264 CMOS Global Shutter
* - Sensor Size
  - `2/3"`
* - Frame Rate
  - `24 fps`
* - Bit Depth
  - `12 bit`
* - Interface
  - GigE, PoE
```

### GPIO connector, Hirose 6-pin

```{figure} ../../../../_shared/media/images/Pin_Cam.png
:alt: Hirose 6-pin GPIO connector
:align: center
:width: 70%

Rear view of the camera with connectors
```

```{list-table}
:header-rows: 1
:widths: 10 20 70

* - **Pin**
  - **Signal**
  - **Description**
* - 1
  - Power
  - `12V` or `24V` DC power input
* - 2
  - Line1
  - Opto-isolated input
* - 3
  - Line2
  - Configurable GPIO, software-controlled, without opto-isolation
* - 4
  - Line0
  - Opto-isolated output
* - 5
  - IO GND
  - Opto-isolated ground
* - 6
  - GND
  - Ground
```

```{warning}
**Mandatory network requirements**

The Gigabit Ethernet interface is mandatory and requires compatible network infrastructure, Gigabit Ethernet switch and Ethernet cables of at least Cat6 or Cat7 with S/STP shielding.

Failure to comply with this requirement completely compromises camera operation. Verify that all network components, cables, switches, and ports, support the GigE standard.
```

### Power supply methods

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - **Method**
  - **Description**
  - **Requirements**
* - **PoE**
  - Power and data over a single Ethernet cable. Consumption `3.2 W @ 12 Vdc`.
  - Requires a compatible PoE injector or PoE switch, `IEEE 802.3af/at`
* - **External Camera Cable Supplied in the Kit**
  - External DC power through 6-pin Hirose connector, `12V or 24V`. Included in the kit.
  - A separate Ethernet cable is still required for data
```

```{tip}
**Which method to choose**

- **PoE**: ideal for clean installations with a single cable, but requires dedicated network hardware
- **External power supply**: the most flexible standard solution, recommended for most applications
```

(cavo)=
### Power Cable

```{figure} ../../../../_shared/media/images/Cavo_Specfiche.png
:alt: Camera power cable specifications
:align: center
:width: 100%

Camera power cable specifications
```

```{list-table}
:widths: 30 70
:header-rows: 1

* - Parameter
  - Value
* - **Description**
  - 10 m I/O cable, HRS6P connector
* - **Compatibility**
  - CIC-series cameras
* - **Length**
  - 10 m, 33 ft
* - **Connector 1**
  - Push/Pull 6P RECP Shell SZ 7 Female
* - **Conductor section**
  - 22 AWG
* - **Cable type**
  - Shielded, 3 twisted pairs, flexible
* - **Cable colors**
  - Pin 1: Brown, Pin 2: Green, Pin 3: Pink, Pin 4: Yellow, Pin 5: Gray, Pin 6: White
* - **Shielding**
  - Shield on all conductors
* - **Compliance**
  - UL/CSA and RoHS
```

### Physical specifications and dimensions

![Camera dimensions](../../../../_shared/media/images/Dimensioni_Cam__ab884007b7.png)

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Feature**
  - **Value**
* - Width × Height, body
  - 29 × 29 mm
* - Depth, body
  - 42.0 mm
* - Total depth, including rear connector
  - 48.9 mm
* - Front protrusion, lens mount
  - 12.60 mm
* - Side mounting hole center distance, M2
  - 20.0 × 23.7 mm
* - Front mounting holes
  - 2× M2, depth 3 mm
* - Side mounting holes
  - 4× M2, depth 3.5 mm + 3× M3, depth 3.5 mm
* - Weight
  - 88 g
```

---

(specifiche_obiettivo)=
## Lens

```{figure} ../../../../_shared/media/images/Ottica_000046.png
:alt: FlexiVision One lens
:align: center
:width: 50%
```

```{dropdown} 35 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|------------|-----------------------------|--------|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.069 | 0.167 |
| **Focal Length (mm)** | 34.97 | 34.97 |
| **F Number (Fno)** | 2.00 ~ 16.00 | 2.00 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 507.0 | 200.0 / 207.0 |
| **Object-Image Distance (mm)** | 555.75 | 259.16 |
| **Mechanical Tube Length (mm)** | 36.30 ~ 38.20 | 36.30 ~ 38.20 |
| **Lens Back Focus (mm)** | 14.75 | 18.16 |
| **Depth of Field (mm)** | 35.476 | 6.336 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 37.60 / -22.61 | 37.60 / -22.61 |
| **Entrance/Exit Pupil Position (mm)** | 25.22 / -41.78 | 25.22 / -41.78 |
| **Entrance/Exit Pupil Diameter (mm)** | 17.03 / 26.36 | 17.03 / 26.36 |
| **Field Angle (°) H × V** | 13.69 × 10.34 | 12.62 × 9.76 |
| **TV Distortion (%)** | -0.088 | -0.142 |
| **Relative Illumination (%)** | 44.95 | 50.20 |
| **Weight (g)** | 50 | 50 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

```{dropdown} 25 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.049 | 0.152 |
| **Focal Length (mm)** | 25.00 | 25.00 |
| **F Number (Fno)** | 1.60 ~ 16.00 | 1.60 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 510.0 | 150.0 / 160.0 |
| **Object-Image Distance (mm)** | 553.34 | 205.92 |
| **Mechanical Tube Length (mm)** | 34.60 ~ 38.50 | 34.60 ~ 38.50 |
| **Lens Back Focus (mm)** | 13.75 | 16.33 |
| **Depth of Field @PCoC 0.04 mm (mm)** | 54.223 | 5.835 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 29.42 / -12.46 | 29.42 / -12.46 |
| **Entrance/Exit Pupil Position (mm)** | 18.48 / -31.94 | 18.48 / -31.94 |
| **Entrance/Exit Pupil Diameter (mm)** | 15.92 / 28.32 | 15.92 / 28.32 |
| **Field Angle (°) H × V** | 19.39 × 14.64 | 18.05 × 13.89 |
| **TV Distortion (%)** | -0.041 | -0.271 |
| **Relative Illumination (%)** | 49.78 | 53.52 |
| **Weight (g)** | 50 | 50 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

```{dropdown} 16 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.031 | 0.095 |
| **Focal Length (mm)** | 16.16 | 16.16 |
| **F Number (Fno)** | 1.60 ~ 16.00 | 1.60 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 507.0 | 150.0 / 157.0 |
| **Object-Image Distance (mm)** | 554.26 | 205.30 |
| **Mechanical Tube Length (mm)** | 35.50 ~ 37.00 | 35.50 ~ 37.00 |
| **Lens Back Focus (mm)** | 12.16 | 13.20 |
| **Depth of Field @PCoC 0.04 mm (mm)** | 131.893 | 14.387 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 28.44 / -4.50 | 28.44 / -4.50 |
| **Entrance/Exit Pupil Position (mm)** | 18.85 / -28.07 | 18.85 / -28.07 |
| **Entrance/Exit Pupil Diameter (mm)** | 10.18 / 25.02 | 10.18 / 25.02 |
| **Field Angle (°) H × V** | 30.37 × 22.92 | 29.62 × 22.39 |
| **TV Distortion (%)** | -0.472 | -0.674 |
| **Relative Illumination (%)** | 32.75 | 36.61 |
| **Weight (g)** | 50 | 50 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

```{dropdown} 12 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.023 | 0.075 |
| **Focal Length (mm)** | 12.00 | 12.00 |
| **F Number (Fno)** | 1.80 ~ 16.00 | 1.80 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 505.6 | 150.0 / 155.0 |
| **Object-Image Distance (mm)** | 559.55 | 209.55 |
| **Mechanical Tube Length (mm)** | 39.20 ~ 40.10 | 39.20 ~ 40.10 |
| **Lens Back Focus (mm)** | 12.23 | 12.84 |
| **Depth of Field @PCoC 0.04 mm (mm)** | 277.576 | 28.121 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 17.71 / -0.05 | 17.71 / -0.05 |
| **Entrance/Exit Pupil Position (mm)** | 11.68 / -12.18 | 11.68 / -12.18 |
| **Entrance/Exit Pupil Diameter (mm)** | 6.67 / 13.41 | 6.67 / 13.41 |
| **Field Angle (°) H × V** | 40.54 × 30.77 | 39.40 × 30.05 |
| **TV Distortion (%)** | -0.983 | -0.905 |
| **Relative Illumination (%)** | 40.64 | 42.64 |
| **Weight (g)** | 60 | 60 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

---

(specifiche_VC)=
## VisionController

```{figure} ../../../../_shared/media/images/PC.png
:alt: FlexiVision One VisionController
:align: center
:width: 50%
```

The FlexiVision One system operates on an industrial PC, the VisionController, which acts as the main controller for the vision software. ARS supplies the VisionController already preconfigured and tested with FlexiVision One installed.

### Electrical specifications

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Feature**
  - **Specification**
* - CPU
  - Intel Core i3-1115G4 `1.7 (4.1) GHz`
* - Memory, RAM
  - 8G DDR4 3200 MHz
* - Storage
  - 256G
* - TPM
  - TPM 2.0
* - Operating System
  - Win11 LTSC 2024
* - Power Button
  - Yes, front panel with indicator light
* - Ethernet Ports
  - **i3/i7:** 3× Gb LAN
* - USB Ports
  - 6× USB 3.0 Type A
* - Video Output
  - 2× HDMI
* - Audio
  - Line Out + MIC, 2-in-1 jack
* - Power Supply, V DC
  - 12 ~ 32 V DC
* - Operating Temperature
  - `1°C ~ +50°C`
* - Storage Temperature
  - `-20°C ~ +65°C`
* - Humidity
  - `<90%`, non-condensing
* - Enclosure Material
  - Aluminum alloy + steel
* - Protection Rating
  - IP20
* - Installation Method
  - Wall mounting, optional DIN rail
* - Power Consumption
  - 25 W
* - Dimensions, W × H × D
  - 59.8 × 200 × 119.5 mm
* - Weight
  - 2 kg
* - Certifications
  - CE, UL
```

### PC ports

```{figure} ../../../../_shared/media/images/Spec_Elettriche_PC.png
:alt: VisionController electrical layout
:align: center
:width: 50%
```

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - **Ref.**
  - **Connector**
  - **Description**
* - A
  - Power button
  - Device power on and off
* - B
  - ETH 10/100/1000 Mbit - RJ45, LAN 1
  - Gigabit Ethernet Port 1
* - C
  - ETH 10/100/1000 Mbit - RJ45, LAN 2
  - Gigabit Ethernet Port 2
* - D
  - Serial Port, RS232, COM1
  - RS232 serial interface COM1
* - E
  - Serial Port, RS232, COM2
  - RS232 serial interface COM2
* - F
  - Power input connector
  - `12-32V DC` power input, 3-pin terminal block
* - G
  - Audio Out + MIC, 3.5 mm jack
  - 1× line audio output + microphone input, 3.5 mm jack
* - H
  - 6× USB-A
  - USB ports, USB 3.0 Type A for i3/i7 versions
* - I
  - Video Port 2
  - **B2B12/B2B14:** HDMI 2 - **B2B15/B2B16:** DisplayPort
* - L
  - HDMI Port 1
  - HDMI video output 1
* - M
  - ETH 10/100/1000 Mbit - RJ45, LAN 3
  - Gigabit Ethernet Port 3
```

### Physical specifications

```{figure} ../../../../_shared/media/images/dimensioni_VC.png
:alt: VisionController dimensions
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Screw holes**
  - M5
* - **Feature**
  - **Value**
* - Width, overall with brackets
  - 245.00 mm
* - Width, body
  - 227.00 mm
* - Connector panel width
  - 200.00 mm
* - Height, overall with brackets
  - 123.00 mm
* - Height, body
  - 120.00 mm
* - Depth
  - 61.10 mm
```

---

(laser)=
## Laser Tool for Calibration

The Laser Tool is an advanced calibration solution that improves the precision with which the robot reference point is saved.
Its main advantage is that it does not require physical contact with the calibration grid. By working as a high-precision pointer, the laser allows the operator to align the target point visually and repeatably on the grid, offering much greater accuracy than a physical tip tool.
This precision is essential for successful calibration and fits perfectly with the repeatability guaranteed by the ARS dedicated calibration grid.

![Laser Calibration Tool](../../../../_shared/media/images/laser.png)

| Feature | Laser Tool | Standard Tip Tool |
|--|--|--|
| Reference Method | Non-contact, visual pointer | Contact, physical mechanical tip |
| Reference Precision | Maximum precision, the operator aligns the point visually with high accuracy | Medium, dependent on operator visibility |
| Ease of Use | Simplifies the visual alignment procedure | Requires more attention in positioning and avoiding tilt |
| Key Advantage | Makes it possible to save the robot reference point with the highest possible fidelity, essential for final picking accuracy | Basic method, but less precise than the laser |

```{image} ../../../../_shared/media/images/laserscomp.png
:width: 1px
:class: hidden
```
```{raw} html
<div style="display: flex; align-items: flex-start; gap: 2rem;">
  <img src="../../_images/laserscomp.png" style="width: 280px; flex-shrink: 0;" />
  <table style="border-collapse: collapse; font-size: 0.95em; align-self: center;">
    <thead>
      <tr style="background: #d0d0d0;">
        <th style="padding: 6px 16px; text-align: left;">POS.</th>
        <th style="padding: 6px 16px; text-align: left;">DESCRIPTION</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 5px 16px;">1</td><td style="padding: 5px 16px;">UPPER CLOSING CAP</td></tr>
      <tr><td style="padding: 5px 16px;">2</td><td style="padding: 5px 16px;">CR2032 3V COIN BATTERY HOLDER</td></tr>
      <tr><td style="padding: 5px 16px;">3</td><td style="padding: 5px 16px;">COUPLING FLANGE</td></tr>
      <tr><td style="padding: 5px 16px;">4</td><td style="padding: 5px 16px;">CLAMP</td></tr>
      <tr><td style="padding: 5px 16px;">5</td><td style="padding: 5px 16px;">TOOL BODY</td></tr>
      <tr><td style="padding: 5px 16px;">6</td><td style="padding: 5px 16px;">LASER POINTER</td></tr>
      <tr><td style="padding: 5px 16px;">7</td><td style="padding: 5px 16px;">SPRING DAMPER</td></tr>
      <tr><td style="padding: 5px 16px;">8</td><td style="padding: 5px 16px;">SPACER SUPPORT</td></tr>
    </tbody>
  </table>
</div>
```

:::{important}
To replace the two batteries of the laser tool, follow the dedicated maintenance procedure.
:::

:::{admonition} Recommendation
:class: tip
Using the Laser Tool together with the ARS dedicated calibration grid is the most robust and precise method for FlexiVision One system installation.
:::

---

(specifiche_griglia)=
## Calibration Grid

```{figure} ../../../../_shared/media/images/Calib_Grid.png
:alt: Calibration Grid
:align: center
:width: 50%
```

Excellent calibration is the fundamental requirement for FlexiVision One system accuracy. Only high-precision calibration guarantees that the coordinates detected by the camera, in pixels, are converted accurately into real robot coordinates, in millimeters, ensuring success of the picking application.

### Calibration grid technical specifications

```{dropdown} Grid for FlexiBowl 200
![Grid 200](../../../../_shared/media/images/griglia200.JPG)
```

```{dropdown} Grid for FlexiBowl 350
![Grid 350](../../../../_shared/media/images/griglia350.JPG)
```

```{dropdown} Grid for FlexiBowl 500
![Grid 500](../../../../_shared/media/images/griglia500.JPG)
```

```{dropdown} Grid for FlexiBowl 650
![Grid 650](../../../../_shared/media/images/griglia650.JPG)
```

```{dropdown} Grid for FlexiBowl 800
![Grid 800](../../../../_shared/media/images/griglia800.JPG)
```

```{dropdown} Grid for FlexiBowl 1200
![Grid 1200](../../../../_shared/media/images/griglia1200.JPG)
```

For detailed calibration procedures, refer to [Camera Calibration](../QUICKSTART/SETUP/14_calibrazione_camera.md).

---

## Connection overview

![Connection overview](../../../../_shared/media/images/panoramicacollegamenti.png)

*Complete connection diagram of the FlexiVision One system with robot and FlexiBowl*

```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **From**
  - **To**
  - **Connection**
* - Power mains
  - FlexiBowl
  - `110/230 Vac` power supply
* - Power mains
  - Robot
  - Power supply according to the specifications of your robot
* - Power mains
  - Camera
  - `24 Vdc` power supply
* - Power mains
  - Illuminator, light
  - `24 Vdc` power supply
* - Power mains
  - Hopper Controller
  - `110/230 Vac` power supply
* - Hopper Controller
  - Hopper
  - Power and signal
* - Robot
  - Hopper Controller
  - Digital I/O
* - VisionController
  - Camera
  - Ethernet TCP
* - VisionController
  - FlexiBowl
  - Ethernet TCP
* - VisionController
  - Robot
  - Ethernet TCP
```

For detailed electrical diagrams, refer to [Wiring and Connections](cablaggio).

---

## Optional components

Additional components available separately:

:::{card} TopLight
:link: toplight
:link-type: ref
:class-card: shadow
:::

:::{card} TopLight Power Cable
:link: cavoalimtoplight
:link-type: ref
:class-card: shadow
:::

:::{card} Backlight
:link: backlight
:link-type: ref
:class-card: shadow
:::

:::{card} Switch
:link: switch
:link-type: ref
:class-card: shadow
:::

:::{card} Display
:link: display
:link-type: ref
:class-card: shadow
:::
