import gi

# Es fundamental especificar la versión ANTES de importar Gtk
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

# Cuando la aplicación se inicia...
def on_activate(app):
    # ... crear una ventana nueva...
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("TUX ENGINER")
    win.set_default_size(1600, 900)

    # ... con un botón dentro...
    btn = Gtk.Button(label='Bienvenido mai')
    win.set_child(btn)
    win.present()

# Crear la aplicación
app = Gtk.Application(application_id='com.ejemplo.GtkApp')
app.connect('activate', on_activate)

# Ejecutar la aplicación
app.run(None)
