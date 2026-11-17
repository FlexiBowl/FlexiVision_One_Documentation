(start_control)=
# **Comando `start_control_`**

```{important}
**Funzione Expert**

La gestione delle telecamere di controllo (**Control Camera**) è una funzione **Expert**: richiede conoscenza di Cognex VisionPro e degli script C#, ed è destinata a utenti esperti. Per informazioni sulla modalità Expert, consultare [Cosa è e Quando Serve](../EXPERT/32_Expert.md).
```

```{note}
**Prerequisiti**

Il comando `start_control_` richiede una telecamera di controllo configurata e uno script VisionPro caricato. Consultare [Telecamere di Controllo](33_Telecamere_Controllo.md). Disponibile dalla versione software v0.24.
```

Il comando `start_control_` consente al robot di richiedere un'ispezione visiva con una telecamera di controllo. Il robot può aggiungere un parametro testuale, che FlexiVision inoltra allo [script VisionPro](35_Script_VisionPro.md).

## Formato del comando

```
start_control_<parametro>
```

L'**underscore finale** del prefisso è **obbligatorio**. Il parametro può essere vuoto oppure contenere numeri, lettere e ulteriori underscore.

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - Comando inviato dal robot
  - Testo ricevuto da VisionPro
  - Comportamento dello script di esempio
* - `start_control_`
  - `""` (vuoto)
  - Esegue entrambi i PMRedLine
* - `start_control_1`
  - `"1"`
  - Esegue solo PMRedLine 1
* - `start_control_2`
  - `"2"`
  - Esegue solo PMRedLine 2
* - `start_control_ABC_123`
  - `"ABC_123"`
  - Parametro personalizzato: richiede logica dedicata nello script
```

```{important}
Il parametro è trattato come **testo**. FlexiVision non attribuisce alcun significato a valori come `ABC_123`: è lo script VisionPro del cliente che deve interpretarli.
```

```{note}
Anche `start_control_ 1` viene letto come parametro `"1"`: gli spazi all'inizio e alla fine vengono eliminati. Per evitare ambiguità si raccomanda di inviare `start_control_1`, senza spazi.

Il prefisso `start_control_` non viene passato allo script: arriva soltanto la parte successiva (ad esempio `"2"` per `start_control_2`).
```

Il comando può essere eseguito anche **senza robot connesso** dall'HMI tramite **Test Tool**; in tal caso il risultato è mostrato nell'HMI ma non viene trasmesso via TCP.

## Risposta al robot

La risposta è la stringa `Output_String` prodotta dallo script VisionPro. Il formato mostrato di seguito è quello dello **script di esempio** e può essere adattato al protocollo richiesto dal robot.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Situazione
  - Esempio di Output_String
* - Oggetto trovato
  - `X=125.450;Y=78.320;Rz=45.000`
* - Nessun oggetto trovato
  - `Not_Found`
* - Entrambi i tool eseguiti
  - `1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found`
* - Parametro non previsto
  - `#Error_Control_INVALID_CONTROL`
* - Errore al tool 2
  - `#Error_Control_TOOL_RUN;Tool=2`
```

Per ogni tool eseguito viene utilizzato soltanto il **primo oggetto** riconosciuto. Se sono eseguiti entrambi i tool, le risposte sono precedute dai prefissi `1:` e `2:` e separate da `|`.

```{note}
- `X` e `Y` sono espressi nel sistema di coordinate configurato nello strumento VisionPro (pixel o unità calibrate): non sono automaticamente in millimetri.
- `Rz` è espresso in gradi.
- Tre cifre decimali; il punto è sempre usato come separatore decimale, indipendentemente dalla lingua di Windows.
```

### Not_Found ed errori

`Not_Found` **non è un errore**: indica che il tool è stato eseguito ma non ha trovato alcun oggetto. Gli **errori degli script di controllo** iniziano sempre con il prefisso `#Error_Control_`; gli errori della telecamera possono essere comunicati separatamente con il prefisso `#Error_Camera`. Se almeno un tool produce un errore di esecuzione, lo script scrive l'errore all'inizio della risposta (nell'esempio ha priorità il tool 1).

L'elenco completo dei messaggi e delle azioni consigliate è disponibile in [Risoluzione problemi – Telecamere di Controllo](../TROUBLESHOOTING/26j_Telecamere_Controllo.md).

## Esempi di scambio

**Caso A – solo Locator 2**

Comando inviato dal robot: `start_control_2`. VisionPro riceve `Input_Control = "2"`, esegue `CogPMRedLineTool2`, legge X, Y e Rz del primo risultato e produce la risposta testuale. Il display mostra il record del Tool 2.

**Caso B – due Locator**

Comando inviato: `start_control_`. VisionPro riceve una stringa vuota ed esegue entrambi i tool. La risposta contiene due sezioni, una per ogni locator. Il record dell'immagine proviene dal Tool 1, salvo diversa scelta nello script.

**Caso C – parametro applicativo**

Comando inviato: `start_control_ABC_123`. Il parametro raggiunge VisionPro senza essere interpretato da FlexiVision. Lo script di esempio risponde `#Error_Control_INVALID_CONTROL`; per usarlo come comando reale occorre aggiungere la relativa logica nello script C#.

```{tip}
Per l'elenco completo dei comandi robot, consultare [Protocollo Comunicazione Robot-Visione](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```
