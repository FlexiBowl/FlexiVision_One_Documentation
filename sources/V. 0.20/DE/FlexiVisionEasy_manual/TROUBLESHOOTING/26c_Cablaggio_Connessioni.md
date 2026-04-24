# **Cablaggio e Connessioni**
(troubleshooting_alimentazione)=
## Problemi di Alimentazione FlexiBowl 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **LED READY non si accende**
  - • Alimentazione non collegata correttamente
    
    • Switch AC in posizione "O" invece di "I"
    
    • Cavo alimentazione danneggiato
    
    • Fusibili all'interno del pannello frontale bruciati 
  - • Verificare connessione alimentazione secondo manuale FlexiBowl
    
    • Portare switch in posizione "I" (ON)
    
    • Ispezionare cavo per danni e sostituire se necessario
    
    • Contattare supporto tecnico per sostituzione fusibile
* - **FlexiBowl si spegne casualmente**
  - • Connessione alimentazione allentata
    
    • Interferenze elettriche
    
  - • Serrare connessioni alimentazione
    
    • Collegare a linea dedicata con filtro EMI

```
(troubleshooting_ethernet)=
## Problemi di Connessione Ethernet 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl non comunica con VisionController**
  - • FlexiBowl non acceso (LED READY spento)  
    • Cavo Ethernet non collegato correttamente al FlexiBowl e/o al VisionController  
    • Cavo Ethernet danneggiato    
    • Indirizzo IP errato  
    • FlexiBowl e VisionController su subnet diverse  
    • Firewall blocca comunicazione  
    • Porta Ethernet VisionController guasta  
  - • Verificare LED READY acceso sul FlexiBowl  
    • Verificare connessione fisica cavo Ethernet su entrambi i lati  
    • Testare cavo con cable tester o sostituire  
    • Verificare configurazione IP in [FlexiBowl Setup](../QUICKSTART/SETUP/13a_FB_Setup.md)  
    • Configurare FlexiBowl e VisionController nella stessa rete (es: 192.168.1.x)  
    • Disabilitare temporaneamente firewall per test  
    • Provare altra porta Ethernet del VisionController  
* - **Connessione intermittente**  
  - • Cavo troppo lungo (> 100m)  
    • Connettore RJ45 danneggiato o mal crimpato  
    • Interferenze elettromagnetiche  
  - • Ridurre lunghezza cavo sotto 100m o usare switch intermedio  
    • Sostituire connettori o cavo completo  
    • Utilizzare cavo schermato (STP) lontano da fonti EMI  
```
(troubleshooting_pneumatica)=
## Problemi Pneumatici (Aria Compressa)

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Flip non funziona o impulso molto debole**
  - • Aria compressa non collegata  
    • Tubo pneumatico danneggiato o ostruito  
    • Regolatore di pressione chiuso o su minimo  
    
    • Pressione insufficiente (< 5 bar)
    
    
    
    • Perdite nel circuito pneumatico
    
    
  - • Collegare aria compressa alla connessione FlexiBowl (vedere manuale)  

    • Verificare tubo per pieghe/ostruzioni, sostituire se necessario  
    • Aprire regolatore di pressione sul pannello di controllo  
    
    • Aumentare pressione a 5-6 bar
    
    
    
    • Ispezionare raccordi con acqua saponata, serrare o sostituire
    
    
* - **Air-blow non funziona**
  - • FlexiBowl non predisposto con opzione Air-Blow  

    • Deviatori ad aria non alimentati esternamente   

    • Regolatori Flusso chiusi   

    • Pressione aria insufficiente  
  
    
    • Elettrovalvola guasta
  - • Verificare che il FlexiBowl ordinato abbia la voce Option Blow Test sia True  nel foglio produzione   

    • Verificare che alimentazione Pneumatica esterna sia presente (tubo fornito)     

    • In presenza di più deviatori ad aria, controllare che il regolatore di flusso sul lato del FlexiBowl sia impostato sopra lo zero     

    • Controllare pressione aria (5-6 bar)    

    
    • seguire [Istruzioni]()
