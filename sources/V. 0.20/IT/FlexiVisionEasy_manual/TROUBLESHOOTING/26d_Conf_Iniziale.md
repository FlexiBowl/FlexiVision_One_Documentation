# **Setup Iniziale**
```{warning}
**Componenti non raggiungibili**

Se FlexiBowl®, robot o camera non sono raggiungibili:

1. Verificare che tutti i cavi Ethernet siano collegati correttamente
2. Controllare che switch/router siano accesi
3. Verificare gli indirizzi IP di tutti i dispositivi:
   - Devono essere sulla stessa subnet (es: 192.168.1.x)
   - Non devono esserci conflitti di IP (due dispositivi con stesso IP)
4. Utilizzare il comando `ping` da terminale per testare la raggiungibilità
5. Disabilitare temporaneamente il firewall di Windows sulla porta/adattatore usato per le telecamere GigE

Per dettagli sulla configurazione di rete, vedere [Cablaggio e Connessioni](cablaggio).
```
(troubleshooting_cam_setup)=
## **Troubleshooting per la sezione Camera Setup**

```{warning}
**Problemi di messa a fuoco**

Se l'immagine appare sfocata:

1. Verificare che la camera sia alla distanza di lavoro corretta ([Calcolo Distanza Ottimale](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Controllare che la lente sia avvitata completamente 
3. Verificare che non ci siano sporcizia o impronte sulla lente
4. Assicurarsi che la camera sia montata perfettamente parallela alla superficie di lavoro del FlexiBowl®

```
```{tip}
**Problemi di luminosità**

Se l'immagine acquisita è troppo scura o troppo chiara:

**Troppo scura**:
- Verificare che il backlight/toplight sia acceso (Config FlexiBowl®)
- Aumentare il tempo di esposizione (parametro Cam Exposure in [Camera FLB])

**Troppo chiara (sovraesposta)**:
- Ridurre il tempo di esposizione (parametro Cam Exposure in [Camera FLB])
- Verificare che non ci sia luce ambientale eccessiva
- Regolare l'apertura del diaframma nel corpo dell'ottica della camera 
  :::{warning}
  Fare particolare attenzione nel maneggiare la camera, in quanto, se la calibrazione è già stata effettuata, anche un piccolo spostamento della camera può compromettere l'affidabilità della calibrazione 
  :::
```
```{note}
**Performance acquisizione**

Se l'acquisizione immagini è lenta:
- Verificare che il cavo Ethernet sia Gigabit (da  Cat6 in su )
- Controllare che lo switch di rete sia Gigabit Ethernet (non Fast Ethernet 100Mbps)
- Cambiare il Latency Level se non ci sono problemi di schermate blu
- Ridurre il Packet Size a 1500-2000 


Il frame rate massimo della camera è 24 fps (immagini al secondo), sufficiente per tutte le applicazioni di picking standard.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Immagine troppo scura**
  - • Esposizione camera troppo bassa
    
    • Toplight spento o guasto

    • Backlight spento o guasto

    • Toplight con potenza insufficiente
    
    • Lente con tappo protettivo
  - • Aumentare esposizione in Camera Setup
    
    • Verificare che il toplight sia acceso 
    
    • Verificare che in Configurazione FlexiBowl® sia accesa la spunta Light On
    
    • Verificare alimentazione toplight
    
    • Rimuovere tappo protettivo lente
* - **Immagine troppo chiara (sovraesposta)**
  - • Esposizione camera troppo alta
    
    • Riflessi da superficie FlexiBowl®
  - • Diminuire esposizione in Camera Setup
    
    • Sostituire superficie grip con una meno riflettente
* - **Immagine sfocata**
  - • Lente non a fuoco 
    
    • Lente non avvitata completamente
    
    • Lente sporca
    
    • Camera in movimento/vibrazioni
  - • Correggere fuoco camera
    
    • Avvitare lente fino a contatto metal-metal
    
    • Pulire lente con panno in microfibra
    
    • Fissare meglio camera e ridurre vibrazioni
* - **Immagine con artefatti o linee**
  - • Interferenze elettromagnetiche
    
    • Cavo camera danneggiato
    
    • Sensore camera danneggiato
  - • Allontanare cavo camera da fonti EMI, usare cavo schermato
    
    • Sostituire cavo Ethernet camera
    
    • Sostituire camera
* - **Camera non acquisisce durante ciclo**
  - • Trigger non configurato
    
  - • Configurare trigger acquisizione correttamente
* - **Camera non processa durante ciclo**
  - 
```
(scelta_camera)=
### Procedura di configurazione 

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
:::{video} ../../../../_shared/media/videos/Step2_calib.mp4
  :width: 100%
  :align: center
