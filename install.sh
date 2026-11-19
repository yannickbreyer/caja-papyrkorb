#!/usr/bin/env bash
set -e

EXT_DIR="$HOME/.local/share/caja-python/extensions"

echo "Installiere Caja-Erweiterung 'Papyrkorb leeren'..."
mkdir -p "$EXT_DIR"

if command -v gio >/dev/null 2>&1; then
    echo "Erkannt: Modernes MATE-System (GTK 3 / Python 3)"
    cp src/empty_trash.py "$EXT_DIR/empty_trash.py"
else
    echo "Erkannt: Älteres MATE-System (GTK 2 / Python 2, z. B. Linux Mint 17)"
    cp src/empty_trash_legacy.py "$EXT_DIR/empty_trash.py"
fi

echo "Starte Caja neu..."
caja -q 2>/dev/null || true

echo "Fertig! Öffne Caja und navigiere zu trash:///, um die Erweiterung zu nutzen."
