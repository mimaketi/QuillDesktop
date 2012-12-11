"""
Straight Line

EXAMPLES::

    >>> sample_line
    line from (0.175,0.532) to (0.629,0.442)
"""

from graphics_object_color import GraphicsObjectThicknessColor



class Line(GraphicsObjectThicknessColor):
    
    def __init__(self, thickness, red, green, blue, x0, y0, x1, y1):
        super(Line, self).__init__(thickness, red, green, blue)
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self):
        s  = 'line from ('
        s += str(round(self._x0,3)) + ','
        s += str(round(self._y0,3)) + ') to (' 
        s += str(round(self._x1,3)) + ','
        s += str(round(self._y1,3)) + ')'
        return s

    def x0(self):
        """
        Return the x-coordinate of the first point.

        EXAMPLES::
        
            >>> sample_line
            line from (0.175,0.532) to (0.629,0.442)
            >>> sample_line.x0()
            0.17479963600635529
        """        
        return self._x0

    def y0(self):
        """
        Return the y-coordinate of the first point.

        EXAMPLES::
        
            >>> sample_line
            line from (0.175,0.532) to (0.629,0.442)
            >>> sample_line.y0()
            0.5317864418029785
        """
        return self._y0

    def x1(self):
        """
        Return the x-coordinate of the second point.

        EXAMPLES::
        
            >>> sample_line
            line from (0.175,0.532) to (0.629,0.442)
            >>> sample_line.x1()
            0.629351019859314
        """
        return self._x1

    def y1(self):
        """
        Return the y-coordinate of the second point.

        EXAMPLES::
        
            >>> sample_line
            line from (0.175,0.532) to (0.629,0.442)
            >>> sample_line.y1()
            0.44183480739593506
        """
        return self._y1
    
    
