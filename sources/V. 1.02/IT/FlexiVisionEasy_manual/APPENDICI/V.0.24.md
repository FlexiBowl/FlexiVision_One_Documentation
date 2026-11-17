# V. 0.24

## **Nuove Funzionalità**

### Telecamere di Controllo

- Aggiunta la gestione di **3 telecamere di controllo** indipendenti, associate rispettivamente a FLB1, FLB2 e FLB3.
- Implementato il comando robot `start_control_` con supporto a parametri personalizzati, inoltrati agli script VisionPro.
- Aggiunta la gestione di script VisionPro personalizzabili, con output testuale e immagini `CogRecord` comprensive dei risultati grafici.
- Implementati i Main Task dedicati alle telecamere di controllo, con gestione degli errori, logging e invio dei risultati al robot.
- Abilitata l'esecuzione dei controlli anche senza robot connesso, per eseguire test locali da HMI.
- Aggiunte pagine HMI condivise per la configurazione della camera, la configurazione di VisionPro e la visualizzazione runtime delle tre telecamere di controllo.

## **Miglioramenti**

### Clearances (Istogrammi)

- Aggiornata la gestione delle regioni per tutti gli 8 modelli, gli 8 Histogram e le 3 telecamere, preservando posizione, dimensioni e geometria delle ROI salvate.

## **Problemi Risolti**

### Ricette

- Corretto il reset delle ROI degli Histogram durante il cambio ricetta.
