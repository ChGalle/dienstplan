# Dienstplan to Markdown

Dieses Skript übernimmt einen DSM-Dienstplan der Feuerwehr Düsseldorf als PDF-Datei und kann einen Dienstplan
für einen bestimmten Kollegen als Markdown-Text-Datei erzeugen.

---

Das Skript wird folgendermaßen ausgeführt:

`# python dienstplan2md.py /pfad/zum/dienstplan.pdf`

Das Ergebnis ergibt dann eine Textdatei mit folgendem Inhalt:

|    | Nachname, Vorname   |
|---:|:--------------------|
|  1 |                     |
|  2 |                     |
|  3 | 24 Std              |
|  4 |                     |
|  5 | 24 Std              |
|  6 |                     |
|  7 |                     |
|  8 |                     |
|  9 | Tagdienst 16:00 Uhr |
| 10 |                     |
| 11 |                     |
| 12 |                     |
| 13 | Fortbildung         |
| 14 |                     |
| 15 | 24 Std              |
| 16 |                     |
| 17 | X-Dienst            |
| 18 |                     |
| 19 | 24 Std              |
| 20 |                     |
| 21 |                     |
| 22 |                     |
| 23 | V-Dienst            |
| 24 |                     |
| 25 | 24 Std              |
| 26 |                     |
| 27 |                     |
| 28 |                     |
| 29 | 24 Std              |
| 30 |                     |
| 31 |                     |

Auf Wunsch kann dann auch diese Tabelle auf einem Epson-TM88V Kassenbon-Drucker ausgedruckt werden. 

## Bekannte Bugs
- Wenn mehrere Vornamen vorhanden sind, müssen diese ganz exakt eingegeben werden.
- Es sind nicht sämtliche DSM-Kürzel vorhanden
- Bisher werden neben den Namen nur * und # herausgefiltert, da mir weitere Sonderzeichen der Wachen noch nicht bekannt sind.

## ToDo
- [x] Die wichtigsten DSM-Kürzel in Klartext anzeigen
- [ ] Verzicht auf die exakte Eingabe sämtlicher Vornamen

### Abhängigkeiten
- pdfplumber
- pandas
- sys
- pathlib
- escpos


