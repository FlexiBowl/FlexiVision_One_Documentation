# **Pagina DashBoard**
L’interfaccia di FlexiVision One è strutturata in sezioni funzionali che guidano l’utente dalla configurazione iniziale alla gestione operativa del sistema.
Ogni pagina fornisce informazioni in tempo reale su stato macchina, connessioni, prestazioni e parametri di processo, con accesso diretto alle funzioni principali.
La navigazione è progettata per garantire semplicità d’uso, controllo immediato delle operazioni e monitoraggio continuo delle performance di visione, alimentazione e robot.


<img src="../../../../_shared/media/images/pagina_dashboardW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_dashboardB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Descrizione Pagina Dashboard
:header-rows: 1
:widths: 10 90

* - **#**
  - **Descrizione**

* - 1
  - **Area Visione e Rilevamento**
    * **Detected vision parts con grafico**: quanti componenti sono stati rilevati nell'immagine corrente e l'andamento nel tempo (30s).
    

* - 2
  - **Stato Operativo**
    * **In run**: indicatore luminoso che segnala se il sistema è in funzione o fermo.
    * **In run time**: cronometro che indica il tempo totale di attività del sistema.

* - 3
  - **Controlli e Selezione**
    * **Menù tendina FlexiBowl®**: permette di selezionare il dispositivo FlexiBowl® su cui si intende operare.
    * **Test Locator**: avvia movimentazioni cicliche di FlexiBowl® e tramoggia finché ci sono componenti nell'area di visione.

* - 4
  - **Stato Connessioni**
    * **FlexiBowl®**: indica lo stato della connessione in tempo reale con il FlexiBowl®.
    * **Robot**: indica lo stato della connessione in tempo reale con il robot.

* - 5
  - **Analisi Tempi di Ciclo (Timings)**
    * **Camera/Locator processing time**: tempi singoli di scatto immagine e riconoscimento componenti.
    * **Total vision processing Time**: somma dei tempi di camera e locator.
    * **Total FlexiBowl® / Robot time**: tempo per una sequenza di movimento FB e per un singolo pick & place del robot.
    * **Total processing time**: tempo totale del processo (Visione + FB + Robot).
    * **Fill hopper**: storico degli scarichi effettuati dalla tramoggia sul disco del FlexiBowl®.
    * **Vision - FlexiBowl® - Robot**: grafico comparativo delle tre funzioni per capire l'impatto di ogni singolo processo sul tempo totale.
* - 6
  - **Grafici di Performance e Storico**
    * **Elenco modelli rilevati**: tabella con coordinate (**X**, **Y**), rotazione (**Rot**) del componente e lo **Score** (grado di similarità dell'oggetto riconosciuto rispetto al modello di riferimento).
    * **Parts per minute**: grafico della media dei componenti prelevati al minuto.
```