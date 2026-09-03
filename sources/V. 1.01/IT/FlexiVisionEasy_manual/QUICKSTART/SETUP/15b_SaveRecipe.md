(ricettabase)=
# **Salvare la ricetta**

Una volta completati tutti i setup dei componenti, l'ultimo passo prima di procedere alla creazione dei modelli, è il salvataggio della ricetta. 

````{list-table}
:header-rows: 0
:widths: 10 90

* - **1**
  - Accedere alla sezione <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon" > dal pulsante in alto

* - **2**
  - Inserire il nome della ricetta.

    Utilizzare un nome descrittivo (es: "Ricetta_Base").

    Evitare caratteri speciali o spazi (usare underscore ``_`` al posto degli spazi).

* - **3**
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

    **Formato suggerito**: `[LINEA]_[PRODOTTO]_[VARIANTE]_[GG_MM_AAAA]`

    Un nome chiaro facilita la gestione quando si hanno molte ricette diverse.
    :::

* - **4**
  - Cliccare su **Save Recipe** per salvare la ricetta
````

```{warning}
**Backup ricette**

Dopo aver creato e configurato una ricetta:
- Utilizzare la funzione di backup del software ([Backup Management](backup))
- Esportare periodicamente le ricette su supporto esterno
- Documentare parametri critici su supporto cartaceo/digitale

Una ricetta ben configurata rappresenta ore di lavoro. Proteggerla adeguatamente previene perdite di dati.
```