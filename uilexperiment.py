#!/usr/bin/env python3

import gui

from gui.uilwindow import UilWindowGtk
from gui.uilwindow import UilApp
import gui.mainloop
import sys

# program name
PROGRAM_NAME = "Uil Experiment"

mainwin = UilWindowGtk(name=PROGRAM_NAME)
app     = UilApp(mainwin)


if __name__ == "__main__":
    gui.mainloop.start(app, mainwin, sys.argv)
