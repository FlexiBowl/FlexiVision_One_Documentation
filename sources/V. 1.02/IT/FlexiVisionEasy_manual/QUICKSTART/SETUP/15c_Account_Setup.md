# **Account Setup**

La pagina **Account Setup** permette di creare ed eliminare gli account utente di FlexiVision One. A ogni account è assegnato un **livello di accesso**, che stabilisce quali funzioni del software può utilizzare.

```{note}
La gestione degli account è riservata agli utenti di livello **5** (**Engineer**).
```

---

## Accesso alla configurazione Account

:::{list-table}
:widths: 10 90

* - **1**
  - Aprire la pagina **Setup**.
* - **2**
  - Nel menu a tendina **Name** selezionare **Engineer**.
* - **3**
  - Nel campo **Password** inserire `3`.
* - **4**
  - Premere **Login** e confermare il messaggio di accesso riuscito con **OK**.
* - **5**
  - Premere l'icona **Account Setup**.
:::

```{note}
L'accesso è effettivo solo dopo aver premuto **Login**. L'utente attivo e il suo livello sono indicati alla voce **Current User Name**.
```

---

## Panoramica interfaccia Account Setup

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Sezione
  - Descrizione
* - **Elenco account** (sinistra)
  - Mostra gli account esistenti. Con **Delete Account** si elimina quello selezionato.
* - **Nuovo account** (destra)
  - Campi **Account Name**, **Account Password**, **Account Level** e pulsante **Create Account**.
:::

---

## Creazione di un nuovo account

### *Step 1: Inserimento dati*

:::{list-table}
:widths: 10 90

* - **6**
  - Nel campo **Account Name** inserire il nome del nuovo account.
* - **7**
  - Nel campo **Account Password** inserire la password del nuovo account.
* - **8**
  - Nel campo **Account Level** inserire il livello di accesso, da `1` a `5` (vedere [Livelli di accesso](#livelli-di-accesso)).
* - **9**
  - Premere **Create Account**. Il nuovo account compare nell'elenco a sinistra.
:::

### *Step 2: Accesso con il nuovo account*

:::{list-table}
:widths: 10 90

* - **10**
  - Tornare alla pagina **Setup** e selezionare il nuovo account nel menu a tendina **Name**.
* - **11**
  - Inserire la password e premere **Login**.
:::

Il video mostra la creazione di un account di livello 3, l'accesso con il nuovo account e i messaggi visualizzati quando il livello non è sufficiente.

:::{video} ../../../../../_shared/media/videos/new_account.mp4
     :width: 100%
     :align: center
:::

---

## Eliminazione di un account

Eseguire i passi da 1 a 5 di [Accesso alla configurazione Account](#accesso-alla-configurazione-account), quindi procedere come segue.

:::{list-table}
:widths: 10 90

* - **6**
  - Nell'elenco a sinistra selezionare l'account da eliminare.
* - **7**
  - Premere **Delete Account**. L'account viene rimosso dall'elenco e dal menu a tendina della pagina **Setup**.
:::

```{warning}
L'eliminazione è immediata e non viene richiesta alcuna conferma. Verificare l'account selezionato prima di premere **Delete Account**.
```

:::{video} ../../../../../_shared/media/videos/delete_account.mp4
     :width: 100%
     :align: center
:::

---

(livelli-di-accesso)=
## Livelli di accesso

FlexiVision One dispone di tre profili predefiniti. Un account creato dall'utente riceve i permessi corrispondenti al livello assegnato.

:::{list-table}
:header-rows: 1
:widths: 20 20 60

* - Livello
  - Profilo
  - Utilizzo
* - 1 – 3
  - **Operator**
  - Funzioni di base: consultazione della Home, caricamento delle ricette e backup.
* - 4
  - **Technician**
  - Funzioni di Operator, più test, gestione delle ricette, setup dell'impianto e licenza software.
* - 5
  - **Engineer**
  - Funzioni di Technician, più **Protocol Setup** e **Account Setup**.
:::

### *Funzioni abilitate per profilo*

:::{list-table}
:header-rows: 1
:widths: 16 33 17 17 17

* - Pagina
  - Funzione
  - Operator (1 – 3)
  - Technician (4)
  - Engineer (5)
* - Home
  - Contact Us
  - Sì
  - Sì
  - Sì
* - Home
  - Documentation
  - Sì
  - Sì
  - Sì
* - Home
  - Quick Start
  - Sì
  - Sì
  - Sì
* - Dashboard
  - Test
  - —
  - Sì
  - Sì
* - Recipes
  - Load Recipe
  - Sì
  - Sì
  - Sì
* - Recipes
  - Backup
  - Sì
  - Sì
  - Sì
* - Recipes
  - Import Backup
  - —
  - Sì
  - Sì
* - Recipes
  - New Recipe
  - —
  - Sì
  - Sì
* - Recipes
  - Save Recipe
  - —
  - Sì
  - Sì
* - Recipes
  - Edit Recipe
  - —
  - Sì
  - Sì
* - Recipes
  - Delete Recipe
  - —
  - Sì
  - Sì
* - Setup
  - Camera Setup
  - —
  - Sì
  - Sì
* - Setup
  - FlexiBowl® Setup
  - —
  - Sì
  - Sì
* - Setup
  - Hopper Setup
  - —
  - Sì
  - Sì
* - Setup
  - Robot Setup
  - —
  - Sì
  - Sì
* - Setup
  - License Software
  - —
  - Sì
  - Sì
* - Setup
  - Protocol Setup
  - —
  - —
  - Sì
* - Setup
  - Account Setup
  - —
  - —
  - Sì
* - Generale
  - Chiusura dell'applicazione
  - —
  - Sì
  - Sì
:::

Se si tenta di usare una funzione non abilitata, compare il messaggio **Insufficient Access Level**, che riporta il livello richiesto e quello dell'utente attivo.

### *Logout automatico*

- **Technician**: logout automatico dopo 5 minuti.
- **Engineer**: nessun logout automatico.

```{tip}
Assegnare a ogni utente il livello più basso sufficiente per le sue mansioni, in modo da evitare modifiche accidentali a ricette e configurazioni.
```
