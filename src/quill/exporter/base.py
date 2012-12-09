"""
Base class for all exporters
"""


class ExporterBase(object):

    def begin_export(self):
        """
        Called at the beginning of the export process.
        """
        pass

    def end_export(self):
        """
        Called at the beginning of the export process.
        """
        pass

    ##################################################################
    #
    # Most radical way to implement your own exporter: override the
    # book() method and do it all yourself.
    #
    ##################################################################

    def book(self, book):
        """
        Export the notebook.

        :param book: the notebook to export
        """
        self.begin_export()
        book.save(self)
        self.end_export()

    
