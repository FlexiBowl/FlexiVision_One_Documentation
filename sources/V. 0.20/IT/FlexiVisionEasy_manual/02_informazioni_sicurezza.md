# **Informazioni di Sicurezza**

Le seguenti istruzioni di sicurezza, precauzioni generali e norme relative alla movimentazione e all'ambiente operativo devono essere scrupolosamente rispettate per garantire la sicurezza del personale, l'integrità del prodotto e il corretto funzionamento dell'impianto.

```{warning}
**Responsabilità dell'utente**

Il rispetto di tutte le norme di sicurezza riportate in questa sezione è obbligatorio e di responsabilità dell'utilizzatore finale. Il mancato rispetto può causare danni a persone, apparecchiature o compromettere il funzionamento del sistema.
```

---

## Sicurezza operativa

### Integrazione con sistemi robotizzati


```{warning} **Requisiti di sicurezza della cella**  

FlexiVision One opera in stretta connessione con sistemi robotizzati di terze parti. L'utente deve garantire che l'area di lavoro sia dotata di tutte le misure di sicurezza necessarie imposte dalle normative pertinenti.
```


```{warning} **Attenzione durante l'operatività**    

Durante il funzionamento del sistema, tenere sempre conto di:

- Ingombri fisici del robot e del FlexiBowl®
- Traiettorie e velocità dei movimenti robotici
- Possibili situazioni impreviste (caduta pezzi, errori di prelievo)
- Zone di pericolo durante le fasi di movimentazione del FlexiBowl®
```

### Precauzioni generali prima degli interventi


```{warning} **Disconnessione alimentazioni**  

Prima di eseguire qualsiasi intervento di manutenzione, modifica o ispezione sul sistema, assicurarsi sempre che:

- Tutte le fonti di alimentazione elettrica siano disconnesse (VisionController, FlexiBowl®, Camera, Illuminatore)
- L'alimentazione pneumatica sia scaricata e disconnessa (se presente)
- I cavi di collegamento siano fisicamente scollegati
- Il robot sia in modalità di sicurezza o completamente spento
```


```{warning} **Procedure di sicurezza**    

Non affidarsi esclusivamente agli interruttori: utilizzare procedure di lockout/tagout (LOTO) quando disponibili.
```

### Modifiche e manomissioni


```{warning} **Divieto di modifiche non autorizzate**    

Non modificare mai il prodotto o i suoi componenti senza espressa autorizzazione scritta di ARS S.r.l.
```

```{warning} **Conseguenze delle modifiche**    

Modifiche non autorizzate possono:

- Causare malfunzionamenti del sistema
- Invalidare la garanzia
- Creare rischi di lesioni, scosse elettriche o incendi
- Compromettere le certificazioni di sicurezza del prodotto
```

---

## Predisposizioni a carico del cliente

Fatti salvi eventuali accordi contrattuali diversi, le seguenti predisposizioni sono **normalmente a carico del Cliente**:

````{list-table}
:header-rows: 1
:widths: 25 75

* - Categoria
  - Descrizione
* - **Locali**
  - Opere murarie, fondazioni, canalizzazioni e illuminazione eventualmente richieste.
* - **Impianti elettrici**
  - Fino ai punti di alimentazione della macchina, in conformità alle norme vigenti nel paese di installazione. Le specifiche tecniche sono contenute nel contratto di vendita. Il Costruttore declina ogni responsabilità se il cliente non riesce a garantirle.
* - **Alimentazione elettrica**
  - Compreso il conduttore di messa a terra, secondo le caratteristiche e tolleranze specificate nel presente manuale.
* - **Servizi ausiliari**
  - Adeguati alle esigenze della macchina.
* - **Utensili e materiali di consumo**
  - Occorrenti per il montaggio e l'installazione.
* - **Lubrificanti**
  - Necessari per la messa in moto della macchina.
* - **Alimentazione pneumatica**
  - Adeguata come da specifica nel paragrafo "Dati tecnici".
* - **Movimentazione**
  - Mezzi di sollevamento e movimentazione adeguati.
````

---

## Condizioni ambientali ammesse

Il sistema è progettato per uso **esclusivamente interno**, al riparo da agenti atmosferici e aggressivi. L'ambiente non deve essere classificato ATEX.

````{list-table}
:header-rows: 1
:widths: 30 70

* - Parametro
  - Limite ammesso
* - **Temperatura ambiente**
  - 5 ÷ 40 °C
* - **Umidità relativa**
  - 5 – 90% (senza condensa), variazione max 0,005 p.u./h
* - **Illuminazione ambiente**
  - Luce a neon
* - **Polveri**
  - Assenza di polveri eccessive, abrasive o combustibili
* - **Vapori e gas**
  - Assenza di fumi corrosivi, vapori oleosi, miscele esplosive
* - **Vibrazioni e urti**
  - Assenza di vibrazioni, urti o scosse anomale
* - **Variazioni termiche**
  - Massimo 5K/h
* - **Altre esclusioni**
  - Aria salmastra, intemperie, radiazioni nucleari, condizioni non usuali di stoccaggio
````

````{warning}
Condizioni ambientali diverse da quelle specificate possono causare gravi danni alla macchina e far decadere la garanzia.
````

````{important}
La superficie di lavoro deve essere sufficientemente illuminata. In presenza di zone d'ombra o dislivelli, è cura dell'utente predisporre dispositivi di illuminazione adeguati.
````

