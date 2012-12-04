"""
Base class for all exporters
"""


class ExporterBase(object):

    def __init__(self, output_filename):
        self

    def title(self):
        return self._title

    def creation_time(self):
        return self._ctime

    def modification_time(self):
        return self._mtime

    def save(self, book):
        """
        Save 
        """
        raise NotImplemented


    
