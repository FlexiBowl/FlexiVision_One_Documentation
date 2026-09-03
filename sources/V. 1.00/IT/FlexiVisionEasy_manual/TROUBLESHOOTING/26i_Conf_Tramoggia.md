(troubleshooting_conf_tramoggia)=
# **Configurazione Tramoggia** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni

* - **Area di controllo non definibile**
  - • Immagine non acquisita
    
    • Sezione sbagliata
  - • Acquisire immagine test
    
    • Accedere tramite Config Hopper X


* - **AUTO non calcola Mean e Std Dev correttamente**
  - • CAPTURE non eseguiti
    
    • Ordine CAPTURE invertito
    
    • Area controllo troppo piccola
  - • Eseguire CAPTURE vuoto poi CAPTURE pieno
    
    • Ripetere nell'ordine corretto
    
    • Ingrandire area di controllo
* - **TEST sempre VERDE (tramoggia non si attiva mai)**
  - • Soglia troppo permissiva
    
    • CAPTURE pieno con troppi componenti
    
    • Mean calcolato errato
  - • Ripetere CAPTURE pieno con numero minimo corretto
    
    • Verificare AUTO ricalcola correttamente
    
    • Regolare manualmente soglia se necessario
* - **TEST sempre ROSSO (tramoggia si attiva sempre)**
  - • Soglia troppo restrittiva
    
    • CAPTURE vuoto con componenti presenti
    
  - • Ripetere CAPTURE vuoto con area completamente pulita
    
    • Ripetere AUTO

* - **Time vibrazione non produce effetto desiderato**
  - • Valore troppo basso
    
    • Valore troppo alto 
    
    • Livello vasca tramoggia variabile
  - • Iniziare con 500ms
    
    • Incrementare ±100ms per regolare flusso
    
    • **CRITICO**: Mantenere carico costante nella vasca

* - **Tramoggia scarica in momenti sbagliati**
  - • Steps non corretto

    • Hardware del Controller Tramoggia non configurato correttamente 

  - • Ricalcolare Steps

    • Controllare le specifiche di configurazione nel [manuale dedicato alla Tramoggia]() 
```

