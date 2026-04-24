# **Panoramica Applicazione Mix**
Questa sezione introduce il concetto di **Applicazione Mix** in FlexiVision One, spiegando in cosa si differenzia da un'applicazione standard e come configurarla correttamente a livello di ricetta e modelli.

---

## Cos'è un'Applicazione Mix?

Un'**Applicazione Mix** è una configurazione applicativa in cui all'interno della stessa ricetta coesistono modelli relativi a **componenti completamente diversi tra loro**.

In un'applicazione Mix, il robot è in grado di riconoscere e prelevare **più tipologie di pezzi differenti** presenti contemporaneamente nell'area di lavoro, senza dover cambiare ricetta o interrompere il ciclo. La visione identifica ogni pezzo presente sul FlexiBowl® e restituisce al robot le coordinate del pezzo prelevabile più idoneo, indipendentemente dalla sua tipologia.
```{tip}
**Esempio tipico:** sul FlexiBowl® possono trovarsi contemporaneamente viti, dadi e rondelle. Il robot preleva qualsiasi pezzo riconosciuto, ottimizzando il throughput senza interruzioni.
```

---

## Applicazione Standard vs Applicazione Mix

| Caratteristica | Applicazione Standard | Applicazione Mix |
|---|---|---|
| **Tipologie di pezzi** | Un solo tipo di pezzo  | Più tipologie di pezzi completamente diversi tra loro |
| **Modelli nella ricetta** | Tutti i modelli si riferiscono allo stesso componente | I modelli si possono riferire anche a componenti distinti |
| **Comportamento del robot** | Preleva sempre lo stesso pezzo anche in posizioni diverse (creando più modelli)| Preleva qualsiasi pezzo riconosciuto, indipendentemente dalla tipologia |
| **Configurazione software** | Nessuna differenza rispetto alla modalità Mix | Nessuna differenza rispetto alla modalità Standard |
| **Selezione della modalità** | Non richiesta: dipende dai modelli inseriti nella ricetta | Non richiesta: dipende dai modelli inseriti nella ricetta |
| **Comandi robot** | Famiglia `start_..` | Famiglia `mix_..` |

```{note}
A livello software non esiste una scelta esplicita tra modalità Standard e Mix: la distinzione è determinata esclusivamente dal **contenuto della ricetta**. Se tutti i modelli presenti si riferiscono allo stesso pezzo (o alle sue diverse facce), si tratta di un'applicazione Standard. Se i modelli si riferiscono a pezzi diversi, si tratta automaticamente di un'applicazione Mix.
```

---

## Come si crea una ricetta Mix?

Il processo di creazione di una ricetta Mix è **identico** a quello di una ricetta Standard. Non è necessario selezionare alcuna opzione preliminare. Si può quindi seguire la procedura di [Creazione Ricette e Modelli - Panoramica](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md)

La differenza si manifesta **nella fase di creazione dei modelli**:

- In un'applicazione **Standard**, tutti i modelli inseriti nella ricetta rappresentano lo stesso componente (ad esempio: faccia A, faccia B, faccia C dello stesso pezzo).
- In un'applicazione **Mix**, i modelli inseriti rappresentano **componenti completamente diversi** (ad esempio: Pezzo A, Pezzo B, Pezzo C — tre componenti distinti con geometrie differenti).
```{important}
Ogni modello all'interno di una ricetta Mix deve essere addestrato separatamente con il proprio pezzo fisico di riferimento, seguendo la procedura standard descritta in [Creare un Nuovo Modello](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Le clearances e le coordinate robot pick devono essere calibrate individualmente per ciascun componente.
```

---

## Prossimi passi

Una volta compreso il concetto di Applicazione Mix e configurata la ricetta con i modelli dei diversi componenti, il passo successivo riguarda l'adattamento dei **comandi robot** necessari per operare in modalità Mix:

**→ [Comandi Applicazione Mix](29_Comandi_Mix.md)**

