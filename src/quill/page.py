"""
Page of a Notebook

The :class:`Page` class stores everything that is drawn on the page as
well as format data of the page (like aspect ratio).
"""



class Page(object):
    """
    Page of a notebook

    EXAMPLES::
        
        >>> type(sample_page)
        <class 'quill.page.Page'>
        >>> print sample_page
        page number 0
    """
    
    def __init__(self, number, uuid, aspect_ratio, strokes, lines, images):
        self._book = None
        self._number = number
        self._uuid = uuid
        self._aspect_ratio = aspect_ratio
        self._strokes = tuple(strokes)
        self._lines = tuple(lines)
        self._images = tuple(images)
        for graphics_object in self._strokes + self._images:
            graphics_object._place_on_page(self)

    def _place_in_book(self, book):
        """
        Helper to set the notebook that the page is on.
        """
        if (self._book is not None) and (self._book is not book):
            raise ValueError('page may only be placed in one book')
        self._book = book

    def book(self):
        """
        Return the notebook containing the page.

        :rtype: a :class:`~quill.book.Book`

        EXAMPLES::

            >>> sample_page.book()    # doctest: +ELLIPSIS
            Book title: Example Notebook
            Uuid: 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
            Created ...
            Last modified ...
        """
        return self._book

    def number(self):
        """
        Return the page number.

        :rtype: integer

        EXAMPLES::
        
            >>> sample_page.number()
            0
        """
        return self._number

    def uuid(self):
        """
        Return the page uuid.

        :rtype: string

        EXAMPLES::
        
            >>> sample_page.uuid()
            '9aa10c71-c872-4d2b-b97e-1845fd5a4cfc'
        """
        return self._uuid
        

    def aspect_ratio(self):
        """
        Return the aspect ratio.

        :rtype: float, the ratio of width divided by height.

        EXAMPLES::
        
            >>> sample_page.aspect_ratio()
            0.7071067690849304
        """
        return self._aspect_ratio

    def strokes(self):
        """
        Return the strokes 
        
        :rtype: a tuple of :class:`~quill.stroke.Stroke` objects

        EXAMPLES::

            >>> len(sample_page.strokes())
            125
            >>> sample_page.strokes()[0]
            pen stroke with 40 points
        """
        return self._strokes

    def lines(self):
        """
        Return the straight lines
        
        :rtype: a tuple of :class:`~quill.line.Line` objects

        EXAMPLES::

            >>> len(sample_page.lines())
            2
            >>> sample_page.lines()[0]
            line from (0.175,0.532) to (0.629,0.442)
        """
        return self._lines

    def images(self):
        """
        Return the images 
        
        :rtype: a tuple of :class:`~quill.image.Image` objects

        EXAMPLES::

            >>> sample_page.images()
            (image at (0.13,0.605):(0.455,0.739),)
        """
        return self._images

    def __repr__(self):
        s = 'page number '+str(self.number())
        return s

