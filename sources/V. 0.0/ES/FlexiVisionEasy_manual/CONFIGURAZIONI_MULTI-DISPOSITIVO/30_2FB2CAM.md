# **2 FlexiBowl® e 2 Camere**

Questa sezione descrive le configurazioni disponibili quando si desidera operare con **due FlexiBowl®** e **due camere** gestiti da un unico VisionController FlexiVision One.

---

## Panoramica della configurazione

In una configurazione **2 FlexiBowl® + 2 Camere**, il sistema comprende due stazioni di alimentazione e visione indipendenti, entrambe gestite dallo stesso VisionController. Ciascuna stazione è composta da:

* 1 FlexiBowl®
* 1 Camera con ottica dedicata
* 1 Tramoggia (opzionale, se presente)

Le due stazioni comunicano con il VisionController attraverso uno **Switch di rete**.

```{important}
Lo **Switch** è un componente **obbligatorio** in tutte le configurazioni multi-dispositivo. Senza di esso non è possibile collegare contemporaneamente più FlexiBowl® e più camere al VisionController. Per le specifiche tecniche e i codici d'ordine, consultare la sezione [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Questa configurazione supporta due varianti operative, in base al numero di robot disponibili nell'impianto:
| | **Variante A** | **Variante B** |
|---|---|---|
| **Robot** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Camere** | 2 | 2 |
| **Logica operativa** | Il robot raggiunge entrambe le stazioni | Ogni robot è dedicato a una stazione |
| **Switch richiesto** | Sì | Sì |


---

## Variante A — 1 Robot, 2 FlexiBowl®

![Panoramica Sistema 2FB2CAM1Robot](../../../../_shared/media/images/2FB2CAM1R.png)

In questa variante un **singolo robot** opera su entrambe le stazioni. Il robot è posizionato in modo da poter raggiungere l'area di picking di ciascun FlexiBowl®, alternando il prelievo tra le due stazioni sulla base dei comandi ricevuti.

Ogni stazione gestisce una propria ricetta indipendente. Su ciascuna stazione è possibile configurare un'applicazione di tipo **Standard** o **Mix**, con modelli di componenti diversi all'interno della stessa ricetta.

| Parametro | Valore |
|---|---|
| FlexiBowl® | 2 |
| Camere | 2 |
| Robot | 1 |
| Switch richiesto | **Sì** |

```{important}
**Ricetta base e gestione delle ricette**

Come per la configurazione singola, anche in una configurazione 2FB + 2CAM il processo parte dalla creazione di un'**unica ricetta base**, che contiene i setup hardware e la calibrazione della camera per l'intero sistema. Questa ricetta base viene poi **duplicata** per ciascuna stazione: ogni duplicato costituisce la ricetta operativa di quella stazione, all'interno della quale vengono creati i modelli dei pezzi (fino a 8 per stazione).

Per questo è fondamentale che l'associazione tra i dispositivi venga configurata correttamente fin dall'inizio:

* **Camera 1** → FlexiBowl® 1 (+ Tramoggia 1, se presente)
* **Camera 2** → FlexiBowl® 2 (+ Tramoggia 2, se presente)

Un'associazione errata in fase di setup si ripercuoterebbe su tutte le ricette derivate, compromettendo il riconoscimento dei pezzi e il corretto funzionamento dell'intero sistema.
```
---

## Variante B — 2 Robot, 2 FlexiBowl®

![Panoramica Sistema 2FB2CAM2Robot](../../../../_shared/media/images/2FB2CAM2R.png)

In questa variante ogni robot è dedicato a una singola stazione: il **Robot 1** effettua il picking sul FlexiBowl® 1, il **Robot 2** effettua il picking sul FlexiBowl® 2. Le due celle sono indipendenti e non si sovrappongono.

Anche in questa variante ciascuna stazione supporta applicazioni sia di tipo **Standard** che **Mix**.

| Parametro | Valore |
|---|---|
| FlexiBowl® | 2 |
| Camere | 2 |
| Robot | 2 |
| Switch richiesto | **Sì** |

```{tip}
Questa variante garantisce la massima produttività, con le due celle che operano in parallelo e in modo completamente autonomo.
```

```{important}
**Ricetta base e gestione delle ricette**

Come per la configurazione singola, anche in una configurazione 2FB + 2CAM il processo parte dalla creazione di un'**unica ricetta base**, che contiene i setup hardware e la calibrazione della camera per l'intero sistema. Questa ricetta base viene poi **duplicata** per ciascuna stazione: ogni duplicato costituisce la ricetta operativa di quella stazione, all'interno della quale vengono creati i modelli dei pezzi (fino a 8 per stazione).

Per questo è fondamentale che l'associazione tra i dispositivi venga configurata correttamente fin dall'inizio:

