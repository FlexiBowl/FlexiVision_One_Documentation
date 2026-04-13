# **Manuale FlexiVision One**

## **Benvenuto nel manuale di FlexiVision One!**  
Siamo entusiasti di darvi il benvenuto alla vostra nuova guida di FlexiVision One!
Questo manuale è stato creato appositamente per essere il vostro punto di riferimento chiaro e affidabile. Ci auguriamo che, consultandolo, possiate godere appieno di tutti i benefici del nostro sistema.
Il vostro parere è fondamentale per noi: non esitate a fornirci il vostro feedback [contattandoci](https://www.flexibowl.it/contatti)! 

*- Il Team di Ars Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Cosa è FlexiVision One?**  
FlexiVision One è la nostra soluzione di visione basata su VisionController, pensata per guidare il robot e disponibile come componente aggiuntivo per i sistemi FlexiBowl®.
Mantenendo tutte le potenti funzionalità della versione precedente, permettendo quindi lo scarico, la separazione, il riconoscimento e il prelievo dei pezzi sfusi sulla superficie dell’alimentatore, FlexiVision One rivoluziona l'esperienza utente.
Grazie a una guida passo passo completa e a strumenti intuitivi, abbiamo estremamente semplificato il processo, rendendo la programmazione e l'utilizzo accessibili e utilizzabili da chiunque, indipendentemente dal livello di esperienza.

## **Panoramica del sistema** 
Schema esemplificativo del sistema con collegamenti fino a tre FlexiBowl, tre camere e tre tramogge.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Schema esemplificativo del sistema FlexiVision One
```
## **Come leggere il manuale**  
Questo manuale è stato concepito per supportare sia la fase di progettazione e integrazione di sistema, sia la fase di installazione e messa in servizio in campo. 
Per questo motivo, è diviso in delle macro-sezioni con destinatari e finalità distinte.
  
## **Qual è la sezione che stai cercando?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Se devi...
  - L'informazione si trova in...

* - Verificare dimensioni, pesi, requisiti elettrici e protocolli di comunicazione
  - [**RIFERIMENTO TECNICO E SPECIFICHE**](specifiche_tecniche)

* - Installare i componenti, cablare il sistema, configurare la rete o calibrare camera/robot
  - [**INSTALLAZIONE DEL SISTEMA**](Installazione_Meccanica) e [**QUICKSTART**](quickstart)

* - Programmare un nuovo modello pezzo o configurare il sistema di alimentazione
  - [**QUICKSTART**](quickstart)

* - Risolvere problemi o richiedere assistenza
  - [**TROUBLESHOOTING**](troubleshooting) e [**SUPPORT**](support)
```
## **Gruppi di intervento e responsabilità**

La corretta implementazione di FlexiVision One richiede la collaborazione di diverse figure professionali. Questa tabella chiarisce ruoli e responsabilità:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Figura professionale
  - Responsabilità principali
  - Sezioni del manuale di riferimento

* - **Integratore di sistema**
  - Progettazione layout, dimensionamento componenti, verifica requisiti tecnici
  - Riferimento tecnico e specifiche, Opzioni

* - **Tecnico installatore**
  - Montaggio meccanico, cablaggio elettrico, configurazione rete
  - Installazione del sistema, Cablaggio e connessioni

* - **Programmatore robot**
  - Calibrazione camera-robot, integrazione plugin, programmazione logiche di prelievo
  - Quickstart, Protocol Setup, Calibrazione

* - **Operatore di linea**
  - Creazione nuovi modelli pezzo, configurazione parametri FlexiBowl, monitoraggio prestazioni
  - Verifica risultati Run Time

* - **Manutentore**
  - Diagnosi problemi, sostituzione componenti, aggiornamenti software
  - Nuovo modello, Configurazione FlexiBowl, Troubleshooting, Support
```

## **Convenzioni e simboli utilizzati**

In tutto il manuale vengono utilizzati banner informativi per evidenziare contenuti importanti:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Tipo
  - Significato

* - ```{warning}
    Avvertenza
    ```
  - Indica una situazione potenzialmente pericolosa o una procedura critica che, se non eseguita correttamente, potrebbe provocare danni all'apparecchiatura o malfunzionamenti gravi del sistema.

* - ```{important}
    Importante
    ```
  - Evidenzia informazioni fondamentali che non devono essere ignorate per garantire il corretto funzionamento del sistema o la sicurezza dell'operazione.

* - ```{note}
    Nota informativa
    ```
  - Fornisce informazioni essenziali per il corretto svolgimento della procedura, chiarimenti tecnici o rimandi a capitoli correlati.

* - ```{tip}
    Suggerimento
    ```
  - Suggerisce una pratica ottimale, un'alternativa o un consiglio che può semplificare l'installazione o migliorare le prestazioni del sistema.

* - ```{error}
    Errore
    ```
  - Indica un errore critico o una condizione di guasto che richiede intervento immediato. Segnala situazioni che compromettono il funzionamento del sistema e richiedono azione correttiva.
```







```{toctree}
:hidden:
:caption: PRIMA DI INIZIARE 

FlexiVisionEasy_manual/01_informazioni_preliminari.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/02_informazioni_sicurezza.md
```  
```{toctree}
:hidden:
FlexiVisionEasy_manual/03_Unboxing_Contenuto.md
```    
```{toctree} 
:hidden:
FlexiVisionEasy_manual/27_Support.md

```
```{toctree} 
:hidden:
FlexiVisionEasy_manual/27b_Glossario.md

```

```{toctree}
:hidden:
:caption: RIFERIMENTO TECNICO E SPECIFICHE 

FlexiVisionEasy_manual/rif_tecnico_specifiche/04_Specifiche_FlexiVision.md
```    

```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md
```   

```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md
```    
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/integrazione_software/06_PlugIn.md
```    
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/integrazione_software/07_Backup_management.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/08_Opzioni.md
```   
```{toctree}
:hidden:
:caption: INSTALLAZIONE DEL SISTEMA

FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md
```     
  
```{toctree}
:hidden:
:caption: QUICKSTART

FlexiVisionEasy_manual/QUICKSTART/12_Panoramica_Interfaccia.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/SETUP/13_setup.md
``` 


```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/24_Verifica_Risultati.md
```

```{toctree}
:hidden:
:caption: APPLICAZIONI MIX

FlexiVisionEasy_manual/APPLICAZIONI_MIX/28_Panoramica_Mix.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/APPLICAZIONI_MIX/29_Comandi_Mix.md
```  

```{toctree}
:hidden:
:caption: CONFIGURAZIONI MULTI-DISPOSITIVO

FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/30_2FB2CAM.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/31_3FB3CAM.md
```  


```{toctree}  
:hidden:
:caption: GARANZIA 

FlexiVisionEasy_manual/25_Garanzia.md
```

```{toctree}  
:hidden:
:caption: TROUBLESHOOTING

FlexiVisionEasy_manual/TROUBLESHOOTING/26_trb_shooting_guide.md
```






