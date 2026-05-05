(camerasetup)=
# **Passo 3: Camera Setup**

Questa sezione descrive la procedura per configurare e testare la telecamera industriale del sistema FlexiVision One. La corretta configurazione della camera è fondamentale per garantire l'acquisizione di immagini di qualità.

```{note}
**Prerequisiti**

Prima di procedere, assicurarsi che:
- La camera sia stata installata meccanicamente alla distanza corretta
- Il cavo Ethernet della camera sia connesso al VisionController
- La camera sia alimentata (tramite PoE o alimentazione esterna)
- FlexiBowl sia configurato e il backlight funzionante (per test acquisizione)
```

---

## Accesso alla configurazione Camera

```{list-table}

* - **1** 
  - Dalla pagina principale del software, cliccare su <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Nella pagina SETUP, identificare e cliccare sull'icona **Camera Setup**
    ```{dropdown} Pagina Setup 
       ![Pagina Setup](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - Si apre la pagina di configurazione delle camere
```

---

## Panoramica interfaccia Camera Setup

La pagina Camera Setup presenta tre riquadri informativi principali e un'area di configurazione:
![Paagina Camera Setup](../../../../../_shared/media/images/pagina_camsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sezione
  - Descrizione
* - **Selected Camera**
  - Mostra l'identificazione della camera attualmente selezionata
* - **Camera Serial Number**
  - Visualizza il numero seriale univoco della camera connessa
* - **Status**
  - Indica lo stato della connessione
* - **Calibration Result**
  - Mostra il risultato della calibrazione della camera
* - **Config Camera**
  - Pulsante per aprire la pagina di configurazione dettagliata
```

---

## Procedura di configurazione

inserire immagini delle schermate per ogni passaggio per renderli più chiari e visibili 

:::{note}
Per comodità e coerenza, si consiglia di far coincidere il numero della camera con il corrispondente FlexiBowl: 
 - ✅ Camera installata sopra FlexiBowl 1: CAM-CIC-5000-20G-12345 > Seleziono Camera 1 FlexiBowl 1 e in "Image Acquisition Device" seleziono CAM-CIC-5000-20G-12345
:::

```{list-table}
* - **Accesso configurazione**
  - 1. Cliccare sul pulsante **Config Camera X** (dove X è il numero della camera)
    2. Si apre la prima pagina della procedura guidata per la calibrazione, in cui è possibile modificare il parametro **Cam Exposure**

* - **Attivazione modalità avanzata**
  - 3. Cliccare sul pulsante **Expert** (in basso a destra)
    4. Questa modalità fornisce accesso a tutte le impostazioni avanzate della camera necessarie per la configurazione iniziale
* - **Configurazione image acquisition device**
  - 5. Nel pannello **Expert**, cliccare sulla sezione **Image Acquisition** da **Settings**
    6. Cliccare su **Image Acquisition Device**
    7. Si apre un menu di selezione dei dispositivi di acquisizione disponibili
* -  **Identificazione camera specifica**
  - 8. Dal menu dei dispositivi, selezionare la camera desiderata
        - Cercare nell'elenco il numero seriale o il modello della camera
        - Esempio: "CAM-CIC-5000-20G-XXXXX" (dove XXXXX è il seriale)
    9. Cliccare sulla camera per selezionarla 
```

```{tip}
**Identificazione del seriale corretto**

Se sono elencate multiple camere o dispositivi:
- Il numero seriale è riportato su un'etichetta sulla camera fisica
- Confrontare l'ultimo gruppo di caratteri del seriale per identificare la camera corretta
- In caso di dubbio, disconnettere fisicamente altre camere per identificare quella in uso
```


```{list-table} 
* - **Selezione video format**
  - 11. Cliccare su **Video Formats** 
    12. Dalla lista dei formati disponibili, selezionare **Generic GigEVision**
    13. Selezionare **Mono** (monocromatico) come tipo di sensore
```


```{warning}
**Formato corretto obbligatorio**

È fondamentale selezionare **Generic GigEVision Mono**:
- Altri formati potrebbero non funzionare o causare errori
- Formati a colori non sono compatibili con questa camera
- Se il formato non è disponibile, potrebbero mancare driver o configurazioni di sistema
```

```{list-table}
* - **Attivazione sistema di acquisizione**
  - 14. Dopo aver selezionato il formato corretto, cliccare su **Initialize Acquisition**  
    15.Attendere il completamento dell'inizializzazione (pochi secondi)
* - **Verifica funzionamento acquisizione**
  - 16. Localizzare il pulsante **Run** in alto a sinistra dell'interfaccia (icona "play")
    17. Cliccare su **Run** ripetutamente 05-10 volte) per acquisire immagini di test
    18. Osservare l'area di visualizzazione immagine:
        - Dovrebbe mostrare la vista della camera sul FlexiBowl
        - L'immagine dovrebbe aggiornarsi ad ogni click su Run
```

```{warning}
**Diagnosi schermo completamente blu**

Se durante i test l'immagine acquisita appare **completamente blu**  almeno una volta:

**Causa**: Problema di comunicazione GigE (latenza di rete o dimensione pacchetti non ottimale)

**Soluzione**:

1. Dal menu in alto, selezionare **GigE** (o **GigE Vision Settings**)

2. Modificare i seguenti parametri:
   - **Latency Level** (Livello di Latenza)
   - **Packet Size** (Dimensione Pacchetto)

Procedere con gli step successivi per la configurazione ottimale di questi parametri.
```

---

### Latency Level (Livello di Latenza)

```{note}
**Regolazione latency**

Il parametro **Latency Level** controlla il buffer di comunicazione tra camera e VisionController.

**Valori tipici**:
- Valore predefinito: 0
- Range disponibile: 0-3

**Come regolare**:

1. Aumentare gradualmente il valore 
2. Dopo ogni modifica, testare l'acquisizione (pulsante Run) 5-10 volte
3. Se non si verificano più schermate blu, il valore è corretto
4. Se le schermate blu persistono, aumentare ulteriormente o provare con modifiche al parametro Packet Size
```

### Packet Size (Dimensione Pacchetto)

```{note}
**Regolazione packet size**

Il parametro **Packet Size** definisce la dimensione dei pacchetti dati trasmessi sulla rete Ethernet.

**Valori tipici**:
- Valore predefinito: 8164 bytes

**Come regolare**:

1. Ridurre gradualmente 08000, 7000, ecc.)
2. Dopo ogni modifica, testare l'acquisizione (pulsante Run) 5-10 volte
3. Se non si verificano più schermate blu, il valore è corretto
4. Se le schermate blu persistono, diminuire ulteriormente o provare con modifiche al parametro Latency Level
```


---

```{list-table}
* - **Verifica finale e salvataggio**
  - 19. Cliccare su **Run** almeno 2-3 volte consecutivamente  
    20. Verificare che:  
      - Nessuna immagine appaia completamente blu o nera
      - Le immagini si aggiornino regolarmente
      - La superficie del FlexiBowl sia chiaramente visibile
      - L'illuminazione sia uniforme
    21. Se tutti i test sono positivi, la configurazione è corretta
```
---
