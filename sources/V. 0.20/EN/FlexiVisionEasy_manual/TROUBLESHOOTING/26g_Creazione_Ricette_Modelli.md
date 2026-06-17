# **Creating Recipes and models**

(troubleshooting_nuova_ricetta)=
## Troubleshooting for the Create a New Recipe section

```{warning}
**Error while saving**

If saving the recipe fails:
- Check that there is sufficient space on the disk
- Ensure that the name does not contain any inadmissible characters (`/ \ : * ? " < > |`)
- Check that a recipe with the same name does not already exist
- Check that you have permission to write on the software folder
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Unable to create new recipe**
  - • Disk full
    
    • Recipe name contains inadmissible characters
  - • Free up disk space
    
    • Avoid special characters in the name (/ \ : * ? " < > |)

* - **Recipe saved but configurations lost**
  - • Saving not confirmed correctly
    
    • Forced software shutdown
    
    • Disk write error
  - • Always click 'Save Recipe' and wait for confirmation
    
    • Close software correctly
    
    • Check Windows error log
* - **Unable to upload created recipe**
  - • Corrupt recipe file
    
    • File path changed
  - • Restore from backup if available
    
    • Check recipe folder path in configuration
* - **Loaded recipe has wrong configuration**
  - • Wrong recipe selected
    
    • Changes not saved previously
    
    • Conflict between recipes with similar names
  - • Check recipe name in top bar
    
    • Reload correct recipe from list
    
    • Use unambiguous naming conventions
```

(troubleshooting_nuovo_modello)=
## Troubleshooting for the Create a New Model section

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions

* - **Grab Train Image captures black image**
  - • Camera not connected
    
    • Toplight off

    • Backlight off 
    
    • Exposure too low
    
    • Lens with protective cap
  - • Check camera connection in Camera Setup
    
    • Switch on toplight and check power supply

    • Check that light on in FlexiBowl® Configuration is ticked
    
    • Increase camera exposure
    
    • Remove lens cap
* - **ROI does not move or resize**
  - • Image not captured
    
    • Software blocked
  - • Run Grab Train Image first
    
    • Reboot software

* - **Apply Train does not generate model**
  - • ROI too small
    
    • Image without sufficient contrast
  
  - • Enlarge ROI to include the whole component
    
    • Improve contrast/illumination

* - **Model created includes surface texture**
  - • Feature Threshold too low
    
    • Insufficient component-surface contrast
  - • Increase Feature Threshold (e.g.: from 0.3 to 0.6)
    
    • Improve lighting to increase contrast
* - **Model created has too few lines**
  - • Feature Threshold too high
    
    • Blurred image

    • Image without sufficient contrast
  - • Decrease Feature Threshold (e.g.: from 0.8 to 0.5)
    
    • Check camera focus and correct if necessary

    • Improve contrast/illumination

* - **Model includes light reflections**
  - • Feature Threshold too low
    
    • Uneven lighting
    
  - • Increase Feature Threshold
    
    • Adjust toplight position/angle


* - **Unable to name model**
  - • Name contains inadmissible characters
    
    • Name too long
  - • Use only letters, numbers, underscores and hyphens
    
    • Limit name to max 50 characters
```

(troubleshooting_modelli_roi)=
## Troubleshooting for the ROI and Tolerance Definition section

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions

* - **Test does not detect any components**
  - • Accept Threshold too high
    
    • Components outside the Region Search
    
    • Incorrect model
    
    • Lighting changed compared to training
  - • Decrease Accept Threshold (e.g.: from 0.90 to 0.75)
    
    • Enlarge Region Search to include components
    
    • Repeat model training
    
    • Stabilise lighting
* - **Test detects too many false positives**
  - • Accept Threshold too low
    
    • Model too simple/generic
    
    • There are very similar components but at the same time with many differences
  - • Increase Accept Threshold (e.g.: from 0.70 to 0.85)
    
    • Redo model with lower Feature Threshold (more detailed)
    
    • Separate into different models if necessary
* - **Test detects components but scores too low**
  - • Variability real components vs. training model
    
    • Different lighting
    
    • Components dirty/damaged
    
    • Model too detailed
  - • Check component quality and clean if necessary
    
    • Standardise lighting
    
    • Discard damaged components
    
    • Redo model with higher Feature Threshold (less detailed)

* - **Results Panel empty even with visible components**
  - • No component exceeds Accept Threshold
    
    • Region Search does not include components
    
    • Test not performed
  - • Decrease Accept Threshold
    
    • Check and expand Region Search
    
    • Click Test button
* - **Incorrect X,Y,Rotation coordinates**
  - • Camera calibration not performed or performed incorrectly
    
    • Incorrect reference system
    
    • Camera moved after calibration
  - • Perform full camera calibration or review current one
    
    • Check coordinate system origin
    
    • Repeat camera calibration
```

(troubleshooting_istogrammi)=
## Troubleshooting for the Histograms section

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Cannot enable histogram**
  - • Model not identified
    
    • Maximum histogram limit reached (8 per model)
    
    • Slot already occupied
  - • Complete model configuration first
    
    • Disable unused histograms
    
    • Select free slot

* - **AUTO does not calculate correctly**
  - • Histogram area too small
    
    • Histogram outside the image
    
    • Image not loaded
  - • Enlarge histogram area
    
    • Move histogram within visible area
    
    • Capture new image
* - **Test always RED even with area clear**
  - • AUTO calibration performed with area occupied
    
    • Shadow or reflection in the area
    
    • FlexiBowl® border included in the area
    
    • Dirt on surface
  - • Repeat AUTO with area completely clear
    
    • Exclude areas with shadows/reflections
    
    • Reduce area excluding borders
    
    • Clean FlexiBowl® surface
* - **Test always GREEN even with area occupied**
  - • AUTO calibration performed with components already present
    
    • Badly calculated thresholds
    
    • Insufficient contrast
  - • Repeat AUTO making sure area is completely empty
    
    • Repeat calibration with stable lighting
    
    • Improve lighting contrast
* - **Histogram triggers accidentally**
  - • Too large an area includes variable zones
    
    • Unstable lighting
    
    • Threshold too narrow
  - • Reduce area to minimum necessary
    
    • Stabilise lighting
    
    • Repeat AUTO calibration
* - **Histogram does not trigger when it should**
  - • Area too small does not include obstacle
    
    • Threshold too permissive
    
  - • Enlarge histogram area
    
    • Repeat AUTO calibration with higher contrast
    
* - **Unable to create second histogram for gripper**
  - • Wrong histogram slot selected
  - • Go back to list and select Histogram 2
* - **Multiple histogram test does not work**
  - • Not all histograms enabled
    
    • Incomplete configuration
    
    • Conflict between histograms
  - • Check that all required histograms are enabled
    
    • Complete AUTO configuration for each histogram
    
    • Check that areas do not overlap
```

(troubleshooting_robot_pick)=
## Troubleshooting for the Robot Pick Calibration section

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Robot coordinates not available (lost/forgotten)**
  - • Not noted during physical preparation
    
    • Lost note sheet
    
    • Coordinates overwritten
  - • **MANDATORY**: Repeat the entire physical preparation from point 1 to point 9 of [Creating Model](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md)
    
    • Save coordinates in digital files as well as on paper
    
    • Take a picture of pendant robot display
* - **Find Object does not detect component**
  - • Reference component moved
    
    • Accept Threshold too high
    
    • Component outside Region Search
  - • Verify reference component position
    
    • Temporarily lower Accept Threshold
    
    • Check Region Search includes component
* - **Vision Result shows wrong coordinates**
  - • Camera calibration not performed
    
    • Coordinate system not configured
    
    • Camera moved after calibration
  - • Perform camera calibration before Robot Pick
    
    • Check reference system origin
    
    • Repeat camera calibration
* - **Unable to enter robot coordinates**
  - • Blocked fields
    
    • Enable Robot Pick not activated
    
    • Wrong number format
  - • Click Enable Robot Pick first
    
    • Activate fields by clicking on them
    
    • Use point as decimal separator
* - **Gripper Offset calculates absurd values**
  - • Robot coordinates entered incorrectly
    
    • X and Y swapped
    
    • Wrong +/- sign
    
    • Incorrect or approximate decimals
  - • **CRITICAL**: Check each coordinate carefully
    
    • Check order X, Y, RZ
    
    • Check coordinate signs
    
    • Copy values exactly as noted without approximations
* - **Robot picks at wrong positions after calibration**
  - • Robot coordinates noted were wrong
    
    • Robot Frame/Tool changed after annotation
    
    • Reference component was moved during annotation
    
    • Gripper Offset not saved
  - • Repeat physical preparation verifying correct Frame/Tool
    
    • Ensure same Frame/Tool for annotation and picking
    
    • Repeat setup with correctly positioned component
    
    • Save recipe after calculating Gripper Offset
* - **Robot offset only valid for reference component**
  - • High optical distortion
    
    • Camera calibration inaccurate
    
    • Region Search too large compared to calibration
  - • Improve camera calibration
    
    • Use low-distortion lens
    
    • Reduce Region Search if possible
* - **Unable to save Gripper Offset**
  - • Recipe not uploaded
    
    • Insufficient permissions
    
    • Disk full
  - • Check correctly loaded recipe
    
    • Verify write permissions
    
    • Free disk space
* - **Robot RZ rotation always incorrect**
  - • RZ robot was not at 0° during setup
    
    • Last robot axis incorrect
    
    • Rotated coordinate system
  - • Repeat setup bringing last robot axis to RZ=0°
    
    • Check that the selected tool is correct
    
    • Check coordinate system orientation
```



