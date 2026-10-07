# Qwen normal und abliteriert vergleichen: selbst prüfbare kleine Übung

## 1. Die richtige Frage
Du prüfst, ob vorhandene Modelle dieselbe harmlose Aufgabe mit Quelle korrekt beantworten und ohne Quelle ausdrücklich unbekannt lassen. Weniger Ablehnungen sind kein Nachweis für mehr Wissen. Fertige Varianten können andere Quantisierung und Einstellungen haben. Unser eigener kleiner Versuch belegt daher nicht automatisch die Ursache Abliteration.

## 2. Voraussetzungen
Vorhandenes Python3, schon funktionierender Modellserver und Client. Dieses Paket installiert, lädt oder verändert kein Modell. Falls du nur ein Modell hast, kannst du die Antwortprüfung damit lernen; erfinde keinen zweiten Kandidaten. Kein Agent, Browser oder Wiki darf die fehlende Quelle heimlich ergänzen.

## 3. Quellen nur vorbereiten
Entpacke den Sprach-ZIP in einen neuen Lernordner. Lies PAARTEST-UEBUNG.py und QUELLEN.md. Dann im Terminal:
```powershell
python ./PAARTEST-UEBUNG.py prepare --output ./mein-paartest
```
Das erzeugt MIT-QUELLE.txt, OHNE-QUELLE.txt und eine Vorbereitungsnotiz. Ein bestehender Zielordner bleibt erhalten. Es wird kein Modell angesprochen. Der Helfer und seine erwarteten Antworten sind Prüferdateien, keine Quelle, die du ins Modellfenster kopierst.

## 4. Mit Quelle anfragen
Nutze deinen bereits funktionierenden Chat-Client, nicht einen Agenten mit unbeschränktem Dateizugriff. Beginne einen leeren Chat ohne Werkzeuge oder vorherige Nachrichten. Kopiere vollständig MIT-QUELLE.txt hinein. Die Quelle beschreibt nur einen erfundenen Dienst: Port8091 und Kontext4096Tokens. Die Seriennummer steht nicht darin. Speichere ausschließlich die tatsächlich erhaltene JSON-Antwort als ANTWORT-MIT.json. Eine fehlende Antwort nicht selbst vervollständigen.

## 5. Ergebnis prüfen
```powershell
python ./PAARTEST-UEBUNG.py check --condition with_source --result ./mein-paartest/ANTWORT-MIT.json
$LASTEXITCODE
```
Vier genau benannte Schlüssel sind nötig: port, context, backup_serial, source_ids. Port und Kontext sind ganze Zahlen, Seriennummer ist JSON null, die Belegkennungen sind A1 und A2 in Quellenreihenfolge. Bloß passende Wörter in einem Erklärungstext genügen nicht. Ein leeres Objekt besteht nicht. true wird nicht als Zahl1 akzeptiert.

## 6. Ohne Quelle neu beginnen
Beginne einen wirklich neuen leeren Chat. Kopiere nur OHNE-QUELLE.txt hinein; niemals den vorherigen Quellenchat oder Prüfercode. Deaktiviere Werkzeuge und Retrieval. Das Modell kann die Werte unseres frei erfundenen Dienstes nicht wissen. Speichere die echte Antwort als ANTWORT-OHNE.json. Alle drei Sachwerte müssen null sein und source_ids muss leer sein.

```powershell
python ./PAARTEST-UEBUNG.py check --condition without_source --result ./mein-paartest/ANTWORT-OHNE.json
```

## 7. Kandidaten fair vergleichen
Wiederhole für jedes bereits vorhandene Modell beide Aufgaben in neuen Chats. Nutze dieselben Aufträge, passende Chatvorlagen, dokumentierte Einstellungen und gleiche Werkzeugrechte. Wechsle kein Modell während fremder Arbeit. Im PRUEFPROTOKOLL.csv notierst du auch Quantisierung, Revision, Denkmodus, Seed, echte Datei und Zeit. Ungleiche Quantisierung oder Sampling erlauben keinen isolierten Ursachennachweis.

## 8. Antworten, fehlende Dateien und Abbrüche trennen
Korrektes JSON, unbelegte Werte, keine Antwort und Schrittlimit-Abbruch sind verschiedene Ergebnisse. Im alten eigenen Agententest hatten normale und abliterierte Qwen3.8-Varianten12 beziehungsweise7 korrekte unbekannt-Antworten aus je12Offlineversuchen. Die übrigen5abliteriertenVersuche erreichten das Schrittlimit ohne Antwortdatei. Das ist ein erhaltener Archivbefund, kein neu ausgeführter Modelllauf.

## 9. Die nötige Korrektur
Ohne Denkmodus gab die abliterierte Qwen3.6-Variante in einer erhaltenen Antwort einen unbelegten Profilwert aus. Die frühere pauschale Aussage, die Modelle erfinden nichts, war falsch. In jener Reihe waren7 versus3 von je12Versuchen vollständig korrekt; es gab zusätzlich einen unbelegten Wert. Mit dem damaligen Hersteller-Sampling waren es12 versus2. Diese Reihen getrennt lesen und nicht zu einem allgemeinen Qualitätsurteil vermischen.

## 10. Prüferfehler ehrlich behandeln
Beim heutigen Offline-Audit wurden96 erhaltene Versuche gelesen. Alle damals bestandenen unbekannt-Antworten bestehen auch die strenge Prüfung auf vorhandene Schlüssel und echtes null. Trotzdem hatte der alte Prüfer Schwächen: fehlende Schlüssel konnten als null gelten, und ein Fehlertext konnte eine fehlende Antwort mit Teilpunkten versehen. Deshalb trennt der neue Lernprüfer Schema, Fakten und fehlende Ergebnisse.

## 11. Tempo einordnen
Token pro Sekunde, Gesamtdauer und Werkzeugschritte sind getrennte Größen. Cache und Quantisierung beeinflussen den Vergleich. Ein schnellerer Ausgabetakt ist kein Beweis für früher abgeschlossene Arbeit. Eigene ältere Gesamtvergleiche waren nicht nach Quantisierung kontrolliert. Unser kleines Paket startet keine neue Inferenz und behauptet keinen Sieger für alle Aufgaben.

## 12. Was danach wirklich feststeht
Du hast einen nachvollziehbaren kleinen Antwortvertrag und kannst eigene tatsächliche Modellantworten damit prüfen. Unsere ausgeführten Prüfertests sind Autor-Testdateien, keine neuen Modellantworten. Der Archiveinblick hat eine konkret nötige Korrektur bestätigt. Von zwei Aufgaben und wenigen Wiederholungen führt kein direkter Schluss auf allgemeine Intelligenz, sichere Werkzeugarbeit oder die Wirkung jeder Abliteration.
