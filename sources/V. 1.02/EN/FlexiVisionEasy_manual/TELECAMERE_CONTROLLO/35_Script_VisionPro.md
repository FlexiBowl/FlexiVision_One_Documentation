(script_visionpro)=
# **VisionPro Script**

```{important}
**Expert function**

Control Camera management is an **Expert** function: it requires knowledge of Cognex VisionPro and C# scripts, and is intended for experienced users. For information on Expert mode, see [What it is and When it is needed](../EXPERT/32_Expert.md).
```

```{note}
**Prerequisites**

Before modifying the script, see [Control Cameras](33_Telecamere_Controllo.md) and [`start_control_` command](34_Comando_start_control.md). Available from software version v0.24.
```

The VisionPro **ToolBlock** of the control cameras provides a complete C# example, based on two Cognex `CogPMRedLineTool` tools. The command received from the robot determines which tools are run; the script builds a text response and selects the image record to be shown on the FlexiVision Runtime page.

The customer works **on the VisionPro ToolBlock**, without having to configure or modify the expressions of the HMI page: the input and output names must remain those exposed by the ToolBlock.

## Data flow

```{list-table}
:header-rows: 1
:widths: 40 60

* - Input / processing
  - Result
* - **Robot** → `start_control_<parameter>`
  - The text following the prefix becomes `Input_Control`.
* - **Input_Control** → tool selection
  - Runs PMRedLine 1, PMRedLine 2 or both.
* - **Results[0].GetPose()**
  - Reads X, Y and rotation of the first available result.
* - **Output_String**
  - Returns coordinates, `Not_Found` or a `#Error_Control_` error.
* - **Output_Image**
  - Returns a `CogRecord` that can be displayed in the HMI with the available graphics.
```

## ToolBlock inputs and outputs

```{list-table}
:header-rows: 1
:widths: 25 20 55

* - Name
  - Type
  - Function
* - **Image**
  - `ICogImage`
  - Image acquired by the camera, connected to the vision tools.
* - **Input_Control**
  - `String`
  - Optional text parameter received after `start_control_`.
* - **Output_String**
  - `String`
  - Text returned to FlexiVision (for example coordinates or `Not_Found`).
* - **Output_Image**
  - `CogRecord`
  - Graphic record intended for the Runtime display.
```

```{important}
The names of the two outputs must remain **`Output_String`** and **`Output_Image`** in order to keep the links already set up with the HMI. The structure of the HMI must not be modified.
```

## How the script interprets the command

The sample code checks `Input_Control`: empty value = both PMRedLines; `"1"` = first tool; `"2"` = second tool. Unexpected values produce an error. This part is **customizable** to handle custom commands.

```csharp
string control = Convert.ToString(mToolBlock.Inputs["Input_Control"].Value).Trim();
bool run1 = control == "" || control == "1";
bool run2 = control == "" || control == "2";
```

```{list-table}
:header-rows: 1
:widths: 35 25 40

* - Robot command
  - Tools run
  - Text / image
* - `start_control_`
  - 1 and 2
  - Responses of both; image of tool 1.
* - `start_control_1`
  - Tool 1 only
  - Response and image of tool 1.
* - `start_control_2`
  - Tool 2 only
  - Response and image of tool 2.
* - `start_control_ABC_123`
  - None, in the example
  - `Output_String` = `#Error_Control_INVALID_CONTROL`.
```

The sample script supports **exactly three choices**. The parameter is free at protocol level, but the default C# logic must be extended to accept custom values such as `ABC_123`.

## Output_String: text response

For each tool that is run, the script reads the first object recognized (`Results[0]`), derives X and Y from it, converts the rotation from radians to degrees (`Rz = Rotation × 180 / π`) and builds a string with three decimal places (`F3` format). The dot is always used as the decimal separator through `CultureInfo.InvariantCulture`.

The `GetLocatorResult()` function receives a `CogPMRedLineTool` that has already been run and returns a string: if `Results` is null it reports `#Error_Control_TOOL_RUN`; if `Results.Count` is zero it returns `Not_Found`; otherwise it reads `Results[0].GetPose()`, where `TranslationX` and `TranslationY` provide the coordinates.

