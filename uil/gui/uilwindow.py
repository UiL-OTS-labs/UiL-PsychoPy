
import gi
gi.require_version("Gtk", "3.0")
# gi.require_version("Gio", "2.0")
from gi.repository import GLib, Gio, Gtk


class UilApp(Gtk.Application):
    """The uil application"""

    def __init__(self, mainwin, *args, **kwargs):
        super(UilApp, self).__init__(*args, **kwargs)
        self.uilmainwin = mainwin

    def do_startup(self):
        """Handles the startup function"""
        Gtk.Application.do_startup(self)
        print ("Do startup")


    def do_activate(self):
        """Handles the "activate" signal."""
        print(u"signal activate")
        self.add_window(self.uilmainwin)


class UilWindowMenuGtk:
    """represents the menu model"""


class UilWindowHeaderGtk(Gtk.HeaderBar):
    """Represents a header bar to control the app"""

    def __init__(self, title, *args, **kwargs):
        super(UilWindowHeaderGtk, self).__init__(*args, **kwargs)
        self.set_title(title)

class UilWindowGtk(Gtk.ApplicationWindow):
    """The main application window."""
    
    def __init__(self, *args, **kwargs):
        super(UilWindowGtk, self).__init__(*args, **kwargs)
        self.set_property("default-width", 600)
        self.set_property("default-height", 800)
        titlebar = UilWindowHeaderGtk("Run a experiment")
        self.box = Gtk.VBox()
        #self.box.set_orientation(Gtk.vertical)
        self.add(self.box)
        self.box.add(titlebar)
        self.show_all()

    def do_delete(self):
        """When the window is about to be destroyed."""
        print("Delete Event")
        #print("GMenuModel", self.get_menubar())

#window = Gtk.Window(title="Hello World")
#window.show()
#window.connect("destroy", Gtk.main_quit)
#Gtk.main()
