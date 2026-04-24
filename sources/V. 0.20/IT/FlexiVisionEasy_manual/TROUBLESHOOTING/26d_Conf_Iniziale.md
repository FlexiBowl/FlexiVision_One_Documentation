# **Setup Iniziale**
```{warning}
**Componenti non raggiungibili**

Se FlexiBowl, robot o camera non sono raggiungibili:

1. Verificare che tutti i cavi Ethernet siano collegati correttamente
2. Controllare che switch/router siano accesi
3. Verificare gli indirizzi IP di tutti i dispositivi:
   - Devono essere sulla stessa subnet (es: 192.168.1.x)
   - Non devono esserci conflitti di IP (due dispositivi con stesso IP)
4. Utilizzare il comando `ping` da terminale per testare la raggiungibilità
5. Disabilitare temporaneamente il firewall di Windows sulla porta/adattatore usato per le telecamere GigE

Per dettagli sulla configurazione di rete, vedere [Cablaggio e Connessioni](cablaggio).
```
(troubleshooting_fb_setup)=
## Troubleshooting per la sezione Passo 4: FlexiBowl Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl non risponde ai comandi software**
  - • Indirizzo IP non configurato o errato
    
    • FlexiBowl non connesso in rete
    
    • Firewall blocca comunicazione
    
    • FlexiBowl non acceso
  - • Verificare e configurare correttamente IP in FlexiBowl Setup
    
    • Testare connessione con ping da VisionController
    
    • Disabilitare firewall temporaneamente per test
    
    • Verificare LED READY acceso su FlexiBowl
* - **Impossibile salvare configurazione FlexiBowl**
  - • Disco pieno

  - • Liberare spazio su disco
 
* - **Parametri FlexiBowl non si applicano**
  - • Pulsante "Synchronize Parameters" non premuto
    
    • Connessione FlexiBowl persa
    
    • FlexiBowl in errore
  - • Cliccare sempre "Synchronize Parameters" dopo modifiche
    
    • Verificare stabilità connessione Ethernet
    
    • Riavviare FlexiBowl 
* - **Wizard FlexiBowl calcola parametri errati**
  - • Caratterizzazione componente non corretta (geometria/comportamento)
    
    • Modello FlexiBowl selezionato errato
    
    • Senso rotazione impostato male
  - • Rivedere selezione geometria (FLAT/CYLINDRICAL/COMPLEX)
    
    • Verificare taglia FlexiBowl installato vs selezionato
    
    • Verificare senso rotazione fisico e confrontare con impostazione
```

(troubleshooting_hopper_setup)=
## Troubleshooting per la sezione Passo 5: Hopper Setup 

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
## Troubleshooting per la sezione Passo 6: Robot Setup

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

(troubleshooting_cam_setup)=
## Troubleshooting per la sezione Passo 7: Camera Setup 

```{warning}
**Problemi di messa a fuoco**

Se l'immagine appare sfocata:

1. Verificare che la camera sia alla distanza di lavoro corretta ([Calcolo Distanza Ottimale](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Controllare che la lente sia avvitata completamente 
3. Verificare che non ci siano sporcizia o impronte sulla lente
4. Assicurarsi che la camera sia montata perfettamente parallela al piatto FlexiBowl

```
```{tip}
**Problemi di luminosità**

Se l'immagine acquisita è troppo scura o troppo chiara:

**Troppo scura**:
- Verificare che il backlight/toplight sia acceso (Config FlexiBowl)
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
    
    • Verificare che in Configurazione FlexiBowl sia accesa la spunta Light On
    
    • Verificare alimentazione toplight
    
    • Rimuovere tappo protettivo lente
* - **Immagine troppo chiara (sovraesposta)**
  - • Esposizione camera troppo alta
    
    • Riflessi da superficie FlexiBowl
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



