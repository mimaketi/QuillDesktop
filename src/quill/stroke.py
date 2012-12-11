"""
Single Pen Stroke

EXAMPLES::

    >>> sample_stroke
    pen stroke with 40 points
"""

from graphics_object_color import GraphicsObjectThicknessColor



class Stroke(GraphicsObjectThicknessColor):
    
    def __init__(self, pressure, thickness, red, green, blue, points):
        super(Stroke, self).__init__(thickness, red, green, blue)
        self._pressure = pressure
        self._points = tuple(points)

    def __repr__(self):
        return 'pen stroke with '+str(self.n_points())+' points'
        
    def has_pressure(self):
        """
        Return whether the pen stroke has varying width (fountain pen tool).
        
        :rtype: boolean
        
        EXAMPLES::
        
            >>> sample_stroke.has_pressure()
            False
        """
        return self._pressure

    def thickness(self):
        """
        Return the pen thickness.

        The thickness is counted ``1/1600f`` of the page
        height. Quill's "ultra-fine" pen has a thickness of 1.

        :rtype: integer

        EXAMPLES::

            >>> sample_stroke.thickness()
            5
        """
        return self._thickness

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
