#!/usr/bin/env python3

"""This module contains utilities to generate Nicely formated text stimuli
"""

import cairo
import gi
gi.require_foreign("cairo")
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
gi.require_version('PangoCairo', '1.0')

from gi.repository import Pango
from gi.repository import PangoCairo
from ..utils import color

import numpy as np


class Font:
    """A description of a font to use with"""

    # Font styles
    STYLE_NORMAL = Pango.Style.NORMAL
    STYLE_OBLIQUE = Pango.Style.OBLIQUE
    STYLE_ITALIC = Pango.Style.ITALIC

    WEIGHT_THIN = Pango.Weight.THIN
    WEIGHT_ULTRALIGHT = Pango.Weight.ULTRALIGHT
    WEIGHT_LIGHT = Pango.Weight.LIGHT
    WEIGHT_SEMILIGHT = Pango.Weight.SEMILIGHT
    WEIGHT_BOOK = Pango.Weight.BOOK
    WEIGHT_NORMAL = Pango.Weight.NORMAL
    WEIGHT_MEDIUM = Pango.Weight.MEDIUM
    WEIGHT_SEMIBOLD = Pango.Weight.SEMIBOLD
    WEIGHT_BOLD = Pango.Weight.BOLD
    WEIGHT_ULTRABOLD = Pango.Weight.ULTRABOLD
    WEIGHT_HEAVY = Pango.Weight.HEAVY
    WEIGHT_ULTRAHEAVY = Pango.Weight.ULTRAHEAVY

    def __init__(self,
                 family,
                 size=16,
                 style=STYLE_NORMAL,
                 weight=WEIGHT_NORMAL):
        self.description = Pango.FontDescription()
        self.set_size(size)
        self.set_weight(weight)
        self.set_style(style)
        self.set_family(family)

    def set_weight(self, weight):
        """set the font weight"""
        self.description.set_weight(weight)

    def set_style(self, style):
        """set the font style"""
        self.description.set_style(style)

    def set_size(self, size):
        """set the font size"""
        self.description.set_size(size * Pango.SCALE)

    def set_family(self, fam):
        """Return the font family"""
        self.description.set_family(fam)

    def __str__(self):
        """Return a string that represents a font, this string can be
        used to construct a new Font instance with the Font.from_string()
        static method.
        """
        return self.description.to_string()

    @staticmethod
    def list_font_families():
        map = PangoCairo.font_map_get_default()
        fonts = Pango.FontMap.list_families(map)
        fonts = [f.get_name() for f in fonts]
        return fonts # Pango.pango_font_map_list_families()

    @staticmethod
    def from_string(fontstr):
        """Obtain a new font from a string description"""
        descr = Pango.FontDescription.from_string(fontstr)
        new = Font()
        new.description = descr
        return new


class TextStimulus:
    """TextStimulus create a picture that contains nicely formatted text"""

    def __init__(self, width, height, font, text=None):
        self.surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.width = width
        self.height = height
        self.indent = 50.0
        #self.cr = cairo.Context(self.surf)
        #self.layout = PangoCairo.create_layout(self.cr)
        self.background_color = color.Color(1, 1, 1)
        self.fontcolor = color.Color()
        if text:
            self.set_text(text)
        self.font = font

    def draw(self):
        """draws the current stimulus"""
        cr = cairo.Context(self.surf)
        layout = PangoCairo.create_layout(cr)
        context = layout.get_context()
        context.set_base_gravity(Pango.Gravity.AUTO)
        layout.set_markup(self.text, len(self.text.encode('utf8')))

        cr.save()
        cr.scale(self.width, self.height)
        cr.move_to(0, 0)
        cr.line_to(1, 0)
        cr.line_to(1, 1)
        cr.line_to(0, 1)
        cr.close_path()
        cr.restore()

        c = self.background_color
        # print(c)
        cr.set_source_rgba(c.r, c.g, c.b, c.a)
        cr.fill()

        layout.set_font_description(self.font.description)
        layout.set_justify(True)
        layout.set_width(self.width * Pango.SCALE)
        layout.set_wrap(Pango.WrapMode.WORD)
        layout.set_indent(self.indent * Pango.SCALE)

        # draw text with font color
        c = self.fontcolor
        cr.set_source_rgba(c.r, c.g, c.b, c.a)

        # Create path for contents
        PangoCairo.layout_path(cr, layout)
        cr.fill()

        # make sure drawing commands are finished before it is used.
        self.surf.flush()

    def save_as_png(self, fn):
        """Store the image surface as png."""
        self.surf.write_to_png(fn)

    def set_text(self, text, draw=False):
        """Set the text and (re-) draw the stimulus"""
        self.text = text
        if draw:
            self.draw()

    def size(self):
        """Return a tuple of width, height"""
        return self.width, self.height

    def psychopy_texture(self):
        """Returns a numpy array that is suitable to use as a psychopy texture.
        psychopy likes its textures in a [-1.0, 1.0] range, so the result
        from this function should math that.

        returns tuple of np.array
        """
        import matplotlib.pyplot as plt
        tmax = 255.0
        nchannels = 4 #alpha, red, green, blue
        out = np.array(self.surf.get_data(), dtype='float')
        out = np.asarray(self.surf.get_data(),dtype='float')
        print("out.shape", out.shape, len(out.shape))
        out /= tmax
        out = out*2.0 - 1.0
        combined = out.reshape([self.height, self.width, nchannels])
        texture = combined[:, :, 0:3]
        #texture =
        print ("Texture.shape = ", texture.shape)
        mask = combined[:, :, 3]
        # return texture, mask
        return np.flip(texture, 0), mask
