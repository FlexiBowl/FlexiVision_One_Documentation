# **Creazione Ricette e modelli** 

(troubleshooting_nuova_ricetta)=
## Troubleshooting per la sezione Creare una Nuova Ricetta 

```{warning}
**Errore durante salvataggio**

Se il salvataggio della ricetta fallisce:
- Verificare che ci sia sufficiente spazio sul disco 
- Assicurarsi che il nome non contenga caratteri non ammessi N`/ \ : * ? " < > |`)
- Verificare che non esista già una ricetta con lo stesso nome
- Verificare di avere permessi di scrittura sulla cartella del software
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Impossibile creare nuova ricetta**
  - • Disco pieno
    
    • Nome ricetta contiene caratteri non ammessi
  - • Liberare spazio su disco
    
    • Evitare caratteri speciali nel nome N/ \ : * ? " < > |)

* - **Ricetta salvata ma configurazioni perse**
  - • Salvataggio non confermato correttamente
    
    • Chiusura forzata software
    
    • Errore scrittura disco
  - • Cliccare sempre "Save Recipe" e attendere conferma
    
    • Chiudere software correttamente
    
    • Verificare log errori Windows
* - **Impossibile caricare ricetta creata**
  - • File ricetta corrotto
    
    • Percorso file cambiato
  - • Ripristinare da backup se disponibile
    
    • Verificare percorso cartella ricette in configurazione
* - **Ricetta caricata ha configurazioni errate**
  - • Ricetta sbagliata selezionata
    
    • Modifiche non salvate in precedenza
    
    • Conflitto tra ricette con nomi simili
  - • Verificare nome ricetta nella barra superiore
    
    • Ricaricare ricetta corretta dall'elenco
    
    • Utilizzare naming convention univoche
```

(troubleshooting_nuovo_modello)=
## Troubleshooting per la sezione Creare un Nuovo Modello 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni

* - **Grab Train Image acquisisce immagine nera**
  - • Camera non connessa
    
    • Toplight spento

    • Backlight spento 
    
    • Esposizione troppo bassa
    
    • Lente con tappo protettivo
  - • Verificare connessione camera in Camera Setup
    
    • Accendere toplight e verificare alimentazione

    • Controllare che light on in Configurazione FlexiBowl sia spuntato
    
    • Aumentare esposizione camera
    
    • Rimuovere tappo lente
* - **ROI non si sposta o ridimensiona**
  - • Immagine non acquisita
    
    • Software bloccato
  - • Eseguire Grab Train Image prima
    
    • Riavviare software

* - **Apply Train non genera modello**
  - • ROI troppo piccolo
    
    • Immagine senza contrasto sufficiente
  
  - • Ingrandire ROI per includere tutto il componente
    
    • Migliorare contrasto/illuminazione

* - **Modello creato include trama superficie**
  - • Feature Threshold troppo basso
    
    • Contrasto insufficiente componente-superficie
  - • Aumentare Feature Threshold Nes: da 0.3 a 0.6)
    
    • Migliorare illuminazione per aumentare contrasto
* - **Modello creato ha troppe poche linee**
  - • Feature Threshold troppo alto
    
    • Immagine sfocata

    • Immagine senza contrasto sufficiente
  - • Diminuire Feature Threshold Nes: da 0.8 a 0.5)
    
    • Verificare fuoco camera e correggere se necessario

     • Migliorare contrasto/illuminazione

* - **Modello include riflessi luce**
  - • Feature Threshold troppo basso
    
    • Illuminazione non uniforme
    
  - • Aumentare Feature Threshold
    
    • Regolare posizione/angolo toplight


* - **Impossibile nominare modello**
  - • Nome contiene caratteri non ammessi
    
    • Lunghezza nome eccessiva
  - • Usare solo lettere, numeri, underscore e trattini
    
    • Limitare nome a max 50 caratteri
```

(troubleshooting_modelli_roi)=
## Troubleshooting per la sezione Definizione ROI e Tolleranze 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni

