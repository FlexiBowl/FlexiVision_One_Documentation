(script_visionpro)=
# **Script de VisionPro**

```{important}
**Función Expert**

La gestión de las cámaras de control (**Control Camera**) es una función **Expert**: requiere conocimientos de Cognex VisionPro y de scripts en C#, y está destinada a usuarios expertos. Para obtener información sobre el modo Expert, consulte [Qué es y cuándo se necesita](../EXPERT/32_Expert.md).
```

```{note}
**Requisitos previos**

Antes de modificar el script, consulte [Cámaras de control](33_Telecamere_Controllo.md) y [Comando `start_control_`](34_Comando_start_control.md). Disponible a partir de la versión de software v0.24.
```

El **ToolBlock** de VisionPro de las cámaras de control ofrece un ejemplo completo en C#, basado en dos herramientas Cognex `CogPMRedLineTool`. El comando recibido del robot determina qué herramientas se ejecutan; el script construye una respuesta de texto y selecciona el registro de imagen que se mostrará en la página Runtime de FlexiVision.

El cliente trabaja **en el ToolBlock de VisionPro**, sin tener que configurar ni modificar las expresiones de la página HMI: los nombres de entrada y salida deben seguir siendo los que expone el ToolBlock.

## Esquema de datos

```{list-table}
:header-rows: 1
:widths: 40 60

* - Entrada / procesamiento
  - Resultado
* - **Robot** → `start_control_<parámetro>`
  - El texto que sigue al prefijo se convierte en `Input_Control`.
* - **Input_Control** → selección de herramientas
  - Ejecuta PMRedLine 1, PMRedLine 2 o ambas.
* - **Results[0].GetPose()**
  - Lee X, Y y la rotación del primer resultado disponible.
* - **Output_String**
  - Devuelve coordenadas, `Not_Found` o un error `#Error_Control_`.
* - **Output_Image**
  - Devuelve un `CogRecord` que se puede visualizar en la HMI con los gráficos disponibles.
```

## Entradas y salidas del ToolBlock

```{list-table}
:header-rows: 1
:widths: 25 20 55

* - Nombre
  - Tipo
  - Función
* - **Image**
  - `ICogImage`
  - Imagen adquirida por la cámara, conectada a las herramientas de visión.
* - **Input_Control**
  - `String`
  - Parámetro de texto opcional recibido tras `start_control_`.
* - **Output_String**
  - `String`
  - Texto devuelto a FlexiVision (por ejemplo, coordenadas o `Not_Found`).
* - **Output_Image**
  - `CogRecord`
  - Registro gráfico destinado a la visualización Runtime.
```

```{important}
Los nombres de las dos salidas deben seguir siendo **`Output_String`** y **`Output_Image`** para mantener los enlaces ya preparados con la HMI. La estructura de la HMI no debe modificarse.
```

## Cómo interpreta el script el comando

El código de ejemplo comprueba `Input_Control`: valor vacío = ambas PMRedLine; `"1"` = primera herramienta; `"2"` = segunda herramienta. Los valores no previstos producen un error. Esta parte es **modificable** para gestionar comandos personalizados.

```csharp
string control = Convert.ToString(mToolBlock.Inputs["Input_Control"].Value).Trim();
bool run1 = control == "" || control == "1";
bool run2 = control == "" || control == "2";
```

```{list-table}
:header-rows: 1
:widths: 35 25 40

* - Comando del robot
  - Herramientas ejecutadas
  - Texto / imagen
* - `start_control_`
  - 1 y 2
  - Respuestas de ambas; imagen de la herramienta 1.
* - `start_control_1`
  - Solo 1
  - Respuesta e imagen de la herramienta 1.
* - `start_control_2`
  - Solo 2
  - Respuesta e imagen de la herramienta 2.
* - `start_control_ABC_123`
  - Ninguna, en el ejemplo
  - `Output_String` = `#Error_Control_INVALID_CONTROL`.
```

El script de ejemplo admite **exactamente tres opciones**. El parámetro es libre a nivel de protocolo, pero la lógica C# predeterminada debe ampliarse para aceptar valores personalizados como `ABC_123`.

## Output_String: respuesta de texto

Para cada herramienta ejecutada, el script lee el primer objeto reconocido (`Results[0]`), obtiene X e Y, convierte la rotación de radianes a grados (`Rz = Rotation × 180 / π`) y forma una cadena con tres decimales (formato `F3`). El punto se usa siempre como separador decimal mediante `CultureInfo.InvariantCulture`.

La función `GetLocatorResult()` recibe un `CogPMRedLineTool` ya ejecutado y devuelve una cadena: si `Results` es nulo, señala `#Error_Control_TOOL_RUN`; si `Results.Count` es cero, devuelve `Not_Found`; en caso contrario lee `Results[0].GetPose()`, donde `TranslationX` y `TranslationY` proporcionan las coordenadas.

