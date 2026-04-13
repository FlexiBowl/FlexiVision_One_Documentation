(troubleshooting_calib_cam)=
# **Calibrazione Camera**

## **Pattern non rilevato**

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

## **Calibrazione sempre "Bad" o "Acceptable"**

```{warning}
**Qualità calibrazione insufficiente**

Se nonostante le regolazioni la calibrazione rimane sotto "Excellent":

1. Verificare la distanza di lavoro camera-FlexiBowl (deve essere quella calcolata)
2. Controllare che la camera sia parallela rispetto al piano del FlexiBowl (deve essere perfettamente orizzontale)
3. Assicurarsi che la camera sia stabile (no vibrazioni durante acquisizione)
4. Verificare che l'obiettivo sia avvitato completamente 

Se il problema persiste, potrebbe esserci un problema meccanico nel montaggio. Consultare [Installazione Meccanica]009_Installazione_Meccanica.md) per revisione.
```

## **Errori dopo cambio illuminazione**

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



