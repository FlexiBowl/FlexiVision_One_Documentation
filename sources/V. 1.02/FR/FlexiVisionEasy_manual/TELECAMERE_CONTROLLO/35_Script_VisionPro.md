(script_visionpro)=
# **Script VisionPro**

```{important}
**Fonction Expert**

La gestion des caméras de contrôle (**Control Camera**) est une fonction **Expert** : elle requiert la connaissance de Cognex VisionPro et des scripts C#, et s'adresse aux utilisateurs expérimentés. Pour plus d'informations sur le mode Expert, consultez [Qu'est-ce que c'est et quand sert-il ?](../EXPERT/32_Expert.md).
```

```{note}
**Prérequis**

Avant de modifier le script, consultez [Caméras de contrôle](33_Telecamere_Controllo.md) et [Commande `start_control_`](34_Comando_start_control.md). Disponible à partir de la version logicielle v0.24.
```

Le **ToolBlock** VisionPro des caméras de contrôle met à disposition un exemple C# complet, basé sur deux outils Cognex `CogPMRedLineTool`. La commande reçue du robot détermine quels outils sont exécutés ; le script construit une réponse textuelle et sélectionne l'enregistrement d'image à afficher dans la page Runtime de FlexiVision.

Le client travaille **sur le ToolBlock VisionPro**, sans avoir à configurer ni à modifier les expressions de la page HMI : les noms d'entrée et de sortie doivent rester ceux exposés par le ToolBlock.

## Schéma des données

```{list-table}
:header-rows: 1
:widths: 40 60

* - Entrée / traitement
  - Résultat
* - **Robot** → `start_control_<paramètre>`
  - Le texte qui suit le préfixe devient `Input_Control`.
* - **Input_Control** → choix des outils
  - Exécute PMRedLine 1, PMRedLine 2 ou les deux.
* - **Results[0].GetPose()**
  - Lit X, Y et la rotation du premier résultat disponible.
* - **Output_String**
  - Renvoie les coordonnées, `Not_Found` ou une erreur `#Error_Control_`.
* - **Output_Image**
  - Renvoie un `CogRecord` affichable dans la HMI avec les graphiques disponibles.
```

## Entrées et sorties du ToolBlock

```{list-table}
:header-rows: 1
:widths: 25 20 55

* - Nom
  - Type
  - Fonction
* - **Image**
  - `ICogImage`
  - Image acquise par la caméra, connectée aux outils de vision.
* - **Input_Control**
  - `String`
  - Paramètre textuel facultatif reçu après `start_control_`.
* - **Output_String**
  - `String`
  - Texte renvoyé à FlexiVision (par exemple des coordonnées ou `Not_Found`).
* - **Output_Image**
  - `CogRecord`
  - Enregistrement graphique destiné à l'affichage Runtime.
```

```{important}
Les noms des deux sorties doivent rester **`Output_String`** et **`Output_Image`** afin de conserver les liaisons déjà prévues avec la HMI. La structure de la HMI ne doit pas être modifiée.
```

## Comment le script interprète la commande

Le code d'exemple contrôle `Input_Control` : valeur vide = les deux PMRedLine ; `"1"` = premier outil ; `"2"` = deuxième outil. Les valeurs non prévues produisent une erreur. Cette partie est **modifiable** pour gérer des commandes personnalisées.

```csharp
string control = Convert.ToString(mToolBlock.Inputs["Input_Control"].Value).Trim();
bool run1 = control == "" || control == "1";
bool run2 = control == "" || control == "2";
```

```{list-table}
:header-rows: 1
:widths: 35 25 40

* - Commande robot
  - Outils exécutés
  - Texte / image
* - `start_control_`
  - 1 et 2
  - Réponses des deux ; image de l'outil 1.
* - `start_control_1`
  - 1 seulement
  - Réponse et image de l'outil 1.
* - `start_control_2`
  - 2 seulement
  - Réponse et image de l'outil 2.
* - `start_control_ABC_123`
  - Aucun, dans l'exemple
  - `Output_String` = `#Error_Control_INVALID_CONTROL`.
```

Le script d'exemple prend en charge **exactement trois choix**. Le paramètre est libre au niveau du protocole, mais la logique C# par défaut doit être étendue pour accepter des valeurs personnalisées telles que `ABC_123`.

## Output_String : réponse textuelle

Pour chaque outil exécuté, le script lit le premier objet reconnu (`Results[0]`), en déduit X et Y, convertit la rotation de radians en degrés (`Rz = Rotation × 180 / π`) et forme une chaîne avec trois décimales (format `F3`). Le point est toujours utilisé comme séparateur décimal via `CultureInfo.InvariantCulture`.

La fonction `GetLocatorResult()` reçoit un `CogPMRedLineTool` déjà exécuté et renvoie une chaîne : si `Results` est nul, elle signale `#Error_Control_TOOL_RUN` ; si `Results.Count` est égal à zéro, elle renvoie `Not_Found` ; sinon elle lit `Results[0].GetPose()`, où `TranslationX` et `TranslationY` fournissent les coordonnées.