Las fórmulas y los formatos de respuesta se describen en [Comando `start_control_`](34_Comando_start_control.md).

```{note}
Las coordenadas X e Y pertenecen al sistema de referencia configurado en la herramienta de VisionPro y no son automáticamente milímetros. El formato mostrado es un ejemplo y puede adaptarse al protocolo requerido por el robot.
```

## Output_Image: imagen con resultados gráficos

La salida `Output_Image` es de tipo **`CogRecord`**, no un archivo de imagen, y no requiere guardarse en disco. En el ejemplo, el script obtiene el `LastRunRecord` de la PMRedLine seleccionada, extrae el subregistro `InputImage` y lo asigna a la salida gráfica que se muestra en la HMI.

```csharp
CogRecord lastRecord = displayTool.CreateLastRunRecord() as CogRecord;
CogRecord imageRecord = lastRecord.SubRecords["InputImage"] as CogRecord;
mToolBlock.Outputs["Output_Image"].Value = imageRecord;
```

El subregistro debe contener una imagen válida (`ICogImage`); los gráficos mostrados dependen de los resultados y de los ajustes de registro de la herramienta de VisionPro, y pueden incluir las superposiciones gráficas de la PMRedLine.

```{note}
**Selección de la visualización**

Con `Input_Control = "2"` se muestra el registro de la PMRedLine 2. Con `"1"` o con el parámetro vacío se muestra el de la PMRedLine 1. Cuando se ejecutan ambas herramientas, la salida de texto incluye los dos resultados, pero la imagen procede de la **primera herramienta**. Los gráficos de las dos herramientas no se combinan automáticamente: para mostrar la herramienta 2 u otro subregistro, modifique la sección *"6 - Select tool for image output"* del script.
```

## Secuencia de ejecución (GroupRun)

```{list-table}
:header-rows: 1
:widths: 35 65

* - Fase
  - Comportamiento del código
* - **1 – Reset outputs**
  - Pone a cero `Output_Image` y `Output_String` antes de la inspección.
* - **2 – Read Input_Control**
  - Lee el parámetro y autoriza los valores vacío, `"1"` o `"2"`.
* - **3 – Get tool references**
  - Obtiene `CogPMRedLineTool1` y `CogPMRedLineTool2` por nombre.
* - **4 – Execute locators**
  - Ejecuta mediante `RunTool()` solo los locators solicitados.
* - **5 – Generate Output_String**
  - Compone la respuesta, dando prioridad a los errores de ejecución.
* - **6 – Select display tool**
  - Elige qué herramienta proporciona el registro gráfico que se mostrará.
* - **7 – Get LastRunRecord**
  - Lee el registro de la última ejecución de la herramienta seleccionada.
* - **8 – Extract InputImage**
  - Extrae el subregistro `InputImage` y comprueba que contenga `ICogImage`.
* - **9 – Export Output_Image**
  - Asigna el `CogRecord` validado a la salida gráfica de la HMI.
```

## Personalizar el script

1. **Selección de herramientas**: modificar la lectura de `Input_Control` para iniciar las herramientas deseadas.
2. **Formato de los resultados**: adaptar `GetLocatorResult()` y la composición de `Output_String` al robot o al control requerido.
3. **Selección de la imagen**: elegir qué `LastRunRecord` y qué subregistro mostrar mediante `Output_Image`.
4. **Verificación**: guardar el script y probar los comandos desde el modo de prueba o desde el robot, comprobando texto e imagen.

### Partes personalizables y partes que se deben conservar

```{list-table}
:header-rows: 1
:widths: 50 50

* - Se puede personalizar
  - Se debe mantener coherente
* - Criterios de selección de herramientas para nuevos parámetros.
  - Lectura de la entrada `Input_Control`.
* - Herramientas de visión y nombres de las herramientas ejecutadas.
  - Referencias que correspondan a las herramientas realmente presentes.
* - Formato y contenido de `Output_String`, puntuación, varios objetos.
  - Prefijo `#Error_Control_` para los errores.
* - Registro o subregistro asignado a `Output_Image`.
  - `Output_Image` debe seguir siendo un `CogRecord` compatible.
* - Calibraciones, coordenadas y unidades de medida.
  - Comprobación del formato que espera el robot.
```

```{important}
Antes de cargar un script modificado, realice una prueba con parámetro vacío, una prueba para cada locator y al menos una prueba de error. Compruebe en la HMI que `Output_String` y `Output_Image` se actualizan y que el robot recibe únicamente el formato acordado.
```

## Apéndice A – Script de VisionPro completo

A continuación se reproduce íntegramente el script de ejemplo suministrado con FlexiVision One v0.24. Los comentarios del código fuente están en inglés; las secciones están numeradas para facilitar las modificaciones. El código muestra cómo definir la lógica de la respuesta y cómo seleccionar la imagen con los gráficos que se van a mostrar.

**CogToolBlockAdvancedScript – ejemplo en C#**

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
