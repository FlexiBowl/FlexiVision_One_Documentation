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

Il sistema supporta i seguenti comandi tramite stringhe di testo inviate sulla connessione TCP/IP:

### Gestione ricette

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `set_Recipe=nome_ricetta`
  - Carica la ricetta corrispondente al "nome_ricetta" specificato
  - Nessuno
* - `get_Recipe`
  - Restituisce il nome della ricetta attualmente caricata
  - `nome_ricetta`
```

### Comandi di localizzazione

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Locator`
  - Avvia il processo di localizzazione dei pezzi. Se non sono presenti pezzi prelevabili, richiama automaticamente la routine di movimentazione del FlexiBowl.
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Ferma il processo di localizzazione
  - Nessuno
* - `turn_Locator`
  - Se nessun pezzo è stato prelevato, fa ruotare il FlexiBowl e riavvia la ricerca
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Avvia la localizzazione senza attivare il FlexiBowl (solo acquisizione immagine)
  - `Pattern_n;x;y;r`/ Nessuno
* - `state_Locator`
  - Restituisce lo stato diagnostico del localizzatore
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

### Comandi FlexiBowl

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Empty`
  - Avvia la sequenza di svuotamento rapido (Quick-Emptying) del FlexiBowl
  - `start_Empty ended`
```


### Segnali hopper opzionale

```{note}
Se la tramoggia deve essere attivata, riceveremo la stringa: `"Hopper;signalnumber;time"`

```



Per informazioni dettagliate sull'installazione fisica e i collegamenti elettrici, procedere con le sezioni successive:
- [Calcolo Distanza Ottimale Camera](05_Calcolo_distanza_ottimale.md)
- [Installazione Meccanica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Cablaggio e Connessioni](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