The formulas and response formats are described in [`start_control_` command](34_Comando_start_control.md).

```{note}
The X and Y coordinates belong to the reference system configured in the VisionPro tool and are not automatically millimeters. The format shown is an example and can be adapted to the protocol required by the robot.
```

## Output_Image: image with graphic results

The `Output_Image` output is of type **`CogRecord`**, not an image file, and does not require saving to disk. In the example, the script retrieves the `LastRunRecord` of the selected PMRedLine, extracts the `InputImage` subrecord and assigns it to the graphic output displayed in the HMI.

```csharp
CogRecord lastRecord = displayTool.CreateLastRunRecord() as CogRecord;
CogRecord imageRecord = lastRecord.SubRecords["InputImage"] as CogRecord;
mToolBlock.Outputs["Output_Image"].Value = imageRecord;
```

The subrecord must contain a valid image (`ICogImage`); the graphics displayed depend on the results and on the recording settings of the VisionPro tool, and may include the PMRedLine graphic overlays.

```{note}
**Display selection**

With `Input_Control = "2"` the record of PMRedLine 2 is shown. With `"1"` or an empty parameter, the record of PMRedLine 1 is shown. When both tools are run, the text output includes both results, but the image comes from the **first tool**. The graphics of the two tools are not combined automatically: to show Tool 2 or another subrecord, modify the section *"6 - Select tool for image output"* of the script.
```

## Execution sequence (GroupRun)

```{list-table}
:header-rows: 1
:widths: 35 65

* - Phase
  - Code behavior
* - **1 – Reset outputs**
  - Clears `Output_Image` and `Output_String` before the inspection.
* - **2 – Read Input_Control**
  - Reads the parameter and accepts the values empty, `"1"` or `"2"`.
* - **3 – Get tool references**
  - Retrieves `CogPMRedLineTool1` and `CogPMRedLineTool2` by name.
* - **4 – Execute locators**
  - Runs only the requested locators through `RunTool()`.
* - **5 – Generate Output_String**
  - Builds the response, giving priority to execution errors.
* - **6 – Select display tool**
  - Chooses which tool provides the graphic record to be shown.
* - **7 – Get LastRunRecord**
  - Reads the record of the last run of the selected tool.
* - **8 – Extract InputImage**
  - Extracts the `InputImage` subrecord and checks that it contains `ICogImage`.
* - **9 – Export Output_Image**
  - Assigns the validated `CogRecord` to the HMI graphic output.
```

## Customizing the script

1. **Tool selection**: modify the reading of `Input_Control` to start the desired tools.
2. **Result formatting**: adapt `GetLocatorResult()` and the composition of `Output_String` to the robot or check required.
3. **Image selection**: choose which `LastRunRecord` and which subrecord to display through `Output_Image`.
4. **Verification**: save the script and try the commands from test mode or from the robot, checking text and image.

### What can be customized and what must be preserved

```{list-table}
:header-rows: 1
:widths: 50 50

* - Can be customized
  - To be kept consistent
* - Tool selection criteria for new parameters.
  - Reading of the `Input_Control` input.
* - Vision tools and names of the tools run.
  - References matching the tools actually present.
* - Format and content of `Output_String`, score, multiple objects.
  - `#Error_Control_` prefix for errors.
* - Record or subrecord assigned to `Output_Image`.
  - `Output_Image` must remain a compatible `CogRecord`.
* - Calibrations, coordinates and units of measurement.
  - Check of the format the robot expects.
