# **Account Setup**

Auf der Seite **Account Setup** werden die Benutzerkonten von FlexiVision One angelegt und gelöscht. Jedem Konto wird eine **Zugriffsstufe** zugewiesen, die festlegt, welche Softwarefunktionen es nutzen kann.

```{note}
Die Kontoverwaltung ist Benutzern der Stufe **5** (**Engineer**) vorbehalten.
```

---

(accesso-alla-configurazione-account)=
## Zugriff auf die Kontokonfiguration

:::{list-table}
:widths: 10 90

* - **1**
  - Die Seite **Setup** öffnen.
* - **2**
  - Im Dropdown-Menü **Name** den Eintrag **Engineer** auswählen.
* - **3**
  - Im Feld **Password** `3` eingeben.
* - **4**
  - Auf **Login** klicken und die Meldung zur erfolgreichen Anmeldung mit **OK** bestätigen.
* - **5**
  - Auf das Symbol **Account Setup** klicken.
:::

```{note}
Die Anmeldung wird erst nach dem Klicken auf **Login** wirksam. Der aktive Benutzer und seine Stufe werden unter **Current User Name** angezeigt.
```

---

## Übersicht über die Benutzeroberfläche Account Setup

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Bereich
  - Beschreibung
* - **Kontoliste** (links)
  - Zeigt die vorhandenen Konten an. Mit **Delete Account** wird das ausgewählte Konto gelöscht.
* - **Neues Konto** (rechts)
  - Felder **Account Name**, **Account Password**, **Account Level** und Schaltfläche **Create Account**.
:::

---

## Neues Konto anlegen

### *Schritt 1: Dateneingabe*

:::{list-table}
:widths: 10 90

* - **6**
  - Im Feld **Account Name** den Namen des neuen Kontos eingeben.
* - **7**
  - Im Feld **Account Password** das Passwort des neuen Kontos eingeben.
* - **8**
  - Im Feld **Account Level** die Zugriffsstufe von `1` bis `5` eingeben (siehe [Zugriffsstufen](#livelli-di-accesso)).
* - **9**
  - Auf **Create Account** klicken. Das neue Konto erscheint in der Liste links.
:::

### *Schritt 2: Anmeldung mit dem neuen Konto*

:::{list-table}
:widths: 10 90

* - **10**
  - Zur Seite **Setup** zurückkehren und das neue Konto im Dropdown-Menü **Name** auswählen.
* - **11**
  - Das Passwort eingeben und auf **Login** klicken.
:::

Das Video zeigt das Anlegen eines Kontos der Stufe 3, die Anmeldung mit dem neuen Konto und die Meldungen, die bei unzureichender Stufe angezeigt werden.

:::{video} ../../../../../_shared/media/videos/new_account.mp4
     :width: 100%
     :align: center
:::

---

## Konto löschen

Die Schritte 1 bis 5 unter [Zugriff auf die Kontokonfiguration](#accesso-alla-configurazione-account) ausführen und anschließend wie folgt vorgehen.

:::{list-table}
:widths: 10 90

* - **6**
  - In der Liste links das zu löschende Konto auswählen.
* - **7**
  - Auf **Delete Account** klicken. Das Konto wird aus der Liste und aus dem Dropdown-Menü der Seite **Setup** entfernt.
:::

```{important}
Die vordefinierten Konten **Operator**, **Technician** und **Engineer** können nicht gelöscht werden.
```

```{warning}
Das Löschen erfolgt sofort und ohne Sicherheitsabfrage. Vor dem Klicken auf **Delete Account** das ausgewählte Konto überprüfen.
```

:::{video} ../../../../../_shared/media/videos/delete_account.mp4
     :width: 100%
     :align: center
:::

---

(livelli-di-accesso)=
## Zugriffsstufen

FlexiVision One verfügt über drei vordefinierte Profile. Ein vom Benutzer angelegtes Konto erhält die Berechtigungen der zugewiesenen Stufe.

:::{list-table}
:header-rows: 1
:widths: 20 20 60

* - Stufe
  - Profil
  - Verwendung
* - 1 – 3
  - **Operator**
  - Grundfunktionen: Aufrufen der Seite Home, Laden von Rezepten und Backup.
* - 4
  - **Technician**
  - Funktionen von Operator sowie Test, Rezeptverwaltung, Einrichtung der Anlage und Softwarelizenz.
* - 5
  - **Engineer**
  - Funktionen von Technician sowie **Protocol Setup** und **Account Setup**.
:::

### *Freigegebene Funktionen je Profil*

:::{list-table}
:header-rows: 1
:widths: 16 33 17 17 17

* - Seite
  - Funktion
  - Operator (1 – 3)
  - Technician (4)
  - Engineer (5)
* - Home
  - Contact Us
  - Ja
  - Ja
  - Ja
* - Home
  - Documentation
  - Ja
  - Ja
  - Ja
* - Home
  - Quick Start
  - Ja
  - Ja
  - Ja
* - Dashboard
  - Test
  - —
  - Ja
  - Ja
* - Recipes
  - Load Recipe
  - Ja
  - Ja
  - Ja
* - Recipes
  - Backup
  - Ja
  - Ja
  - Ja
* - Recipes
  - Import Backup
  - —
  - Ja
  - Ja
* - Recipes
  - New Recipe
  - —
  - Ja
  - Ja
* - Recipes
  - Save Recipe
  - —
  - Ja
  - Ja
* - Recipes
  - Edit Recipe
  - —
  - Ja
  - Ja
* - Recipes
  - Delete Recipe
  - —
  - Ja
  - Ja
* - Setup
  - Camera Setup
  - —
  - Ja
  - Ja
* - Setup
  - FlexiBowl® Setup
  - —
  - Ja
  - Ja
* - Setup
  - Hopper Setup
  - —
  - Ja
  - Ja
* - Setup
  - Robot Setup
  - —
  - Ja
  - Ja
* - Setup
  - License Software
  - —
  - Ja
  - Ja
* - Setup
  - Protocol Setup
  - —
  - —
  - Ja
* - Setup
  - Account Setup
  - —
  - —
  - Ja
* - Allgemein
  - Schließen der Anwendung
  - —
  - Ja
  - Ja
:::

Wird versucht, eine nicht freigegebene Funktion zu nutzen, erscheint die Meldung **Insufficient Access Level** mit der erforderlichen Stufe und der Stufe des aktiven Benutzers.

### *Automatische Abmeldung*

- **Technician**: automatische Abmeldung nach 5 Minuten.
- **Engineer**: keine automatische Abmeldung.

```{tip}
Jedem Benutzer die niedrigste für seine Aufgaben ausreichende Stufe zuweisen, um versehentliche Änderungen an Rezepten und Konfigurationen zu vermeiden.
```
