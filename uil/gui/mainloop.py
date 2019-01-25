'''This file includes the mainloops for the main application
The start symbol in this file refers to the mainloop of the desired/available
windowing toolkit.

supported: Gtk-3.0

'''
have_gtk = False
have_qt  = False

try:
    import gi
    gi.require_version("Gtk", "3.0")
    gi.require_version("Gio", "2.0")
    from gi.repository import Gtk
    from gi.repository import Gio
    have_gtk = True
except ImportError as e:
    have_gtk = false


_start = None
if have_gtk:
    _start = Gtk.main
elif have_qt:
    # start a qt app
    raise NotImplementedError("This program hasn't implemented qt")
    pass
else:
    RuntimeError('No available start function for the gui toolkit.')


def start(app, mainwin, argv):
    if have_gtk:
        app.run(argv)