# V. 0.22


```{note}
This page refers to version **1.01** of this manual, which is compatible with **FlexiVision Studio v0.21** and **v0.22**.
```

## **New Features**

### Mix Applications

- Added combined handling of `mix_locator` commands for Robot 1, Robot 2, and Robot 3: it is now possible to call multiple models simultaneously within a single string (e.g., `mix_locator_12`, `mix_locator_248`, `mix_locator_12345678`).
- Added a validity check for `mix_locator` commands: if the received string does not contain valid models (1 through 8), the system returns a specific error.
- Added protection for the `start_locator` and `mix_locator` commands: if a Locator is already running, the command is ignored, preventing unwanted task restarts and unexpected changes to active models.

### Clearances (Histograms)

- Added support for three region types for the Histogram tools—**Rectangle**, **Annular Sector**, and **Circle**—selectable via a dedicated menu on the recipe page, for all available models and histograms.
- Updated the Histogram Test page to correctly display the new region types, shown in green or red depending on the test result.
- Added a graphical display of the Histogram index and the key metrics for the selected region.

### FlexiBowl®

- Added the **Belt Check** function to check the belt’s wear and cleanliness:
  - capture a reference image of the clean belt using the **Save Clean Reference** button;
  - automatic comparison, using a histogram, between the reference image and the current image of the belt;
  - Automatic classification of the belt as **Light**, **Dark**, or **Medium** based on the brightness of the reference image;
  - Display of the belt’s condition with a percentage value, color, and text label (**Good**, **Warning**, **Poor**);
  - Display of the date of the last Belt Check for each FlexiBowl®.
- Added the **Hopper Step Setup** wizard to calculate the number of sequences needed to reach the hopper zone, with the **Reset Steps**, **Test Sequence**, and **Save Hopper Step** functions, and a corresponding calibration status indicator.
- Added the ability to manually enter FlexiBowl® parameters via the keyboard, as an alternative to adjusting them using sliders.
- Added a non-modal warning message when FlexiBowl® parameters are modified but have not yet been synchronized with the actual device.
- **Auto Reset FlexiBowl** has been added: if an error is already present when a motion command is initiated, the system automatically performs a reset before executing the command.

### Security and Access

- Added access level checks for common interface buttons: protected functions verify the current user level before execution and display a message if permissions are insufficient.

## **Improvements**

### Recipe Creation Wizard

- Added a check for the Picking Offset to the **NEXT** button: if the offset is enabled, it must be calculated and valid before you can proceed in the wizard.

### Recipe Interface

- Fixed the display format for Robot Pick offsets on the recipe pages, forcing the use of a period as the decimal separator instead of a comma.

## **Resolved Issues**

### Backup Management

- Fixed an error that occurred during backup creation when the path on the PC contained spaces.

### Sequences

- Fixed a display issue that could cause commands to appear duplicated in the list of sequences.