```

```{important}
Before loading a modified script, run a test with an empty parameter, one test for each locator and at least one error test. Check in the HMI that `Output_String` and `Output_Image` are updated and that the robot receives only the agreed format.
```

## Appendix A – Complete VisionPro script

The sample script supplied with FlexiVision One v0.24 is reproduced in full below. The comments in the source are in English; the sections are numbered to make modifications easier. The code shows how to define the response logic and how to select the image with the graphics to be displayed.

**CogToolBlockAdvancedScript – C# example**

```csharp
#region namespace imports
using System;
using System.Globalization;
using Cognex.VisionPro;
using Cognex.VisionPro.ToolBlock;
using Cognex.VisionPro.Implementation;
using Cognex.VisionPro.PMRedLine;
#endregion

// ============================================================================
// FLEXIVISION - CUSTOM VISIONPRO SCRIPT EXAMPLE
// ============================================================================
//
// DESCRIPTION
// -----------
// This script demonstrates how to execute Cognex VisionPro inspection tools,
// retrieve object positions, generate custom result strings, and export
// graphical inspection records to the FlexiVision HMI.
//
// The example uses two CogPMRedLineTools. Customers can customize this script
// to implement their own inspection logic using other VisionPro tools.
//
// ROBOT COMMAND FORMAT
// --------------------
// FlexiVision receives the following commands from the robot:
//
// start_control_       -> Input_Control = ""
// start_control_1       -> Input_Control = "1"
// start_control_2       -> Input_Control = "2"
// start_control_ABC_123 -> Input_Control = "ABC_123"
//
// The parameter following "start_control_" is forwarded to VisionPro.
// The customer script determines how to interpret the received parameter.
//
// INPUTS
// ------
// Image         : Camera image connected to the inspection tools.
// Input_Control : Optional parameter received from the robot.
//
// OUTPUTS
// -------
// Output_String : Inspection results or error information.
// Output_Image : CogRecord containing the selected image and graphical data.
//
// RESULT FORMAT
// -------------
// Object found:
// X=125.450;Y=78.320;Rz=45.000
//
// Object not found:
// Not_Found
//
// Both tools executed:
// 1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found
//
// ERROR HANDLING
// --------------
// All execution errors must start with the following prefix:
//
// #Error_Control_
//

// Examples:
// #Error_Control_INVALID_CONTROL
// #Error_Control_TOOL_NOT_FOUND
// #Error_Control_TOOL_RUN
// #Error_Control_LAST_RECORD_NULL
// #Error_Control_INPUT_IMAGE_RECORD_NULL
// #Error_Control_RECORD_WITHOUT_IMAGE
//
// IMPORTANT
// ---------
// - Only the first detected object is returned for each locator.
// - X and Y use the coordinate system configured in VisionPro.
// - Rz is expressed in degrees.
// - Not_Found is an inspection result, not an execution error.
// - Output_Image is permanently linked to the FlexiVision HMI.
// - Customers can customize the script without modifying the HMI.
//
// ============================================================================

public class CogToolBlockAdvancedScript : CogToolBlockAdvancedScriptBase
{
    // ========================================================================
    // PRIVATE VARIABLES
    // ========================================================================

    // Reference to the VisionPro ToolBlock hosting this script.
    // Provides access to inputs, outputs, and inspection tools.

    private CogToolBlock mToolBlock;

    // ========================================================================
    // FUNCTION - GET LOCATOR RESULT
    // ========================================================================
    //
    // Extracts the position and rotation of the first detected object.
    //
    // RETURN VALUES
    // -------------
    // Object found : X=125.450;Y=78.320;Rz=45.000
    // Object missing : Not_Found
    // Results invalid: #Error_Control_TOOL_RUN
    //
    // CUSTOMIZATION
    // -------------
    // Customers can modify this function to:
    // - Change the result string format.
    // - Include additional information such as matching score.
    // - Return multiple detected objects.
    // - Apply custom coordinate transformations.
    // - Adapt the output to their robot communication protocol.
    //
    // ========================================================================

