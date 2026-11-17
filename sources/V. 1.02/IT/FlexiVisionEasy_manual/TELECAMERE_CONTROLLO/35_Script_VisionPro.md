(script_visionpro)=
# **Script VisionPro**

```{important}
**Funzione Expert**

La gestione delle telecamere di controllo (**Control Camera**) è una funzione **Expert**: richiede conoscenza di Cognex VisionPro e degli script C#, ed è destinata a utenti esperti. Per informazioni sulla modalità Expert, consultare [Cosa è e Quando Serve](../EXPERT/32_Expert.md).
```

```{note}
**Prerequisiti**

Prima di modificare lo script, consultare [Telecamere di Controllo](33_Telecamere_Controllo.md) e [Comando `start_control_`](34_Comando_start_control.md). Disponibile dalla versione software v0.24.
```

Il **ToolBlock** VisionPro delle telecamere di controllo mette a disposizione un esempio C# completo, basato su due strumenti Cognex `CogPMRedLineTool`. Il comando ricevuto dal robot determina quali strumenti vengono eseguiti; lo script costruisce una risposta testuale e seleziona il record immagine da mostrare nella pagina Runtime di FlexiVision.

Il cliente lavora **sul ToolBlock VisionPro**, senza dover configurare o modificare le espressioni della pagina HMI: i nomi di ingresso e uscita devono restare quelli esposti dal ToolBlock.

## Schema dei dati

```{list-table}
:header-rows: 1
:widths: 40 60

* - Ingresso / elaborazione
  - Risultato
* - **Robot** → `start_control_<parametro>`
  - Il testo che segue il prefisso diventa `Input_Control`.
* - **Input_Control** → scelta dei tool
  - Esegue PMRedLine 1, PMRedLine 2 oppure entrambi.
* - **Results[0].GetPose()**
  - Legge X, Y e rotazione del primo risultato disponibile.
* - **Output_String**
  - Restituisce coordinate, `Not_Found` o un errore `#Error_Control_`.
* - **Output_Image**
  - Restituisce un `CogRecord` visualizzabile in HMI con le grafiche disponibili.
```

## Ingressi e uscite del ToolBlock

```{list-table}
:header-rows: 1
:widths: 25 20 55

* - Nome
  - Tipo
  - Funzione
* - **Image**
  - `ICogImage`
  - Immagine acquisita dalla telecamera, collegata agli strumenti di visione.
* - **Input_Control**
  - `String`
  - Parametro testuale opzionale ricevuto dopo `start_control_`.
* - **Output_String**
  - `String`
  - Testo restituito a FlexiVision (ad esempio coordinate o `Not_Found`).
* - **Output_Image**
  - `CogRecord`
  - Record grafico destinato al display Runtime.
```

```{important}
Le denominazioni delle due uscite devono rimanere **`Output_String`** e **`Output_Image`** per mantenere i collegamenti già predisposti con l'HMI. La struttura dell'HMI non deve essere modificata.
```

## Come lo script interpreta il comando

Il codice di esempio controlla `Input_Control`: valore vuoto = entrambi i PMRedLine; `"1"` = primo tool; `"2"` = secondo tool. I valori non previsti producono un errore. Questa parte è **modificabile** per gestire comandi personalizzati.

```csharp
string control = Convert.ToString(mToolBlock.Inputs["Input_Control"].Value).Trim();
bool run1 = control == "" || control == "1";
bool run2 = control == "" || control == "2";
```

```{list-table}
:header-rows: 1
:widths: 35 25 40

* - Comando robot
  - Tool eseguiti
  - Testo / immagine
* - `start_control_`
  - 1 e 2
  - Risposte di entrambi; immagine del tool 1.
* - `start_control_1`
  - Solo 1
  - Risposta e immagine del tool 1.
* - `start_control_2`
  - Solo 2
  - Risposta e immagine del tool 2.
* - `start_control_ABC_123`
  - Nessuno, nell'esempio
  - `Output_String` = `#Error_Control_INVALID_CONTROL`.
```

Lo script di esempio supporta **esattamente tre scelte**. Il parametro è libero a livello di protocollo, ma la logica C# predefinita deve essere estesa per accettare valori personalizzati come `ABC_123`.

## Output_String: risposta testuale

Per ogni tool eseguito, lo script legge il primo oggetto riconosciuto (`Results[0]`), ne ricava X e Y, converte la rotazione da radianti a gradi (`Rz = Rotation × 180 / π`) e forma una stringa con tre cifre decimali (formato `F3`). Il punto è sempre usato come separatore decimale tramite `CultureInfo.InvariantCulture`.

La funzione `GetLocatorResult()` riceve un `CogPMRedLineTool` già eseguito e restituisce una stringa: se `Results` è nullo segnala `#Error_Control_TOOL_RUN`; se `Results.Count` è zero restituisce `Not_Found`; altrimenti legge `Results[0].GetPose()`, dove `TranslationX` e `TranslationY` forniscono le coordinate.

