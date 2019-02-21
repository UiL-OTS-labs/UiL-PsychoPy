"""Contains Color related classes and functions"""

def uint_to_float(value,  bits=8):
    """Convert a integer in the range [0, 2**bits) to a floatingpoint
    value in the ranges [0, 1], this operation is saturating, meaning
    that values larger, or smaller than the input range are given, the value
    will be change to the maximal or 0 respectively.
    This function is based on the
    """
    intmax = 2**bits - 1
    if value > intmax:
        value = intmax
    elif value < 0:
        value = 0
    return value / (intmax)


def float_to_uint(value, bits=8):
    """Converts a value from the range [0,1] back to a integer in the
    range of [0, 2**bits-1]
    """
    if value > 1.0:
        value = 1.0
    elif value < 0.0:
        value = 0.0
    return int(value * (2**bits - 1))



class Color:
    """Internally a color consists of 4 in"""

    def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0):
        self.r = float(r)
        self.b = float(b)
        self.g = float(g)
        self.a = float(a)

    def __repr__(self):
        return "Color({}, {}, {}, {})".format(self.r, self.b, self.g, self.a)

    @staticmethod
    def from_ints(r=0, g=0, b=0, a=255, bits=8):
        """Construct a new color value from integer color values"""
        return Color(
            uint_to_float(r, bits),
            uint_to_float(g, bits),
            uint_to_float(b, bits),
            uint_to_float(a, bits)
        )