:::

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
        - Dovrebbe mostrare la vista della camera sul FlexiBowl®
        - L'immagine dovrebbe aggiornarsi ad ogni click su Run
```

(schermo_blu)=
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

#### Latency Level (Livello di Latenza)

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

#### Packet Size (Dimensione Pacchetto)

```{note}
**Regolazione packet size**

Il parametro **Packet Size** definisce la dimensione dei pacchetti dati trasmessi sulla rete Ethernet.

**Valori tipici**:
- Valore predefinito: 8164 bytes

**Come regolare**:

1. Ridurre gradualmente 08000, 7000, ecc.
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
      - La superficie del FlexiBowl® sia chiaramente visibile
      - L'illuminazione sia uniforme
    21. Se tutti i test sono positivi, la configurazione è corretta
```

(troubleshooting_calib_cam)=
## **Calibrazione Camera**

### Pattern non rilevato

```{warning}
**Errore: "Unable to detect calibration pattern"**

Causa: Il software non riesce a identificare il pattern della griglia.

**Soluzioni**:
- Aumentare il contrasto (regolare esposizione o illuminazione)
- Verificare che l'intera griglia sia visibile nell'immagine
- Migliorare la messa a fuoco
- Pulire la superficie della griglia (polvere o impronte possono interferire)
- Verificare che la griglia sia quella corretta (quadrati, non cerchi o altri pattern)
```

### Calibrazione sempre "Bad" o "Acceptable"

```{warning}
**Qualità calibrazione insufficiente**

Se nonostante le regolazioni la calibrazione rimane sotto "Excellent":

1. Verificare la distanza di lavoro camera-FlexiBowl® (deve essere quella calcolata)
2. Controllare che la camera sia parallela rispetto al piano del FlexiBowl® (deve essere perfettamente orizzontale)
3. Assicurarsi che la camera sia stabile (no vibrazioni durante acquisizione)
4. Verificare che l'obiettivo sia avvitato completamente 

Se il problema persiste, potrebbe esserci un problema meccanico nel montaggio. Consultare [Installazione Meccanica]009_Installazione_Meccanica.md) per revisione.
```

### Errori dopo cambio illuminazione

```{tip}
**Ri-calibrazione dopo cambio backlight/toplight**

Se si passa da backlight a toplight (o viceversa):

1. La calibrazione geometrica rimane valida (non serve rifarla)
2. È necessario solo regolare l'esposizione della camera per il nuovo tipo di illuminazione
3. Acquisire un'immagine di test per verificare che il pattern sia ancora ben visibile

In generale, è consigliabile decidere fin dall'inizio il tipo di illuminazione da utilizzare e mantenere quella configurazione.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Calibrazione fallisce (errore software)**
  - • Griglia di calibrazione non rilevato correttamente
    
    • Illuminazione insufficiente/eccessiva
    
    • Griglia calibrazione danneggiato o sporco
    
  - • Posizionare target piano e ben visibile
    
    • Regolare esposizione camera per visualizzare bene il target
    
    • Utilizzare Griglia calibrazione pulito e integro
    
* - **Errore di calibrazione troppo elevato**
  - • Camera non perfettamente ortogonale alla superficie
    
    • Griglia calibrazione non piano
    
    • Distorsione ottica eccessiva
    
  - • Verificare ortogonalità camera con livella (tolleranza ±1°)
    
    • Posizionare target su superficie rigida e piana
    
    • Verificare qualità ottica lente, pulire o sostituire
    
