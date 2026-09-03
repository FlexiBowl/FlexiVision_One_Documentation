(camerasetup)=
# **Camera Setup**

Questa sezione descrive la procedura per configurare e testare la telecamera industriale del sistema FlexiVision One. La corretta configurazione della camera è fondamentale per garantire l'acquisizione di immagini di qualità.

```{note}
**Prerequisiti**

Prima di procedere, assicurarsi che:
- La camera sia stata installata meccanicamente alla distanza corretta
- Il cavo Ethernet della camera sia connesso al VisionController
- La camera sia alimentata (tramite PoE o alimentazione esterna)
- FlexiBowl® sia configurato e il backlight funzionante (per test acquisizione)
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
  - Mostra l'identificazione della camera attualmente selezionata. Viene mostrata automaticamente all'avvio di FlexiVision One. 
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


:::{note}
Per comodità e coerenza, si consiglia di far coincidere il numero della camera con il corrispondente FlexiBowl®: 
 - ✅ Camera installata sopra FlexiBowl® 1: CAM-CIC-5000-20G-12345 > Seleziono Camera 1 FlexiBowl® 1 
:::

:::{warning}
Nel caso in cui la camera non dovesse essere visibile alla prima apertura di FlexiVision, consultare la sezione [Troubleshooting per la sezione Camera Setup](scelta_camera)
:::


---
## Passi successivi

Una volta completato il Setup della camera, procedere con:

- [Calibrazione Camera](calibrazione)
- [FlexiBowl® Setup](fbsetup)
- [Hopper Setup](13b_Hopper_Setup.md)
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Salvare La Ricetta](ricettabase)

