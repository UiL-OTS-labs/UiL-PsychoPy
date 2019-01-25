#!/usr/bin/env python3


from uil.gui.uilwindow import UilWindowGtk
from uil.gui.uilwindow import UilApp
import uil.gui.mainloop
import sys

# program name
PROGRAM_NAME = "Uil Experiment"

mainwin = UilWindowGtk(name=PROGRAM_NAME)
app     = UilApp(mainwin)


if __name__ == "__main__":
    uil.gui.mainloop.start(app, mainwin, sys.argv)
