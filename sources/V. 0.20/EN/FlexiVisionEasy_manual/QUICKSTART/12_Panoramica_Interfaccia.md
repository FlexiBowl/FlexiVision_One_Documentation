

# **DashBoard page**
<img src="../../../../_shared/media/images/pagina_dashboardW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_dashboardB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Dashboard Page Description
:header-rows: 1
:widths: 10 90

* - **#**
  - **Description**

* - 1
  - **Vision and Detection Area**
    * **Detected vision parts with graph**: how many components were detected in the current image and the trend over time (30s).
    

* - 2
  - **Operating Status**
    * **In run**: indicator light showing whether the system is running or stopped.
    * **In run time**: chronometer indicating total system uptime.

* - 3
  - **Controls and Selection**
    * **FlexiBowl® drop-down menu**: allows you to select the FlexiBowl® device you wish to operate on.
    * **Test Locator**: starts cyclic movements of FlexiBowl® and hopper as long as there are components in the vision area.

* - 4
  - **Connection Status**
    * **FlexiBowl®**: indicates the status of the real-time connection with the FlexiBowl®.
    * **Robot**: indicates the status of the real-time connection with the robot.

* - 5
  - **Timings Analysis**
    * **Camera/Locator processing time**: individual image shot and component identification timing.
    * **Total vision processing time**: sum of camera and locator times.
    * **Total FlexiBowl® / Robot time**: time for a FB movement sequence and a single robot pick & place.
    * **Total processing time**: total process time (Vision + FB + Robot).
    * **Fill hopper**: log of discharges from the hopper onto the FlexiBowl® disc.
    * **Vision - FlexiBowl® - Robot**: comparative graph of the three functions to understand the impact of each individual process on the total time.
* - 6
  - **Performance Graphs and Log**
    * **List of detected models**: table with co-ordinates (**X**, **Y**), rotation (**Rot**) of the component and the **Score** (degree of similarity of the identified object compared to the reference model).
    * **Parts per minute**: graph of average parts picked per minute.
```
(recipes)=
# **Recipes page**
<img src="../../../../_shared/media/images/pagina_recipesW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_recipesB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Recipes Page Description
:header-rows: 1
:widths: 10 90

* - **#**
  - **Description**

* - 1
  - **Recipe Database Management**
    * **Backup**: backs up all recipes to a single .xml file, which can be saved in the desired position.
    * **Import backup**: allows the import of any backup previously done with FlexiVision One.
    * **Load recipe**: uploads the recipe selected in the list above to make it operational.
    * **Delete recipe**: permanently deletes the selected recipe from the list.

* - 2
  - **Creating and Saving**
    * **New recipe**: starts the creation of a new recipe. After choosing the name and the FlexiBowl® we are working with, the model creation menu opens directly.
      :::{note}
        The recipe must then be saved by clicking Save.
      :::
    * **Save recipe**: saves the current recipe by overwriting the edited parameters or creates a new file if it does not yet exist.

* - 3
  - **Edit Recipe**
    * **Edit recipe**: direct button that takes you to the configuration and model creation menu for the currently selected recipe.
```

# **Setup Page**
<img src="../../../../_shared/media/images/pagina_setupW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_setupB.png" class="only-dark" style="width: 20%; height: auto;">


```{list-table} Setup Page Description
:header-rows: 1
:widths: 10 90

* - **#**
  - **Description**

* - 1
  - **Status Information**
     - **Current selected recipe**: indicates the name of the recipe currently in use.
     - **Current user name**: shows the logged-in user and the respective login level.
     - **In Run**: indicates whether the application is active.

* - 2
  - **Access Panel**
     - **Name**: field for entering the user name.
     - **Login**: button to confirm credentials and log in to the system.

* - 3
  - **Camera setup**: section dedicated to the configuration of camera parameters.
* - 4
  - **FlexiBowl® setup**: area for setting the movement and control parameters of the FlexiBowl®.
     
* - 5
  - **Hopper setup**: configuration of hopper parameters (vibration and discharge).
     
* - 6
  - **Robot setup**: section for configuring robot communication.

* - 7
  - **Protocol setup**: parameter configuration page defining how many objects the vision must or can return in each cycle, in what order they are prioritised and which statistical values to use based on the number of robot picks and the maximum time to manage each component.
     
* - 8
  - **Account setup**: allows the various user accounts to be configured according to login levels.

* - 9
  - **Laser pointer**: allows a laser tool to be used to simulate a pick in the absence of the robot.
* - 10
  - **Evaluate PPM**: allows you to estimate parts per minute (PPM) when using the laser pointer.

* - 11
  - **Software Licence**: page for activating software licence.
```
# **INFO keys**
There is an INFO key available at the top right of each of the operating sections.
This button has an explanation of the Step By Step procedure. The same procedure can be seen in the video tutorial.
```{dropdown} Info key on the [FLB Camera](cameraFLB) page

   :::{video} ../../../../_shared/media/videos/TastoInfo_CameraFLB_1280x720.mp4
   :width: 100%
   :align: center
   :::

```

```{dropdown} Info key on the page [Calibration](calibrazione)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Calibration_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Train Model](modello)

   :::{video} ../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Define Robot Picking Area](robotarea)

   :::{video} ../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Locator Model](locator)

   :::{video} ../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Clearances](clearances)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Clearances_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Clearance 1](clearance1)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Clearance1_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Picking Offset](pickingoffset)

   :::{video} ../../../../_shared/media/videos/TastoInfo_PickingOffset_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Define Hopper Area](definehopperarea)

   :::{video} ../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info button for the page [Define Value Hopper](definevaluehopper)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
