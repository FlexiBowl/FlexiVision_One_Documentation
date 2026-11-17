# Manuale FlexiVision One 

Questa pagina raccoglie la cronologia delle revisioni del presente manuale e indica con quali versioni del software FlexiVision One ciascuna revisione è compatibile.

```{important}
Consultare sempre la versione del manuale compatibile con la versione del software installata, per accedere alle informazioni più aggiornate su funzionalità, sicurezza e procedure.
```

## Compatibilità

| Versione manuale | Versioni software FlexiVision One compatibili |
|---|---|
| **1.02** (attuale) | v0.23, v0.24 |
| **1.01** | v0.21, v0.22 |
| **1.00** | v0.20, v0.21, v0.22 |

## Cronologia delle revisioni

### Versione 1.02

Data di pubblicazione: 17/11/2026

**Pagine aggiunte**

- Nuova sezione **Telecamere di Controllo**, con le pagine:
  - [Telecamere di Controllo](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md): panoramica, sequenza di funzionamento, utilizzo dalla HMI (Setup Camera Ctrl, Setup Tool Ctrl, View Runtime, Test Tool) e prova rapida di accettazione.
  - [Comando `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md): formato del comando, parametri, risposte al robot ed esempi di scambio.
  - [Script VisionPro](../TELECAMERE_CONTROLLO/35_Script_VisionPro.md): interfaccia del ToolBlock, personalizzazione dello script e Appendice A con lo script C# completo.
- Aggiunta la pagina [Risoluzione problemi – Telecamere di Controllo](../TROUBLESHOOTING/26j_Telecamere_Controllo.md) con i messaggi `#Error_Control_…` e `#Error_Camera…` e le azioni consigliate.
- Tutte le pagine della sezione Telecamere di Controllo riportano in cima un banner che indica che la **Control Camera** è una funzione **Expert**.

**Pagine aggiornate**

- [Protocollo Comunicazione Robot-Visione](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): aggiunta la sottosezione "Comandi telecamere di controllo" con il comando `start_control_<parametro>`.
- [Risoluzione Problemi](../TROUBLESHOOTING/26_trb_shooting_guide.md): aggiunta la scheda "Telecamere di Controllo".
- [Glossario](../27b_Glossario.md): aggiunti i termini CogRecord, PMRedLine, Telecamera di Controllo, ToolBlock e VisionPro.
- Note di Rilascio – Software: aggiunte le versioni [V. 0.23](V.0.23.md) e [V. 0.24](V.0.24.md) e aggiornata la pagina [Software FlexiVision One](Release_Notes_Software.md).
- Aggiornata la tabella di compatibilità con le versioni software v0.23 e v0.24.

### Versione 1.01

Data di pubblicazione: 04/09/2026

- Aggiunta la pagina **Check Belt** (Monitoraggio Disco) nel Quickstart e la relativa voce nella pagina Setup della Panoramica Interfaccia.
- Aggiornata la sezione Hopper Setup con le procedure guidate **Wizard Steps** e **Wizard Time**.
- Aggiornata la sezione Istogrammi con la scelta della tipologia di regione per le Clearances (Rectangle, Annulus Section, Circle).
- Aggiornata la sezione Applicazioni Mix con i comandi multi-modello `mix_Locator_<modelli>` e la protezione sui comandi già in esecuzione.
- Aggiunta al Protocollo di Comunicazione Robot-Visione la sottosezione "Come usare correttamente i comandi Start e Mix".
- Aggiornata la sezione FlexiBowl® Setup: inserimento manuale dei parametri da tastiera e avviso in caso di parametri non sincronizzati.
- Aggiornata la sezione Robot Pick: formato degli offset con il punto come separatore decimale e controllo sul Picking Offset prima di proseguire con **Next**.
- Aggiunta alla sezione Setup l'indicazione sul controllo del livello di accesso utente.
- Riorganizzata la sezione Note di Rilascio, separando le note del software FlexiVision One da quelle del manuale.

### Versione 1.00

Data di pubblicazione: 01/08/2026

- Prima edizione del manuale.
