"""
Image

This module is the data model for an image on a page

EXAMPLES::

    >>> sample_image  # doctest: +ELLIPSIS
    image at (0.13,0.605):(0.455,0.739)
"""

from graphics_object import GraphicsObject


class Image(GraphicsObject):
    """
    Embedded image on a page.
    """

    def __init__(self, uuid, x0, x1, y0, y1, constrain_aspect):
        super(Image, self).__init__()
        self._uuid = uuid
        self._x0 = x0
        self._x1 = x1
        self._y0 = y0
        self._y1 = y1

    def __repr__(self):
        s  = 'image at ('
        s += str(round(self._x0,3)) + ','
        s += str(round(self._y0,3)) + '):(' 
        s += str(round(self._x1,3)) + ','
        s += str(round(self._y1,3)) + ')'
        return s
