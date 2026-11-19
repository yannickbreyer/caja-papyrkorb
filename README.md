🌐 **Language:** English | [Deutsch](README.de.md)

# Caja Papyrkorb Extension

A lightweight Python extension for the MATE file manager **Caja** that adds a **"Papyrkorb leeren"** ("Empty Trash") context menu entry with a confirmation dialog and dynamic system icons when viewing `trash:///`.

*(Note: "Papyrkorb" is a German play on words combining **Papyrus**, **Python**, and **Papierkorb** [trash can] to clearly distinguish it from Caja's built-in "Empty Trash" entry.)*

## Motivation
I created this extension because I am used to emptying the recycle bin via the context menu in Windows.

## Features
- **Context-sensitive:** Appears exclusively when `trash:///` is open.
- **Clear distinction:** Uses the label **"Papyrkorb leeren"** to set itself apart from Caja's built-in menu item.
- **Safety prompt:** Confirmation dialog before permanently deleting files (including an info notice if the trash is already empty).
- **Dynamic system icons:** Automatically switches between `user-trash` and `user-trash-full`.
- **Backward compatible:** Includes both a modern version (GTK 3 / Python 3) and a legacy version for older distributions (e.g., Linux Mint 17).

## Prerequisites

### Modern Systems (Ubuntu MATE 18.04+, Linux Mint 18.2+, Debian 10+)
- MATE Desktop with **Caja**
- `python3-caja`

```bash
sudo apt update
sudo apt install python3-caja
```

### Legacy Systems (e.g., Linux Mint 17 / MATE 1.8)
- MATE Desktop with **Caja**
- `python-caja`
- `zenity` and `gvfs-bin` (usually pre-installed)

```bash
sudo apt-get update
sudo apt-get install python-caja zenity gvfs-bin
```

## Installation
The installation script automatically detects whether you are running a modern or legacy MATE system and copies the appropriate file:

```bash
git clone https://github.com/yannickbreyer/caja-papyrkorb.git
cd caja-papyrkorb
chmod +x install.sh
./install.sh
```

### Manual Installation (optional)
If you prefer copying the file manually:
- **Modern systems:** `cp src/empty_trash.py ~/.local/share/caja-python/extensions/empty_trash.py`
- **Legacy systems:** `cp src/empty_trash_legacy.py ~/.local/share/caja-python/extensions/empty_trash.py`

Then restart Caja using `caja -q`.

## Uninstallation
```bash
rm -f ~/.local/share/caja-python/extensions/empty_trash.py
caja -q
```

## License
MIT License
