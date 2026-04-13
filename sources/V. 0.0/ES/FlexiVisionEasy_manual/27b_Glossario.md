# **Glossario** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Termine
  - Definizione
* - **Accept Threshold**
  - Soglia minima di similitudine (score 0.0–1.0) affinché un oggetto rilevato venga accettato dal pattern matching. Valori tipici: 0.70–0.90.
* - **Air-blow**
  - Modulo pneumatico opzionale per la separazione dei componenti sul disco tramite getti d'aria compressa. Richiede alimentazione a 5–6 bar.
* - **Artefatto**
  - Difetto nell'immagine acquisita causato da interferenze elettromagnetiche, problemi di cablaggio o malfunzionamenti del sensore.
* - **Calibrazione Camera**
  - Correlazione pixel/coordinate reali tramite target di calibrazione con pattern noto. Calcola i parametri intrinseci ed estrinseci della camera.
* - **Clearance**
  - Analisi della distribuzione dei livelli di grigio su un'area definita. Utilizzato per rilevare presenza/assenza di oggetti (controllo pinza, area libera).
* - **Camera POE**
  - Camera industriale alimentata e connessa tramite unico cavo Ethernet. Standard: IEEE 802.3af (15.4W) o 802.3at (30W).
* - **CAPTURE**
  - Comando software per acquisire le immagini di riferimento del disco vuoto e pieno, necessarie al calcolo automatico delle soglie della tramoggia.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Categorie geometriche dei componenti nel FlexiBowl Wizard. *FLAT*: forme piatte (rondelle, guarnizioni). *CYLINDRICAL*: forme cilindriche (perni, viti). *COMPLEX*: geometrie irregolari o asimmetriche.
* - **Distanza di Lavoro**
  - Distanza ottimale tra lente e superficie del disco. Tipicamente 950–1000mm nelle configurazioni standard.
* - **Distorsione Ottica**
  - Deformazione geometrica dell'immagine dovuta alla lente. Compensata automaticamente durante la calibrazione camera.
* - **Esposizione**
  - Tempo di raccolta luce del sensore camera. Misurato in μs o ms; influenza direttamente la qualità dell'immagine in produzione.
* - **Feature Threshold**
  - Soglia di estrazione delle caratteristiche (bordi, linee) durante il training del modello. Valori tipici: 0.3–0.8.
* - **FlexiBowl**
  - Sistema di alimentazione a disco rotante vibrante per il posizionamento e orientamento casuale dei componenti ai fini del prelievo robotico.
* - **FlexiBowl Wizard**
  - Procedura guidata per il calcolo automatico dei parametri ottimali del FlexiBowl in base alla geometria e al comportamento dei componenti.
* - **Flip**
  - Impulso pneumatico sotto il disco per riposizionare i componenti. Configurabile tramite *Flip Count* (numero di impulsi) e *Flip Delay* (intervallo in ms tra impulsi).
* - **Grab Train Image**
  - Comando software per acquisire l'immagine da usare nel training di un nuovo modello.
* - **Gripper Offset**
  - Vettore di correzione (ΔX, ΔY, ΔRZ) che compensa lo scostamento tra il centro ottico del sistema di visione e il TCP del gripper.
* - **Hotspot**
  - Zona di riflesso diretta della luce nell'immagine. Appare come area sovraesposta e può compromettere il riconoscimento.
* - **Lente**
  - Componente ottico della camera. Deve essere avvitata a contatto metal-metal; la focale (es. 16mm, 25mm) determina il campo visivo alla distanza di lavoro.
* - **Model (Modello)**
  - Template geometrico del componente creato in fase di training. Ogni ricetta supporta fino a 8 modelli.
* - **Origine Modello**
  - Punto di riferimento sul componente usato come centro del sistema di coordinate per il calcolo delle posizioni. Corrisponde tipicamente al TCP di presa.
* - **Ortogonalità**
  - Perpendicolarità della camera rispetto al disco (tolleranza ±1°). Verificabile con livella di precisione.
* - **Pattern Matching**
  - Algoritmo che localizza i componenti nell'immagine confrontandoli con il modello di riferimento registrato in fase di training.
* - **Protocol (Protocollo)**
  - Formato di comunicazione tra VisionController e robot. Definisce struttura dei messaggi, ordine delle coordinate e unità di misura.
* - **Recipe (Ricetta)**
  - File XML contenente tutti i parametri di configurazione del sistema: modelli, soglie, calibrazioni, setup FlexiBowl e robot.
* - **Region Search**
  - Area rettangolare nell'immagine entro cui il pattern matching esegue la ricerca. Riduce i tempi di elaborazione e aumenta la precisione.
* - **ROI (Region of Interest)**
  - Area rettangolare che delimita il componente nell'immagine durante il training del modello.
* - **RZ / Rotation Z**
  - Angolo di rotazione attorno all'asse Z comunicato al robot per l'orientamento del componente. Espresso in gradi (0–360°).
* - **Score**
  - Indice di similitudine (0.0–1.0) tra il modello e l'oggetto rilevato. Determina la confidenza del riconoscimento.
* - **Simulatori Ingombro Pinza**
  - Oggetti fisici posizionati attorno al componente durante il training per escludere dal modello le aree occupate dalla pinza in fase di prelievo.
* - **Steps**
  - Numero di cicli di vibrazione della tramoggia necessari affinché i componenti raggiungano l'area di prelievo. Parametro critico per la sincronizzazione con il ciclo robot.
* - **Subnet**
  - FlexiBowl e VisionController devono condividere la stessa subnet (es. 192.168.1.x) per la comunicazione TCP/IP.
* - **Synchronize Parameters**
  - Comando software che trasferisce i parametri dal VisionController al FlexiBowl. Obbligatorio dopo ogni modifica per rendere effettive le impostazioni.
* - **Target di Calibrazione**
  - Pattern geometrico stampato (cerchi o scacchiera) con dimensioni note e superficie piana, usato per la calibrazione camera.
* - **Timeout**
  - Tempo massimo di attesa per una risposta in comunicazione. Al superamento viene generato un errore.
* - **Tilt**
  - Inclinazione della camera rispetto al piano orizzontale. Valore ammesso: 0° ± 1°.
* - **Toplight**
  - Illuminatore LED posizionato sopra il disco che garantisce illuminazione uniforme dall'alto. Alimentazione: 24V DC.
* - **Training**
  - Processo di creazione del modello di riconoscimento tramite selezione delle caratteristiche distintive del componente da un'immagine di riferimento.
* - **Trigger**
  - Segnale di avvio dell'acquisizione immagine. Può essere software (temporizzato) o hardware (segnale elettrico esterno).
* - **Vision Result**
  - Output del sistema di visione: coordinate (X, Y, RZ) e score del componente rilevato, trasmesso al robot per il prelievo.
* - **VisionController**
  - Computer industriale che esegue FlexiVision One, gestisce le camere, elabora le immagini e comunica con FlexiBowl e robot.
```