Le formule e i formati di risposta sono descritti in [Comando `start_control_`](34_Comando_start_control.md).

```{note}
Le coordinate X e Y appartengono al sistema di riferimento configurato nello strumento VisionPro e non sono automaticamente millimetri. Il formato mostrato è un esempio e può essere adattato al protocollo richiesto dal robot.
```

## Output_Image: immagine con risultati grafici

L'uscita `Output_Image` è di tipo **`CogRecord`**, non un file immagine, e non richiede un salvataggio su disco. Nell'esempio lo script recupera il `LastRunRecord` del PMRedLine selezionato, estrae il sottorecord `InputImage` e lo assegna all'uscita grafica visualizzata in HMI.

```csharp
CogRecord lastRecord = displayTool.CreateLastRunRecord() as CogRecord;
CogRecord imageRecord = lastRecord.SubRecords["InputImage"] as CogRecord;
mToolBlock.Outputs["Output_Image"].Value = imageRecord;
```

Il sottorecord deve contenere un'immagine valida (`ICogImage`); le grafiche visualizzate dipendono dai risultati e dalle impostazioni di registrazione del tool VisionPro, e possono includere le sovrapposizioni grafiche del PMRedLine.

```{note}
**Selezione del display**

Con `Input_Control = "2"` viene mostrato il record del PMRedLine 2. Con `"1"` o parametro vuoto viene mostrato quello del PMRedLine 1. Quando entrambi i tool vengono eseguiti, l'output testuale include entrambi gli esiti, ma l'immagine proviene dal **primo tool**. Non vengono combinate automaticamente le grafiche dei due tool: per mostrare il Tool 2 o un altro sottorecord, modificare la sezione *"6 - Select tool for image output"* dello script.
```

## Sequenza di esecuzione (GroupRun)

```{list-table}
:header-rows: 1
:widths: 35 65

* - Fase
  - Comportamento del codice
* - **1 – Reset outputs**
  - Azzera `Output_Image` e `Output_String` prima dell'ispezione.
* - **2 – Read Input_Control**
  - Legge il parametro e autorizza i valori vuoto, `"1"` oppure `"2"`.
* - **3 – Get tool references**
  - Recupera `CogPMRedLineTool1` e `CogPMRedLineTool2` per nome.
* - **4 – Execute locators**
  - Esegue tramite `RunTool()` soltanto i locator richiesti.
* - **5 – Generate Output_String**
  - Compone la risposta, dando priorità agli errori di esecuzione.
* - **6 – Select display tool**
  - Sceglie quale tool fornisce il record grafico da mostrare.
* - **7 – Get LastRunRecord**
  - Legge il record dell'ultima esecuzione del tool selezionato.
* - **8 – Extract InputImage**
  - Estrae il sottorecord `InputImage` e verifica che contenga `ICogImage`.
* - **9 – Export Output_Image**
  - Assegna il `CogRecord` validato all'uscita grafica HMI.
```

## Personalizzare lo script

1. **Selezione degli strumenti**: modificare la lettura di `Input_Control` per avviare i tool desiderati.
2. **Formattazione dei risultati**: adattare `GetLocatorResult()` e la composizione di `Output_String` al robot o al controllo richiesto.
3. **Selezione dell'immagine**: scegliere quale `LastRunRecord` e quale sottorecord visualizzare tramite `Output_Image`.
4. **Verifica**: salvare lo script e provare i comandi dalla modalità di test o dal robot, controllando testo e immagine.

### Parti personalizzabili e parti da preservare

```{list-table}
:header-rows: 1
:widths: 50 50

* - È possibile personalizzare
  - Da mantenere coerente
* - Criteri di selezione dei tool per nuovi parametri.
  - Lettura dell'ingresso `Input_Control`.
* - Strumenti di visione e nomi dei tool eseguiti.
  - Riferimenti corrispondenti ai tool effettivamente presenti.
* - Formato e contenuto di `Output_String`, score, più oggetti.
  - Prefisso `#Error_Control_` per gli errori.
* - Record o sottorecord assegnato a `Output_Image`.
  - `Output_Image` deve restare un `CogRecord` compatibile.
* - Calibrazioni, coordinate e unità di misura.
  - Verifica del formato che il robot si aspetta.
```

```{important}
Prima di caricare uno script modificato, eseguire un test con parametro vuoto, un test per ciascun locator e almeno un test di errore. Controllare in HMI che `Output_String` e `Output_Image` si aggiornino e che il robot riceva soltanto il formato concordato.
```

## Appendice A – Script VisionPro completo

Di seguito è riportato integralmente lo script di esempio fornito con FlexiVision One v0.24. I commenti nel sorgente sono in inglese; le sezioni sono numerate per facilitare le modifiche. Il codice mostra come definire la logica della risposta e come selezionare l'immagine con le grafiche da visualizzare.

**CogToolBlockAdvancedScript – esempio C#**

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