Les formules et les formats de réponse sont décrits dans [Commande `start_control_`](34_Comando_start_control.md).

```{note}
Les coordonnées X et Y appartiennent au système de référence configuré dans l'outil VisionPro et ne sont pas automatiquement des millimètres. Le format présenté est un exemple et peut être adapté au protocole requis par le robot.
```

## Output_Image : image avec résultats graphiques

La sortie `Output_Image` est de type **`CogRecord`**, et non un fichier image, et ne nécessite pas d'enregistrement sur disque. Dans l'exemple, le script récupère le `LastRunRecord` du PMRedLine sélectionné, extrait le sous-enregistrement `InputImage` et l'affecte à la sortie graphique affichée dans la HMI.

```csharp
CogRecord lastRecord = displayTool.CreateLastRunRecord() as CogRecord;
CogRecord imageRecord = lastRecord.SubRecords["InputImage"] as CogRecord;
mToolBlock.Outputs["Output_Image"].Value = imageRecord;
```

Le sous-enregistrement doit contenir une image valide (`ICogImage`) ; les graphiques affichés dépendent des résultats et des paramètres d'enregistrement de l'outil VisionPro, et peuvent inclure les superpositions graphiques du PMRedLine.

```{note}
**Sélection de l'affichage**

Avec `Input_Control = "2"`, l'enregistrement du PMRedLine 2 est affiché. Avec `"1"` ou un paramètre vide, c'est celui du PMRedLine 1 qui est affiché. Lorsque les deux outils sont exécutés, la sortie textuelle inclut les deux résultats, mais l'image provient du **premier outil**. Les graphiques des deux outils ne sont pas combinés automatiquement : pour afficher l'outil 2 ou un autre sous-enregistrement, modifiez la section *« 6 - Select tool for image output »* du script.
```

## Séquence d'exécution (GroupRun)

```{list-table}
:header-rows: 1
:widths: 35 65

* - Phase
  - Comportement du code
* - **1 – Reset outputs**
  - Réinitialise `Output_Image` et `Output_String` avant l'inspection.
* - **2 – Read Input_Control**
  - Lit le paramètre et autorise les valeurs vide, `"1"` ou `"2"`.
* - **3 – Get tool references**
  - Récupère `CogPMRedLineTool1` et `CogPMRedLineTool2` par leur nom.
* - **4 – Execute locators**
  - Exécute via `RunTool()` uniquement les locators demandés.
* - **5 – Generate Output_String**
  - Compose la réponse en donnant la priorité aux erreurs d'exécution.
* - **6 – Select display tool**
  - Choisit quel outil fournit l'enregistrement graphique à afficher.
* - **7 – Get LastRunRecord**
  - Lit l'enregistrement de la dernière exécution de l'outil sélectionné.
* - **8 – Extract InputImage**
  - Extrait le sous-enregistrement `InputImage` et vérifie qu'il contient `ICogImage`.
* - **9 – Export Output_Image**
  - Affecte le `CogRecord` validé à la sortie graphique de la HMI.
```

## Personnaliser le script

1. **Sélection des outils** : modifier la lecture de `Input_Control` pour lancer les outils souhaités.
2. **Mise en forme des résultats** : adapter `GetLocatorResult()` et la composition de `Output_String` au robot ou au contrôle requis.
3. **Sélection de l'image** : choisir quel `LastRunRecord` et quel sous-enregistrement afficher via `Output_Image`.
4. **Vérification** : enregistrer le script et essayer les commandes depuis le mode test ou depuis le robot, en contrôlant le texte et l'image.

### Parties personnalisables et parties à préserver

```{list-table}
:header-rows: 1
:widths: 50 50

* - Peut être personnalisé
  - À maintenir cohérent
* - Critères de sélection des outils pour de nouveaux paramètres.
  - Lecture de l'entrée `Input_Control`.
* - Outils de vision et noms des outils exécutés.
  - Références correspondant aux outils réellement présents.
* - Format et contenu de `Output_String`, score, objets multiples.
  - Préfixe `#Error_Control_` pour les erreurs.
* - Enregistrement ou sous-enregistrement affecté à `Output_Image`.
  - `Output_Image` doit rester un `CogRecord` compatible.
* - Calibrations, coordonnées et unités de mesure.
  - Vérification du format attendu par le robot.
```

```{important}
Avant de charger un script modifié, effectuez un test avec un paramètre vide, un test pour chaque locator et au moins un test d'erreur. Vérifiez dans la HMI que `Output_String` et `Output_Image` sont mis à jour et que le robot reçoit uniquement le format convenu.
```

## Annexe A – Script VisionPro complet

Le script d'exemple fourni avec FlexiVision One v0.24 est reproduit intégralement ci-dessous. Les commentaires du code source sont en anglais ; les sections sont numérotées pour faciliter les modifications. Le code montre comment définir la logique de la réponse et comment sélectionner l'image avec les graphiques à afficher.

**CogToolBlockAdvancedScript – exemple C#**

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
