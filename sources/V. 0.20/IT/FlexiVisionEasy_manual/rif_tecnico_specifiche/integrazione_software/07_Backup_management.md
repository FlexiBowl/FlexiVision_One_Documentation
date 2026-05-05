(backup)=
# **BackUp Management**

## **Panoramica**

L'intera configurazione di FlexiVision One — setup hardware, calibrazioni, modelli dei pezzi e parametri di protocollo — è contenuta nei file ricetta. Per questo motivo, i backup sono fondamentali per mantenere al sicuro tutti i dati.

```{important}
Si raccomanda di eseguire un backup dopo ogni creazione o modifica significativa di una ricetta, prima di aggiornare il software FlexiVision e prima di qualsiasi intervento hardware sul sistema.

**Regola minima:** almeno una volta a settimana durante la normale operatività.
```

---

## **Procedura di Backup**

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Step**
  - **Azione**
* - Click Backup
  - Nel menu Ricette, cliccare il pulsante Backup.
* - Scegliere la cartella FlexiVision
  - Individuare la cartella runtime di FlexiVision One sul VisionController.
* - Scegliere la cartella di destinazione
  - Selezionare la cartella di destinazione del backup.
* - Nominazione con data
  - Assegnare sempre un nome che includa la data, la versione software e l'identificativo del sistema o altre informazioni utili come il nome del cliente. Esempi:
    
    - `FV_Recipes_LineA_20260402_SW1.2.xml`
    - `Backup_FlexiVision_ClientABC_Plant3_20260402.xml`
    - `Recipes_FB500_Commissioning_20260315_v1.zip`
    
    Includere la versione software (visibile nella Home page) nel nome o in un file di testo allegato.
```

---

## **Procedura di Import Backup**

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Step**
  - **Azione**
* - Click Import Backup
  - Dalla sezione Ricette, cliccare su Import Backup.
* - Selezionare la cartella runtime di FlexiVision
  - **Selezionare la cartella che contiene l'installazione di FlexiVision.**
* - Selezionare il path del backup
  - Impostare il percorso del file di backup. FlexiVision si riavvierà durante questo processo.
* - Verifiche post-ripristino
  - Dopo il ripristino, eseguire le seguenti verifiche prima di riavviare la produzione:

    1. Verificare che tutte le ricette attese siano presenti nell'elenco della pagina Ricette.
    2. Confermare che la ricetta principale possa essere caricata senza errori.
    3. Verificare che FlexiBowl® e i test di connessione della camera siano positivi (verdi) in Camera Setup.
    4. Confermare che il Dashboard mostri i dispositivi correttamente connessi.

    **Eseguire un ciclo di test con la ricetta operativa principale per verificare il corretto funzionamento.**
```

---

## **Gestione corretta delle ricette**

```{list-table}
:header-rows: 1
:widths: 25 37 38

* - **Azione**
  - **Metodo corretto**
  - **Metodo da evitare**
* - Rinominare una ricetta
  - Pagina Ricette → funzione Rinomina nel software.
  - Rinominare il file XML tramite Esplora File.
* - Eliminare una ricetta
  - Pagina Ricette → pulsante **Elimina Ricetta**.
  - Eliminare il file XML manualmente.
* - Copiare una ricetta su un altro sistema
  - Pagina Ricette → Backup → Import Backup sull'altro sistema.
  - Copiare e incollare i file XML tra due cartelle Recipes.
* - Modificare un parametro di ricetta
  - Aprire la ricetta in modalità **Modifica** nel software.
  - Modificare il file XML con un editor di testo.
```
