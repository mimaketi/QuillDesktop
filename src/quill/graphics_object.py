"""
Base Class for Graphics Objects

Anything that is on a page derives from this class.
"""


class GraphicsObject(object):
    
    def __init__(self):
        self._page = None

    def _place_on_page(self, page):
        """
        Helper to set the page that this graphics object is on.
        """
        if self._page is not None:
            raise ValueError('graphics objects may only be placed on one page')
        self._page = page

    def page(self):
        """
        Return the page that the graphics object is on.
        
        :rtype: a :class:`~quill.page.Page`
        
        EXAMPLES::
         
            >>> sample_stroke.page()
            page number 0
        """
        return self._page

    def save(self, exporter):
        """
        Save the page using an exporter.
        """
        pass