    private string GetLocatorResult(CogPMRedLineTool tool)
    {
        // --------------------------------------------------------------------
        // STEP 1 - CHECK RESULT AVAILABILITY
        // --------------------------------------------------------------------
        // A null results collection indicates that inspection results
        // are not available.

        if (tool.Results == null)
            return "#Error_Control_TOOL_RUN";

        // --------------------------------------------------------------------
        // STEP 2 - CHECK OBJECT DETECTION
        // --------------------------------------------------------------------
        // Return Not_Found when no objects are detected.
        // This is a valid inspection result, not an execution error.

        if (tool.Results.Count == 0)
            return "Not_Found";

        // --------------------------------------------------------------------
        // STEP 3 - GET THE FIRST DETECTED OBJECT
        // --------------------------------------------------------------------
        // Results[0] contains the first result returned by the locator.
        // GetPose() provides the object's position and orientation.

        CogTransform2DLinear pose = tool.Results[0].GetPose();

        // --------------------------------------------------------------------
        // STEP 4 - EXTRACT POSITION AND ROTATION
        // --------------------------------------------------------------------
        // X and Y use the coordinate system configured in VisionPro.
        // Rotation is converted from radians to degrees.

        double x = pose.TranslationX;
        double y = pose.TranslationY;
        double rz = pose.Rotation * 180.0 / Math.PI;

        // --------------------------------------------------------------------
        // STEP 5 - FORMAT RESULT STRING
        // --------------------------------------------------------------------
        // F3 specifies three decimal places.
        // InvariantCulture ensures that the decimal separator is always a dot.
        //
        // CUSTOMIZATION:
        // Modify the format according to the required robot protocol.

        return "X=" + x.ToString("F3", CultureInfo.InvariantCulture) +
            ";Y=" + y.ToString("F3", CultureInfo.InvariantCulture) +
            ";Rz=" + rz.ToString("F3", CultureInfo.InvariantCulture);
    }

    // ========================================================================
    // MAIN FUNCTION - GROUP RUN
    // ========================================================================
    //
    // EXECUTION SEQUENCE
    // ------------------
    // 1. Reset outputs.
    // 2. Read Input_Control.
    // 3. Retrieve inspection tools.
    // 4. Execute selected locators.
    // 5. Generate Output_String.
    // 6. Select the tool for image visualization.
    // 7. Retrieve its LastRunRecord.
    // 8. Extract the image record.
    // 9. Export the record to the FlexiVision HMI.
    //
    // ========================================================================

