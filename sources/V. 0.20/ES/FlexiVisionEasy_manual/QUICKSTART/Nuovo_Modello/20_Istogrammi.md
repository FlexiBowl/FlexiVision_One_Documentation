(istogrammi)=
# **Le Clearances** 
 In questa pagina vedremo come configurare le Clearances per verificare che le aree critiche siano libere da ostacoli.

 **Cos'è una Clearance?**  
Una **Clearance** in FlexiVision One è uno strumento che monitora un'area specifica dell'immagine per verificare che sia libera. Viene utilizzato per controllare, ad esempio, che lo spazio necessario alla pinza per afferrare il componente non sia occupato da altri oggetti.
````{note} Principio di Funzionamento.

La Clearance analizza le variazioni dei livelli di grigio in un'area definita:
- 🟢 **Verde** → Area libera (OK per il prelievo)
- 🔴 **Rosso** → Area occupata (presenza di ostacoli)
````
:::{attention}
L'utilizzo delle Clearances varia al variare del pezzo di cui si deve fare il modello. Questa è una valutazione a carico della figura incaricata di creare l'applicazione. 
:::
--- 
(setupclearances)=
## **Step 1: Setup Fisico**

:::{danger} **Attenzione!**
  Vi mostreremo la procedura con il Tool Pinza, in quanto necessita obbligatoriamente della configurazione di Clearances per i modelli. Altri Tool per il robot potrebbero non aver bisogno delle Clearances per simularne l'ingombro. 
:::
:::{video} ../../../../../_shared/media/videos/Step1.mp4
    :width: 100%
    :align: center
:::
````{list-table}
:widths: 5 95

* - **1**
  - Dal **pendant del robot**:
    - Selezionare il **frame** e il **tool** calibrato su FlexiVision One
    - Portare l'**ultimo asse** del tool a **rotazione zero** (Rz = 0°)
* - **2**
  - Simulare una presa:
    - Aprire la pinza
    - Portare il tool del robot sul componente a livello della superficie, come per afferrarlo
* - **3**
  - Posizionare **due oggetti** ai lati della pinza per avere, una volta rimosso il robot, le aree libere fra il componente di riferimento e i due oggetti.  
  Esse rappresenteranno le aree di ingombro della pinza del robot. 
    
    :::{important}
    Lasciare gli oggetti leggermente più distanti del necessario per evitare errori nella creazione del modello. (margine 2-3 mm)
    :::
    
* - **4**
  - Annotare le Coordinate:
    - Salvare le coordinate dell'ultimo asse del robot:
      - **X** (coordinata X)
      - **Y** (coordinata Y)
      - **Rz** (rotazione attorno a Z)
    
    :::{important}
    Annotare queste coordinate! Saranno indispensabili nella fase di calibrazione robot.
    :::
* - **5**
  - Allontanare il robot con il pendant **senza spostare nulla** sulla superficie
````
---

## **Step 2: Accesso alla pagina Clearance**
````{list-table}
:widths: 5 95

* - **6**
  - Dalla pagina **Locator Model**, dopo aver cliccato su **Next**, si aprirà l'elenco delle clearance disponibili (fino a 8 per modello).
    
    :::{dropdown} **Pagina Clearances**
    
      ![Pagina Clearances](../../../../../_shared/media/images/pagina_clearances.png)
    
      | Elemento | Descrizione |
      |----------|-------------|
      | **Clearance 1...8** | Slot disponibili per creare fino a 8 clearance diversi per lo stesso modello |
      | **Test (globale)** | Pulsante per testare simultaneamente tutte le clearance abilitate |
      | **Next** | Avanzamento alla fase successiva (Robot Pick) dopo configurazione clearance |
    :::
