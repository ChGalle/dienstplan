import pdfplumber
import pandas as pd
import sys
from pathlib import PurePath
from escpos import *


if len(sys.argv) > 1:
    f = sys.argv[1]
else:
    raise AttributeError("Es wurde keine Datei als Argument übergeben.")

pdf = pdfplumber.open(f)
page = pdf.pages[0]
table = page.extract_table()


def printBon():
    p = printer.Usb(0x04b8, 0x0e02)
    # Zentriere den Druck - Wähle Schriftart A
    p.set(align='center', font='a')
    # Drucke das Datum der Eingabe auf den Kopf des Bons
    p.textln(f'{date}\n\n')
    # Drucke die Tabelle als Markdown-String
    p.text(result.to_markdown())
    # Schneide den Bon
    p.cut()
    # Gib den USB-Anschluss frei
    p.close()


# Extrahiere den Dateinamen der Eingangsdatei
dateiname = PurePath(f).stem

# Monatsname

date = input("Gib den Monat des Dienstplans ein: ")
# Eingabe des Mitarbeiters aus dem Dienstplan
name = input('Gib deinen Namen im Format "Nachname, Vorname" ein: ')

drucken = int(
    input('Möchtest du eine (1)txt-Datei, (2)einen Bon drucken oder (3)beides? '))

# Erstelle das Dataframe
df = pd.DataFrame(table[1:], columns=table[0])

# Räume die Sonderzeichen in den Namen auf, die von der Wache schon mal eingetragen werden
for column in ["Name"]:
    df[column] = df[column].str.replace("+", "", regex=True)
    df[column] = df[column].str.replace("*", "", regex=True)


# Lösche die Wochentage aus den Datumsspalten
df.columns = df.columns.str.replace("Mo", "")
df.columns = df.columns.str.replace("Di", "")
df.columns = df.columns.str.replace("Mi", "")
df.columns = df.columns.str.replace("Do", "")
df.columns = df.columns.str.replace("Fr", "")
df.columns = df.columns.str.replace("Sa", "")
df.columns = df.columns.str.replace("So", "")

# Wähle den Datensatz entsprechend des Mitarbeiters aus
df.set_index("Name", inplace=True)
df.replace("-", None, inplace=True)
# Ersetze die DSM Kürzel durch Text
df.replace({'O': '24 Std', 'X': 'X-Dienst',
           'V1': 'V-Dienst', 'A1': 'Fortbildung', 'TE1': 'Tagdienst 16:00 Uhr', 'TE2': 'Tagdienst 14:00 Uhr'}, inplace=True)

result = df.loc[name]

match drucken:
    case 1:
        # Erstelle eine Markdown-Datei als txt-Datei
        result.to_markdown(f'{dateiname}_{name}.txt')
    case 2:
        printBon()
    case 3:
        # Erstelle eine Markdown-Datei als txt-Datei
        result.to_markdown(f'{dateiname}_{name}.txt')
        printBon()
    case _:
        print('Ein Fehler ist aufgetreten')