* - **Coordinate reali non corrispondono a quelle misurate**
  - • Fattore di scala errato (Tile Size errato)
    
    • Camera spostata dopo calibrazione
    
  - • Ripetere calibrazione completa
    
    • Fissare saldamente camera per evitare spostamenti
    
    • Verificare dimensioni target calibrazione secondo documentazione
* - **Calibrazione valida solo al centro immagine**
  - • Distorsione ottica periferica
    
    • Calibrazione con troppo pochi punti
  - • Utilizzare lente di qualità superiore a bassa distorsione
    
    • Verificare che la distanza di lavoro sia corretta
```



(troubleshooting_fb_setup)=
## **Troubleshooting per la sezione FlexiBowl® Setup**

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl® non risponde ai comandi software**
  - • Indirizzo IP non configurato o errato
    
    • FlexiBowl® non connesso in rete
    
    • Firewall blocca comunicazione
    
    • FlexiBowl® non acceso
  - • Verificare e configurare correttamente IP in FlexiBowl® Setup
    
    • Testare connessione con ping da VisionController
    
    • Disabilitare firewall temporaneamente per test
    
    • Verificare LED READY acceso su FlexiBowl®
* - **Impossibile salvare configurazione FlexiBowl®**
  - • Disco pieno

  - • Liberare spazio su disco
 
* - **Parametri FlexiBowl® non si applicano**
  - • Pulsante "Synchronize Parameters" non premuto
    
    • Connessione FlexiBowl® persa
    
    • FlexiBowl® in errore
  - • Cliccare sempre "Synchronize Parameters" dopo modifiche
    
    • Verificare stabilità connessione Ethernet
    
    • Riavviare FlexiBowl® 
* - **Wizard FlexiBowl® calcola parametri errati**
  - • Caratterizzazione componente non corretta (geometria/comportamento)
    
    • Modello FlexiBowl® selezionato errato
    
    • Senso rotazione impostato male
  - • Rivedere selezione geometria (FLAT/CYLINDRICAL/COMPLEX)
    
    • Verificare taglia FlexiBowl® installato vs selezionato
    
    • Verificare senso rotazione fisico e confrontare con impostazione
```

(troubleshooting_hopper_setup)=
## **Troubleshooting per la sezione Hopper Setup** 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Tramoggia non si attiva mai automaticamente**
  - • Hopper non abilitato in software  
    • Campo Signal errato
    • Area di controllo non definita
    
    • Soglie non calibrate
    
    • Tramoggia non collegata elettricamente
  - • Abilitare checkbox "Enable Hopper X"  
    • Verificare che il numero **Signal** corrisponda al DO fisicamente connesso
    • Definire area di controllo in "Define Area Check"
    
    • Eseguire calibrazione soglie con CAPTURE vuoto/pieno
    
    • Verificare collegamenti elettrici 
* - **Tramoggia si attiva continuamente**
  - • Soglie calibrate in modo errato
    
    • Tempo vibrazione insufficiente (scarica troppo pochi pezzi)
    
    • Parameter "Steps" errato
  - • Ripetere calibrazione rimuovendo TUTTI i pezzi per CAPTURE vuoto
    
    • Aumentare parametro "Time" (es: da 500ms a 700ms)
    
    • Ricalcolare "Steps" contando cicli effettivi
* - **Test hopper sempre rosso (non si attiva)**
  - • Troppi componenti nell'area durante calibrazione
    
    • Illuminazione cambiata tra calibrazione e test
    
    • Riflessi/ombre nell'area di controllo
  - • Ripetere calibrazione con numero minimo corretto di pezzi
    
    • Eseguire calibrazione e test con illuminazione stabile
    
    • Riposizionare area escludendo zone con riflessi
* - **Test hopper sempre verde (si attiva sempre)**
  - • Area di controllo include zone non pertinenti
    
    • Calibrazione vuoto eseguita con pezzi presenti
    
    • Expression Builder non calcolato correttamente
  - • Ridefinire area di controllo più stretta
    
    • Ripetere CAPTURE vuoto assicurandosi area completamente pulita
    
    • Cliccare nuovamente su AUTO per ricalcolare Mean e Std Dev
