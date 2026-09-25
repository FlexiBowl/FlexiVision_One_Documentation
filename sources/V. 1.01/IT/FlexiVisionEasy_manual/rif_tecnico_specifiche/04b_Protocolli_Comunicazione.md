(protocollo)=
# **Protocollo Comunicazione Robot-Visione**

FlexiVision One comunica con il robot tramite protocollo **TCP/IP** su rete Ethernet. 

## Specifiche protocollo

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parametro
  - Valore
* - Protocollo
  - TCP/IP
* - Porta
  - Configurabile (default: FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Carattere di terminazione
  - CHR(13) - Carriage Return
* - Formato dati
  - Stringa ASCII
* - Timeout
  - Configurabile (default: 5000 ms)
* - Encoding
  - UTF-8
```

## Comandi disponibili

Il sistema supporta i seguenti comandi tramite stringhe di testo inviate sulla connessione TCP/IP.

### *Gestione ricette*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `set_recipe=<nome>`
  - Carica la ricetta indicata e avvia la sincronizzazione dei FlexiBowl® collegati.
  - Nessuno
* - `get_recipe`
  - Restituisce il nome della ricetta attualmente caricata.
  - `<nome_ricetta>`
```

Esempio:

```
set_recipe=MyRecipe
```

oppure:

```
get_recipe
→ MyRecipe
```

### *Comandi di localizzazione*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Locator`
  - Avvia il processo di localizzazione dei pezzi. Se non sono presenti pezzi prelevabili, richiama automaticamente la routine di movimentazione del FlexiBowl®. Se il Locator è già attivo, il comando viene ignorato senza riavviare il processo.
    :::{important}
    Se al momento del comando non risulta selezionato/abilitato alcun modello, il sistema restituisce un messaggio di errore e il Locator non viene avviato.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Ferma il processo di localizzazione.
  - Nessuno
* - `turn_Locator`
  - Se nessun pezzo è stato prelevato, richiede una nuova movimentazione del FlexiBowl® e riavvia il processo di ricerca.
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Avvia la localizzazione senza attivare il FlexiBowl®; viene eseguita solamente l'acquisizione e la ricerca sull'immagine.
  - `Pattern_n;x;y;r` / Nessuno
* - `state_Locator`
  - Restituisce lo stato diagnostico del processo di localizzazione.
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
* - `mix_Locator_<modelli>`
    :::{tip}
    Per maggiori informazioni, consultare la [sezione dedicata ai comandi mix](mix)
    :::
  - Seleziona dinamicamente uno o più modelli e avvia il Locator. I modelli precedentemente selezionati vengono prima disabilitati. I numeri disponibili sono da 1 a 8 (es. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
    :::{note}
    Se il Locator è già in esecuzione, il comando viene ignorato e la selezione corrente non viene modificata.
    :::
  - Normale risultato del Locator / `#Error_mix_locator_not_valid` (se non viene individuato alcun modello valido)
```

:::{note}
Altri separatori di stringa disponibili, oltre `;`, sono: `,`, `|`, `:`, `&`, `$`, `@`, `#`. 
:::

:::{note}
Per `start_Locator` e `mix_Locator_<modelli>`, quando il Locator è già in esecuzione, al robot non viene inviata alcuna risposta.
:::

### *Come usare correttamente i comandi Start e Mix*

FlexiVision One supporta due modalità applicative distinte, a seconda che sul FlexiBowl® venga caricato un solo tipo di componente oppure più componenti diversi contemporaneamente. Il comando da utilizzare dipende dalla configurazione dell'applicazione: `start_Locator` e `mix_Locator_<modelli>` **non vanno mai usati in modo intercambiabile all'interno della stessa ricetta**.

**Applicazione standard – un solo componente**

In un'applicazione standard è caricato sul FlexiBowl® un solo tipo di componente. I diversi modelli vengono usati per riconoscere le diverse facce di presa dello stesso componente, ad esempio:

- Modello 1 = Prodotto, faccia di presa 1
- Modello 2 = stesso Prodotto, faccia di presa 2
- Modello 3 = stesso Prodotto, faccia di presa 3

In questa configurazione si utilizza esclusivamente `start_Locator`: il comando avvia automaticamente la ricerca sequenziale tra tutti i modelli creati (prima il Modello 1, poi il Modello 2, il Modello 3 e così via). Se non viene trovata alcuna istanza valida, il FlexiBowl® ruota e il ciclo di ricerca riparte.

```{important}
In un'applicazione standard **non vanno mai inviati comandi mix** (`mix_Locator_<modelli>`). La ricerca tra le diverse facce dello stesso componente è già gestita automaticamente da `start_Locator`.
```

**Applicazione mix – componenti diversi**

In un'applicazione mix sono caricati sul FlexiBowl® più componenti diversi contemporaneamente. Ogni modello è associato a un componente specifico e/o a una sua faccia di presa, ad esempio:

- Modello 1 = Componente 1
- Modello 2 = Componente 2

I comandi corrispondenti sono:

- `mix_Locator_1` → cerca solo il Componente 1 (Modello 1)
- `mix_Locator_2` → cerca solo il Componente 2 (Modello 2)

A differenza di `start_Locator`, un comando mix cerca **esclusivamente** i modelli indicati nel numero del comando. Per cercare più modelli contemporaneamente — che siano facce diverse dello stesso componente o componenti differenti — basta concatenare i relativi numeri, ad esempio:

- Modello 1 = Componente 1, faccia di presa 1
- Modello 2 = Componente 1, faccia di presa 2
- Modello 3 = Componente 2, faccia di presa 1
- Modello 4 = Componente 2, faccia di presa 2

In questo caso:

- `mix_Locator_12` → cerca contemporaneamente i Modelli 1 e 2 (entrambe le facce del Componente 1)
- `mix_Locator_34` → cerca contemporaneamente i Modelli 3 e 4 (entrambe le facce del Componente 2)

Ogni comando mix cerca quindi solo ed esclusivamente i modelli associati a quel comando, senza estendere la ricerca agli altri modelli presenti nella ricetta.

**Riepilogo**

| Configurazione applicazione | Comando da usare |
| --- | --- |
| Un solo componente, con una o più facce di presa | `start_Locator` |
| Più componenti diversi caricati insieme | `mix_Locator_<modelli>` |

```{note}
I due comandi non sono intercambiabili: `mix_Locator_12` **non** si comporta come `start_Locator` e non esegue una ricerca sequenziale automatica tra tutti i modelli — cerca solo i modelli 1 e 2.
```

### *Comandi FlexiBowl® – Emptying*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Empty`
  - Avvia la sequenza di svuotamento rapido (Quick-Emptying) del FlexiBowl®. Il comando non può essere eseguito mentre il Locator è attivo.
  - `Start_Empty Started` / `Locator is Running` / `#Error_flexibowl_not_connect`
* - `stop_Empty`
  - Arresta la sequenza di svuotamento del FlexiBowl®.
  - `Stop_Empty Command Sent` / `#Error_flexibowl_not_connect`
* - `state_Empty`
  - Restituisce lo stato corrente della sequenza di svuotamento.
  - `Emptying Running` / `Emptying Stopped` / `#Error_flexibowl_not_connect` / `#Error_invalid_emptying_state`
```

### *Segnali hopper opzionale*

```{note}
Se la tramoggia deve essere attivata, riceveremo la stringa: `"Hopper;signalnumber;time"`
```

## Errori generali

```{note}
**Licenza FlexiVision**: se la licenza software non è attiva, i comandi robot vengono rifiutati e viene restituito:
`#Error_License_not_active`
```

---

## Comandi Avanzati / Service

I comandi seguenti sono riservati a personale tecnico.

### *Connessione FlexiBowl®*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `connect_flb`
  - Richiede la connessione al FlexiBowl®. Se non è connesso, viene avviato il relativo task di connessione.
  - `#Flb1_connected` / `#Flb1_Not_connected`
```

---

Per informazioni dettagliate sull'installazione fisica e i collegamenti elettrici, procedere con le sezioni successive:
- [Calcolo Distanza Ottimale Camera](05_Calcolo_distanza_ottimale.md)
- [Installazione Meccanica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Cablaggio e Connessioni](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
