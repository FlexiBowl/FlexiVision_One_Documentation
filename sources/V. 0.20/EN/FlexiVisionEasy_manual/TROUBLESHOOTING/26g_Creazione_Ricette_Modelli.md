# **Recipe and Model Creation**

(troubleshooting_nuova_ricetta)=
## Troubleshooting for Create a New Recipe

```{warning}
**Error during save**

If recipe saving fails:
- Verify that there is enough free disk space
- Make sure the name does not contain forbidden characters, `/ \\ : * ? " < > |`
- Verify that no recipe with the same name already exists
- Verify that you have write permissions on the software folder
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Impossible to create a new recipe**
  - • Disk full

    • Recipe name contains forbidden characters
  - • Free disk space

    • Avoid special characters in the name, `/ \\ : * ? " < > |`

* - **Recipe saved but settings are lost**
  - • Save not confirmed correctly

    • Forced software shutdown

    • Disk write error
  - • Always click `"Save Recipe"` and wait for confirmation

    • Close the software correctly

    • Check Windows error logs
* - **Impossible to load the created recipe**
  - • Corrupted recipe file

    • File path changed
  - • Restore from backup if available

    • Verify the configured recipe folder path
* - **Loaded recipe contains wrong settings**
  - • Wrong recipe selected

    • Previous changes not saved

    • Conflict between recipes with similar names
  - • Verify the recipe name in the top bar

    • Reload the correct recipe from the list

    • Use unique naming conventions
```

(troubleshooting_nuovo_modello)=
## Troubleshooting for Create a New Model

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions

* - **Grab Train Image acquires a black image**
  - • Camera not connected

    • TopLight off

    • Backlight off

    • Exposure too low

    • Lens cap still installed
  - • Verify camera connection in Camera Setup

    • Turn on the TopLight and verify its power supply

    • Check that Light On is enabled in FlexiBowl Configuration

    • Increase camera exposure

    • Remove the lens cap
* - **ROI cannot be moved or resized**
  - • Image not acquired

    • Software frozen
  - • Execute Grab Train Image first

    • Restart the software

* - **Apply Train does not generate a model**
  - • ROI too small

    • Image without enough contrast

  - • Enlarge ROI so it includes the full component

    • Improve contrast or illumination

* - **Created model includes surface texture**
  - • Feature Threshold too low

    • Insufficient contrast between component and surface
  - • Increase Feature Threshold, for example from `0.3` to `0.6`

    • Improve lighting to increase contrast
* - **Created model has too few lines**
  - • Feature Threshold too high

    • Blurred image

    • Image without enough contrast
  - • Decrease Feature Threshold, for example from `0.8` to `0.5`

    • Verify camera focus and correct it if needed

    • Improve contrast or illumination

* - **Model includes light reflections**
  - • Feature Threshold too low

    • Non-uniform illumination

  - • Increase Feature Threshold

    • Adjust TopLight position or angle

* - **Impossible to assign a model name**
  - • Name contains forbidden characters

    • Name too long
  - • Use only letters, numbers, underscores, and hyphens

    • Limit the name to 50 characters maximum
```

(troubleshooting_modelli_roi)=
## Troubleshooting for ROI Definition and Tolerances

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions

* - **Test does not detect any component**
  - • Accept Threshold too high

    • Components outside the Region Search

    • Incorrect model

    • Lighting changed compared with training
  - • Decrease Accept Threshold, for example from `0.90` to `0.75`

    • Enlarge Region Search so it includes the components

    • Repeat model training

    • Stabilize the lighting
* - **Test detects too many false positives**
  - • Accept Threshold too low

    • Model too simple or too generic

    • Components present that are partly similar but also significantly different
  - • Increase Accept Threshold, for example from `0.70` to `0.85`

    • Recreate the model with a lower Feature Threshold, more detailed

    • Split them into separate models if necessary
* - **Test detects components but scores are too low**
  - • Real component variability compared with the training model

    • Different illumination

    • Dirty or damaged components

    • Model too detailed
  - • Verify component quality and clean them if necessary

    • Standardize lighting

    • Reject damaged components

    • Recreate the model with a higher Feature Threshold, less detailed

* - **Results Panel empty even with visible components**
  - • No component exceeds the Accept Threshold

    • Region Search does not include the components

    • Test not executed
  - • Decrease Accept Threshold

    • Verify and enlarge the Region Search

    • Click the Test button
* - **X, Y, Rotation coordinates incorrect**
  - • Camera calibration not performed or performed badly

    • Wrong reference system

    • Camera moved after calibration
  - • Perform complete camera calibration or review the current one

    • Verify the coordinate system origin

    • Repeat camera calibration
