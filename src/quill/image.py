"""
Image

This module is the data model for an image on a page

EXAMPLES::

    >>> sample_image
    image at (0.13,0.605):(0.455,0.739)
"""

from graphics_object import GraphicsObject


class Image(GraphicsObject):
    """
    Embedded image on a page.
    """

    def __init__(self, uuid, x0, x1, y0, y1, constrain_aspect, jpg_data):
        super(Image, self).__init__()
        self._uuid = uuid
        self._x0 = x0
        self._x1 = x1
        self._y0 = y0
        self._y1 = y1
        self._constrain = constrain_aspect
        self._data = jpg_data

    def __repr__(self):
        s  = 'image at ('
        s += str(round(self._x0,3)) + ','
        s += str(round(self._y0,3)) + '):(' 
        s += str(round(self._x1,3)) + ','
        s += str(round(self._y1,3)) + ')'
        return s

    def data(self):
        r"""
        Return the image data (jpg).

        :rtype: string

        EXAMPLES::
        
            >>> sample_image.data()    # doctest: +ELLIPSIS
            '\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00...
        """
        return self._data
    
    def uuid(self):
        """
        Return the image uuid.

        :rtype: string

        EXAMPLES::
        
            >>> sample_image.uuid()
            'ce34de3c-daeb-4a81-8620-e170441946c1'
        """
        return self._uuid

    def constrain_aspect(self):
        """
        Whether the aspect ratio should be constrained when resizing.

        :rtype: boolean

        EXAMPLES::

            >>> sample_image.constrain_aspect()
            True
        """
        return self._constrain

    def x0(self):
        """
        Return the minimum x-coordinate.

        :rtype: float
        
        EXAMPLES::

            >>> sample_image.x0()
            0.12979288399219513
        """
        return self._x0
    
    def x1(self):
        """
        Return the maximum x-coordinate.

        :rtype: float
        
        EXAMPLES::

            >>> sample_image.x1()
            0.4552972912788391
        """
        return self._x1

    def y0(self):
        """
        Return the minimum y-coordinate.

        :rtype: float
        
        EXAMPLES::

            >>> sample_image.y1()
            0.7390127182006836
        """
        return self._y0

    def y1(self):
        """
        Return the maximum y-coordinate.

        :rtype: float
        
        EXAMPLES::

            >>> sample_image.y1()
            0.7390127182006836
        """
        return self._y1
    
