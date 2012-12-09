"""
More advanced base class
"""

from base import ExporterBase


class ExporterBase2(ExporterBase):
    
    def title(self, title):
        """
        Set the title.
        """
        self._title = title

    def uuid(self, uuid):
        self._uuid = uuid

    def creation_time(self, ctime):
        self._ctime = ctime

    def modification_time(self, mtime):
        self._mtime = mtime

    ##################################################################
    #
    # Easier way to implement your own exporter: define exporters for
    # all graphics objects.
    #
    ##################################################################

    def page(self, page):
        """
        Add a new page to the exported document.
        """
        pass

    def stroke(self, image):
        pass
        
    def image(self, image):
        pass

