# -*- coding: utf-8 -*-
import subprocess
from gi.repository import Caja, GObject, Gio


class EmptyTrashExtension(GObject.GObject, Caja.MenuProvider):
    def _is_trash_empty(self):
        """Prüft, ob der Papierkorb leer ist."""
        trash_dir = Gio.File.new_for_uri('trash:///')
        try:
            enumerator = trash_dir.enumerate_children('standard::name', 0, None)
            is_empty = enumerator.next_file(None) is None
            enumerator.close(None)
            return is_empty
        except Exception:
            return False

    def _on_empty_trash(self, menu_item, window):
        """Prüft den Papierkorb und zeigt entweder einen Hinweis oder den Lösch-Dialog."""
        if self._is_trash_empty():
            subprocess.call([
                'zenity', '--info',
                '--title=Papyrkorb',
                '--text=Der Papierkorb ist bereits leer.'
            ])
            return

        res = subprocess.call([
            'zenity', '--question',
            '--title=Papierkorb wirklich leeren?',
            '--text=Möchten Sie alle Elemente im Papierkorb wirklich unwiderruflich löschen?',
            '--ok-label=Papierkorb leeren',
            '--cancel-label=Abbrechen'
        ])
        if res == 0:
            subprocess.call(['gvfs-trash', '--empty'])

    def get_background_items(self, window, file):
        if file.get_uri() != 'trash:///':
            return []

        is_empty = self._is_trash_empty()
        item = Caja.MenuItem(
            name='EmptyTrashExtension::EmptyTrash',
            label='Papyrkorb leeren',
            tip='Alle Elemente im Papierkorb endgültig löschen',
            icon='user-trash' if is_empty else 'user-trash-full'
        )
        item.set_property('sensitive', not is_empty)
        item.connect('activate', self._on_empty_trash, window)

        return [item]