* **Camera 1** → FlexiBowl® 1 (+ Tramoggia 1, se presente)
* **Camera 2** → FlexiBowl® 2 (+ Tramoggia 2, se presente)

Un'associazione errata in fase di setup si ripercuoterebbe su tutte le ricette derivate, compromettendo il riconoscimento dei pezzi e il corretto funzionamento dell'intero sistema.
```

---

## Componenti necessari

### Kit base FlexiVision One

Il **kit base FlexiVision One** (fornito con il sistema) include già tutto il necessario per la **prima stazione** (camera, ottica, cavi, griglia di calibrazione). Non è necessario acquistare un secondo kit completo per la seconda stazione.

### Kit Camera Aggiuntiva

Per la seconda stazione è sufficiente acquistare il **Kit Camera Aggiuntiva**, disponibile in una versione specifica per ogni taglia di FlexiBowl®. Il kit include:

* 1 Camera
* 1 Ottica dedicata alla taglia FlexiBowl®
* 1 Griglia di calibrazione
* 1 Cavo alimentazione camera
* 2 Cavi Ethernet

Selezionare il kit in base alla taglia del **secondo** FlexiBowl®:

| Taglia FlexiBowl® | Codice Kit Camera Aggiuntiva | Ottica inclusa |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |
```{note}
Se le due stazioni utilizzano FlexiBowl® di **taglie diverse**, il Kit Camera Aggiuntiva deve essere selezionato in base alla taglia del FlexiBowl® della seconda stazione. La prima stazione è già coperta dal kit base.
```

### Switch

Lo Switch è sempre necessario nelle configurazioni multi-dispositivo. Per codice, specifiche elettriche e fisiche consultare la sezione dedicata:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Cablaggio

Lo schema di cablaggio è identico per entrambe le varianti: tutti i dispositivi di campo (FlexiBowl®, camere, robot) si collegano allo **Switch**, e lo Switch si collega al **VisionController** tramite una singola porta Ethernet. La differenza tra Variante A e Variante B riguarda esclusivamente il numero di robot connessi allo Switch.
```{important}
Lo Switch dispone di **8 porte Ethernet**. Verificare che il numero totale di dispositivi da collegare non superi la capacità disponibile, tenendo conto di tutti i FlexiBowl®, camere e robot presenti.
```

### Schema di connessione

| Dispositivo | Collegamento |
|---|---|
| FlexiBowl® 1 | Porta Ethernet → Switch |
| FlexiBowl® 2 | Porta Ethernet → Switch |
| Camera 1 | Cavo Ethernet → Switch |
| Camera 2 | Cavo Ethernet → Switch |
| Robot 1 | Porta Ethernet → Switch |
| Robot 2 *(solo Variante B)* | Porta Ethernet → Switch |
| **Switch** | **Porta Ethernet → VisionController** |
```{tip}
Verificare che a ciascun dispositivo sia assegnato un indirizzo IP univoco nella stessa subnet. Le porte TCP/IP utilizzate dal VisionController per le due stazioni sono configurabili: per default **FB1 → 4001**, **FB2 → 4002**. Consultare la sezione [Protocollo Comunicazione Robot-Visione](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) per i dettagli.
```

### Porte Switch occupate per variante

| Porta Switch | Variante A (1 Robot) | Variante B (2 Robot) |
|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | Camera 1 | Camera 1 |
| 4 | Camera 2 | Camera 2 |
| 5 | Robot 1 | Robot 1 |
| 6 | VisionController | Robot 2 |
| 7 | — | VisionController |
| 8 | — | — |

```{note}
**Cablaggio dei singoli componenti**

Le procedure di collegamento fisico di ciascun componente (FlexiBowl®, camera, tramoggia, robot) sono descritte integralmente nella sezione [Cablaggio e Connessioni](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md). In una configurazione 2FB + 2CAM le stesse operazioni vanno semplicemente eseguite **due volte** — una per ciascuna stazione — con l'unica differenza che ogni dispositivo si collega allo **Switch** anziché direttamente al VisionController.
```
```{important}
**Associazione dispositivi nel software**

FlexiVision One è in grado di gestire contemporaneamente tutte le stazioni, ma è fondamentale che l'associazione tra i dispositivi venga configurata correttamente nel software. Assicurarsi di associare:

* **Camera 1** → FlexiBowl® 1 (+ Tramoggia 1, se presente)
* **Camera 2** → FlexiBowl® 2 (+ Tramoggia 2, se presente)

Un'associazione errata comprometterebbe la localizzazione dei pezzi e il corretto funzionamento dell'intero sistema.
```

**→ [Configurazione Iniziale del Sistema](../QUICKSTART/SETUP/13_setup.md)**

