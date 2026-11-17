(telecamere_controllo)=
# **Telecamere di Controllo**

```{important}
**Funzione Expert**

La gestione delle telecamere di controllo (**Control Camera**) è una funzione **Expert**: richiede conoscenza di Cognex VisionPro e degli script C#, ed è destinata a utenti esperti. Per informazioni sulla modalità Expert, consultare [Cosa è e Quando Serve](../EXPERT/32_Expert.md).
```

```{note}
**Disponibile dalla versione software v0.24**

Le funzioni descritte in questa sezione sono state introdotte con FlexiVision One v0.24. Consultare le [Note di Rilascio – V. 0.24](../APPENDICI/V.0.24.md).
```

Oltre alla telecamera di visione utilizzata per il prelievo, FlexiVision One gestisce **3 telecamere di controllo indipendenti**, associate rispettivamente a **FLB1**, **FLB2** e **FLB3**. Le telecamere di controllo permettono di eseguire un'**ispezione visiva** su richiesta del robot, ad esempio la verifica di un pezzo prelevato, e di restituire al robot l'esito del controllo.

## A cosa serve

Il comando `start_control_` consente al robot di richiedere a FlexiVision un'ispezione con una telecamera di controllo. Il robot può aggiungere un **parametro testuale** dopo il carattere di sottolineatura (`_`): FlexiVision inoltra il parametro allo **script VisionPro**, che decide quali strumenti eseguire e quali risultati restituire.

```{important}
**Principio di funzionamento**

La configurazione HMI resta invariata: il cliente può adattare le regole di ispezione e il formato dei risultati modificando il proprio **script VisionPro**, senza intervenire sull'interfaccia di FlexiVision One.
```

## Sequenza di funzionamento

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - #
  - Attore
  - Azione
* - 1
  - **Robot**
  - Invia `start_control_` oppure `start_control_<parametro>`.
* - 2
  - **FlexiVision**
  - Acquisisce l'immagine con la telecamera di controllo associata e avvia lo script VisionPro.
* - 3
  - **VisionPro**
  - Esegue gli strumenti selezionati e prepara una risposta testuale e un record grafico.
* - 4
  - **FlexiVision**
  - Mostra immagine e stringa nell'HMI; invia la stringa al robot **solo se connesso**.
```

Per ogni controllo, FlexiVision gestisce un **Main Task** dedicato alla telecamera di controllo, con gestione degli errori, logging e invio dei risultati al robot.

## Utilizzo dalla HMI

Le pagine HMI delle telecamere di controllo sono **condivise** tra i dispositivi: dalla sezione **Control FlexiBowl®** si seleziona il dispositivo interessato.

```{list-table}
:header-rows: 1
:widths: 25 75

* - Pagina
  - Funzione
* - **Setup Camera Ctrl**
  - Configurazione della telecamera di controllo.
* - **Setup Tool Ctrl**
  - Configurazione di VisionPro: permette di intervenire sugli strumenti e sullo script VisionPro (vedi [Script VisionPro](35_Script_VisionPro.md)).
* - **View Runtime**
  - Visualizzazione di immagine e risultato del controllo.
* - **Test Tool**
  - Avvia un controllo locale, anche senza robot collegato.
```

```{note}
Con il comando **Test Tool** il controllo viene eseguito anche **senza robot connesso**: in questo caso il risultato viene mostrato nell'HMI ma **non viene trasmesso via TCP**.
```

## Prova rapida di accettazione

Dopo aver installato o modificato lo script VisionPro, eseguire le seguenti verifiche:

- ☐ Inviare `start_control_1` e verificare esito testuale e immagine del PMRedLine 1.
- ☐ Inviare `start_control_2` e verificare esito testuale e immagine del PMRedLine 2.
- ☐ Inviare `start_control_` e verificare che la stringa contenga entrambi i risultati.
- ☐ Inviare `start_control_ABC` e verificare l'errore `INVALID_CONTROL` dello script di esempio.
- ☐ Eseguire **Test Tool** con robot scollegato e verificare che HMI e VisionPro restino operativi.

## Approfondimenti

- [Comando `start_control_`](34_Comando_start_control.md): formato del comando, parametri, risposte ed esempi di scambio.
- [Script VisionPro](35_Script_VisionPro.md): interfaccia dello script, personalizzazione e codice completo di esempio.
- [Risoluzione problemi – Telecamere di Controllo](../TROUBLESHOOTING/26j_Telecamere_Controllo.md): messaggi di errore e azioni consigliate.
- [Protocollo Comunicazione Robot-Visione](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): elenco completo dei comandi robot.
