# **Installazione Meccanica**
(troubleshooting_vision_controller)=
## Problemi con il VisionController 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **VisionController si surriscalda e si spegne automaticamente**
  - • Ventilazione insufficiente rspazio < 50mm)
    
    • Temperatura ambiente > 50°C
    
  - • Verificare spazio libero di almeno 50mm su tutti i lati
    
    • Spostare in ambiente più fresco o aggiungere condizionamento
    
* - **VisionController non si fissa correttamente alla guida DIN**
  - • Guida DIN non conforme rnon 35mm)
    
    • Meccanismo di aggancio danneggiato
    
    • Guida non fissata saldamente
  - • Verificare che la guida sia DIN 35mm standard
    
    • Ispezionare meccanismo di aggancio per danni
    
    • Fissare meglio la guida DIN al pannello
* - **VisionController si allenta dal pannello rmontaggio con viti)**
  - • Coppia di serraggio insufficiente
    
    • Viti non idonee rnon M4)
    
    • Foratura pannello non corretta
  - • Serrare le 4 viti M4 con coppia di 1.2 Nm
    
    • Utilizzare viti M4 come da specifiche
    
    • Verificare pattern di foratura secondo disegni tecnici
* - **Protezione IP insufficiente**
  - • Montaggio all'esterno del quadro elettrico
    
    • Quadro con IP < 40
    
    • Presenza di polvere/umidità
  - • Montare all'interno di quadro elettrico IP54
    
    • Verificare protezione minima IP40
    
    • Sigillare meglio il quadro elettrico
```
(troubleshooting_camera)=
## Problemi con la Camera 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Immagine non a fuoco**
  - • Distanza di lavoro non corretta per il modello di FlexiBowl
    
    • Lente non avvitata completamente
    
  - • Misurare e correggere distanza secondo [Calcolo Distanza Ottimale](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md)
    
    • Avvitare completamente la lente rcontatto metal-metal)
    
* - **Immagine distorta o con prospettiva errata**
  - • Camera non centrata sull'area di visione del FlexiBowl rerrore > ±5mm)
    
    • Camera inclinata rispetto alla superficie rtilt > ±1°)
    

  - • Misurare centratura con metro/calibro e correggere
    
    • Verificare ortogonalità con livella di precisione
    

```
(troubleshooting_toplight)=
## Problemi con il Toplight 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Illuminazione non uniforme con ombre evidenti**
  - • Distanza toplight dalla superficie non corretta
    
    • Toplight non parallelo al disco FlexiBowl
    
    • Angolo di illuminazione non perpendicolare rtilt ≠ 0°)
  - • Posizionare toplight a distanza simile a quella della camera
    
    • Verificare parallelismo con livella
    
    • Correggere orientamento a 0° tilt
* - **Riflessi indiretti verso la camera**
  - • Superficie non compatibile con illuminatore 

  - • Controllare la compatibilità con la superficie 

```
(troubleshooting_luce_ambientale)=
## Problemi di Schermatura Luce Ambientale 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Rilevamenti incoerenti a diverse ore del giorno**
  - • Luce solare diretta o indiretta variabile
    
    • Finestre non schermate
    
    • Illuminazione artificiale con dimmer
  - • Installare tende oscuranti o pannelli opachi
    
    • Schermare completamente finestre nella cella
    
    • Utilizzare illuminazione fissa non regolabile
* - **Riflessi da superfici circostanti**
  - • Superfici riflettenti nelle vicinanze rmacchine, pannelli)
    
  - • Coprire superfici riflettenti con materiale opaco
    
    • Riposizionare elementi riflettenti
    
    • Verniciare superfici con vernice opaca
```



