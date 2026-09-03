# V. 0.22


```{note}
Questa pagina si riferisce alla versione **1.01** del presente manuale, compatibile con **FlexiVision Studio v0.21** e **v0.22**.
```

## **Nuove Funzionalità**

### Applicazioni Mix

- Aggiunta la gestione combinata dei comandi `mix_locator` per Robot 1, Robot 2 e Robot 3: è ora possibile richiamare più modelli contemporaneamente all'interno di un'unica stringa (ad es. `mix_locator_12`, `mix_locator_248`, `mix_locator_12345678`).
- Aggiunto un controllo di validità sui comandi `mix_locator`: se la stringa ricevuta non contiene modelli validi (da 1 a 8), il sistema restituisce un errore dedicato.
- Aggiunta una protezione sui comandi `start_locator` e `mix_locator`: se un Locator è già in esecuzione, il comando viene ignorato, evitando riavvii indesiderati del task e modifiche impreviste ai modelli attivi.

### Clearances (Istogrammi)

- Aggiunto il supporto a tre tipologie di regione per i tool Histogram — **Rettangolo**, **Settore Anulare** e **Cerchio** — selezionabili tramite un menu dedicato nella pagina ricetta, per tutti i modelli e gli istogrammi disponibili.
- Aggiornata la pagina Test Histogram per visualizzare correttamente le nuove tipologie di regione, disegnate in verde o rosso in base all'esito del controllo.
- Aggiunta la visualizzazione grafica dell'indice Histogram e delle misure principali della regione selezionata.

### FlexiBowl®

- Aggiunta la funzione **Belt Check** per il controllo dello stato di usura e pulizia del nastro:
  - acquisizione di un'immagine di riferimento del nastro pulito tramite il pulsante **Save Clean Reference**;
  - confronto automatico, tramite Histogram, tra l'immagine di riferimento e quella attuale del nastro;
  - classificazione automatica del nastro in **Light**, **Dark** o **Medium** in base alla luminosità della reference;
  - visualizzazione dello stato del nastro con valore percentuale, colore e indicazione testuale (**Good**, **Warning**, **Poor**);
  - visualizzazione della data dell'ultimo controllo Belt Check per ciascun FlexiBowl®.
- Aggiunta la procedura guidata **Hopper Step Setup** per calcolare il numero di sequenze necessarie a raggiungere la zona tramoggia, con le funzioni **Reset Steps**, **Test Sequence** e **Save Hopper Step**, e relativa indicazione dello stato di calibrazione.
- Aggiunta la possibilità di inserire manualmente da tastiera i parametri dei FlexiBowl®, in alternativa alla regolazione tramite slider.
- Aggiunto un messaggio di avviso non modale quando i parametri di un FlexiBowl® vengono modificati ma non sono ancora sincronizzati con il dispositivo reale.
- Aggiunto l'**Auto Reset FlexiBowl**: se all'avvio di un comando di movimento è già presente un errore, il sistema esegue automaticamente il reset prima di avviare il comando.

### Sicurezza e Accessi

- Aggiunto il controllo del livello di accesso sui pulsanti comuni dell'interfaccia: le funzioni protette verificano il livello utente corrente prima dell'esecuzione, mostrando un messaggio in caso di permessi insufficienti.

## **Miglioramenti**

### Wizard di Creazione Ricetta

- Aggiunto un controllo sul Picking Offset al pulsante **NEXT**: se l'offset è abilitato, deve essere calcolato e valido prima di poter proseguire nel wizard.

### Interfaccia Ricetta

- Corretto il formato di visualizzazione degli offset Robot Pick nelle pagine ricetta, forzando il punto come separatore decimale al posto della virgola.

## **Problemi Risolti**

### BackUp Management

- Corretto un errore nella creazione del backup che si verificava quando il percorso sul PC conteneva spazi.

### Sequenze

- Risolto un problema di visualizzazione che poteva mostrare comandi apparentemente duplicati nell'elenco delle sequenze.
