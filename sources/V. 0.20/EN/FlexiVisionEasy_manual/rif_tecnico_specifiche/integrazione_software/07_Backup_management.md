(backup)=
# **BackUp Management**

## **Overview**

FlexiVision One backup consists of copying the `Recipes` folder located on the VisionController. This folder contains all recipes configured in the system — including models, recognition parameters, and associated settings — and represents the only user data that must be preserved.

Since no dedicated tool is required, the backup process is reduced to a simple copy-and-paste operation through File Explorer.
```{important}
It is recommended to perform a backup every time a recipe is created or modified, and in any case before any software update or maintenance intervention on the VisionController.
```

---

## **Backup Contents**

The following structure is present inside the FlexiVision One installation folder:
```
C:\FlexiVision One\
├── Data\
├── Languages\
├── Recipes\          ← unica cartella da includere nel backup
├── Flexivision_Smart_018
└── Package.dat
```

The only folder that contains user data is `Recipes\`. The other folders and files present belong to the software installation and must not be included in the backup.
```{note}
The exact path of the installation folder may vary depending on the system configuration. If in doubt, check the path in the software settings.
```

---

## **Backup Procedure**
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Step**
  - **Action**
* - 1
  - Make sure that the FlexiVision One software is **closed**.
* - 2
  - Open File Explorer on the VisionController and navigate to `C:\FlexiVision One\`.
* - 3
  - Right-click the `Recipes` folder and select **Copy**.
* - 4
  - Navigate to the desired backup destination (USB drive, network folder, NAS, etc.).
* - 5
  - Paste the folder into the destination. It is recommended to rename it by including the date, for example: `Recipes_backup_2025-06-01`.
```
```{warning}
Do not perform the backup while the FlexiVision One software is running. Copying open files may result in an incomplete or corrupted backup.
```

---

## **Restore Procedure**

In case of data loss or VisionController replacement, previous recipes can be restored by following these steps:
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Step**
  - **Action**
* - 1
  - Make sure that FlexiVision One is installed on the VisionController and **closed**.
* - 2
  - Open File Explorer and navigate to `C:\FlexiVision One\`.
* - 3
  - Rename the existing `Recipes` folder (e.g. `Recipes_old`) as a precautionary measure.
* - 4
  - Copy the backup folder to `C:\FlexiVision One\` and rename it `Recipes`.
* - 5
  - Start FlexiVision One: all previously saved recipes will be available again.
```
```{important}
The software version installed on the VisionController must be compatible with the version used at the time of the backup. In case of a software update, contact technical support before proceeding with the restore.
```

---

## **Recommendations**

- Keep at least **two backup copies** in separate physical locations (e.g. a local USB drive and a remote network folder).
- Always label backups with **date and software version** to make them easier to identify over time.
- Do not manually modify the contents of the `Recipes` folder: recipes must be managed exclusively through the FlexiVision One interface.
```{tip}
For environments with multiple VisionController units, it is recommended to centralize backups in a shared network folder, organized by machine name and date.
```
