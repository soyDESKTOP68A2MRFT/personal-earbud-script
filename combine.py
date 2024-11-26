import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SyncApp:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("sync_window.glade")
        
        # Obtener los objetos de la interfaz
        self.window = builder.get_object("main_window")
        self.message_label = builder.get_object("message_label")
        self.sync_button = builder.get_object("sync_button")
        self.connect_button = builder.get_object("connect_button")
        self.disconnect_button = builder.get_object("disconnect_button")
        
        # Conectar las señales a las funciones correspondientes
        self.sync_button.connect("clicked", self.on_sync_clicked)
        self.connect_button.connect("clicked", self.on_connect_clicked)
        self.disconnect_button.connect("clicked", self.on_disconnect_clicked)
        self.window.connect("destroy", Gtk.main_quit)

    def on_sync_clicked(self, button):
        """Sincronizar los audífonos"""
        try:
            # Ejecutar el script con la opción 'sync' (sincronización)
            result = subprocess.run(["/home/joni/combine.sh", "sync"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos sincronizados con éxito")
        except subprocess.CalledProcessError as e:
            self.message_label.set_text("No se pudieron sincronizar los audífonos")

    def on_connect_clicked(self, button):
        """Conectar los audífonos"""
        try:
            # Ejecutar el script con la opción 'connect' (conexión)
            result = subprocess.run(["/home/joni/combine.sh", "connect"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos conectados con éxito")
        except subprocess.CalledProcessError as e:
            self.message_label.set_text("No se pudieron conectar los audífonos")

    def on_disconnect_clicked(self, button):
        """Desconectar los audífonos"""
        try:
            # Ejecutar el script con la opción 'disconnect'
            result = subprocess.run(["/home/joni/combine.sh", "disconnect"], capture_output=True, text=True, check=True)
            self.message_label.set_text("Audífonos desconectados con éxito")
        except subprocess.CalledProcessError as e:
            self.message_label.set_text("No se pudieron desconectar los audífonos")
    
    def run(self):
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    app = SyncApp()
    app.run()
