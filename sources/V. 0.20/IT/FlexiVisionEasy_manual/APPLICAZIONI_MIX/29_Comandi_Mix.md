# **Comandi Applicazione Mix**
```{note}
**Prerequisiti**

Prima di procedere con questa sezione, assicurarsi di aver compreso il funzionamento dell'Applicazione Mix e di aver configurato correttamente la ricetta con i modelli dei diversi componenti. Consultare [Panoramica Applicazione Mix](28_Panoramica_Mix.md).
```

---

## Differenze lato robot

In un'Applicazione Mix, i comandi TCP/IP inviati dal robot al sistema di visione cambiano rispetto a quelli di un'applicazione Standard.

La principale differenza riguarda la **famiglia di comandi di localizzazione**: i comandi che nell'applicazione Standard hanno prefisso `start_` vengono sostituiti dalla famiglia equivalente con prefisso `mix_`.

Questa variazione consente al sistema di visione di attivare la logica di riconoscimento **multi-componente**, restituendo al robot non solo le coordinate del pezzo localizzato, ma anche l'**identificativo del modello** riconosciuto, così che il programma robot possa selezionare la strategia di prelievo corretta per ogni tipologia di pezzo.
```{important}
Il valore di ritorno dei comandi Mix include sempre l'identificativo del pattern riconosciuto (`Pattern_n`). Il programma robot deve essere predisposto per gestire le diverse tipologie di risposta e adottare la logica di prelievo appropriata in base al modello identificato.
```

---

## Comandi disponibili in modalità Mix

### Gestione ricette

| Comando | Azione | Valore di Ritorno |
|---|---|---|
| `set_Recipe=nome_ricetta` | Carica la ricetta Mix specificata | Nessuno |
| `get_Recipe` | Restituisce il nome della ricetta attualmente caricata | `nome_ricetta` |
```{note}
I comandi di gestione ricetta sono identici tra modalità Standard e Mix.
```

### Comandi di localizzazione Mix

I comandi di localizzazione Mix consentono al robot di richiedere le coordinate di uno specifico modello all'interno della ricetta. Ogni comando è dedicato a un singolo modello e gestisce autonomamente il ciclo di ricerca, inclusa la movimentazione del FlexiBowl® e l'attivazione della tramoggia se necessario.

Il comportamento di `mix_Locator_n` è il seguente:

1. Il sistema acquisisce un'immagine e cerca il Modello `n`.
2. Se il modello non viene trovato alla prima acquisizione, il FlexiBowl® viene azionato automaticamente e la ricerca riprende.
3. Il ciclo continua finché il Modello `n` non viene localizzato oppure viene inviato il comando `stop_Locator`.
4. Durante l'intera fase di ricerca, la tramoggia viene attivata automaticamente se necessario.
```{important}
Ogni comando `mix_Locator_n` cerca **esclusivamente** il modello corrispondente al numero `n`.   
Questo significa che per richiedere le coordinate di un modello diverso è necessario utilizzare il comando specifico per quel modello (es. `mix_Locator_2` per il Modello 2, `mix_Locator_3` per il Modello 3, e così via).
```

| Comando | Azione | Valore di Ritorno |
|---|---|---|
| `mix_Locator_1` | Avvia la ricerca del **Modello 1**. Se non trovato, aziona il FlexiBowl® e ripete la ricerca automaticamente fino al ritrovamento o a `stop_Locator`. Attiva la tramoggia se necessario. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Come sopra, per il **Modello 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Come sopra, per il **Modello 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | Come sopra, per il **Modello 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | Se nessun pezzo è stato prelevato, fa ruotare il FlexiBowl® e riavvia la ricerca multi-componente | `Pattern_n;x;y;r` |
| `test_Locator` | Avvia la localizzazione multi-componente senza attivare il FlexiBowl® (solo acquisizione immagine) | `Pattern_n;x;y;r` / Nessuno |
| `stop_Locator` | Interrompe qualsiasi ricerca in corso | Nessuno |
| `state_Locator` | Restituisce lo stato diagnostico del localizzatore | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
Il numero massimo di modelli gestibili all'interno di una singola ricetta Mix è **8**, corrispondenti ai comandi `mix_Locator_1` … `mix_Locator_8`. Il programma robot può richiedere i modelli in qualsiasi ordine e combinazione, a seconda della logica applicativa.
```

### Comandi FlexiBowl®

| Comando | Azione | Valore di Ritorno |
|---|---|---|
| `start_Empty` | Avvia la sequenza di svuotamento rapido del FlexiBowl® | `start_Empty ended` |

### Segnali hopper opzionale
```{note}
Se la tramoggia deve essere attivata, riceveremo la stringa: `"Hopper;signalnumber;time"`
```

---

## Formato del valore di ritorno

In modalità Mix, il valore di ritorno dei comandi di localizzazione ha il seguente formato:
```
Pattern_n;x;y;r
```

| Campo | Descrizione |
|---|---|
| `Pattern_n` | Identificativo del modello riconosciuto (es. `Pattern_1`, `Pattern_2`, …). Corrisponde al numero del modello richiesto con il comando `mix_Locator_n`. |
| `x` | Coordinata X del pezzo nell'area di lavoro (in mm, nel sistema di riferimento del robot) |
| `y` | Coordinata Y del pezzo nell'area di lavoro (in mm, nel sistema di riferimento del robot) |
| `r` | Angolo di rotazione del pezzo (in gradi) |
```{tip}
Il campo `Pattern_n` è il parametro chiave per le applicazioni Mix: il programma robot deve utilizzarlo per selezionare la routine di prelievo corretta (posizione di approccio, apertura pinza, forza di presa, ecc.) in base alla tipologia di pezzo identificata.
```

---


Per informazioni sul protocollo di comunicazione e i parametri di connessione TCP/IP, consultare:

**→ [Protocollo Comunicazione Robot-Visione](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
