(telecamere_controllo)=
# **Control Cameras**

```{important}
**Expert function**

Control Camera management is an **Expert** function: it requires knowledge of Cognex VisionPro and C# scripts, and is intended for experienced users. For information on Expert mode, see [What it is and When it is needed](../EXPERT/32_Expert.md).
```

```{note}
**Available from software version v0.24**

The functions described in this section were introduced with FlexiVision One v0.24. See the [Release Notes – V. 0.24](../APPENDICI/V.0.24.md).
```

In addition to the vision camera used for picking, FlexiVision One manages **3 independent control cameras**, associated with **FLB1**, **FLB2** and **FLB3** respectively. Control cameras make it possible to perform a **visual inspection** at the robot's request, for example to check a picked part, and to return the outcome of the check to the robot.

## What it is used for

The `start_control_` command allows the robot to request an inspection from FlexiVision using a control camera. The robot can add a **text parameter** after the underscore (`_`): FlexiVision forwards the parameter to the **VisionPro script**, which decides which tools to run and which results to return.

```{important}
**Operating principle**

The HMI configuration remains unchanged: the customer can adapt the inspection rules and the result format by editing their own **VisionPro script**, without touching the FlexiVision One interface.
```

## Operating sequence

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - #
  - Actor
  - Action
* - 1
  - **Robot**
  - Sends `start_control_` or `start_control_<parameter>`.
* - 2
  - **FlexiVision**
  - Acquires the image with the associated control camera and starts the VisionPro script.
* - 3
  - **VisionPro**
  - Runs the selected tools and prepares a text response and a graphic record.
* - 4
  - **FlexiVision**
  - Shows the image and the string in the HMI; sends the string to the robot **only if connected**.
```

For each check, FlexiVision manages a **Main Task** dedicated to the control camera, with error handling, logging and sending of the results to the robot.

## Using it from the HMI

The HMI pages of the control cameras are **shared** among the devices: select the relevant device from the **Control FlexiBowl®** section.

```{list-table}
:header-rows: 1
:widths: 25 75

* - Page
  - Function
* - **Setup Camera Ctrl**
  - Configuration of the control camera.
* - **Setup Tool Ctrl**
  - VisionPro configuration: allows you to work on the tools and on the VisionPro script (see [VisionPro Script](35_Script_VisionPro.md)).
* - **View Runtime**
  - Display of the image and of the check result.
* - **Test Tool**
  - Starts a local check, even without a connected robot.
```

```{note}
With the **Test Tool** command the check is run even **without a connected robot**: in this case the result is shown in the HMI but is **not transmitted via TCP**.
```

## Quick acceptance test

After installing or modifying the VisionPro script, carry out the following checks:

- ☐ Send `start_control_1` and check the text result and the image of PMRedLine 1.
- ☐ Send `start_control_2` and check the text result and the image of PMRedLine 2.
- ☐ Send `start_control_` and check that the string contains both results.
- ☐ Send `start_control_ABC` and check the `INVALID_CONTROL` error of the sample script.
- ☐ Run **Test Tool** with the robot disconnected and check that the HMI and VisionPro remain operational.

## Further reading

- [`start_control_` command](34_Comando_start_control.md): command format, parameters, responses and example exchanges.
- [VisionPro Script](35_Script_VisionPro.md): script interface, customization and complete sample code.
- [Troubleshooting – Control Cameras](../TROUBLESHOOTING/26j_Telecamere_Controllo.md): error messages and recommended actions.
- [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): complete list of robot commands.