La macchina è progettata e costruita per funzionare, in sicurezza, nelle seguenti condizioni ambientali:

| Condizioni ambientali ammesse | |
|---|---|
| **Temperatura** ambiente | 5 ÷ 40 °C |
| **Range di umidità** | 5 – 90% (senza condensa) |
| **Illuminazione ambiente** | Luce a neon |

```{warning}
Condizioni ambientali diverse da quelle specificate possono causare gravi danni alla macchina. Il posizionamento della macchina in ambienti non corrispondenti a quanto indicato fa decadere la garanzia per gli organi da sostituire.
```

```{important}
La superficie di lavoro deve essere sufficientemente illuminata. Nel caso in cui sul posto di lavoro si riscontrino zone d'ombra o dislivelli, sarà cura dell'utente predisporre dispositivi di illuminazione adeguati.
```

---

## Condizioni ambientali e protezione

### Protezione da liquidi


```{warning} **Rischio contatto con liquidi**    

Non utilizzare il prodotto in ambienti dove il VisionController, la camera o altri componenti elettronici possano entrare in contatto con:

- Gocce d'acqua o spruzzi
- Oli, lubrificanti o altri liquidi industriali
- Condensa o umidità eccessiva
- Polveri conduttive
```

```{note} **Soluzioni per ambienti critici**    

Se il sistema deve operare in ambienti con presenza di liquidi, prevedere adeguate protezioni (custodie IP65 o superiori) e consultare il servizio tecnico ARS per soluzioni personalizzate.
```

### Temperature operative


```{warning} **Superfici calde - Temperature massime**    

In condizioni di utilizzo intenso o ambienti caldi, alcuni componenti del sistema possono raggiungere temperature elevate:

- VisionController: fino a 50°C sulle superfici esterne
- Illuminatore LED: fino a 40°C sulla superficie frontale
- Camera industriale: fino a 50°C sul corpo metallico
```


```{warning} **Responsabilità del cliente**    

È responsabilità del cliente:

- Documentare i rischi termici nella propria valutazione dei rischi
- Istruire il personale sulle procedure per evitare contatti accidentali
- Prevedere segnaletica di avvertimento dove necessario
- Garantire adeguata ventilazione dei componenti
```

### Condizioni ambientali per installazione e stoccaggio

```{note} **Requisiti ambientali - Tabella di riferimento**    

Per garantire durata e affidabilità, il VisionController e la camera devono essere utilizzati e conservati nelle seguenti condizioni:

| Parametro | Condizioni operative | Condizioni di stoccaggio |
|-----------|---------------------|--------------------------|
| **Temperatura** | +5°C ÷ +40°C | +5°C ÷ +40°C |
| **Umidità relativa** | <90% (senza condensa) | <90% (senza condensa) |
```

```{note} **Precauzioni aggiuntive per l'ambiente**    

Per preservare l'integrità dei componenti:

- Evitare l'esposizione diretta alla luce solare
- Proteggere da vibrazioni eccessive durante lo stoccaggio
- Mantenere in ambiente asciutto e privo di polveri aggressive
- La camera è sensibile agli shock meccanici: maneggiare con cura
```

---

## Trasporto e movimentazione

### Ricezione e ispezione

```{note} **Ispezione all'arrivo**    

Alla ricezione del prodotto, prima di firmare la bolla di consegna:

1. **Ispezione esterna dell'imballaggio**: Verificare l'integrità della scatola e dell'imballo esterno. Controllare la presenza di eventuali segni di urti, schiacciamenti o bagnature.
2. **Verifica contenuto**: Confrontare il contenuto con la nota di consegna. Verificare la presenza di tutti i componenti ordinati.
```

```{note} **In caso di danni o discrepanze**    

Se si riscontrano problemi:

- NON firmare la ricevuta come "conforme"
- Annotare i danni sul documento di trasporto
- Fotografare eventuali danni evidenti
- Contattare immediatamente il servizio assistenza ARS:
  [service@arsautomation.com](mailto:service@arsautomation.com)
  [us.service@arsautomation.com](mailto:us.service@arsautomation.com) se si contatta dall'America
```

### Movimentazione e stoccaggio

Per prevenire danni durante trasporto e stoccaggio:

```{tip}
**Durante il trasporto:**
- Movimentare sempre l'imballaggio in posizione verticale (rispettare le frecce "ALTO" sull'imballo)
- Non far cadere o urtare la confezione
- Utilizzare carrelli o transpallet adeguati al peso
- Evitare sbalzi termici improvvisi
```

```{tip}
**Durante lo stoccaggio:**
- Conservare in luogo asciutto e coperto
- Non sovrapporre altri carichi sull'imballaggio
- Non salire o appoggiarsi sull'imballaggio
- Rispettare le condizioni ambientali indicate nella tabella precedente
```

```{tip}
**Durante il disimballaggio:**
- Aprire con cura per non danneggiare i componenti interni
- Conservare l'imballo originale per eventuali resi o trasporti futuri
- Verificare la presenza di tutti gli accessori e della documentazione
```

---

## Smaltimento e fine vita

```{warning}
Quando il prodotto raggiunge la fine del suo ciclo di vita, deve essere smaltito in conformità con le normative vigenti relative ai rifiuti di apparecchiature elettriche ed elettroniche (RAEE/WEEE).
```

