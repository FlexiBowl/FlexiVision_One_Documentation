(script_visionpro)=
# **VisionPro-Skript**

```{important}
**Expert-Funktion**

Die Verwaltung der Kontrollkameras (**Control Camera**) ist eine **Expert**-Funktion: Sie erfordert Kenntnisse in Cognex VisionPro und C#-Skripten und richtet sich an erfahrene Anwender. Informationen zum Expert-Modus finden Sie unter [Worum es sich handelt und wann es benötigt wird](../EXPERT/32_Expert.md).
```

```{note}
**Voraussetzungen**

Lesen Sie vor der Änderung des Skripts [Kontrollkameras](33_Telecamere_Controllo.md) und [Befehl `start_control_`](34_Comando_start_control.md). Verfügbar ab Softwareversion v0.24.
```

Der VisionPro-**ToolBlock** der Kontrollkameras stellt ein vollständiges C#-Beispiel bereit, das auf zwei Cognex-Tools vom Typ `CogPMRedLineTool` basiert. Der vom Roboter empfangene Befehl bestimmt, welche Tools ausgeführt werden; das Skript erstellt eine Textantwort und wählt den Bilddatensatz aus, der auf der Runtime-Seite von FlexiVision angezeigt wird.

Der Kunde arbeitet **am VisionPro-ToolBlock**, ohne die Ausdrücke der HMI-Seite konfigurieren oder ändern zu müssen: Die Namen der Ein- und Ausgänge müssen die vom ToolBlock bereitgestellten bleiben.

## Datenschema

```{list-table}
:header-rows: 1
:widths: 40 60

* - Eingang / Verarbeitung
  - Ergebnis
* - **Roboter** → `start_control_<Parameter>`
  - Der auf das Präfix folgende Text wird zu `Input_Control`.
* - **Input_Control** → Tool-Auswahl
  - Führt PMRedLine 1, PMRedLine 2 oder beide aus.
* - **Results[0].GetPose()**
  - Liest X, Y und Rotation des ersten verfügbaren Ergebnisses.
* - **Output_String**
  - Gibt Koordinaten, `Not_Found` oder einen Fehler `#Error_Control_` zurück.
* - **Output_Image**
  - Gibt einen `CogRecord` zurück, der in der HMI mit den verfügbaren Grafiken angezeigt werden kann.
```

## Ein- und Ausgänge des ToolBlocks

```{list-table}
:header-rows: 1
:widths: 25 20 55

* - Name
  - Typ
  - Funktion
* - **Image**
  - `ICogImage`
  - Von der Kamera aufgenommenes Bild, mit den Vision-Tools verbunden.
* - **Input_Control**
  - `String`
  - Optionaler Textparameter, der nach `start_control_` empfangen wird.
* - **Output_String**
  - `String`
  - An FlexiVision zurückgegebener Text (zum Beispiel Koordinaten oder `Not_Found`).
* - **Output_Image**
  - `CogRecord`
  - Grafikdatensatz für die Runtime-Anzeige.
```

```{important}
Die Bezeichnungen der beiden Ausgänge müssen **`Output_String`** und **`Output_Image`** bleiben, damit die bereits eingerichteten Verknüpfungen mit der HMI erhalten bleiben. Die Struktur der HMI darf nicht geändert werden.
```

## Wie das Skript den Befehl interpretiert

Der Beispielcode prüft `Input_Control`: leerer Wert = beide PMRedLines; `"1"` = erstes Tool; `"2"` = zweites Tool. Nicht vorgesehene Werte erzeugen einen Fehler. Dieser Teil ist **anpassbar**, um benutzerdefinierte Befehle zu verarbeiten.

```csharp
string control = Convert.ToString(mToolBlock.Inputs["Input_Control"].Value).Trim();
bool run1 = control == "" || control == "1";
bool run2 = control == "" || control == "2";
```

```{list-table}
:header-rows: 1
:widths: 35 25 40

* - Roboterbefehl
  - Ausgeführte Tools
  - Text / Bild
* - `start_control_`
  - 1 und 2
  - Antworten beider Tools; Bild von Tool 1.
* - `start_control_1`
  - Nur 1
  - Antwort und Bild von Tool 1.
* - `start_control_2`
  - Nur 2
  - Antwort und Bild von Tool 2.
* - `start_control_ABC_123`
  - Im Beispiel keines
  - `Output_String` = `#Error_Control_INVALID_CONTROL`.
```

Das Beispielskript unterstützt **genau drei Auswahlmöglichkeiten**. Der Parameter ist auf Protokollebene frei, die standardmäßige C#-Logik muss jedoch erweitert werden, um benutzerdefinierte Werte wie `ABC_123` zu akzeptieren.

## Output_String: Textantwort

Für jedes ausgeführte Tool liest das Skript das erste erkannte Objekt (`Results[0]`), ermittelt daraus X und Y, rechnet die Rotation von Radiant in Grad um (`Rz = Rotation × 180 / π`) und bildet eine Zeichenfolge mit drei Dezimalstellen (Format `F3`). Als Dezimaltrennzeichen wird über `CultureInfo.InvariantCulture` immer der Punkt verwendet.

Die Funktion `GetLocatorResult()` erhält ein bereits ausgeführtes `CogPMRedLineTool` und gibt eine Zeichenfolge zurück: Ist `Results` null, meldet sie `#Error_Control_TOOL_RUN`; ist `Results.Count` null, gibt sie `Not_Found` zurück; andernfalls liest sie `Results[0].GetPose()`, wobei `TranslationX` und `TranslationY` die Koordinaten liefern.

