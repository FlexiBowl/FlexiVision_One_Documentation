# **Sicherheitsinformationen**

Die folgenden Sicherheitsanweisungen, allgemeinen Vorsichtsmaßnahmen und Vorschriften zur Handhabung und zur Betriebsumgebung müssen strikt eingehalten werden, um die Sicherheit des Personals, die Integrität des Produkts und den ordnungsgemäßen Betrieb der Anlage zu gewährleisten.

```{warning}
**Verantwortung des Benutzers**

Die Einhaltung aller in diesem Abschnitt aufgeführten Sicherheitsvorschriften ist verpflichtend und liegt in der Verantwortung des Endanwenders. Eine Nichtbeachtung kann zu Personenschäden, Schäden an Geräten oder zur Beeinträchtigung des Systembetriebs führen.
```

---

## Betriebssicherheit

### Integration mit Robotersystemen

#### **Sicherheitsanforderungen der Zelle**

```{warning}
FlexiVision One arbeitet in enger Verbindung mit Robotersystemen von Drittanbietern. Der Benutzer muss sicherstellen, dass der Arbeitsbereich mit allen erforderlichen Sicherheitsmaßnahmen ausgestattet ist, die durch die einschlägigen Vorschriften vorgeschrieben sind
```
#### **Aufmerksamkeit während des Betriebs**

```{warning}

Während des Systembetriebs ist stets Folgendes zu berücksichtigen:

- Physische Abmessungen von Roboter und FlexiBowl
- Bahnen und Geschwindigkeiten der Roboterbewegungen
- Mögliche unvorhergesehene Situationen (herabfallende Teile, Entnahmefehler)
- Gefahrenbereiche während der Vibrationsphasen des FlexiBowl
```

### Allgemeine Vorsichtsmaßnahmen vor Eingriffen

#### **Trennen der Versorgungen**

```{warning}
Vor der Durchführung von Wartungs-, Änderungs- oder Inspektionsarbeiten am System ist stets sicherzustellen, dass:

- Alle elektrischen Versorgungsquellen getrennt sind (VisionController, FlexiBowl, Kamera, Beleuchtung)
- Die pneumatische Versorgung entlüftet und getrennt ist (falls vorhanden)
- Die Verbindungskabel physisch abgezogen sind
- Der Roboter sich im Sicherheitsmodus befindet oder vollständig ausgeschaltet ist
```
#### **Sicherheitsverfahren**

```{warning}

Verlassen Sie sich nicht ausschließlich auf Schalter: Verwenden Sie Lockout/Tagout-Verfahren (LOTO), sofern verfügbar.
```

### Änderungen und Manipulationen

#### **Verbot nicht autorisierter Änderungen**

```{warning}
Verändern Sie das Produkt oder seine Komponenten niemals ohne ausdrückliche schriftliche Genehmigung von ARS S.r.l.
```
#### **Folgen von Änderungen**

```{warning}
Nicht autorisierte Änderungen können:

- Systemstörungen verursachen
- Die Garantie ungültig machen
- Risiken von Verletzungen, Stromschlägen oder Bränden verursachen
- Die Sicherheitszertifizierungen des Produkts beeinträchtigen
```

---

## Umgebungsbedingungen und Schutz

### Schutz vor Flüssigkeiten

#### **Risiko des Kontakts mit Flüssigkeiten**

```{warning}

Verwenden Sie das Produkt nicht in Umgebungen, in denen der VisionController, die Kamera oder andere elektronische Komponenten mit Folgendem in Kontakt kommen können:

- Wassertropfen oder Spritzwasser
- Öle, Schmierstoffe oder andere industrielle Flüssigkeiten
- Kondensat oder übermäßige Feuchtigkeit
- Leitfähige Stäube
```
#### **Lösungen für kritische Umgebungen**

```{note}

Wenn das System in Umgebungen mit Flüssigkeiten betrieben werden muss, sind geeignete Schutzmaßnahmen (Gehäuse IP65 oder höher) vorzusehen und der technische Service von ARS für kundenspezifische Lösungen zu konsultieren.
```

### Betriebstemperaturen

#### **Heiße Oberflächen - Maximale Temperaturen**

```{warning}
Bei intensiver Nutzung oder in warmen Umgebungen können einige Systemkomponenten hohe Temperaturen erreichen:

- VisionController: bis zu 50°C an den Außenflächen
- LED-Beleuchtung: bis zu 40°C an der Frontfläche
- Industriekamera: bis zu 50°C am Metallgehäuse
```
#### **Verantwortung des Kunden**

