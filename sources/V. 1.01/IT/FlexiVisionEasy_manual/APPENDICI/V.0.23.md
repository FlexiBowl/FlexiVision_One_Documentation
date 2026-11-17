# V. 0.23

## **Miglioramenti**

### Integrazione Robot

- Rimosso il server TCP dedicato al Laser: tutti i comandi e le comunicazioni Laser vengono ora instradati tramite il client TCP del Robot.

## **Problemi Risolti**

### Wizard Test Air Blow e Test Flip

- Corretto il Wizard per i test **Flip** e **Blow**: aggiunto il controllo dello stato del motore con abilitazione automatica, verifica successiva e gestione dell'errore in caso di mancata abilitazione.