* - **Test non rileva alcun componente**
  - • Accept Threshold troppo alto
    
    • Componenti fuori dalla Region Search
    
    • Modello non corretto
    
    • Illuminazione cambiata rispetto a training
  - • Diminuire Accept Threshold Nes: da 0.90 a 0.75)
    
    • Allargare Region Search per includere componenti
    
    • Ripetere training modello
    
    • Stabilizzare illuminazione
* - **Test rileva troppi falsi positivi**
  - • Accept Threshold troppo basso
    
    • Modello troppo semplice/generico
    
    • Sono presenti componenti molto simili ma che hanno molte differenze allo stesso tempo
  - • Aumentare Accept Threshold Nes: da 0.70 a 0.85)
    
    • Rifare modello con Feature Threshold più basso Npiù dettagliato)
    
    • Separare in modelli diversi se necessario
* - **Test rileva componenti ma con score troppo bassi**
  - • Variabilità componenti reali vs modello training
    
    • Illuminazione diversa
    
    • Componenti sporchi/danneggiati
    
    • Modello troppo dettagliato
  - • Verificare qualità componenti e pulire se necessario
    
    • Standardizzare illuminazione
    
    • Scartare componenti danneggiati
    
    • Rifare modello con Feature Threshold più alto Nmeno dettagliato)

* - **Results Panel vuoto anche con componenti visibili**
  - • Nessun componente supera Accept Threshold
    
    • Region Search non include componenti
    
    • Test non eseguito
  - • Diminuire Accept Threshold
    
    • Verificare e allargare Region Search
    
    • Cliccare pulsante Test
* - **Coordinate X,Y,Rotation non corrette**
  - • Calibrazione camera non eseguita o eseguita male 
    
    • Sistema di riferimento errato
    
    • Camera spostata dopo calibrazione
  - • Eseguire calibrazione camera completa o rivedere quella corrente 
    
    • Verificare origine sistema coordinate
    
    • Ripetere calibrazione camera
```

(troubleshooting_istogrammi)=
## Troubleshooting per la sezione Istogrammi 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Impossibile abilitare istogramma**
  - • Modello non riconosciuto
    
    • Limite massimo istogrammi raggiunto N8 per modello)
    
    • Slot già occupato
  - • Completare configurazione modello prima
    
    • Disabilitare istogrammi non utilizzati
    
    • Selezionare slot libero

* - **AUTO non calcola corretttamente**
  - • Area istogramma troppo piccola
    
    • Istogramma fuori dall'immagine
    
    • Immagine non caricata
  - • Ingrandire area istogramma
    
    • Spostare istogramma dentro area visibile
    
    • Acquisire nuova immagine
* - **Test sempre ROSSO anche con area libera**
  - • Calibrazione AUTO eseguita con area occupata
    
    • Ombra o riflesso nell'area
    
    • Bordo FlexiBowl incluso nell'area
    
    • Sporcizia sulla superficie
  - • Ripetere AUTO con area completamente libera
    
    • Escludere zone con ombre/riflessi
    
    • Ridurre area escludendo bordi
    
    • Pulire superficie FlexiBowl
* - **Test sempre VERDE anche con area occupata**
  - • Calibrazione AUTO eseguita con componenti già presenti
    
    • Soglie calcolate male
    
    • Contrasto insufficiente
  - • Ripetere AUTO assicurandosi area completamente vuota
    
    • Ripetere calibrazione con illuminazione stabile
    
    • Migliorare contrasto illuminazione
* - **Istogramma triggera casualmente**
  - • Area troppo grande include zone variabili
    
    • Illuminazione instabile
    
    • Soglia troppo stretta
  - • Ridurre area al minimo necessario
    
    • Stabilizzare illuminazione
    
    • Ripetere calibrazione AUTO
* - **Istogramma non triggera quando dovrebbe**
  - • Area troppo piccola non include ostacolo
    
    • Soglia troppo permissiva
    
  - • Ingrandire area istogramma
    
    • Ripetere calibrazione AUTO con maggior contrasto
    
* - **Impossibile creare secondo istogramma per pinza**
  -  • Slot istogramma sbagliato selezionato
  -  • Tornare all'elenco e selezionare Histogram 2
* - **Test multipli istogrammi non funziona**
  - • Non tutti gli istogrammi abilitati
    
    • Configurazione incompleta
    
    • Conflitto tra istogrammi
  - • Verificare abilitazione di tutti gli istogrammi necessari
    
    • Completare configurazione AUTO per ogni istogramma
    
    • Verificare che aree non si sovrappongano
```

