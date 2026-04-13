(backup)=
# **Backup Management**

## **Overview**

Backing up FlexiVision One consists of copying the `Recipes` folder located on the VisionController. This folder contains all recipes configured in the system, including models, recognition parameters, and related settings, and it is the only user data that must be preserved.

Since no dedicated tool is required, the backup process is simply a copy-and-paste operation performed with File Explorer.

```{important}
It is recommended to perform a backup every time a recipe is created or modified, and in any case before any software update or maintenance activity on the VisionController.
```

---

## **Backup contents**

Inside the FlexiVision One installation folder, the following structure is present:

```
C:\FlexiVision One\
├── Data\
├── Languages\
├── Recipes\          ← only folder to include in the backup
├── Flexivision_Smart_018
└── Package.dat
```

The only folder containing user data is `Recipes\`. The other folders and files belong to the software installation and must not be included in the backup.

```{note}
The exact installation path may vary depending on the system configuration. If in doubt, verify the path in the software settings.
```

---

## **Backup procedure**

```{list-table}
:header-rows: 1
:widths: 10 90

* - **Step**
  - **Action**
* - 1
  - Make sure FlexiVision One is **closed**.
* - 2
  - Open File Explorer on the VisionController and browse to `C:\FlexiVision One\`.
* - 3
  - Right-click the `Recipes` folder and select **Copy**.
* - 4
  - Browse to the desired backup destination, such as a USB drive, network folder, or NAS.
* - 5
  - Paste the folder into the destination. It is recommended to rename it with the date, for example: `Recipes_backup_2025-06-01`.
```

```{warning}
Do not perform the backup while FlexiVision One is running. Copying open files may result in an incomplete or corrupted backup.
```

---

## **Restore procedure**

In case of data loss or VisionController replacement, previous recipes can be restored by following these steps:

```{list-table}
:header-rows: 1
:widths: 10 90

* - **Step**
  - **Action**
* - 1
  - Make sure FlexiVision One is installed on the VisionController and **closed**.
* - 2
  - Open File Explorer and browse to `C:\FlexiVision One\`.
* - 3
  - Rename the existing `Recipes` folder, for example to `Recipes_old`, as a precaution.
* - 4
  - Copy the backup folder to `C:\FlexiVision One\` and rename it `Recipes`.
* - 5
  - Start FlexiVision One: all previously saved recipes will be available again.
```

```{important}
The software version installed on the VisionController must be compatible with the one used when the backup was created. In case of a software update, contact technical support before proceeding with the restore.
```

---

## **Recommendations**

- Keep at least **two backup copies** in separate physical locations, for example one local USB drive and one remote network folder.
- Always label backups with the **date and software version** so they can be identified easily over time.
- Do not modify the contents of the `Recipes` folder manually: recipes must be managed only through the FlexiVision One interface.

```{tip}
For environments with multiple VisionControllers, it is recommended to centralize backups in a shared network folder organized by machine name and date.
```
