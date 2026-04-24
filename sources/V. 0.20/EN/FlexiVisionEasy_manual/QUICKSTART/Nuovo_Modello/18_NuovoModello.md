(nuovomodello)=
# **Create a New Model**

This page explains how to create a reference model for component recognition.

## **Step 1: Physical setup preparation**

````{list-table}
* - **1**
  - Remove the calibration grid and restore the initial layout:
    - reposition the surface
    - reposition the central flange
    - secure the central flange with its four screws
* - **2**
  - Position one object at the center of the viewing area
````

---

## **Step 2: Access the model**

Once physical preparation is complete, proceed with image acquisition and model creation.

````{list-table}
* - **3**
  - From the **Recipes** page, with the correct recipe selected, click **Edit Recipe**
* - **4**
  - Select the FlexiBowl currently in use
    :::{dropdown}

    :::
* - **5**
  - The available model slots will be shown, up to 8 models per recipe
* - **6**
  - Click **Model 1** to open the **Train Model 1 Cam 1** page
````

#### Train Model interface overview

![Train Model page](../../../../../_shared/media/images/pagina_trainmodel.png)

````{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Function
* - **Enable Model**
  - Activates this model slot and makes it usable
* - **Grab Train Image**
  - Captures a photo of the reference component for training
* - **Score Threshold**
  - Adjusts the model detail level, from 0 for maximum detail to 1 for minimum detail
* - **Train**
  - Generates the model by processing the acquired image
* - **Model Name**
  - Text field used to assign a descriptive name to the model
````

````{tip}
**Managing multiple models**

At this stage only the first model is activated. After completing it, it will be possible to:
- Enable additional slots, Model 2, Model 3, and so on, for different parts inside the same recipe
- Modify existing models
- Disable models that are no longer required

For now, focus on completing the first model.
````

---

## **Step 3: Training procedure**

````{video} ../../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
:width: 100%
:align: center
````

````{list-table}
:widths: 5 95

* - **7**
  - Click **Enable Model** to activate this model. The model is now active and ready to be configured.

* - **8**
  - Click **Grab Train Image** to capture a photo of the reference component positioned on the FlexiBowl

    :::{warning}
    The reference component must remain fixed in that position throughout the entire application creation process.
    :::

* - **9**
  - Move the **ROI box** so that it fully frames the component

* - **10**
  - Move the **origin** reference point to the center of the ROI area

    :::{tip}
    **Where should the origin be placed?**

    The origin is automatically placed at the center of the component.  
    If the pick point does not match the geometric center, move the origin to the:
    - **Pick point**: for asymmetric parts, place it where the gripper actually grasps the part

    *The origin defines point (0,0) of the model coordinate system.*
    :::

* - **11**
  - Use **Score Threshold** to adjust the desired detail level

    ::::{note}
    **Score Threshold**

      ![Score threshold comparison](../../../../../_shared/media/images/confrontomodello.png)

    **Value close to 0** -> detects MORE details, resulting in a more precise model

    **Value close to 1** -> detects FEWER details, resulting in a simpler model
    ::::

    :::{tip}
    **How to choose the optimal Score Threshold**

    **Use a LOW value, 0.1-0.3, when:**
    - The part has many distinctive details such as engravings, logos, or texture
    - Parts are always very similar to each other, with tight tolerances
    - Maximum precision is required even with difficult orientations

    **Use a MEDIUM value, 0.4-0.6, when:**
    - The part has a distinctive but simple shape
    - A balance between precision and tolerance is desired
    - It is the first configuration of a model and a good starting point is needed

    **Use a VERY HIGH value, 0.7-0.9, when:**
    - Significant part-to-part variations are present, with wide tolerances
    - The part surface is highly reflective or variable
    :::

* - **12**
  - Click **Train**
````

---

## **Step 4: Visual check**

After generating the model, it is essential to verify its quality before proceeding.

````{list-table}
* - **13**
  - Zoom into the image to inspect the created model in detail and verify that it is correct

    :::{tip}
      **Characteristics of a valid model**
      ✓ It contains enough lines to recognize the component
      ✓ It does not include the texture of the background surface
      ✓ It avoids light reflections
    :::

    ![Model comparison](../../../../../_shared/media/images/confrontomodello2.png)
````

````{attention}
If the model is not satisfactory:
- Modify the **Score Threshold**
- Click **Train** again
- Repeat until the model is optimal
````

````{tip}
**Optimization strategy**

**Problem: model includes background surface texture**  
-> Solution: increase Score Threshold or increase the Cam Exposure value in `SETUP > Camera Setup > Cam Exposure`

**Problem: model has too few lines and is not distinctive enough**  
-> Solution: decrease Score Threshold

**Problem: model includes reflections**  
-> Solution: increase Score Threshold or adjust camera exposure

Apply gradual changes, typically 0.1 to 0.2 steps, and test every time.
````

---

## **Step 5: Saving**

````{list-table}
* - **14**
  - Name the model with a descriptive name
    :::{tip}
    **Avoid generic names**

    ❌ Names to avoid:
    - `Test`
    - `Trial`
    - `Model1`
    - `New_Model`

    ✓ Recommended names:
    - `Prod_M8_Steel_Screws`
    - `Assembly_Connectors_2024`
    - `QC_Gears_Series_X`

    A clear name makes management easier when many different models are available.
    :::
* - **15**
  - Click **Next** -> the **Define Robot Pick Area** page opens
````

````{seealso}
Proceed to [ROI Definition](roitest) to continue configuration.
````