Die Formeln und Antwortformate sind unter [Befehl `start_control_`](34_Comando_start_control.md) beschrieben.

```{note}
Die Koordinaten X und Y gehören zu dem im VisionPro-Tool konfigurierten Bezugssystem und sind nicht automatisch Millimeter. Das gezeigte Format ist ein Beispiel und kann an das vom Roboter benötigte Protokoll angepasst werden.
```

## Output_Image: Bild mit grafischen Ergebnissen

Der Ausgang `Output_Image` ist vom Typ **`CogRecord`**, keine Bilddatei, und erfordert kein Speichern auf der Festplatte. Im Beispiel ruft das Skript den `LastRunRecord` der ausgewählten PMRedLine ab, extrahiert den Unterdatensatz `InputImage` und weist ihn dem in der HMI angezeigten Grafikausgang zu.

```csharp
CogRecord lastRecord = displayTool.CreateLastRunRecord() as CogRecord;
CogRecord imageRecord = lastRecord.SubRecords["InputImage"] as CogRecord;
mToolBlock.Outputs["Output_Image"].Value = imageRecord;
```

Der Unterdatensatz muss ein gültiges Bild (`ICogImage`) enthalten; die angezeigten Grafiken hängen von den Ergebnissen und den Aufzeichnungseinstellungen des VisionPro-Tools ab und können die grafischen Überlagerungen der PMRedLine umfassen.

```{note}
**Auswahl der Anzeige**

Bei `Input_Control = "2"` wird der Datensatz von PMRedLine 2 angezeigt. Bei `"1"` oder leerem Parameter wird der von PMRedLine 1 angezeigt. Werden beide Tools ausgeführt, enthält die Textausgabe beide Ergebnisse, das Bild stammt jedoch vom **ersten Tool**. Die Grafiken der beiden Tools werden nicht automatisch kombiniert: Um Tool 2 oder einen anderen Unterdatensatz anzuzeigen, ändern Sie den Abschnitt *„6 - Select tool for image output“* des Skripts.
```

## Ausführungsablauf (GroupRun)

```{list-table}
:header-rows: 1
:widths: 35 65

* - Phase
  - Verhalten des Codes
* - **1 – Reset outputs**
  - Setzt `Output_Image` und `Output_String` vor der Prüfung zurück.
* - **2 – Read Input_Control**
  - Liest den Parameter und lässt die Werte leer, `"1"` oder `"2"` zu.
* - **3 – Get tool references**
  - Ruft `CogPMRedLineTool1` und `CogPMRedLineTool2` anhand des Namens ab.
* - **4 – Execute locators**
  - Führt über `RunTool()` nur die angeforderten Locators aus.
* - **5 – Generate Output_String**
  - Erstellt die Antwort und gibt Ausführungsfehlern Vorrang.
* - **6 – Select display tool**
  - Wählt aus, welches Tool den anzuzeigenden Grafikdatensatz liefert.
* - **7 – Get LastRunRecord**
  - Liest den Datensatz der letzten Ausführung des ausgewählten Tools.
* - **8 – Extract InputImage**
  - Extrahiert den Unterdatensatz `InputImage` und prüft, dass er `ICogImage` enthält.
* - **9 – Export Output_Image**
  - Weist den validierten `CogRecord` dem HMI-Grafikausgang zu.
```

## Das Skript anpassen

1. **Tool-Auswahl**: Ändern Sie das Lesen von `Input_Control`, um die gewünschten Tools zu starten.
2. **Formatierung der Ergebnisse**: Passen Sie `GetLocatorResult()` und die Zusammensetzung von `Output_String` an den Roboter oder die geforderte Prüfung an.
3. **Bildauswahl**: Wählen Sie, welcher `LastRunRecord` und welcher Unterdatensatz über `Output_Image` angezeigt wird.
4. **Überprüfung**: Speichern Sie das Skript und testen Sie die Befehle im Testmodus oder vom Roboter aus, und prüfen Sie dabei Text und Bild.

### Anpassbare und beizubehaltende Teile

```{list-table}
:header-rows: 1
:widths: 50 50

* - Kann angepasst werden
  - Konsistent zu halten
* - Kriterien für die Tool-Auswahl bei neuen Parametern.
  - Lesen des Eingangs `Input_Control`.
* - Vision-Tools und Namen der ausgeführten Tools.
  - Referenzen, die den tatsächlich vorhandenen Tools entsprechen.
* - Format und Inhalt von `Output_String`, Score, mehrere Objekte.
  - Präfix `#Error_Control_` für Fehler.
* - Dem `Output_Image` zugewiesener Datensatz oder Unterdatensatz.
  - `Output_Image` muss ein kompatibler `CogRecord` bleiben.
* - Kalibrierungen, Koordinaten und Maßeinheiten.
  - Prüfung des vom Roboter erwarteten Formats.
```

```{important}
Führen Sie vor dem Laden eines geänderten Skripts einen Test mit leerem Parameter, einen Test für jeden Locator und mindestens einen Fehlertest durch. Prüfen Sie in der HMI, dass `Output_String` und `Output_Image` aktualisiert werden und dass der Roboter ausschließlich das vereinbarte Format erhält.
```

## Anhang A – Vollständiges VisionPro-Skript

Nachfolgend ist das mit FlexiVision One v0.24 gelieferte Beispielskript vollständig wiedergegeben. Die Kommentare im Quelltext sind auf Englisch; die Abschnitte sind nummeriert, um Änderungen zu erleichtern. Der Code zeigt, wie die Antwortlogik definiert und das Bild mit den anzuzeigenden Grafiken ausgewählt wird.

**CogToolBlockAdvancedScript – C#-Beispiel**

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
