(start_control)=
# **`start_control_` command**

```{important}
**Expert function**

Control Camera management is an **Expert** function: it requires knowledge of Cognex VisionPro and C# scripts, and is intended for experienced users. For information on Expert mode, see [What it is and When it is needed](../EXPERT/32_Expert.md).
```

```{note}
**Prerequisites**

The `start_control_` command requires a configured control camera and a loaded VisionPro script. See [Control Cameras](33_Telecamere_Controllo.md). Available from software version v0.24.
```

The `start_control_` command allows the robot to request a visual inspection with a control camera. The robot can add a text parameter, which FlexiVision forwards to the [VisionPro script](35_Script_VisionPro.md).

## Command format

```
start_control_<parameter>
```

The **trailing underscore** of the prefix is **mandatory**. The parameter can be empty or contain numbers, letters and further underscores.

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - Command sent by the robot
  - Text received by VisionPro
  - Behavior of the sample script
* - `start_control_`
  - `""` (empty)
  - Runs both PMRedLines
* - `start_control_1`
  - `"1"`
  - Runs PMRedLine 1 only
* - `start_control_2`
  - `"2"`
  - Runs PMRedLine 2 only
* - `start_control_ABC_123`
  - `"ABC_123"`
  - Custom parameter: requires dedicated logic in the script
```

```{important}
The parameter is treated as **text**. FlexiVision assigns no meaning to values such as `ABC_123`: it is the customer's VisionPro script that must interpret them.
```

```{note}
`start_control_ 1` is also read as parameter `"1"`: leading and trailing spaces are removed. To avoid ambiguity, it is recommended to send `start_control_1`, without spaces.

The `start_control_` prefix is not passed to the script: only the part that follows it is received (for example `"2"` for `start_control_2`).
```

The command can also be run **without a connected robot** from the HMI via **Test Tool**; in this case the result is shown in the HMI but is not transmitted via TCP.

## Response to the robot

The response is the `Output_String` string produced by the VisionPro script. The format shown below is that of the **sample script** and can be adapted to the protocol required by the robot.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Situation
  - Example of Output_String
* - Object found
  - `X=125.450;Y=78.320;Rz=45.000`
* - No object found
  - `Not_Found`
* - Both tools run
  - `1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found`
* - Unexpected parameter
  - `#Error_Control_INVALID_CONTROL`
* - Error on tool 2
  - `#Error_Control_TOOL_RUN;Tool=2`
```

For each tool that is run, only the **first object** recognized is used. If both tools are run, the responses are preceded by the prefixes `1:` and `2:` and separated by `|`.

```{note}
- `X` and `Y` are expressed in the coordinate system configured in the VisionPro tool (pixels or calibrated units): they are not automatically in millimeters.
- `Rz` is expressed in degrees.
- Three decimal places; the dot is always used as the decimal separator, regardless of the Windows language.
```

### Not_Found and errors

`Not_Found` **is not an error**: it indicates that the tool was run but found no object. **Control script errors** always begin with the prefix `#Error_Control_`; camera errors may be reported separately with the prefix `#Error_Camera`. If at least one tool produces an execution error, the script writes the error at the beginning of the response (in the example, tool 1 has priority).

The complete list of messages and recommended actions is available in [Troubleshooting – Control Cameras](../TROUBLESHOOTING/26j_Telecamere_Controllo.md).

## Example exchanges

**Case A – Locator 2 only**

Command sent by the robot: `start_control_2`. VisionPro receives `Input_Control = "2"`, runs `CogPMRedLineTool2`, reads X, Y and Rz of the first result and produces the text response. The display shows the record of Tool 2.

**Case B – two Locators**

Command sent: `start_control_`. VisionPro receives an empty string and runs both tools. The response contains two sections, one for each locator. The image record comes from Tool 1, unless the script is changed otherwise.

**Case C – application parameter**

Command sent: `start_control_ABC_123`. The parameter reaches VisionPro without being interpreted by FlexiVision. The sample script responds `#Error_Control_INVALID_CONTROL`; to use it as a real command, the corresponding logic must be added to the C# script.

```{tip}
For the complete list of robot commands, see [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```
