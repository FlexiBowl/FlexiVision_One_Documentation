# **Account Setup**

The **Account Setup** page is used to create and delete FlexiVision One user accounts. Each account is assigned an **access level**, which determines which software functions it can use.

```{note}
Account management is restricted to level **5** users (**Engineer**).
```

---

(accesso-alla-configurazione-account)=
## Access to Account Configuration

:::{list-table}
:widths: 10 90

* - **1**
  - Open the **Setup** page.
* - **2**
  - Select **Engineer** from the **Name** drop-down menu.
* - **3**
  - Enter `3` in the **Password** field.
* - **4**
  - Press **Login** and confirm the successful login message with **OK**.
* - **5**
  - Press the **Account Setup** icon.
:::

```{note}
The login takes effect only after pressing **Login**. The active user and its level are shown under **Current User Name**.
```

---

## Account Setup interface overview

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Account list** (left)
  - Shows the existing accounts. **Delete Account** deletes the selected one.
* - **New account** (right)
  - **Account Name**, **Account Password** and **Account Level** fields and the **Create Account** button.
:::

---

## Creating a new account

### *Step 1: Entering the data*

:::{list-table}
:widths: 10 90

* - **6**
  - Enter the name of the new account in the **Account Name** field.
* - **7**
  - Enter the password of the new account in the **Account Password** field.
* - **8**
  - Enter the access level, from `1` to `5`, in the **Account Level** field (see [Access levels](#livelli-di-accesso)).
* - **9**
  - Press **Create Account**. The new account appears in the list on the left.
:::

### *Step 2: Logging in with the new account*

:::{list-table}
:widths: 10 90

* - **10**
  - Go back to the **Setup** page and select the new account from the **Name** drop-down menu.
* - **11**
  - Enter the password and press **Login**.
:::

The video shows how to create a level 3 account, how to log in with the new account and the messages displayed when the level is not sufficient.

:::{video} ../../../../../_shared/media/videos/new_account.mp4
     :width: 100%
     :align: center
:::

---

## Deleting an account

Carry out steps 1 to 5 of [Access to Account Configuration](#accesso-alla-configurazione-account), then proceed as follows.

:::{list-table}
:widths: 10 90

* - **6**
  - Select the account to be deleted from the list on the left.
* - **7**
  - Press **Delete Account**. The account is removed from the list and from the drop-down menu on the **Setup** page.
:::

```{warning}
Deletion is immediate and no confirmation is requested. Check the selected account before pressing **Delete Account**.
```

:::{video} ../../../../../_shared/media/videos/delete_account.mp4
     :width: 100%
     :align: center
:::

---

(livelli-di-accesso)=
## Access levels

FlexiVision One has three predefined profiles. A user-created account receives the permissions corresponding to its assigned level.

:::{list-table}
:header-rows: 1
:widths: 20 20 60

* - Level
  - Profile
  - Use
* - 1 – 3
  - **Operator**
  - Basic functions: browsing the Home page, loading recipes and backup.
* - 4
  - **Technician**
  - Operator functions, plus testing, recipe management, system setup and software licence.
* - 5
  - **Engineer**
  - Technician functions, plus **Protocol Setup** and **Account Setup**.
:::

### *Functions enabled for each profile*

:::{list-table}
:header-rows: 1
:widths: 16 33 17 17 17

* - Page
  - Function
  - Operator (1 – 3)
  - Technician (4)
  - Engineer (5)
* - Home
  - Contact Us
  - Yes
  - Yes
  - Yes
* - Home
  - Documentation
  - Yes
  - Yes
  - Yes
* - Home
  - Quick Start
  - Yes
  - Yes
  - Yes
* - Dashboard
  - Test
  - —
  - Yes
  - Yes
* - Recipes
  - Load Recipe
  - Yes
  - Yes
  - Yes
* - Recipes
  - Backup
  - Yes
  - Yes
  - Yes
* - Recipes
  - Import Backup
  - —
  - Yes
  - Yes
* - Recipes
  - New Recipe
  - —
  - Yes
  - Yes
* - Recipes
  - Save Recipe
  - —
  - Yes
  - Yes
* - Recipes
  - Edit Recipe
  - —
  - Yes
  - Yes
* - Recipes
  - Delete Recipe
  - —
  - Yes
  - Yes
* - Setup
  - Camera Setup
  - —
  - Yes
  - Yes
* - Setup
  - FlexiBowl® Setup
  - —
  - Yes
  - Yes
* - Setup
  - Hopper Setup
  - —
  - Yes
  - Yes
* - Setup
  - Robot Setup
  - —
  - Yes
  - Yes
* - Setup
  - License Software
  - —
  - Yes
  - Yes
* - Setup
  - Protocol Setup
  - —
  - —
  - Yes
* - Setup
  - Account Setup
  - —
  - —
  - Yes
* - General
  - Closing the application
  - —
  - Yes
  - Yes
:::

If you try to use a function that is not enabled, the **Insufficient Access Level** message appears, showing the required level and that of the active user.

### *Automatic logout*

- **Technician**: automatic logout after 5 minutes.
- **Engineer**: no automatic logout.

```{tip}
Assign each user the lowest level sufficient for their tasks, to avoid accidental changes to recipes and configurations.
```
