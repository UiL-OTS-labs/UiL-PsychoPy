#!/usr/bin/env python3

import cairo as c
import gi
#gi.require_foreign("cairo")
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
gi.require_version("cairo", "1.0")
gi.require_version('PangoCairo', '1.0')

from gi.repository import Gtk
from gi.repository import Pango
from gi.repository import PangoCairo
from gi.repository import cairo
#from cairo import SVGSurface
from ..utils import color

class TextStimulus(cairo.ImageSuface):
    """TextStimulus create a picture that contains nicely formatted text"""

    def __init__(self, width, height, text=none):
        super(self).__init__(cairo.FORMAT_ARGB32, width, height)
        self.width = width
        self.height = height
        self.text = text if text else ""
        self.cr = cairo.Context(self)
        self.layout = PangoCairo.create_layout(self.cr)
        self.background_color = color.Color(1, 1, 1)

    def draw():
        """draws the current stimulus"""
        cr.save()
        cr.scale(self.width, self.height)
        cr.move_to(0,0)
        cr.line_to(1,0)
        cr.line_to(1,1)
        cr.line_to(0,1)
        cr.close_path()
        cr.restore()
        cr.set_fill_color




def _print_rect(rect, name=None):
    print(
        "{}\tx={}\ty={}\twidth={}\theight={}\t".format(
            name if name else "rect",
            rect.x,
            rect.y,
            rect.width,
            rect.height
            )
         )
    

if __name__ == "__main__":
    width, height = 800, 800
    indent        = 50

    outfn = 'pango_pic.png'
    stroke_col  = 0.0,0.0,0.0,1.0
    fill_col    = 1.0,0.0,0.0,1.0

    surf        = c.ImageSurface(c.FORMAT_ARGB32, width, height)
    cr          = c.Context(surf)

    fontstr = "Dejavu Sans 48"
    string  = "Hello, World!";
    lstring =("Hello, World! This is a very long sentence without a linebreak. "
              "This one has one though.\n"
              "<b>blaat.txt</b> <u>Dit</u> is op een nieuwe alinea.")

    cr.save()
    cr.scale(width, height)

    cr.move_to(0, 0)
    cr.line_to(0, 1)
    cr.line_to(1, 1)

    cr.line_to(1, 0)
    cr.line_to(0, 0)

    cr.set_source_rgba(1.0, 1.0, 1.0, 1.0)
    cr.fill()  # use cr.fill_preserve to preserve the path
    cr.restore()

    layout = PangoCairo.create_layout(cr)
    layout.set_justify(True)
    layout.set_width(width * Pango.SCALE)
    layout.set_font_description(Pango.FontDescription.from_string(fontstr))
    layout.set_wrap(Pango.WrapMode.WORD)
    layout.set_indent(indent*Pango.SCALE)
    layout.set_markup(lstring, len(lstring))

    # Create path for contents
    PangoCairo.layout_path(cr, layout)

    # stroke the letters (draw the outline)
    cr.set_line_width(2.0)
    cr.set_source_rgba(*stroke_col)
    cr.stroke_preserve()
    # fill the letters
    # cr.set_source_rgba(*fill_col)
    # cr.fill_preserve()
    # PangoCairo.show_layout(cr, layout)
    ink_rect, logical_rect = layout.get_pixel_extents()
    print_rect(ink_rect, "ink_rect")
    print_rect(logical_rect, "logical_rect")
    ink_rect, logical_rect = layout.get_pixel_extents()
    print_rect(ink_rect, "ink_rect")
    print_rect(logical_rect, "logical_rect")
    surf.write_to_png(outfn)
    surf.finish()