(troubleshooting_robot_pick)=
## Troubleshooting per la sezione Calibrazione Robot Pick 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Coordinate robot non disponibili Nperse/dimenticate)**
  - • Non annotate durante preparazione fisica
    
    • Foglio appunti perso
    
    • Coordinate sovrascritte
  - • **OBBLIGATORIO**: Ripetere l'intera preparazione fisica dal punto 1 al punto 9 di [Creazione Modello](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md)
    
    • Salvare coordinate in file digitale oltre che su carta
    
    • Fotografare display pendant robot
* - **Find Object non rileva componente**
  - • Componente di riferimento spostato
    
    • Accept Threshold troppo alto
    
    • Componente fuori Region Search
  - • Verificare posizione componente riferimento
    
    • Abbassare temporaneamente Accept Threshold
    
    • Verificare Region Search include componente
* - **Vision Result mostra coordinate errate**
  - • Calibrazione camera non eseguita
    
    • Sistema coordinate non configurato
    
    • Camera spostata dopo calibrazione
  - • Eseguire calibrazione camera prima di Robot Pick
    
    • Verificare origine sistema riferimento
    
    • Ripetere calibrazione camera
* - **Impossibile inserire coordinate robot**
  - • Campi bloccati
    
    • Enable Robot Pick non attivato
    
    • Formato numeri errato
  - • Cliccare Enable Robot Pick prima
    
    • Attivare campi cliccandoci sopra
    
    • Usare punto come separatore decimale
* - **Gripper Offset calcola valori assurdi**
  - • Coordinate robot inserite erroneamente
    
    • X e Y scambiati
    
    • Segno +/- errato
    
    • Decimali errati o approssimati
  - • **CRITICO**: Verificare attentamente ogni coordinata
    
    • Controllare ordine X, Y, RZ
    
    • Verificare segni delle coordinate
    
    • Copiare i valori esattamente come annotati senza approssimazioni
* - **Robot preleva in posizioni sbagliate dopo calibrazione**
  - • Coordinate robot annotate erano errate
    
    • Frame/Tool robot cambiato dopo annotazione
    
    • Componente riferimento era spostato durante annotazione
    
    • Gripper Offset non salvato
  - • Ripetere preparazione fisica verificando Frame/Tool corretti
    
    • Assicurarsi stesso Frame/Tool per annotazione e prelievo
    
    • Ripetere setup con componente correttamente posizionato
    
    • Salvare ricetta dopo calcolo Gripper Offset
* - **Offset robot valido solo per componente riferimento**
  - • Distorsione ottica elevata
    
    • Calibrazione camera imprecisa
    
    • Region Search troppo grande rispetto a calibrazione
  - • Migliorare calibrazione camera
    
    • Usare lente a bassa distorsione
    
    • Ridurre Region Search se possibile
* - **Impossibile salvare Gripper Offset**
  - • Ricetta non caricata
    
    • Permessi insufficienti
    
    • Disco pieno
  - • Verificare ricetta caricata correttamente
    
    • Verificare permessi scrittura
    
    • Liberare spazio disco
* - **Rotazione RZ robot sempre errata**
  - • RZ robot non era a 0° durante setup
    
    • Ultimo asse robot non corretto
    
    • Sistema coordinate rotato
  - • Ripetere setup portando ultimo asse robot a RZ=0°
    
    • Verificare che tool selezionato sia corretto
    
    • Verificare orientamento sistema coordinate
```



