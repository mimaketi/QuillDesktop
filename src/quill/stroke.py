"""
Single Pen Stroke

EXAMPLES::

    >>> sample_stroke  # doctest: +ELLIPSIS
    <quill.stroke.Stroke object at 0x...>
"""

from graphics_object import GraphicsObject



class Stroke(GraphicsObject):
    
    def __init__(self, pressure, red, green, blue, points):
        super(Stroke, self).__init__()
        self._pressure = pressure
        self._red = red
        self._green = green
        self._blue = blue
        self._points = tuple(points)
        
    def has_pressure(self):
        """
        Return whether the pen stroke has varying width (fountain pen tool).
        
        :rtype: boolean
        
        EXAMPLES::
        
            >>> sample_stroke.has_pressure()
            False
        """
        return self._pressure

    def red(self):
        """
        Return the red value.

        :rtype: integer from ``0`` to ``0xff``

        EXAMPLES::

            >>> sample_stroke.red()
            128
        """
        return self._red

    def green(self):
        """
        Return the green value.

        :rtype: integer from ``0`` to ``0xff``

        EXAMPLES::

            >>> sample_stroke.green()
            0
        """
        return self._green

    def blue(self):
        """
        Return the blue value.

        :rtype: integer from ``0`` to ``0xff``

        EXAMPLES::

            >>> sample_stroke.blue()
            0
        """
        return self._blue

    def rgb(self):
        """
        Return color.

        :rtype: tuple of three floats, ranging from 0 to 1.

        EXAMPLES::
        
            >>> sample_stroke.red()
            128
            >>> sample_stroke.green()
            0
            >>> sample_stroke.blue()
            0
            >>> sample_stroke.rgb()
            (0.5019607843137255, 0.0, 0.0)
        """
        return (float(self.red()/255.0), float(self.green()/255.0), float(self.blue()/255.0))

    def n_points(self):
        """
        Return the number of sample points.

        :rtype: integer

        EXAMPLES::

            >>> sample_stroke.n_points()
            40
            >>> len(sample_stroke)
            40
        """
        return len(self._points)

    def get_point(self, i):
        """
        Return the ``i``-th point
        
        :param integer i: index of the point to return

        :rtype: a tuple containing three floats (x, y, and pressure)

        EXAMPLES::

            >>> sample_stroke.get_point(24)
            (0.17748723924160004, 0.09612473845481873, 0.5307917594909668)
            >>> sample_stroke[24]
            (0.17748723924160004, 0.09612473845481873, 0.5307917594909668)
        """
        return self._points[i]

    __len__ = n_points

    __getitem__ = get_point
