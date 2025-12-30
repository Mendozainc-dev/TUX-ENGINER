# When the application is launched…
def on_activate(app):
    # … create a new window…
    win = Gtk.ApplicationWindow(application=app)
    # … with a button in it…
    btn = Gtk.Button(label='Hello, World!')
    # … which closes the window when clicked
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)
    win.present()

# Create a new application
app = Gtk.Application(application_id='com.example.GtkApplication')
app.connect('activate', on_activate)

# Run the application
app.run(None)


#este es un test para la app, en el sentido que es para probar la funcionalidad de la aplicacion y todas las herraminentas que se van a usar en el desarrollo de la aplicacion de Tux-Enginer
