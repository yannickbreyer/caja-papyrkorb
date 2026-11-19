import subprocess
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Caja', '2.0')
from gi.repository import Caja, GObject, Gtk, Gio, GLib


class EmptyTrashExtension(GObject.GObject, Caja.MenuProvider):
    def _is_trash_empty(self):
        """Prüft, ob der Papierkorb leer ist."""
        trash_dir = Gio.File.new_for_uri('trash:///')
        try:
            enumerator = trash_dir.enumerate_children(
                'standard::name', Gio.FileQueryInfoFlags.NONE, None
            )
            is_empty = enumerator.next_file(None) is None
            enumerator.close(None)
            return is_empty
        except GLib.Error:
            return False

    def _on_empty_trash(self, menu_item, window):
        """Prüft den Papierkorb und zeigt entweder einen Hinweis oder den Lösch-Dialog."""
        if self._is_trash_empty():
            info_dialog = Gtk.MessageDialog(
                transient_for=window,
                flags=Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text="Der Papierkorb ist bereits leer."
            )
            info_dialog.run()
            info_dialog.destroy()
            return

        dialog = Gtk.MessageDialog(
            transient_for=window,
            flags=Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.NONE,
            text="Papierkorb wirklich leeren?"
        )
        dialog.format_secondary_text(
            "Möchten Sie alle Elemente im Papierkorb wirklich unwiderruflich löschen?"
        )
        dialog.add_button("_Abbrechen", Gtk.ResponseType.CANCEL)
        empty_btn = dialog.add_button("Papierkorb _leeren", Gtk.ResponseType.OK)
        empty_btn.get_style_context().add_class("destructive-action")

        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.OK:
            subprocess.run(['gio', 'trash', '--empty'])

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