    public override bool GroupRun(ref string message, ref CogToolResultConstants result)
    {
        // ====================================================================
        // 1 - RESET OUTPUTS
        // ====================================================================
        // Clear previous results to prevent outdated information
        // from being displayed during a new inspection cycle.

        mToolBlock.Outputs["Output_Image"].Value = null;
        mToolBlock.Outputs["Output_String"].Value = "";

        // ====================================================================
        // 2 - READ ROBOT CONTROL PARAMETER
        // ====================================================================
        // FlexiVision receives the command from the robot and forwards
        // the optional parameter to the VisionPro script.

        //
        // Robot command              VisionPro Input_Control
        // ------------------------------------------------
        // start_control_        ""
        // start_control_1       "1"
        // start_control_2       "2"
        // start_control_ABC     "ABC"
        //
        // In this example:
        // Empty -> Run both inspection tools.
        // "1" -> Run PMRedLine Tool 1.
        // "2" -> Run PMRedLine Tool 2.
        //
        // CUSTOMIZATION:
        // Customers can implement additional control parameters.

        string control = Convert.ToString(mToolBlock.Inputs["Input_Control"].Value).Trim();

        bool run1 = control == "" || control == "1";
        bool run2 = control == "" || control == "2";

        // Reject unsupported control parameters.
        // All error messages must begin with #Error_Control_.

        if (!run1 && !run2)
        {
            mToolBlock.Outputs["Output_String"].Value = "#Error_Control_INVALID_CONTROL";
            return false;
        }

        // ====================================================================
        // 3 - GET INSPECTION TOOL REFERENCES
        // ====================================================================
        // Retrieve the PMRedLine tools from the current ToolBlock.
        //
        // IMPORTANT:
        // Tool names must match those configured in VisionPro.
        //
        // CUSTOMIZATION:
        // Customers can replace these references with other VisionPro tools.

        CogPMRedLineTool tool1 = mToolBlock.Tools["CogPMRedLineTool1"] as CogPMRedLineTool;
        CogPMRedLineTool tool2 = mToolBlock.Tools["CogPMRedLineTool2"] as CogPMRedLineTool;

        // Verify that the required tools are available.

        if (tool1 == null || tool2 == null)
        {
            mToolBlock.Outputs["Output_String"].Value = "#Error_Control_TOOL_NOT_FOUND";
            return false;
        }

        // ====================================================================
        // 4 - EXECUTE SELECTED LOCATORS
        // ====================================================================
        // Execute only the tools enabled by Input_Control.
        //
        // RunTool() executes the selected VisionPro inspection tool.
        // GetLocatorResult() extracts and formats the detected object's pose.
        //
        // If no object is found, the result is Not_Found.

        string result1 = "";
        string result2 = "";

        // --------------------------------------------------------------------
        // EXECUTE PMREDLINE TOOL 1
        // --------------------------------------------------------------------

        if (run1)
        {
            mToolBlock.RunTool(tool1, ref message, ref result);
            result1 = GetLocatorResult(tool1);
        }

        // --------------------------------------------------------------------
        // EXECUTE PMREDLINE TOOL 2
        // --------------------------------------------------------------------

        if (run2)
        {
            mToolBlock.RunTool(tool2, ref message, ref result);
            result2 = GetLocatorResult(tool2);
        }

        // ====================================================================
        // 5 - GENERATE OUTPUT STRING
        // ====================================================================
        // Create the inspection result string sent to FlexiVision.
        //
        // When both tools are executed, their results are separated by "|".
        //
        // Examples:
        //
        // Tool 1:
        // X=125.450;Y=78.320;Rz=45.000
        //
        // Tool 2:
        // X=210.100;Y=90.500;Rz=-30.000
        //
        // Both tools:
        // 1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found
        //
        // ERROR HANDLING:
        // An execution error takes priority over successful inspection
        // results and must appear at the beginning of Output_String.
        //
        // CUSTOMIZATION:
        // Customers can modify the result format for their robot protocol.

        string outputString = "";

        if (run1 && result1.StartsWith("#Error_Control_", StringComparison.Ordinal))
        {
            outputString = result1 + ";Tool=1";
        }
        else if (run2 && result2.StartsWith("#Error_Control_", StringComparison.Ordinal))
        {
            outputString = result2 + ";Tool=2";
        }
        else if (run1 && run2)
        {
            outputString = "1:" + result1 + "|2:" + result2;
        }
        else if (run1)
        {
            outputString = result1;
        }
        else if (run2)
        {
            outputString = result2;
        }

        // Export the result string to FlexiVision.

        mToolBlock.Outputs["Output_String"].Value = outputString;

        // ====================================================================
        // 6 - SELECT TOOL FOR IMAGE OUTPUT
        // ====================================================================
        // Select which inspection tool provides the graphical image record
        // displayed in the FlexiVision HMI.
        //
        // DEFAULT BEHAVIOR
        // ----------------
        // Input_Control = "" -> Display Tool 1.
        // Input_Control = "1" -> Display Tool 1.
        // Input_Control = "2" -> Display Tool 2.
        //
        // IMPORTANT:
        // When both tools execute, only Tool 1 is selected for visualization.
        //
        // CUSTOMIZATION:
        // Customers can select another VisionPro tool's graphical record.

        CogPMRedLineTool displayTool;

        if (control == "2")
        {
            displayTool = tool2;
        }
        else
        {
            displayTool = tool1;
        }

        // ====================================================================
        // 7 - GET LAST RUN RECORD
        // ====================================================================
        // Retrieve the LastRunRecord from the selected inspection tool.
        //
        // The LastRunRecord contains information from the most recent
        // inspection, including image and graphical subrecords when available.

        CogRecord lastRecord = displayTool.CreateLastRunRecord() as CogRecord;

        // Verify that the selected tool provides a valid record.

        if (lastRecord == null)
        {
            mToolBlock.Outputs["Output_String"].Value = "#Error_Control_LAST_RECORD_NULL";
            return false;
        }

        // ====================================================================
        // 8 - EXTRACT IMAGE RECORD
        // ====================================================================
        // Extract the "InputImage" subrecord from the LastRunRecord.
        //
        // This subrecord contains the image used by the inspection tool.
        // Associated graphical information may also be included.
        //
        // IMPORTANT:
        // The record key must match the selected VisionPro tool's
        // LastRunRecord structure.
        //
        // CUSTOMIZATION:
        // Customers can select a different subrecord when using
        // other VisionPro inspection tools.

        CogRecord imageRecord = null;

        try
        {
            imageRecord = lastRecord.SubRecords["InputImage"] as CogRecord;
        }
        catch (Exception)

        {
            imageRecord = null;
        }

        // Verify that the image record exists.

        if (imageRecord == null)
        {
            mToolBlock.Outputs["Output_String"].Value = "#Error_Control_INPUT_IMAGE_RECORD_NULL";
            return false;
        }

        // Verify that the record contains a valid Cognex image.

        if (!(imageRecord.Content is ICogImage))
        {
            mToolBlock.Outputs["Output_String"].Value = "#Error_Control_RECORD_WITHOUT_IMAGE";
            return false;
        }

        // ====================================================================
        // 9 - EXPORT IMAGE RECORD TO FLEXIVISION HMI
        // ====================================================================
        // Assign the selected CogRecord to Output_Image.
        //
        // Output_Image is permanently linked to the FlexiVision HMI.
        //
        // Customers can change the selected graphical record directly
        // in this script without modifying the HMI configuration.
        //
        // IMPORTANT:
        // Output_Image must be configured as a compatible CogRecord output
        // in the VisionPro ToolBlock.

        mToolBlock.Outputs["Output_Image"].Value = imageRecord;

        // --------------------------------------------------------------------
        // END OF GROUP RUN
        // --------------------------------------------------------------------
        // Returning false prevents the default automatic execution
        // of the ToolBlock tools, because this script executes them manually.

        return false;
    }

    // ========================================================================
    // MODIFY CURRENT RUN RECORD
    // ========================================================================
    // Optional method for customizing the current run record.
    // Not required because Output_Image is assigned in GroupRun().

    public override void ModifyCurrentRunRecord(ICogRecord currentRecord)
    {
    }

    // ========================================================================
    // MODIFY LAST RUN RECORD
    // ========================================================================
    // Optional method for modifying the ToolBlock LastRunRecord.
    // The record exported to the HMI is selected inside GroupRun().

    public override void ModifyLastRunRecord(ICogRecord lastRecord)
    {
    }

    // ========================================================================
    // INITIALIZE SCRIPT
    // ========================================================================
    // Called when the VisionPro advanced script is initialized.
    //
    // Stores the reference to the hosting ToolBlock, allowing
    // access to its inputs, outputs, and inspection tools.
    //
    // IMPORTANT:
    // Do not remove base.Initialize(host).

    public override void Initialize(Cognex.VisionPro.ToolGroup.CogToolGroup host)
    {
        // DO NOT REMOVE
        base.Initialize(host);

        this.mToolBlock = (CogToolBlock) host;
    }
}
```
