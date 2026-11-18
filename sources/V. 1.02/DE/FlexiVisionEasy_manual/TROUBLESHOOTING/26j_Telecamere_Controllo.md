(troubleshooting_telecamere_controllo)=
# **Kontrollkameras**

```{important}
**Expert-Funktion**

Die Verwaltung der Kontrollkameras (**Control Camera**) ist eine **Expert**-Funktion: Sie erfordert Kenntnisse in Cognex VisionPro und C#-Skripten und richtet sich an erfahrene Anwender. Informationen zum Expert-Modus finden Sie unter [Worum es sich handelt und wann es benötigt wird](../EXPERT/32_Expert.md).
```

```{note}
Diese Seite betrifft den Befehl `start_control_` und die VisionPro-Skripte (verfügbar ab Softwareversion v0.24). Das vollständige Verfahren finden Sie unter [Kontrollkameras](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) und [Befehl `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md).
```

## Antworten und Fehlermeldungen

Fehler im Zusammenhang mit dem Kontrollskript beginnen mit `#Error_Control_`. Der Fall `Not_Found` **ist kein Softwarefehler**: Er bedeutet, dass der Locator kein Objekt erkannt hat. Kamerafehler können separat mit dem Präfix `#Error_Camera` gemeldet werden.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Antwort
  - Bedeutung / empfohlene Maßnahme
* - `Not_Found`
  - Prüfung ohne Erkennung abgeschlossen: Teil, Bild und Modell prüfen.
* - `#Error_Control_INVALID_CONTROL`
  - Der Parameter wird vom Skript nicht verarbeitet: Text nach `start_control_` prüfen.
* - `#Error_Control_TOOL_NOT_FOUND`
  - Eines der erwarteten Tools ist nicht vorhanden oder hat einen anderen Namen.
* - `#Error_Control_LAST_RECORD_NULL`
  - Der Datensatz der letzten Ausführung des Tools ist nicht verfügbar.
* - `#Error_Control_INPUT_IMAGE_RECORD_NULL`
  - Der Unterdatensatz `InputImage` ist nicht verfügbar.
* - `#Error_Control_RECORD_WITHOUT_IMAGE`
  - Der ausgewählte Datensatz enthält kein gültiges Bild.
* - `#Error_Control_VISIONPRO_JOB`
  - Die Ausführung der VisionPro-Aufgabe hat einen Fehler erzeugt.
* - `#Error_Control_EMPTY_OUTPUT`
  - Das Skript hat keine gültige Zeichenfolge zurückgegeben.
* - `#Error_Camera …`
  - Aufnahmeproblem: Verbindung und Status der Kamera prüfen.
```

```{note}
Das Beispielskript kann auch `#Error_Control_TOOL_RUN` zurückgeben, wenn die Ergebnisse eines Tools nicht verfügbar sind (zum Beispiel `#Error_Control_TOOL_RUN;Tool=2`, wenn der Fehler Tool 2 betrifft). Erzeugt mindestens ein Tool einen Ausführungsfehler, wird der Fehler an den Anfang der Antwort geschrieben.
```

## Schnellprüfungen

- Prüfen, dass der Befehl den **abschließenden Unterstrich** (`start_control_`) enthält und der Parameter keine Leerzeichen enthält.
- Prüfen, dass die Namen der Ein- und Ausgänge des ToolBlocks weiterhin `Image`, `Input_Control`, `Output_String` und `Output_Image` lauten.
- Prüfen, dass der Ausgang `Output_Image` als kompatibler `CogRecord` konfiguriert ist.
- **Test Tool** über die HMI auch ohne angeschlossenen Roboter ausführen, um das Problem von der TCP-Kommunikation zu isolieren: In diesem Fall wird das Ergebnis in der HMI angezeigt, aber nicht an den Roboter übertragen.
- Nach jeder Änderung am Skript den [schnellen Abnahmetest](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) wiederholen.
