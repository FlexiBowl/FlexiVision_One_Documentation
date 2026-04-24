(troubleshooting_calib_cam)=
# **Camera Calibration**

## **Pattern not detected**

```{warning}
**Error: "Unable to detect calibration pattern"**

Cause: The software cannot identify the grid pattern.

**Solutions**:
- Increase contrast (adjust exposure or illumination)
- Verify that the entire grid is visible in the image
- Improve focus
- Clean the grid surface (dust or fingerprints may interfere)
- Verify that the grid is the correct one (squares, not circles or other patterns)
```

## **Calibration always "Bad" or "Acceptable"**

```{warning}
**Insufficient calibration quality**

If, despite adjustments, the calibration remains below "Excellent":

1. Verify the camera-FlexiBowl working distance (it must be the calculated one)
2. Check that the camera is parallel to the FlexiBowl plane (it must be perfectly horizontal)
3. Make sure the camera is stable (no vibrations during acquisition)
4. Verify that the lens is fully screwed in 

If the problem persists, there may be a mechanical issue in the mounting. See [Mechanical Installation]009_Installazione_Meccanica.md) for review.
```

## **Errors after lighting change**

```{tip}
**Re-calibration after backlight/toplight change**

If switching from backlight to toplight (or vice versa):

1. Geometric calibration remains valid (it does not need to be repeated)
2. Only the camera exposure must be adjusted for the new lighting type
3. Acquire a test image to verify that the pattern is still clearly visible

In general, it is advisable to decide from the beginning which type of lighting to use and to maintain that configuration.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Calibration fails (software error)**
  - • Calibration grid not detected correctly
    
    • Insufficient/excessive illumination
    
    • Calibration grid damaged or dirty
    
  - • Position the target flat and clearly visible
    
    • Adjust camera exposure to display the target correctly
    
    • Use a clean and intact calibration grid
    
* - **Calibration error too high**
  - • Camera not perfectly orthogonal to the surface
    
    • Calibration grid not flat
    
    • Excessive optical distortion
    
  - • Verify camera orthogonality with a level (tolerance ±1°)
    
    • Position the target on a rigid and flat surface
    
    • Check optical quality of the lens, clean or replace
    
* - **Real coordinates do not match measured coordinates**
  - • Incorrect scale factor (incorrect Tile Size)
    
    • Camera moved after calibration
    
  - • Repeat complete calibration
    
    • Secure the camera firmly to avoid movement
    
    • Verify calibration target dimensions according to documentation
* - **Calibration valid only at image center**
  - • Peripheral optical distortion
    
    • Calibration with too few points
  - • Use a higher-quality low-distortion lens
    
    • Verify that the working distance is correct
```



