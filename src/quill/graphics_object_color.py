"""
Base Class for Graphics Object with Thickness and Color Information
"""



from graphics_object import GraphicsObject


class GraphicsObjectThicknessColor(GraphicsObject):

    def __init__(self, thickness, red, green, blue):
        super(GraphicsObjectThicknessColor, self).__init__()
        self._thickness = thickness
        self._red = red
        self._green = green
        self._blue = blue
        
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
        
