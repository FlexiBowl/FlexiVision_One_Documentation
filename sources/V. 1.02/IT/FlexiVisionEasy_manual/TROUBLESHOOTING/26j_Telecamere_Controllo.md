(troubleshooting_telecamere_controllo)=
# **Telecamere di Controllo**

```{important}
**Funzione Expert**

La gestione delle telecamere di controllo (**Control Camera**) è una funzione **Expert**: richiede conoscenza di Cognex VisionPro e degli script C#, ed è destinata a utenti esperti. Per informazioni sulla modalità Expert, consultare [Cosa è e Quando Serve](../EXPERT/32_Expert.md).
```

```{note}
Questa pagina riguarda il comando `start_control_` e gli script VisionPro (disponibili dalla versione software v0.24). Per la procedura completa fare riferimento a [Telecamere di Controllo](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) e a [Comando `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md).
```

## Risposte e messaggi di errore

Gli errori relativi allo script di controllo iniziano con `#Error_Control_`. Il caso `Not_Found` **non è un errore software**: significa che il locator non ha rilevato alcun oggetto. Gli errori della telecamera possono essere comunicati separatamente con il prefisso `#Error_Camera`.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Risposta
  - Significato / azione consigliata
* - `Not_Found`
  - Ispezione completata senza riconoscimenti: verificare pezzo, immagine e modello.
* - `#Error_Control_INVALID_CONTROL`
  - Il parametro non è gestito dallo script: verificare il testo dopo `start_control_`.
* - `#Error_Control_TOOL_NOT_FOUND`
  - Uno dei tool attesi non è presente o ha un nome diverso.
* - `#Error_Control_LAST_RECORD_NULL`
  - Non è disponibile il record dell'ultima esecuzione del tool.
* - `#Error_Control_INPUT_IMAGE_RECORD_NULL`
  - Il sottorecord `InputImage` non è disponibile.
* - `#Error_Control_RECORD_WITHOUT_IMAGE`
  - Il record selezionato non contiene un'immagine valida.
* - `#Error_Control_VISIONPRO_JOB`
  - L'esecuzione del task VisionPro ha generato un errore.
* - `#Error_Control_EMPTY_OUTPUT`
  - Lo script non ha restituito una stringa valida.
* - `#Error_Camera …`
  - Problema di acquisizione: controllare connessione e stato della telecamera.
```

```{note}
Lo script di esempio può restituire anche `#Error_Control_TOOL_RUN` quando i risultati di un tool non sono disponibili (ad esempio `#Error_Control_TOOL_RUN;Tool=2` se l'errore riguarda il tool 2). Se almeno un tool produce un errore di esecuzione, l'errore viene scritto all'inizio della risposta.
```

## Verifiche rapide

- Verificare che il comando abbia l'**underscore finale** (`start_control_`) e che il parametro non contenga spazi.
- Verificare che i nomi di ingresso e uscita del ToolBlock siano rimasti `Image`, `Input_Control`, `Output_String` e `Output_Image`.
- Verificare che l'uscita `Output_Image` sia configurata come `CogRecord` compatibile.
- Eseguire **Test Tool** dall'HMI anche senza robot collegato per isolare il problema dalla comunicazione TCP: in questo caso il risultato è mostrato nell'HMI ma non viene trasmesso al robot.
- Dopo ogni modifica allo script, ripetere la [prova rapida di accettazione](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md).
