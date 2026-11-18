(troubleshooting_telecamere_controllo)=
# **Control Cameras**

```{important}
**Expert function**

Control Camera management is an **Expert** function: it requires knowledge of Cognex VisionPro and C# scripts, and is intended for experienced users. For information on Expert mode, see [What it is and When it is needed](../EXPERT/32_Expert.md).
```

```{note}
This page concerns the `start_control_` command and the VisionPro scripts (available from software version v0.24). For the complete procedure, refer to [Control Cameras](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) and [`start_control_` command](../TELECAMERE_CONTROLLO/34_Comando_start_control.md).
```

## Responses and error messages

Errors relating to the control script begin with `#Error_Control_`. The `Not_Found` case **is not a software error**: it means that the locator did not detect any object. Camera errors may be reported separately with the prefix `#Error_Camera`.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Response
  - Meaning / recommended action
* - `Not_Found`
  - Inspection completed with no detections: check the part, the image and the model.
* - `#Error_Control_INVALID_CONTROL`
  - The parameter is not handled by the script: check the text after `start_control_`.
* - `#Error_Control_TOOL_NOT_FOUND`
  - One of the expected tools is missing or has a different name.
* - `#Error_Control_LAST_RECORD_NULL`
  - The record of the tool's last run is not available.
* - `#Error_Control_INPUT_IMAGE_RECORD_NULL`
  - The `InputImage` subrecord is not available.
* - `#Error_Control_RECORD_WITHOUT_IMAGE`
  - The selected record does not contain a valid image.
* - `#Error_Control_VISIONPRO_JOB`
  - The execution of the VisionPro task generated an error.
* - `#Error_Control_EMPTY_OUTPUT`
  - The script did not return a valid string.
* - `#Error_Camera …`
  - Acquisition problem: check the camera connection and status.
```

```{note}
The sample script may also return `#Error_Control_TOOL_RUN` when the results of a tool are not available (for example `#Error_Control_TOOL_RUN;Tool=2` if the error concerns tool 2). If at least one tool produces an execution error, the error is written at the beginning of the response.
```

## Quick checks

- Check that the command has the **trailing underscore** (`start_control_`) and that the parameter contains no spaces.
- Check that the ToolBlock input and output names are still `Image`, `Input_Control`, `Output_String` and `Output_Image`.
- Check that the `Output_Image` output is configured as a compatible `CogRecord`.
- Run **Test Tool** from the HMI even without a connected robot to isolate the problem from TCP communication: in this case the result is shown in the HMI but is not transmitted to the robot.
- After every change to the script, repeat the [quick acceptance test](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md).
