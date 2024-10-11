# ods-utils-py
Mit `ods-utils-py` lässt sich direkt aus Python auf die Automation API von Opendatasoft zugreifen. Voraussetzung ist der Besitz eines gültigen API Schlüssels ([API-Schlüssel erstellen](#api-schlüssel-einrichten)).


## Inhaltsverzeichnis

   - [Installation](#installation)
   - [Voraussetzungen](#voraussetzungen)
   - [Erste Schritte](#erste-schritte)
     - [API-Schlüssel einrichten](#api-schlüssel-einrichten)
   - [Verwendung](#verwendung)
   - [Weiterführende Links](#weiterführende-links)
   - [Lizenz](#lizenz)

---

## Installation

Installation via `pip`:

```bash
pip install ods-utils-py
```

---

## Voraussetzungen

- **Python Version:** 3.11 oder höher
- **API-Schlüssel:** Ein gültiger API-Schlüssel von Opendatasoft

---

## Erste Schritte

### API-Schlüssel einrichten

Um `ods-utils-py` nutzen zu können, wird ein gültiger API-Key von Opendatasoft benötigt. 

[Für die OGD Basel kann der API Key hier erstellt werden](https://data.bs.ch/account/api-keys/).

Für die Key-Erstellung auf anderen Plattformen kann oben rechts auf die Schaltfläche mit dem Benutzernamen geklickt werden, um die Kontoeinstellungen zu öffnen. Unter API-Keys können benutzerdefinierte Keys mit den entsprechenden Berechtigungen erstellt werden. 

Der Name sollte beschreiben wofür er verwendet wird, beispielsweise `"ods_utils_py - <Initialer Name des Keys>"`

Der API Key benötigt die folgenden 4 Berechtigungen:
- Alle Datensätze durchsuchen
- Neue Datensätze erstellen
- Alle Datensätze bearbeiten
- Eigene Datensätze veröffentlichen

Der API Key wird nun als Umgebungsvariable benötigt.

### Umgebungsvariablen einrichten
   Die [`.env.template`](.env.template) Datei kopieren und in `.env` umbenennen:
   - **Windows**
     ```cmd
     copy .env.template .env
     ```
   - **Mac/Linux**
     ```bash
     cp .env.template .env
     ```
   Anschliessend die `.env` Datei öffnen und mit den erforderlichen Zugangsdaten und Informationen ausfüllen.

## Verwendung

Hier ein einfaches Beispiel, um die Anzahl der Datensätze abzurufen:

```python
import ods_utils_py as ods_utils

num_datasets = ods_utils.get_number_of_datasets()
print(f"Derzeit haben wir {num_datasets} Datensätze.")
```

Falls eine gewünschte Funktion nicht existiert, kann sie über _requests_utils implementiert werden:

```python
import ods_utils_py as ods_utils

antwort = ods_utils.requests_get("https://www.example.com")
print(antwort.text)
```

*Hinweis:* Die meisten dieser Funktionen sollen dann langfristig in `ods_utils_py` integriert werden.

---

## Weiterführende Links
Die vollständige Dokumentation der Automation API 1.0 ist [hier](https://help.opendatasoft.com/apis/ods-automation-v1/) zu finden.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei im Repository für den vollständigen Lizenztext.
