(troubleshooting_calib_cam)=
# **Camera Calibration**

## **Pattern not detected**

```{warning}
**Error: "Unable to detect calibration pattern"**

Cause: the software cannot identify the grid pattern.

**Solutions**:
- Increase contrast by adjusting exposure or lighting
- Verify that the entire grid is visible in the image
- Improve focus
- Clean the grid surface, as dust or fingerprints may interfere
- Verify that the correct grid is being used, with squares and not circles or other patterns
```

## **Calibration always rated "Bad" or "Acceptable"**

```{warning}
**Insufficient calibration quality**

If calibration remains below "Excellent" despite the adjustments:

1. Verify the camera-FlexiBowl working distance, which must match the calculated one
2. Check that the camera is parallel to the FlexiBowl plane and perfectly horizontal
3. Make sure the camera is stable and there are no vibrations during acquisition
4. Verify that the lens is fully screwed in

If the problem persists, there may be a mechanical installation issue. Review [Mechanical Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md).
```

## **Errors after changing illumination**

```{tip}
**Recalibration after changing backlight or toplight**

If you switch from backlight to toplight, or vice versa:

1. Geometric calibration remains valid, so it does not need to be repeated
2. Only camera exposure must be adjusted for the new lighting type
3. Acquire a test image to verify that the pattern is still clearly visible

In general, it is recommended to decide the lighting type from the beginning and keep that configuration unchanged.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Calibration fails with software error**
  - • Calibration grid not detected correctly

    • Lighting insufficient or excessive

    • Calibration grid damaged or dirty

  - • Position the target flat and fully visible

    • Adjust camera exposure so the target is clearly visible

    • Use a clean and undamaged calibration grid

* - **Calibration error too high**
  - • Camera not perfectly orthogonal to the surface

    • Calibration grid not perfectly flat

    • Excessive optical distortion

  - • Verify camera orthogonality with a level, tolerance ±1°

    • Position the target on a rigid, flat surface

    • Check lens optical quality and clean or replace it if required

* - **Real coordinates do not match measured coordinates**
  - • Incorrect scale factor, wrong Tile Size

    • Camera moved after calibration

  - • Repeat the complete calibration

    • Secure the camera firmly to prevent movement

    • Verify calibration target dimensions according to the documentation
* - **Calibration valid only at the center of the image**
  - • Peripheral optical distortion

    • Calibration performed with too few points
  - • Use a higher-quality low-distortion lens

    • Verify that the working distance is correct
```