* - **Flusso componenti non uniforme**
  - • Calcolo del tempo di vibrazione errato  
    
    • Carico iniziale troppo elevato che supera il payload
  - • Rivedere il calcolo della vibrazione sulla base del riempimento iniziale 
    
    • Controllare che il carico non superi il payload della tramoggia 
```

(troubleshooting_robot_setup)=
## **Troubleshooting per la sezione Robot Setup**

```{warning}
**Diagnosi connessione fallita**

Se il robot non riesce a stabilire la connessione:

**Verifiche base**:
1. Server FlexiVision One online (indicatore verde)
2. Indirizzo IP corretto nel programma robot
3. Porta corretta nel programma robot (uguale a FlexiVision One)
4. Cavo Ethernet collegato correttamente

**Verifiche rete**:
1. Ping dal VisionController al robot:
   - Aprire Prompt comandi su VisionController
   - `ping <IP_ROBOT>` (es: `ping 192.168.1.10`)
   - Se fallisce: problema di rete fisica/configurazione IP

2. Ping dal robot al VisionController (se disponibile funzione ping sul robot)

3. Verificare che robot e VisionController siano sulla stessa subnet

**Verifiche firewall**:
1. Disabilitare temporaneamente firewall Windows per test
2. Se funziona, problema firewall → configurare eccezione

**Verifiche robot**:
1. Verificare sintassi corretta comando connessione TCP/IP (consultare manuale robot)
2. Controllare timeout connessione (aumentare se necessario)
3. Verificare permessi di rete sul controller robot
```

```{note}
**Stabilizzazione connessione**

Se la connessione si interrompe frequentemente:

1. Verificare qualità cavo Ethernet (utilizzare da Cat6 in su)
2. Evitare cavi troppo lunghi 
3. Verificare che non ci sia traffico di rete eccessivo sulla stessa subnet, si possono utilizzare programmi come Wireshark o TCP dump 
4. Verificare alimentazione stabile del VisionController
5. Controllare log di Windows per errori di rete

Se il problema persiste, contattare supporto tecnico per analisi approfondita.
```
```{warning}
**Sintassi comandi errata**

Se FlexiVision One risponde con "Invalid command":

1. Verificare la sintassi esatta del comando (case-sensitive, underscore, ecc.)
2. Assicurarsi di inviare il carattere terminatore CHR(13) dopo ogni comando
3. Non aggiungere spazi extra all'inizio o alla fine del comando
4. Verificare, nel log messaggi della sezione Robot Setup, il comando che FlexiVision One ha ricevuto 

Esempi corretti vs errati:
- ✅ `start_Locator` (con underscore, minuscolo)
- ❌ `Start_Locator` (maiuscola errata)
- ❌ `start Locator` (spazio invece di underscore)
- ❌ `startLocator` (manca underscore)

Consultare [Protocollo TCP/IP](protocollo) per l'elenco completo e corretto dei comandi.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Robot non si collega a FlexiVision One**
  - • Indirizzo IP robot non sulla stessa sottorete del VisionController
    
    • Porta TCP/IP non configurata
    
    • Firewall VisionController blocca comunicazione
    
  - • Verificare e configurare sottorete corretta in Robot Setup
    
    • Configurare porta TCP/IP (tipicamente 5000 o secondo robot)
    
    • Disabilitare firewall per test
    
    • Selezionare protocollo compatibile con robot in [Protocol Setup](../QUICKSTART/SETUP/15_Protocol_Setup.md)
* - **Robot va in posizioni sbagliate**
  - • Calibrazione robot non eseguita o non eseguita correttamente
    
    • Frame/Tool robot non corretto
    
    • Offset gripper errato
    
    • Coordinate salvate sbagliate durante setup modello
  - • Eseguire calibrazione robot completa
    
    • Verificare Frame e Tool selezionati sul robot
    
    • Ripetere calibrazione Robot Pick con coordinate corrette
    
    • Rifare training modello salvando coordinate precise
* - **Impossibile connettersi al robot**
  - • Robot spento 
    
    • Cavo Ethernet non collegato
    
    • Robot e VisionController su subnet diverse

  - • Accendere robot e portare in automatico
    
    • Verificare connessione fisica Ethernet robot-VisionController
    
    • Configurare robot e VisionController stessa rete
```

