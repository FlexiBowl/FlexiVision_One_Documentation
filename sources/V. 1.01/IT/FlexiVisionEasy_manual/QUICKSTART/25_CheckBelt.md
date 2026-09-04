# **Monitoraggio Disco: Check Belt**

Questa sezione descrive la procedura per verificare lo stato di usura e pulizia del nastro del FlexiBowl® tramite la funzione **Belt Check**.

**Cos'è il Belt Check?**
Il **Belt Check** è uno strumento che confronta l'immagine attuale del nastro con un'immagine di riferimento del nastro pulito (**Clean Reference**), calcolando un indice di somiglianza. Questo permette di monitorare nel tempo il livello di sporco o usura del nastro, individuando per tempo la necessità di manutenzione.

:::{note}
**Prerequisiti**

Prima di procedere, assicurarsi che:

- Il FlexiBowl® sia connesso e configurato ([FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md))
- Il nastro sia visibile e correttamente illuminato 
:::

---

## Accesso alla pagina Check Belt

|||
| **1** | Dalla pagina principale del software, cliccare su **Setup** |
| **2** | Nella pagina SETUP, identificare e cliccare sull'icona **Check Belt** |
| **3** | Si apre la pagina di controllo del nastro, con un blocco per ciascun FlexiBowl® gestito dal sistema |

---

## Panoramica interfaccia Check Belt

:::{image} ../../../../_shared/media/images/beltcheck.png
:width: 100%
:align: center
:::

La pagina è suddivisa in un blocco per ogni FlexiBowl® connesso, ciascuno composto da due sezioni:

| Elemento | Descrizione |
| --- | --- |
| **Flb X Connected** | Indicatore di stato connessione del FlexiBowl® corrispondente (🟢 Verde = connesso, 🔴 Rosso = non connesso) |
| **Save Clean Reference** | Acquisisce e salva l'immagine attuale del nastro come riferimento "pulito", da usare come termine di paragone nei controlli successivi |
| **Delete Clean Reference** | Elimina l'immagine di riferimento salvata in precedenza, per poterne acquisire una nuova |
| **Anteprima camera (prima/dopo)** | Le due miniature mostrano rispettivamente l'immagine di riferimento salvata e l'immagine attuale del nastro al momento del test |
| **Run Belt Check** | Avvia il confronto tra l'immagine di riferimento e quella attuale, calcolando lo stato del nastro |
| **Belt Health Result** | Pannello con l'esito del confronto: barra graduata Clean → Dirty, indicatore colorato, stato testuale e data dell'ultimo controllo |

---

## Procedura

### Step 1: Acquisizione del riferimento pulito

:::{important}
Eseguire questo step **solo con il nastro effettivamente pulito**. L'accuratezza di tutti i controlli futuri dipende dalla qualità di questa immagine di riferimento.
:::

|||
| ----- | ------------------------------------------------------------ |
| **1** | Assicurarsi che il nastro sia pulito e privo di componenti o residui nell'area inquadrata |
| **2** | Cliccare su **Save Clean Reference** |
| **3** | L'immagine viene acquisita e salvata come riferimento; comparirà nella miniatura di sinistra |

:::{tip}
Se il nastro viene sostituito o pulito a fondo, ripetere questo step per aggiornare il riferimento.
:::

### Step 2: Esecuzione del Belt Check

|||
| ----- | ------------------------------------------------------------ |
| **4** | Cliccare su **Run Belt Check** |
| **5** | Il sistema acquisisce l'immagine attuale del nastro (visibile nella miniatura di destra) e la confronta con il riferimento salvato |
| **6** | Il risultato viene mostrato nel pannello **Belt Health Result** |

---

## Interpretazione dei risultati

Il pannello **Belt Health Result** mostra:

| Elemento | Significato |
| --- | --- |
| **Barra graduata** | Rappresentazione visiva della posizione del valore misurato tra i due estremi Clean (pulito) e Dirty (sporco) |
| **Indicatore colorato e testo** | Stato sintetico del nastro: |

| Colore | Testo | Significato |
| --- | --- | --- |
| 🟢 Verde | **Good** | Nastro in buone condizioni |
| 🟡 Giallo | **Warning** | Nastro da monitorare, possibile necessità di pulizia a breve |
| 🔴 Rosso | **Poor** | Nastro sporco o usurato, si consiglia intervento di pulizia/manutenzione |



:::{note}
 *Da confermare*: le soglie percentuali esatte che determinano il passaggio da Good a Warning a Poor.
:::

---