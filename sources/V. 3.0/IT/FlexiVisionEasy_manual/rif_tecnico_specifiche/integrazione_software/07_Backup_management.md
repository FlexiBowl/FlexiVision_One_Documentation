(backup)=
# **BackUp Management**

## **Panoramica**

Il backup di FlexiVision One consiste nella copia della cartella `Recipes` presente sul VisionController. Questa cartella contiene tutte le ricette configurate nel sistema — inclusi modelli, parametri di riconoscimento e impostazioni associate — e rappresenta l'unico dato utente da preservare.

Poiché non è richiesto alcuno strumento dedicato, il processo di backup si riduce a una semplice operazione di copia e incolla tramite Esplora File.
```{important}
Si raccomanda di eseguire un backup ogni volta che viene creata o modificata una ricetta, e comunque prima di qualsiasi aggiornamento software o intervento di manutenzione sul VisionController.
```

---

## **Contenuto del Backup**

All'interno della cartella di installazione di FlexiVision One è presente la seguente struttura:
```
C:\FlexiVision One\
├── Data\
├── Languages\
├── Recipes\          ← unica cartella da includere nel backup
├── Flexivision_Smart_018
└── Package.dat
```

L'unica cartella che contiene dati utente è `Recipes\`. Le altre cartelle e i file presenti appartengono all'installazione del software e non devono essere inclusi nel backup.
```{note}
Il percorso esatto della cartella di installazione può variare in base alla configurazione del sistema. In caso di dubbio, verificare il percorso nelle impostazioni del software.
```

---

## **Procedura di Backup**
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Step**
  - **Azione**
* - 1
  - Assicurarsi che il software FlexiVision One sia **chiuso**.
* - 2
  - Aprire Esplora File sul VisionController e navigare fino a `C:\FlexiVision One\`.
* - 3
  - Fare clic con il tasto destro sulla cartella `Recipes` e selezionare **Copia**.
* - 4
  - Navigare nella destinazione di backup desiderata (chiavetta USB, cartella di rete, NAS, ecc.).
* - 5
  - Incollare la cartella nella destinazione. Si consiglia di rinominarla includendo la data, ad esempio: `Recipes_backup_2025-06-01`.
```
```{warning}
Non eseguire il backup mentre il software FlexiVision One è in esecuzione. La copia di file aperti potrebbe risultare incompleta o corrotta.
```

---

## **Procedura di Ripristino (Restore)**

In caso di perdita dei dati o sostituzione del VisionController, è possibile ripristinare le ricette precedenti seguendo questi passi:
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Step**
  - **Azione**
* - 1
  - Assicurarsi che FlexiVision One sia installato sul VisionController e **chiuso**.
* - 2
  - Aprire Esplora File e navigare fino a `C:\FlexiVision One\`.
* - 3
  - Rinominare la cartella `Recipes` esistente (es. `Recipes_old`) come misura precauzionale.
* - 4
  - Copiare la cartella di backup nella posizione `C:\FlexiVision One\` e rinominarla `Recipes`.
* - 5
  - Avviare FlexiVision One: tutte le ricette precedentemente salvate saranno nuovamente disponibili.
```
```{important}
La versione del software installata sul VisionController deve essere compatibile con quella utilizzata al momento del backup. In caso di aggiornamento software, contattare il supporto tecnico prima di procedere con il ripristino.
```

---

## **Raccomandazioni**

- Conservare almeno **due copie del backup** in posizioni fisiche distinte (es. una chiavetta USB locale e una cartella di rete remota).
- Etichettare sempre i backup con **data e versione software** per facilitarne l'identificazione nel tempo.
- Non modificare il contenuto della cartella `Recipes` manualmente: le ricette devono essere gestite esclusivamente tramite l'interfaccia di FlexiVision One.
```{tip}
Per ambienti con più VisionController, si consiglia di centralizzare i backup in una cartella di rete condivisa, organizzata per nome macchina e data.
```
