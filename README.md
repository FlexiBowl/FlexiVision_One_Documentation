# FlexiVision One Manual

Repository della documentazione tecnica di **FlexiVision One** basata su **Sphinx** e **MyST Markdown**.

## Struttura del progetto

- `sources`
  Cartella unica dei sorgenti del manuale.
- `sources/<versione>/<lingua>`
  Ogni coppia versione/lingua viene scoperta automaticamente dal publisher Python.
- `sources/_shared/media`
  Asset condivisi tra versioni e lingue.
- `sources/_data/footer.html`
  Footer/version selector usato durante il build.
- `build`
  Output HTML finale senza sorgenti.

## Requisiti locali

Installare le dipendenze Python elencate in `requirements.txt`.

Esempio:

```powershell
py -3 -m pip install -r requirements.txt
```

## Build

Workflow consigliato:

- `build_manual.bat`
  Converte i sorgenti in `sources` nel sito HTML finale in `build`
  Se lanciato senza argomenti apre una finestra iniziale per scegliere tra build rapido o build completo con ZIP offline, e tra build totale o mirato su una singola versione/lingua

Esempi:

```powershell
.\build_manual.bat
.\build_manual.bat --version "V. 1.0" --language IT
.\build_manual.bat --mode full
.\build_manual.bat --mode full --version "V. 1.0" --language IT
```

Per centralizzare e ottimizzare gli asset condivisi del sorgente usa direttamente lo script Python dedicato.

Esempi:

```powershell
py -3 tools/manual_publisher/optimize_media.py
py -3 tools/manual_publisher/optimize_media.py --compress-videos
```

## Setup dipendenze

Per preparare l'ambiente locale usa `installer/install_dependencies.bat`.
Lo script installa solo le dipendenze necessarie alla build nel Python locale gia' presente sulla macchina.

## Note operative

- Il progetto usa `myst_parser`, `sphinx_book_theme`, `sphinx_copybutton`, `sphinx_design` e `sphinxcontrib.video`.
- Il selettore multi-versione e multi-lingua e' generato dal publisher Python tramite `versioning-data.js` e `fix_print.js`.
- La build `full` genera il sito HTML e lo ZIP offline, ma non produce piu' il PDF completo del manuale.
- I media condivisi vengono centralizzati in `sources/_shared/media`.
- Gli output HTML gia' presenti nel repository non sono la fonte da modificare a mano.

## Licenza

Il contenuto del repository e' proprietario e riservato ad ARS Automation, come descritto in `LICENSE`.
