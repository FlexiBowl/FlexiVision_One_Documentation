(setupcomponenti)=
# **Configurazione Iniziale del Sistema**

Questa sezione guida l'utente attraverso la configurazione completa dei componenti hardware e software del sistema FlexiVision One. È fondamentale seguire i passaggi nell'ordine indicato per garantire il corretto funzionamento del sistema.

```{note}
**Prerequisiti**

Prima di iniziare la configurazione software, assicurarsi che:
- L'installazione meccanica di tutti i componenti sia completata ([Installazione Meccanica](Installazione_Meccanica))
- Tutti i cavi siano collegati correttamente ([Cablaggio e Connessioni](cablaggio)) 
```

---

## Panoramica del processo di setup

Il processo di configurazione iniziale è composto da sette passaggi principali:

0. **Inserimento Chiave di Licenza** fornita nel kit
1. **Login** - Accesso al software con credenziali utente
2. se presente illuminatore Backlight: **Configurazione Indirizzo IP FlexiBowl** e **Accensione Backlight** 
3. **Camera Setup** - Configurazione della camera
4. **FlexiBowl Setup** - Connessione e configurazione del FlexiBowl
5. **Hopper Setup**  - Configurazione della tramoggia 
6. **Robot Setup** - Configurazione comunicazione con il robot
7. **Protocol Setup** - Configurazione di parametri di protocollo
8. **Rinominare e Salvare la Ricetta Base** - Configurazione del profilo applicativo

:::{note}
Lo schema completo del flusso di setup non e ancora disponibile come immagine esportata in questo repository. Fare riferimento alla sequenza guidata riportata qui sotto.
:::

```{warning}
**Ordine dei passaggi**

L'ordine dei setup è importante! Non saltare passaggi o modificare la sequenza, poiché alcune configurazioni dipendono da quelle precedenti.
```

---

## Operazioni preliminari

:::{important}
Il primo passo prima dell'avvio del software FlexiVision One è inserire la chiave di licenza fornita con il kit. 
:::

### Passo 1: Login al sistema

All'avvio del software FlexiVision One, viene presentata la pagina Home. 
```{list-table} 
   :widths: 10 90
   :header-rows: 0
   * - **0**
     - Cliccare su Setup 
   * - **1**
     - **Selezionare l'utente ENGINEER** dal menu a tendina in alto a destra.
   * - **2**
     - **Inserire la password** '3'.
   * - **3**
     - Cliccare sul pulsante **LOGIN** per accedere all'interfaccia.
```

```{tip}
**Gestione utenti**

FlexiVision One supporta profili utente multipli con diversi livelli di permessi:
- **ARS**
- **Engineer**
- **Technician**
- **Operator**
```

---

### Passo 2: Accendere il Backlight se presente

Dopo il primo login, se è necessario attivare la licenza FlexiVision One, seguire questi passi: 

```{list-table}
* - **1** 
  - Dalla pagina principale del software, cliccare su <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Nella pagina SETUP, identificare e cliccare sull'icona **FlexiBowl Setup**
    ```{dropdown} Pagina Setup 
       ![Pagina Setup](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - Si apre la schermata di configurazione dei FlexiBowl
* - **4**
  - Inserire l'indirizzo IP del FlexiBowl (default: `192.168.1.10` )
* - **5**
  - Dopo aver inserito l'IP, cliccare sul pulsante **Connection Test**
* - **6**
  - Il sistema esegue un test di comunicazione (ping) verso il FlexiBowl
* - **7**
  - Osservare l'indicatore di **Status**:
    - 🟢 **Verde**: Connessione stabilita correttamente
    - 🔴 **Rosso**: Connessione fallita (verificare indirizzo IP e cablaggio)
* - **8** 
  - Cliccare sul pulsante <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **9**
  - Si apre una finestra con i parametri configurabili del FlexiBowl
* - **10**
  - Accendere il backlight spuntando la casella "Light ON"
```
---

### Sequenza setup consigliata

```{list-table}
:header-rows: 1
:widths: 15 35 50

* - Passo
  - Componente
  - Descrizione
* - **3**
  - [Camera Setup](camerasetup)
  - Configurazione acquisizione immagini e test camera
* - **4**
  - [FlexiBowl Setup](fbsetup)
  - Connessione e test comunicazione con FlexiBowl
* - **5**
  - [Hopper Setup](hoppersetup)
  - Configurazione tramoggia esterna se presente
* - **6**
  - [Robot Setup](robotsetup)
  - Configurazione porta TCP/IP e test comunicazione con il robot
* - **7**
  - [Protocol Setup](protocol_setup)
  - Configurazione dei parametri di scambio dati e delle statistiche operative
```

```{warning}
**Importanza della sequenza**

Seguire l'ordine indicato è importante perché la camera ha bisogno che il FlexiBowl sia configurato per testare l'illuminazione e  alcuni parametri dipendono dalle configurazioni precedenti
```

(ricettabase)=
### Passo 8: Salva e Rinomina la ricetta base

Prima di configurare i componenti hardware, è necessario creare una ricetta di base che definisca i parametri del sistema.

````{list-table}
:header-rows: 0
:widths: 10 90

* - **8**
  - Accedere alla sezione |tasto_recipes| dal pulsante in alto

* - **9**
  - Inserire il nome della ricetta.

    Utilizzare un nome descrittivo (es: "Ricetta_Base").

    Evitare caratteri speciali o spazi (usare underscore ``_`` al posto degli spazi).

* - **12**
  - Cliccare su **Save Recipe** per salvare la ricetta
````

```{tip}
**Organizzazione ricette**

FlexiVision One permette di creare ricette multiple per diversi tipi di pezzi o configurazioni. Convenzioni consigliate:

- Utilizzare nomi che identificano chiaramente il pezzo (es: "Vite_M6_Zincata")

Per maggiori dettagli sulla gestione ricette, consultare la sezione [Creare una nuova ricetta](nuovaricetta).
```

---

## Configurazione componenti hardware

Una volta completate le operazioni preliminari, procedere con la configurazione dei componenti hardware nell'ordine seguente.

Tutti i setup hardware sono accessibili dalla pagina centrale **SETUP** del software.


```{list-table} 
* - **14** 
  - Dal menu principale, cliccare su <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **15** 
  - Vengono visualizzate le icone dei diversi componenti da configurare
* - **16**
  - Cliccare sull'icona del componente desiderato per accedere alla sua configurazione specifica
```

---

```{toctree}
:hidden:
13d_Camera_Setup.md
14_calibrazione_camera.md
13a_FB_Setup.md
13b_Hopper_Setup.md
13c_Robot_Setup.md
15_Protocol_Setup.md
```

