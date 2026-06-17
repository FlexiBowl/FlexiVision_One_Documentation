(backup)=
# **Backup Management**

## Overview

The entire configuration of FlexiVision One - hardware setup, calibrations, part models and protocol parameters - is contained in the recipe files. For this reason, backups are essential to keep all data safe.

```{important}
It is recommended to perform a backup after each creation or significant modification of a recipe, before upgrading the FlexiVision software and before any hardware intervention on the system.

**Minimum rule:** at least once a week during normal operation.
```

---

## Backup Procedure

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Step**
  - **Action**
* - Click Backup
  - Click the Backup button in the Recipe menu.
* - Choose the FlexiVision folder
  - Locate the FlexiVision One runtime folder on the VisionController.
* - Choose the destination folder
  - Select the destination folder for the backup.
* - Name with date
  - Always assign a name that includes the date, software version and system identifier or other useful information such as the customer's name. Examples:
    
    - `FV_Recipes_LineA_20260402_SW1.2.xml`
    - `Backup_FlexiVision_ClientABC_Plant3_20260402.xml`
    - `Recipes_FB500_Commissioning_20260315_v1.zip`
    
    Include the software version (visible on the Home page) in the name or in an attached text file.
```

---

## Import Backup Procedure

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Step**
  - **Action**
* - Click Import Backup
  - Click Import Backup from the Recipes section.
* - Select the FlexiVision runtime folder
  - **Select the folder containing the FlexiVision installation.**
* - Select the backup path
  - Set the path of the backup file. FlexiVision will reboot during this process.
* - Post-reset checks
  - After reset, perform the following checks before restarting production:

    1. Check that all expected recipes are listed on the Recipes page.
    2. Confirm that the main recipe can be uploaded without errors.
    3. Check that FlexiBowl® and camera connection tests are passed (green) in Camera Setup.
    4. Confirm that the Dashboard shows the correctly connected devices.

    **Run a test cycle with the main operating recipe to verify correct operation.**
```

---

## Correct recipe management

```{list-table}
:header-rows: 1
:widths: 25 37 38

* - **Action**
  - **Correct method**
  - **Method to avoid**
* - Rename a recipe
  - Recipe page → Rename function in the software.
  - Rename the XML file via File Explorer.
* - Delete a recipe
  - Recipe page → **Delete Recipe** button.
  - Delete the XML file manually.
* - Copy a recipe to another system
  - Recipe Page → Backup → Import Backup to the other system.
  - Copy and paste XML files between two Recipe folders.
* - Edit a recipe parameter
  - Open the recipe in **Edit** mode in the software.
  - Edit the XML file with a text editor.
```