```{warning}
Es liegt in der Verantwortung des Kunden:

- Thermische Risiken in der eigenen Risikobewertung zu dokumentieren
- Das Personal in Verfahren zur Vermeidung unbeabsichtigter Berührungen zu unterweisen
- Warnbeschilderung vorzusehen, wo erforderlich
- Eine ausreichende Belüftung der Komponenten sicherzustellen
```

### Umgebungsbedingungen für Installation und Lagerung

#### **Umgebungsanforderungen - Referenztabelle**

```{note}

Um Lebensdauer und Zuverlässigkeit zu gewährleisten, müssen VisionController und Kamera unter den folgenden Bedingungen verwendet und gelagert werden:

| Parameter | Betriebsbedingungen | Lagerbedingungen |
|-----------|---------------------|--------------------------|
| **Temperatur** | +1°C ÷ +50°C | -20°C ÷ +65°C |
| **Relative Luftfeuchtigkeit** | <90% (ohne Kondensation) | <90% (ohne Kondensation) |


```
#### **Zusätzliche Vorsichtsmaßnahmen für die Umgebung**

```{note}
Zur Erhaltung der Integrität der Komponenten:

- Direkte Sonneneinstrahlung vermeiden
- Während der Lagerung vor übermäßigen Vibrationen schützen
- In trockener Umgebung ohne aggressive Stäube aufbewahren
- Die Kamera ist empfindlich gegenüber mechanischen Stößen: vorsichtig handhaben
```

---

## Transport und Handhabung

### Empfang und Inspektion

#### **Inspektion bei Ankunft**

```{note}
Beim Empfang des Produkts, vor dem Unterzeichnen des Lieferscheins:

1. **Äußere Inspektion der Verpackung**: Die Integrität des Kartons und der Außenverpackung prüfen. Auf mögliche Anzeichen von Stößen, Quetschungen oder Nässe achten.

2. **Inhaltsprüfung**: Den Inhalt mit dem Lieferschein vergleichen. Prüfen, ob alle bestellten Komponenten vorhanden sind.
```

#### **Bei Schäden oder Abweichungen**

```{note}
Wenn Probleme festgestellt werden:

- Die Empfangsbestätigung NICHT als "konform" unterschreiben
- Schäden auf dem Transportdokument vermerken
- Sichtbare Schäden fotografieren
- Umgehend den ARS-Kundendienst kontaktieren: 
    [service@arsautomation.com](mailto:service@arsautomation.com) 
    [us.service@arsautomation.com](mailto:us.service@arsautomation.com), wenn die Kontaktaufnahme aus Amerika erfolgt
```

### Handhabung und Lagerung
Zur Vermeidung von Schäden während Transport und Lagerung:

#### **Transport**

```{tip}
**Während des Transports:**
- Die Verpackung stets in aufrechter Position handhaben (die Pfeile "OBEN" auf der Verpackung beachten)
- Die Verpackung nicht fallen lassen oder Stößen aussetzen
- Dem Gewicht entsprechende Wagen oder Hubwagen verwenden
- Plötzliche Temperaturschwankungen vermeiden
```
#### **Lagerung**

```{tip}
**Während der Lagerung:**
- An einem trockenen und überdachten Ort aufbewahren
- Keine weiteren Lasten auf der Verpackung stapeln
- Nicht auf die Verpackung steigen oder sich darauf abstützen
- Die in der vorherigen Tabelle angegebenen Umgebungsbedingungen einhalten
```
#### **Auspacken**

```{tip}
**Während des Auspackens:**
- Vorsichtig öffnen, um die internen Komponenten nicht zu beschädigen
- Die Originalverpackung für eventuelle Rücksendungen oder zukünftige Transporte aufbewahren
- Prüfen, ob alle Zubehörteile und die Dokumentation vorhanden sind
```

---

## Entsorgung und Lebensende

### **Verantwortungsvolle Entsorgung**

```{warning}

Wenn das Produkt das Ende seines Lebenszyklus erreicht, muss es gemäß den geltenden Vorschriften für Elektro- und Elektronik-Altgeräte (RAEE/WEEE) entsorgt werden.
```
### **Komponenten mit Sonderentsorgung**

```{note}
**Komponenten mit Sonderentsorgung:**
- Elektronische Platinen (VisionController): RAEE Kategorie 6
- Industriekamera: RAEE Kategorie 6
- LED-Beleuchtungen: RAEE Kategorie 5
- Kabel und Steckverbinder: Entsorgung mit elektrischen Materialien
```
---


