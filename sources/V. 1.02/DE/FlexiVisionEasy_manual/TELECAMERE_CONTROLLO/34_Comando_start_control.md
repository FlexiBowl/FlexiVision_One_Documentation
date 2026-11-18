(start_control)=
# **Befehl `start_control_`**

```{important}
**Expert-Funktion**

Die Verwaltung der Kontrollkameras (**Control Camera**) ist eine **Expert**-Funktion: Sie erfordert Kenntnisse in Cognex VisionPro und C#-Skripten und richtet sich an erfahrene Anwender. Informationen zum Expert-Modus finden Sie unter [Worum es sich handelt und wann es benötigt wird](../EXPERT/32_Expert.md).
```

```{note}
**Voraussetzungen**

Der Befehl `start_control_` erfordert eine konfigurierte Kontrollkamera und ein geladenes VisionPro-Skript. Siehe [Kontrollkameras](33_Telecamere_Controllo.md). Verfügbar ab Softwareversion v0.24.
```

Mit dem Befehl `start_control_` kann der Roboter eine Sichtprüfung mit einer Kontrollkamera anfordern. Der Roboter kann einen Textparameter anhängen, den FlexiVision an das [VisionPro-Skript](35_Script_VisionPro.md) weiterleitet.

## Befehlsformat

```
start_control_<Parameter>
```

Der **abschließende Unterstrich** des Präfixes ist **zwingend erforderlich**. Der Parameter kann leer sein oder Zahlen, Buchstaben und weitere Unterstriche enthalten.

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - Vom Roboter gesendeter Befehl
  - Von VisionPro empfangener Text
  - Verhalten des Beispielskripts
* - `start_control_`
  - `""` (leer)
  - Führt beide PMRedLines aus
* - `start_control_1`
  - `"1"`
  - Führt nur PMRedLine 1 aus
* - `start_control_2`
  - `"2"`
  - Führt nur PMRedLine 2 aus
* - `start_control_ABC_123`
  - `"ABC_123"`
  - Benutzerdefinierter Parameter: erfordert eine eigene Logik im Skript
```

```{important}
Der Parameter wird als **Text** behandelt. FlexiVision misst Werten wie `ABC_123` keine Bedeutung bei: Das VisionPro-Skript des Kunden muss sie interpretieren.
```

```{note}
Auch `start_control_ 1` wird als Parameter `"1"` gelesen: Leerzeichen am Anfang und am Ende werden entfernt. Um Mehrdeutigkeiten zu vermeiden, wird empfohlen, `start_control_1` ohne Leerzeichen zu senden.

Das Präfix `start_control_` wird nicht an das Skript übergeben: Es kommt nur der darauffolgende Teil an (zum Beispiel `"2"` bei `start_control_2`).
```

Der Befehl kann auch **ohne verbundenen Roboter** über die HMI mit **Test Tool** ausgeführt werden; in diesem Fall wird das Ergebnis in der HMI angezeigt, aber nicht über TCP übertragen.

## Antwort an den Roboter

Die Antwort ist die vom VisionPro-Skript erzeugte Zeichenfolge `Output_String`. Das nachstehend gezeigte Format ist das des **Beispielskripts** und kann an das vom Roboter benötigte Protokoll angepasst werden.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Situation
  - Beispiel für Output_String
* - Objekt gefunden
  - `X=125.450;Y=78.320;Rz=45.000`
* - Kein Objekt gefunden
  - `Not_Found`
* - Beide Tools ausgeführt
  - `1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found`
* - Nicht vorgesehener Parameter
  - `#Error_Control_INVALID_CONTROL`
* - Fehler bei Tool 2
  - `#Error_Control_TOOL_RUN;Tool=2`
```

Für jedes ausgeführte Tool wird nur das **erste** erkannte Objekt verwendet. Werden beide Tools ausgeführt, werden den Antworten die Präfixe `1:` und `2:` vorangestellt und durch `|` getrennt.

```{note}
- `X` und `Y` werden im Koordinatensystem angegeben, das im VisionPro-Tool konfiguriert ist (Pixel oder kalibrierte Einheiten): Sie sind nicht automatisch in Millimetern.
- `Rz` wird in Grad angegeben.
- Drei Dezimalstellen; als Dezimaltrennzeichen wird immer der Punkt verwendet, unabhängig von der Windows-Sprache.
```

### Not_Found und Fehler

`Not_Found` **ist kein Fehler**: Es zeigt an, dass das Tool ausgeführt wurde, aber kein Objekt gefunden hat. **Fehler der Kontrollskripte** beginnen immer mit dem Präfix `#Error_Control_`; Kamerafehler können separat mit dem Präfix `#Error_Camera` gemeldet werden. Erzeugt mindestens ein Tool einen Ausführungsfehler, schreibt das Skript den Fehler an den Anfang der Antwort (im Beispiel hat Tool 1 Vorrang).

Die vollständige Liste der Meldungen und der empfohlenen Maßnahmen finden Sie unter [Fehlerbehebung – Kontrollkameras](../TROUBLESHOOTING/26j_Telecamere_Controllo.md).

## Beispiele für den Datenaustausch

**Fall A – nur Locator 2**

Vom Roboter gesendeter Befehl: `start_control_2`. VisionPro empfängt `Input_Control = "2"`, führt `CogPMRedLineTool2` aus, liest X, Y und Rz des ersten Ergebnisses und erzeugt die Textantwort. Das Display zeigt den Datensatz von Tool 2.

**Fall B – zwei Locators**

Gesendeter Befehl: `start_control_`. VisionPro empfängt eine leere Zeichenfolge und führt beide Tools aus. Die Antwort enthält zwei Abschnitte, einen pro Locator. Der Bilddatensatz stammt von Tool 1, sofern im Skript nichts anderes festgelegt ist.

**Fall C – anwendungsspezifischer Parameter**

Gesendeter Befehl: `start_control_ABC_123`. Der Parameter erreicht VisionPro, ohne von FlexiVision interpretiert zu werden. Das Beispielskript antwortet `#Error_Control_INVALID_CONTROL`; um ihn als echten Befehl zu verwenden, muss die entsprechende Logik im C#-Skript ergänzt werden.

```{tip}
Die vollständige Liste der Roboterbefehle finden Sie unter [Kommunikationsprotokoll Roboter–Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```