```
(troubleshooting_connessione_camera)=
## Problemi di Connessione Camera

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Camera non rilevata dal VisionController**
  - • Cavo Ethernet camera non collegato
    
    • Camera collegata a porta non POE del VisionController
    

    
    • Indirizzo IP camera in conflitto con quelli di altri dispositivi nella stessa sottorete  
    • Porta POE VisionController guasta
  - • Verificare connessione fisica cavo camera  
    • Collegare camera SOLO a porta POE del VisionController  
    • Reimpostare IP camera o configurare IP statico univoco    
    • Provare altra porta POE del VisionController  
* - **Immagine camera nera o assente**
  - • Illuminatore spento   
    • Esposizione camera troppo bassa  
    • Lente con tappo protettivo non rimosso    
    • Lente non installata    
    • Camera non alimentata (POE non attivo)  
    
     
    • Camera guasta  
  - • Controllare che l'illuminatore sia acceso   
    • Aumentare esposizione in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
    • Rimuovere tappo protettivo lente   
    • Installare lente con focale corretta  
    • Verificare LED camera acceso (indicatore POE attivo)  
    • Sostituire camera  

* - **Camera si disconnette casualmente**
  - • Alimentazione POE insufficiente (potenza < richiesta camera)
    
    • Cavo danneggiato
    
    • Surriscaldamento camera
    
    • Porta POE danneggiata
  - • Verificare potenza POE disponibile   
    • Sostituire cavo Ethernet  
    
    • Migliorare ventilazione area camera  
    
    • Sostituire switch POE o porta VisionController  
```
(troubleshooting_connessione_toplight)=
## Problemi di Connessione Toplight 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Toplight non si accende**
  - • Alimentazione 24V DC non collegata
    
    • Cavo alimentazione danneggiato
    
    • Tensione errata (≠ 24V)
    
    • Toplight guasto
    
    • Fusibile/protezione scattata
  - • Verificare connessione alimentazione 24V DC
    
    • Ispezionare cavo, sostituire se danneggiato
    
    • Misurare tensione con multimetro, deve essere 24V DC (±10%)
    
    • Sostituire toplight
    
    • Verificare protezioni nel quadro elettrico
* - **Luminosità toplight variabile**
  - • Alimentazione instabile
    
    • Connessioni allentate
    
    • Alimentatore sottodimensionato
    
    • Toplight a fine vita
  - • Verificare stabilità tensione alimentazione
    
    • Serrare tutte le connessioni elettriche
    
    • Verificare corrente assorbita vs capacità alimentatore
    
    • Sostituire toplight
* - **Toplight si surriscalda**
  - • Ventilazione insufficiente
    
    • Corrente eccessiva
    
    • Ciclo di lavoro continuo 100%
  - • Migliorare circolazione aria attorno a toplight
    
    • Verificare corrente assorbita non superi specifiche
    
    • Implementare ciclo lavoro intermittente se possibile
```
(troubleshooting_multi)=
## Problemi Configurazioni Multi-Dispositivo
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Sistema con 2-3 FlexiBowl: solo uno comunica**
  - • FlexiBowl spenti  
    • Indirizzi IP duplicati  
    • Cavi incrociati  
  - • Controllare che il FlexiBowl sia acceso  
    • Assegnare IP univoci a ogni FlexiBowl (es: 192.168.1.10, .11, .12)  
    • Verificare corretto cablaggio stella (no daisy-chain)  
* - **Sistema con 2-3 camere: solo una acquisisce**  
  - • Alimentazione non sufficiente   
    • Indirizzi IP camere in conflitto  
  - • Controllare che l'alimentazione sia compresa fra 6 - 26 V  
    • Configurare IP statico univoco per ogni camera  
    • Abilitare tutte le camere in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
* - **Sistema con 2-3 tramogge: controllo errato**  
  - • Tramogge non abilitate individualmente in software  
    • Alimentazione errata   
    • Contatto al robot errato   
  - • Abilitare ogni tramoggia in [Hopper Setup](../QUICKSTART/SETUP/13b_Hopper_Setup.md)  
    • Controllare alimentazione  
    • Controllare contatto al robot   
```