* - **7**
  - Cliccare su **Clearance 1**, si aprirà la pagina relativa alla configurazione della prima clearance "Clearance 1"
    
    :::{dropdown} **Pagina Clearance 1**

      ![Pagina Clearance 1](../../../../../_shared/media/images/pagina_clearance1.png)

      | Parametro | Funzione |
      |-----------|----------|
      | **Enable Histogram** | Attiva questa clearance rendendola operativa |
      | **Expression Builder** | Strumento per configurare automaticamente le soglie di rilevamento |
      | **Mean and Standard Deviation** | Valori statistici calcolati sull'area selezionata (media e deviazione standard dei livelli di grigio) |
      | **Test** | Verifica immediata del funzionamento della clearance |
      | **Result** | Indicatore visivo dello stato (Verde = OK, Rosso = Triggered) |
    :::
````
---

## **Step 3: Attivazione e Posizionamento Area**

:::{video} ../../../../../_shared/media/videos/Step3.mp4
    :width: 100%
    :align: center
:::
````{list-table}
* - **8**
  - Cliccare su **Enable Clearance** per attivare la clearance 
* - **9**
  - Spostare il **riquadro** della Clearance nell'area che deve rimanere libera
      - Tipicamente: area di presa della pinza (una clearance per ogni area di presa della pinza)
      - Margini attorno al componente
      - Zone di passaggio del robot
    :::{important}
    Tenere sempre in considerazione questi due aspetti importanti:
    - La ROI della Clearance, quando viene configurata, deve essere completamente libera (quindi priva di oggetti, ombre, artefatti)
    - Creare sempre una clearance leggermente più grande dello stretto necessario per evitare falsi errori.

    La mancata osservanza di questi due punti potrebbe comportare collisioni del robot con conseguenti danni a FlexiBowl, componenti o robot stesso. 
    :::
````
---

## **Step 4: Configurazione Automatica**

:::{video} ../../../../../_shared/media/videos/Step4.mp4
    :width: 100%
    :align: center
:::
````{list-table}
* - **10**
  - Cliccare su <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> in Expression Builder
* - **11**
  - Cliccare su <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">
* - **12**
  - Verificare che il riquadro diventi **verde** 
* - **13**
  - Cliccare su <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
````
````{warning}
**Cosa fare se il test fallisce (riquadro rosso)?**

Se dopo AUTO il riquadro diventa rosso:

**Possibili cause:**
- C'è effettivamente qualcosa nell'area (pezzo, ombra, sporcizia)
- L'illuminazione è variata tra configurazione AUTO e TEST
- L'area selezionata include bordi del FlexiBowl o artefatti

**Soluzioni:**
1. Verificare visivamente che l'area sia completamente libera
2. Ripetere AUTO con condizioni di illuminazione stabili
3. Ripetere TEST per verificare
````

---

## Clearance Multipli - Quando Usarli

Crea più clearance quando:
- Il tool del robot è una pinza: serve una clearance per ognuna delle due aree occupate dalla pinza ai lati del componente di riferimento 
- Ci sono più punti critici da monitorare
- L'area di presa ha geometrie particolari

### **Step 2-3: Ripetizione**
Selezionare una nuova clearance dalla pagina elenco delle Clearances, tipo "Clearance 2" e ripetere gli Step 2-3.
Ripetere la procedura per ogni clearance necessaria (fino a 8 per modello). 

### **Step 4: Test Complessivo**
Nella pagina di elenco di tutte le clearance, cliccare su **TEST**
Visualizzare tutte le clearance contemporaneamente

---

## Interpretazione Stati

### Stati delle Clearance 
````{list-table}
:header-rows: 1
:widths: 15 35 50

* - Colore
  - Stato
  - Significato
* - 🟢 Verde
  - OK
  - Area libera, prelievo possibile
* - 🔴 Rosso
  - Triggered
  - Area occupata, prelievo non possibile
````

### Cosa Significa "Triggered"?

Una clearance diventa rossa (triggered) quando rileva al suo interno:
- Presenza di altri componenti
- Ombre o riflessi significativi
- Qualsiasi elemento che rende l'area non libera

---

## **Step 5: Finalizzazione**
````{list-table}
* - **14**
  - Dopo aver configurato tutte le clearance necessarie, cliccare su **Next**
* - **15**
  - Si aprirà la pagina **Robot Model Pick Cam**
````
````{seealso}
Procedi alla [Calibrazione Robot](robotpick) per completare la configurazione.
````

