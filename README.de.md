🌐 **Sprache:** [English](README.md) | Deutsch

# Caja Papyrkorb Extension

Eine schlanke Python-Erweiterung für den MATE-Dateimanager **Caja**, die im Papierkorb (`trash:///`) den Kontextmenü-Eintrag **„Papyrkorb leeren“** (eine Anspielung auf *Papyrus*, *Python* und *Papierkorb*) mit einem Bestätigungsdialog und dynamischen System-Icons bereitstellt.

## Motivation
Ich habe diese Erweiterung erstellt, weil ich es von Windows gewohnt bin, den Papierkorb über das Kontextmenü zu leeren.

## Funktionen
- **Kontextabhängig:** Erscheint ausschließlich, wenn `trash:///` geöffnet ist.
- **Klare Unterscheidung:** Hebt sich durch die Bezeichnung **„Papyrkorb leeren“** eindeutig vom eingebauten Caja-Eintrag ab.
- **Sicherheitsabfrage:** Bestätigungsdialog vor dem endgültigen Löschen (inkl. Info-Hinweis, falls der Papierkorb bereits leer ist).
- **Dynamische System-Icons:** Wechselt automatisch zwischen `user-trash` und `user-trash-full`.
- **Abwärtskompatibel:** Enthält sowohl eine moderne Version (GTK 3 / Python 3) als auch eine Legacy-Version für ältere Distributionen (z. B. Linux Mint 17).

## Voraussetzungen

### Moderne Systeme (Ubuntu MATE 18.04+, Linux Mint 18.2+, Debian 10+)
- MATE Desktop mit **Caja**
- `python3-caja`

```bash
sudo apt update
sudo apt install python3-caja
```

### Ältere / Legacy-Systeme (z. B. Linux Mint 17 / MATE 1.8)
- MATE Desktop mit **Caja**
- `python-caja`
- `zenity` und `gvfs-bin` (in der Regel vorinstalliert)

```bash
sudo apt-get update
sudo apt-get install python-caja zenity gvfs-bin
```

## Installation
Das Installationsskript erkennt automatisch, ob ein modernes oder ein älteres MATE-System vorliegt, und kopiert die passende Datei:

```bash
git clone https://github.com/yannickbreyer/caja-papyrkorb.git
cd caja-papyrkorb
chmod +x install.sh
./install.sh
```

### Manuelle Installation (optional)
Falls du die Datei lieber von Hand kopieren möchtest:
- **Moderne Systeme:** `cp src/empty_trash.py ~/.local/share/caja-python/extensions/empty_trash.py`
- **Legacy-Systeme:** `cp src/empty_trash_legacy.py ~/.local/share/caja-python/extensions/empty_trash.py`

Anschließend Caja neu starten mit `caja -q`.

## Deinstallation
```bash
rm -f ~/.local/share/caja-python/extensions/empty_trash.py
caja -q
```

## Lizenz
MIT License
