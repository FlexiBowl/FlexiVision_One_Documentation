(distanza_lavoro)=
# **Calcolo Distanza di Lavoro Ottimale**

Questa sezione definisce la distanza di lavoro (Working Distance) raccomandata tra la telecamera e il piatto FlexiBowl, insieme alla conseguente selezione delle lenti necessarie per garantire il corretto Campo Visivo (Field of View, FOV).

La scelta corretta della distanza di lavoro e della lente è fondamentale per:
- Garantire che l'intera superficie utile del FlexiBowl sia visibile
- Ottenere la risoluzione necessaria per rilevare i pezzi
- Minimizzare le distorsioni ottiche
- Facilitare la calibrazione del sistema

---

## Distanze di lavoro raccomandate e selezione lenti

La scelta della lente è strettamente dipendente dalla distanza di montaggio raccomandata tra la telecamera e la superficie del piatto FlexiBowl. Mantenere la distanza di lavoro standard garantisce il corretto FOV e minimizza i problemi di distorsione ottica.


```{note}
**Lente già inclusa**

La lente appropriata per il modello FlexiBowl specificato nell'ordine è sempre inclusa nel pacchetto FlexiVision One e viene fornita in un imballo separato rispetto alla camera. Non è necessario acquistarla separatamente.
```

### Schema distanze e campo visivo

Il seguente diagramma illustra la relazione tra distanza di lavoro, lunghezza focale della lente e area di visione risultante per i diversi modelli di FlexiBowl.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distanza Di Lavoro
:width: 40%
:align: center
```

**Legenda schema:**
- **Distanza di Lavoro**: Distanza verticale tra la faccia frontale della lente e la superficie del piatto FlexiBowl
- **Area di visione**: Zona della superficie del FlexiBowl coperta dal campo visivo della camera

### Tabella riepilogativa per modello

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modello FlexiBowl
  - Distanza di Lavoro Raccomandata (Working Distance)
  - Lente Inclusa nel Kit (Lunghezza Focale)
* - **FB 200**
  - 800 mm 
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

```{warning}
**Importanza della distanza corretta**

Deviazioni significative dalla distanza di lavoro raccomandata possono causare:

- **Distanza troppo breve**: FOV insufficiente (parte del FlexiBowl non visibile).
- **Distanza troppo lunga**: Risoluzione insufficiente per rilevare pezzi piccoli, sfocatura

Rispettare sempre le distanze indicate in tabella durante il montaggio meccanico della camera.
```
### Posizionamento Camera 

**Configurazione corretta.** La camera deve essere posizionata centralmente e con il medesimo orientamento angolare all’area di visione del FlexiBowl (zona backlight). In questo modo il campo visivo (indicato in verde) copre simmetricamente l’intera area di lavoro, garantendo il corretto funzionamento del sistema di visione.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distanza Di Lavoro
:width: 70%
:align: center
```

**Configurazioni errate.** Le immagini mostrano esempi di posizionamento non corretto della camera: il campo visivo (indicato in rosso) risulta decentrato rispetto all'area di visone, coprendo solo parzialmente l'area di lavoro o includendo zone esterne ad essa. Queste configurazioni compromettono il riconoscimento dei pezzi e il funzionamento del sistema di visione.  

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Distanza Di Lavoro
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Distanza Di Lavoro
:width: 60%
:align: center
```
---

## Posizionamento TopLight 

Se il sistema include un TopLight (illuminatore dall’alto), il suo posizionamento deve avere il medesimo orientamento angolare della camera per garantire un’illuminazione uniforme. Deve essere installato su un supporto meccanicamente indipendente dal supporto della telecamera, tale che, per rimuovere o sostituire il sistema di illuminazione non debba essere necessario allentare o smontare la telecamera.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parametro
  - Valore Consigliato
* - **Distanza dalla superficie FlexiBowl**
  - Simile alla Working Distance della camera (±100 mm)
* - **Posizione rispetto alla camera**
  - Concentrica (stesso asse ottico della camera)
* - **Orientamento**
  - Parallelo alla superficie del FlexiBowl e medesimo orientamento angolare  della telecamera (Lato lungo area di visione - Lato lungo di illuminazione)
* - **Altezza relativa camera-TopLight**
  - Ottica di visione a filo della superficie supperiore Top Light  (Lasciare libero accesso alle ghiere di regolazione dell'ottica di visione)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Distanza Di Lavoro
    :width: 80%
    :align: center
    :::
```

```{tip}
Per ottenere la migliore uniformità di illuminazioneseguire le indicazioni appena riportate 
```

```{warning}
**Evitare riflessioni dirette**

Quando si posiziona il TopLight, assicurarsi che:

- La luce non si rifletta direttamente dalla superficie del FlexiBowl verso la camera (causando abbagliamento)
- Non ci siano ombre causate da componenti meccanici
- L'illuminazione sia il più uniforme possibile su tutta la superficie utile

```

---

## Riferimenti correlati

Per completare l'installazione e la configurazione del sistema:

- **Installazione meccanica camera**: [Installazione Meccanica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Specifiche tecniche camera**: [Specifiche FlexiVision One](04_Specifiche_FlexiVision.md)
- **Calibrazione sistema**: [Calibrazione della Camera](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Cablaggio elettrico**: [Cablaggio e Connessioni](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

