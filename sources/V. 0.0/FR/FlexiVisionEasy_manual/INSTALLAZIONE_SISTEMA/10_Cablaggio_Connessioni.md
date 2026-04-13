(cablaggio)=
# **Cablaggio e Connessioni**
immagine panoramica connessione elettriche 
tipo:  
![Pan Coll](../../../../_shared/media/images/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **Da**
  - **A**
  - **Collegamento**

* - Rete elettrica
  - FlexiBowl
  - Alimentazione 110/220 Vdc

* - Rete elettrica
  - Robot
  - Alimentazione secondo le specifiche del robot in vostro possesso

* - Rete elettrica
  - Camera
  - Alimentazione 24 Vdc

* - Rete elettrica
  - Illuminatore (luce)
  - Alimentazione 24 Vdc

* - Rete elettrica
  - Controller Tramoggia
  - Alimentazione 110/220 Vdc

* - Controller Tramoggia
  - Tramoggia
  - Alimentazione e segnale

* - Robot
  - Controller Tramoggia
  - I/O Digitali

* - VisionController
  - Camera
  - Ethernet TCP

* - VisionController
  - FlexiBowl
  - Ethernet TCP

* - VisionController
  - Robot
  - Ethernet TCP
```

## Procedura guidata di cablaggio

```{list-table} 
:header-rows: 1

* - **Step**
  - **Azione**
* - 1
  - Collegare l'alimentazione del FlexiBowl®.  
    [🔗 Fare riferimento al manuale per le specifiche di alimentazione](http://link-al-manuale.com)
* - 2
  - Collegare il [cavo di alimentazione Hirose 24V](cavo) alla Camera.
* - 3
  - Collegare il FlexiBowl® al VisionController con casvo Ethernet.
* - 4
  - Collegare la Camera al VisionController (PC) con cavo Ethernet.
* - 5
  - Collegare il Robot al VisionController con cavo Ethernet.
* - 6
  - Collegare l'aria compressa al FlexiBowl®.  
    [🔗 Fare riferimento al manuale per le specifiche pneumatiche](http://link-al-manuale.com)
* - 7
  - Se presente, collegare la tramoggia al suo controller
* - 8
  - Se presente, collegare il robot al controller della tramoggia (I/O Digitali)
* - 9 
  - Se presente, alimentare il controller della tramoggia (110/220 V in base all'opzione scelta al momento dell'acquisto della base vibrante della tramoggia)
* - 10
  - Accendere l'interruttore AC del FlexiBowl® (posizione "I"). Il led READY è **ON**.
* - 11
  - Accendere tutti gli altri dispositivi
```
(cablaggio_illuminatore)=
## Cablaggio illuminatore

![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parametro
  - Requisito / Azione
* - **Tensione**
  - 24V DC (±10%). Tensione minima di funzionamento: 20V DC sull'ingresso luce.
* - **Connettore**
  - M12 Male. 
    :::{note}
      Per connettere il toplight, è possibile acquistare anche il suo [cavo di alimentazione](cavoalimtoplight). 
    :::
* - **Pinout connettore**
  - Pin 1: +24V (marrone) — Pin 3: GND (blu) — Pin 4: STROBE PNP (nero)
* - **Modalità STROBE (PNP)**
  - Da 5V a 24V per accensione al 100%. Da 0V a 1V per spegnimento al 100%.
* - **Modalità CONTINUA**
  - Pin 1 (+24V) e Pin 3 (GND) collegati; Pin 4 (PNP) collegato a Pin 1.
* - **Caduta di tensione (cavo M12, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Schermatura**
  - Utilizzare cavi schermati per ridurre le interferenze elettromagnetiche (EMI).
```
```{warning}
**Sicurezza elettrica**

- Rispettare le tensioni di alimentazione e i morsetti di connessione indicati.
- Non modificare né smontare il prodotto.
- Non collegare o pulire l'apparecchio quando è sotto tensione.
- Non guardare direttamente la sorgente luminosa.
```



