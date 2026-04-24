# **Übersicht Mix-Anwendung**
Dieser Abschnitt führt das Konzept der **Mix-Anwendung** in FlexiVision One ein und erklärt, worin sie sich von einer Standardanwendung unterscheidet und wie sie auf Rezeptur- und Modellebene korrekt konfiguriert wird.

---

## Was ist eine Mix-Anwendung?

Eine **Mix-Anwendung** ist eine Anwendungskonfiguration, bei der innerhalb derselben Rezeptur Modelle für **vollständig unterschiedliche Komponenten** koexistieren.

In einer Mix-Anwendung kann der Roboter **mehrere unterschiedliche Teiletypen** erkennen und entnehmen, die gleichzeitig im Arbeitsbereich vorhanden sind, ohne die Rezeptur wechseln oder den Zyklus unterbrechen zu müssen. Das Bildverarbeitungssystem identifiziert jedes auf dem FlexiBowl® vorhandene Teil und gibt dem Roboter die Koordinaten des am besten geeigneten entnehmbaren Teils zurück, unabhängig von dessen Typ.
```{tip}
**Typisches Beispiel:** Auf dem FlexiBowl® können sich gleichzeitig Schrauben, Muttern und Unterlegscheiben befinden. Der Roboter entnimmt jedes erkannte Teil und optimiert den Durchsatz ohne Unterbrechungen.
```

---

## Standardanwendung vs Mix-Anwendung

| Merkmal | Standardanwendung | Mix-Anwendung |
|---|---|---|
| **Teiletypen** | Nur ein Teiletyp  | Mehrere vollständig unterschiedliche Teiletypen |
| **Modelle in der Rezeptur** | Alle Modelle beziehen sich auf dieselbe Komponente | Modelle können sich auch auf unterschiedliche Komponenten beziehen |
| **Roboterverhalten** | Entnimmt immer dasselbe Teil, auch an unterschiedlichen Positionen (durch Erstellung mehrerer Modelle)| Entnimmt jedes erkannte Teil, unabhängig vom Typ |
| **Softwarekonfiguration** | Kein Unterschied gegenüber dem Mix-Modus | Kein Unterschied gegenüber dem Standardmodus |
| **Modusauswahl** | Nicht erforderlich: hängt von den in die Rezeptur eingefügten Modellen ab | Nicht erforderlich: hängt von den in die Rezeptur eingefügten Modellen ab |
| **Roboterbefehle** | Familie `start_..` | Familie `mix_..` |

```{note}
Auf Softwareebene gibt es keine explizite Auswahl zwischen Standard- und Mix-Modus: Die Unterscheidung wird ausschließlich durch den **Inhalt der Rezeptur** bestimmt. Wenn sich alle vorhandenen Modelle auf dasselbe Teil (oder auf dessen verschiedene Seiten) beziehen, handelt es sich um eine Standardanwendung. Wenn sich die Modelle auf unterschiedliche Teile beziehen, handelt es sich automatisch um eine Mix-Anwendung.
```

---

## Wie wird eine Mix-Rezeptur erstellt?

Der Prozess zur Erstellung einer Mix-Rezeptur ist **identisch** mit dem einer Standardrezeptur. Es muss keine vorläufige Option ausgewählt werden. Daher kann das Verfahren [Erstellung von Rezepturen und Modellen - Übersicht](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md) befolgt werden.

Der Unterschied zeigt sich **in der Phase der Modellerstellung**:

- In einer **Standard**-Anwendung stellen alle in die Rezeptur eingefügten Modelle dieselbe Komponente dar (zum Beispiel: Seite A, Seite B, Seite C desselben Teils).
- In einer **Mix**-Anwendung stellen die eingefügten Modelle **vollständig unterschiedliche Komponenten** dar (zum Beispiel: Teil A, Teil B, Teil C — drei unterschiedliche Komponenten mit unterschiedlichen Geometrien).
```{important}
Jedes Modell innerhalb einer Mix-Rezeptur muss separat mit seinem eigenen physischen Referenzteil trainiert werden, gemäß dem Standardverfahren in [Ein neues Modell erstellen](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Clearances und Roboter-Pick-Koordinaten müssen für jede Komponente einzeln kalibriert werden.
```

---

## Nächste Schritte

Nachdem das Konzept der Mix-Anwendung verstanden und die Rezeptur mit den Modellen der verschiedenen Komponenten konfiguriert wurde, betrifft der nächste Schritt die Anpassung der **Roboterbefehle**, die für den Betrieb im Mix-Modus erforderlich sind:

**→ [Befehle der Mix-Anwendung](29_Comandi_Mix.md)**

