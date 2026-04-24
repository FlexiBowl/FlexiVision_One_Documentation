(nuovaricetta)=
# **Creare una Nuova Ricetta**

Questa sezione descrive come creare una nuova ricetta applicativa in FlexiVision One. Una ricetta è il contenitore principale che include tutti i modelli pezzo, le configurazioni FlexiBowl/Hopper e i parametri robot necessari per un'applicazione completa di picking.
```{note}
**Creare una nuova ricetta quando:**

- Si lavora con un **tipo di pezzo completamente diverso**
- Si cambia **applicazione** 

**NON serve creare una nuova ricetta quando:**
- Si aggiunge una faccia dello stesso pezzo (creare nuovo modello nella stessa ricetta per lo stesso pezzo in posizioni diverse)
- Si fanno piccole regolazioni ai parametri esistenti (cam exposure)
- Si modifica solo l'accept threshold, score threshold, ecc.
```

---

## Panoramica interfaccia

Prima di procedere con il training del modello, familiarizzare con l'interfaccia [Recipes](recipes).


## Salvataggio ricetta base

Prima di procedere, assicurarsi di aver salvato la ricetta base creata durante il setup iniziale:
:::{list-table}
  * - **1**
    - Dalla pagina principale, cliccare su **Recipes**
  * - **2**
    - Verificare che la ricetta corrente sia quella base (es: "Ricetta_Base" creata durante il setup)
  * - **3**
    - Cliccare su **Save Recipe**
  * - **4**
    - Mantenere lo stesso nome nel campo di salvataggio (si sta sovrascrivendo la ricetta con le configurazioni aggiornate)
  * - **5**
    - Confermare il salvataggio
:::
```{important}

**Perché salvare la ricetta base?**

La ricetta base contiene tutte le configurazioni hardware completate durante il setup:
- Connessione FlexiBowl (IP, parametri)
- Connessione Hopper 
- Connessione Robot (porta TCP/IP)
- Calibrazione camera

Avere una ricetta base già pronta consente di riutilizzare tutte queste configurazioni senza doverle ripetere.
```

---
## Step 1: Duplicare la ricetta base 

Per partire con la creazione del primo modello, e quindi con la configurazione di una nuova applicazione, si consiglia sempre di duplicare la ricetta base appena salvata.   
Questo è utile perché permette di mantenere salvati a parte tutti i setup appena configurati. E questo è vantaggioso per due motivi: 
- Per iniziare una nuova applicazione con lo stesso sistema, non si deve ripetere tutti i passaggi fatti fin'ora 
- Se cambia un solo elemento nella configurazione, si possono tenere validi i setup di tutti gli altri componenti 
```{list-table}
* - **6**
  - Dalla pagina principale del software FlexiVision One, cliccare su **Recipes**
* - **7**
  - Si apre la pagina di gestione ricette con l'elenco di tutte le ricette esistenti
* - **8**
  - Selezionare la Ricetta Base
* - **9**
  - Duplicare la Ricetta Base
* - **10**
  - Cliccare su Load Recipe 
* - **11**
  - Verificare nella barra superiore che il nome visualizzato sia quello della nuova ricetta
    :::{warning}
    **Lavorare sempre sulla ricetta corretta**

    Con più ricette presenti, verificare sempre che sia selezionata quella corretta prima di iniziare modifiche. Modifiche applicate alla ricetta sbagliata richiedono di rifare il lavoro.
    :::
```
## Step 2: Nominare la Ricetta

Prima di cliccare su "Save Recipe", scegliere un nome descrittivo.
```{list-table}
* - **12**
  - Rinominare la Ricetta duplicata   
    **Convenzioni consigliate:**
    - Nomi che identificano chiaramente il pezzo o l'applicazione
    - Niente spazi (usare `_` o `-`)
    - Includere informazioni rilevanti (tipo pezzo, dimensione, applicazione)
    
    :::{tip}
    **Evitare nomi generici**

    ❌ Nomi da evitare:
    - `Test`, `Prova`, `Ricetta1`, `Nuova_Ricetta`

    ✓ Nomi consigliati:
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    **Formato suggerito**: `[LINEA]_[PRODOTTO]_[VARIANTE]_[ANNO]`

    Un nome chiaro facilita la gestione quando si hanno molte ricette diverse.
    :::
```
```{warning}
**Backup ricette**

Dopo aver creato e configurato una ricetta:
- Utilizzare la funzione di backup del software ([Backup Management](backup))
- Esportare periodicamente le ricette su supporto esterno
- Documentare parametri critici su supporto cartaceo/digitale

Una ricetta ben configurata rappresenta ore di lavoro. Proteggerla adeguatamente previene perdite di dati.
```

---

## Prossimi passi

**→ [Creare un Modello](18_NuovoModello.md)**
```{tip}
**Cosa serve per il prossimo step**

- Pezzi fisici da riconoscere (almeno 10-15 pezzi)
- FlexiBowl vuoto e pulito
- Se il tool del robot che stiamo utilizzando è una pinza, ci occorreranno anche due oggetti diversi dai pezzi di cui si vuole fare il modello da utilizzare come simulatori per l'ingombro del tool. 
- Foglio per annotare coordinate robot (X, Y, RZ)
```
