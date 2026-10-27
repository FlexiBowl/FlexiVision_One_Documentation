# V. 0.22


## **New Features**

### Mix Applications

- Added combined management of the `mix_Locator` commands for Robot 1, Robot 2 and Robot 3: it is now possible to call multiple models at the same time within a single string (e.g. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
- Added a validity check on `mix_Locator` commands: if the received string does not contain valid models (from 1 to 8), the system returns a dedicated error.
- Added a protection on the `start_Locator` and `mix_Locator` commands: if a Locator is already running, the command is ignored, avoiding unwanted task restarts and unexpected changes to the active models.

### Clearances (Histograms)

- Added support for three region types for the Histogram tools — **Rectangle**, **Annular Sector** and **Circle** — selectable through a dedicated menu in the recipe page, for all available models and histograms.
- Updated the Test Histogram page to correctly display the new region types, drawn in green or red depending on the outcome of the check.
- Added the graphical display of the Histogram index and of the main measurements of the selected region.

### FlexiBowl®

- Added the **Belt Check** function to check the wear and cleanliness status of the belt:
  - acquisition of a reference image of the clean belt through the **Save Clean Reference** button;
  - automatic comparison, through Histogram, between the reference image and the current image of the belt;
  - automatic classification of the belt as **Light**, **Dark** or **Medium** based on the brightness of the reference;
  - display of the belt status with percentage value, color and text indication (**Good**, **Warning**, **Poor**);
  - display of the date of the last Belt Check for each FlexiBowl®.
- Added the **Hopper Step Setup** guided procedure to calculate the number of sequences required to reach the hopper area, with the **Reset Steps**, **Test Sequence** and **Save Hopper Step** functions, and the related calibration status indication.
- Added the possibility to enter FlexiBowl® parameters manually from the keyboard, as an alternative to adjustment via slider.
- Added a non-modal warning message when the parameters of a FlexiBowl® are modified but not yet synchronized with the real device.
- Added **Auto Reset FlexiBowl**: if an error is already present when a movement command is started, the system automatically performs the reset before starting the command.

### Security and Access

- Added the access level check on the common interface buttons: protected functions verify the current user level before execution, showing a message in case of insufficient permissions.

## **Improvements**

### Recipe Creation Wizard

- Added a check on the Picking Offset to the **NEXT** button: if the offset is enabled, it must be calculated and valid before proceeding in the wizard.

### Recipe Interface

- Corrected the display format of the Robot Pick offsets in the recipe pages, forcing the dot as decimal separator instead of the comma.

## **Fixed Issues**

### BackUp Management

- Fixed an error in backup creation that occurred when the path on the PC contained spaces.

### Sequences

- Fixed a display issue that could show apparently duplicated commands in the sequence list.