```

(troubleshooting_istogrammi)=
## Troubleshooting for Clearances

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Impossible to enable the histogram**
  - • Model not recognized

    • Maximum number of histograms reached, 8 per model

    • Slot already occupied
  - • Complete model configuration first

    • Disable histograms that are not used

    • Select a free slot

* - **AUTO does not calculate correctly**
  - • Histogram area too small

    • Histogram outside the image

    • Image not loaded
  - • Enlarge the histogram area

    • Move the histogram inside the visible area

    • Acquire a new image
* - **Test always RED even with a free area**
  - • AUTO calibration performed with the area occupied

    • Shadow or reflection in the area

    • FlexiBowl edge included in the area

    • Dirt on the surface
  - • Repeat AUTO with the area completely free

    • Exclude zones with shadows or reflections

    • Reduce the area excluding borders

    • Clean the FlexiBowl surface
* - **Test always GREEN even with an occupied area**
  - • AUTO calibration performed while components were already present

    • Thresholds calculated incorrectly

    • Insufficient contrast
  - • Repeat AUTO making sure the area is completely empty

    • Repeat calibration with stable lighting

    • Improve lighting contrast
* - **Histogram triggers randomly**
  - • Area too large and includes variable zones

    • Unstable lighting

    • Threshold too tight
  - • Reduce the area to the minimum necessary

    • Stabilize the lighting

    • Repeat AUTO calibration
* - **Histogram does not trigger when it should**
  - • Area too small and does not include the obstacle

    • Threshold too permissive

  - • Enlarge the histogram area

    • Repeat AUTO calibration with higher contrast

* - **Impossible to create a second histogram for the gripper**
  - • Wrong histogram slot selected
  - • Return to the list and select Histogram 2
* - **Multiple histogram test does not work**
  - • Not all histograms enabled

    • Incomplete configuration

    • Conflict between histograms
  - • Verify that all required histograms are enabled

    • Complete AUTO configuration for each histogram

    • Verify that the areas do not overlap
```

(troubleshooting_robot_pick)=
## Troubleshooting for Robot Pick Calibration

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Robot coordinates not available, lost or forgotten**
  - • Not written down during physical preparation

    • Note sheet lost

    • Coordinates overwritten
  - • **MANDATORY**: repeat the entire physical preparation from point 1 to point 9 of [Model Creation](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md)

    • Save coordinates in a digital file as well as on paper

    • Take a photo of the robot pendant display
* - **Find Object does not detect the component**
  - • Reference component moved

    • Accept Threshold too high

    • Component outside the Region Search
  - • Verify reference component position

    • Temporarily lower Accept Threshold

    • Verify that Region Search includes the component
* - **Vision Result shows incorrect coordinates**
  - • Camera calibration not performed

    • Coordinate system not configured

    • Camera moved after calibration
  - • Perform camera calibration before Robot Pick

    • Verify the reference system origin

    • Repeat camera calibration
* - **Impossible to enter robot coordinates**
  - • Fields locked

    • Enable Robot Pick not activated

    • Number format incorrect
  - • Click Enable Robot Pick first

    • Activate the fields by clicking them

    • Use a dot as decimal separator
* - **Gripper Offset calculates absurd values**
  - • Robot coordinates entered incorrectly

    • X and Y swapped

    • Wrong plus or minus sign

    • Wrong or rounded decimals
  - • **CRITICAL**: verify every coordinate carefully

    • Check X, Y, RZ order

    • Verify the signs of the coordinates

    • Copy the values exactly as written, without rounding
* - **Robot picks in the wrong positions after calibration**
  - • Noted robot coordinates were wrong

    • Robot Frame or Tool changed after note-taking

    • Reference component moved during note-taking

    • Gripper Offset not saved
  - • Repeat physical preparation verifying correct Frame and Tool

    • Make sure the same Frame and Tool are used for both note-taking and picking

    • Repeat the setup with the component positioned correctly

    • Save the recipe after calculating Gripper Offset
* - **Robot offset valid only for the reference component**
  - • High optical distortion

    • Inaccurate camera calibration

    • Region Search too large compared with the calibration quality
  - • Improve camera calibration

    • Use a low-distortion lens

    • Reduce Region Search if possible
* - **Impossible to save Gripper Offset**
  - • Recipe not loaded

    • Insufficient permissions

    • Disk full
  - • Verify that the recipe is loaded correctly

    • Verify write permissions

    • Free disk space
* - **Robot RZ rotation always wrong**
  - • Robot RZ was not at `0°` during setup

    • Wrong robot last axis

    • Rotated coordinate system
  - • Repeat setup bringing the robot last axis to `RZ = 0°`

    • Verify that the selected tool is correct

    • Verify coordinate system orientation
```
