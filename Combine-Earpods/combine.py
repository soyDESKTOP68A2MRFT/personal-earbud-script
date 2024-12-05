import os
import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SyncApp:
    def __init__(self):
        # Obtener la ruta al directorio del script
        base_path = os.path.dirname(os.path.abspath(__file__))
        glade_file = os.path.join(base_path, "sync_window.glade")
        
        builder = Gtk.Builder()
        builder.add_from_file(glade_file)
        
        # Obtener los objetos de la interfaz
        self.window = builder.get_object("main_window")
        self.message_label = builder.get_object("message_label")
        self.sync_button = builder.get_object("sync_button")
        self.connect_button = builder.get_object("connect_button")
        self.disconnect_button = builder.get_object("disconnect_button")
        self.unsync_button = builder.get_object("unsync_button")
        self.fix_button = builder.get_object("fix_button")
        
        # Conectar las señales a las funciones correspondientes
        self.sync_button.connect("clicked", self.on_sync_clicked)
        self.connect_button.connect("clicked", self.on_connect_clicked)
        self.disconnect_button.connect("clicked", self.on_disconnect_clicked)
        self.unsync_button.connect("clicked", self.on_unsync_clicked)
        self.fix_button.connect("clicked", self.on_fix_clicked)
        self.window.connect("destroy", Gtk.main_quit)

    def on_sync_clicked(self, button):
        """Sincronizar los audífonos"""
        try:
            subprocess.run(["/home/joni/Combine-Earpods/combine.sh", "sync"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos sincronizados con éxito")
        except subprocess.CalledProcessError:
            self.message_label.set_text("No se pudieron sincronizar los audífonos")

    def on_connect_clicked(self, button):
        """Conectar los audífonos"""
        try:
            subprocess.run(["/home/joni/Combine-Earpods/combine.sh", "connect"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos conectados con éxito")
        except subprocess.CalledProcessError:
            self.message_label.set_text("No se pudieron conectar los audífonos")

    def on_disconnect_clicked(self, button):
        """Desconectar los audífonos"""
        try:
            subprocess.run(["/home/joni/Combine-Earpods/combine.sh", "disconnect"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos desconectados con éxito")
        except subprocess.CalledProcessError:
            self.message_label.set_text("No se pudieron desconectar los audífonos")

    def on_unsync_clicked(self, button):
        """Desincronizar los audífonos"""
        try:
            subprocess.run(["/home/joni/Combine-Earpods/combine.sh", "unsync"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos desincronizados con éxito")
        except subprocess.CalledProcessError:
            self.message_label.set_text("No se pudieron desincronizar los audífonos")

    def on_fix_clicked(self, button):
        """Arreglar los audífonos"""
        try:
            subprocess.run(["/home/joni/Combine-Earpods/combine.sh", "fix"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Perfiles de los audífonos alternados con éxito")
        except subprocess.CalledProcessError:
            self.message_label.set_text("Error al alternar los perfiles de los audífonos")

    def run(self):
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    app = SyncApp()
    app.run()
