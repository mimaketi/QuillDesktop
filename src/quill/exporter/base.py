"""
Base class for all exporters
"""

class QuillExporterError(Exception):
    pass



class ExporterBase(object):

    def set_page_numbers(self, numbers=None):
        """
        Set the page numbers to export.

        :param numbers: an integer, a list/tuple/iterable of integers,
                        or ``None`` (default). The page numbers of the
                        pages to export. By default, all pages are
                        exported.

        EXAMPLES::

            >>> from quill.exporter.base import ExporterBase
            >>> exporter = ExporterBase()
            >>> exporter.get_page_numbers(sample_book)
            [0, 1, 2]
            >>> exporter.set_page_numbers(1)
            >>> exporter.get_page_numbers(sample_book)
            [1]
        """
        if numbers is None:
            try:
                del self._page_numbers
            except AttributeError:
                pass
            return
        try:
            self._page_numbers = list(numbers)
        except TypeError:
            self._page_numbers = [int(numbers)]

    def get_page_numbers(self, book):
        """
        Return the page numbers to be exported.
        
        :param book: the notebook to use, instance of
                     :class:`~quill.book.Book`. This is necessary to
                     be able to list all page numbers.

        :rtype: list of integers

        EXAMPLES::

            >>> from quill.exporter.base import ExporterBase
            >>> exporter = ExporterBase()
            >>> exporter.get_page_numbers(sample_book)
            [0, 1, 2]
            >>> exporter.set_page_numbers(1)
            >>> exporter.get_page_numbers(sample_book)
            [1]
        """
        try:
            return self._page_numbers
        except AttributeError:
            return range(book.n_pages())


    ##################################################################
    #
    # Most radical way to implement your own exporter: override the
    # book() method and do it all yourself.
    #
    ##################################################################

    def book(self, book):
        """
        Export the notebook.
        
        Must be implemented in derived classes.

        :param book: the notebook to export
        """
        raise NotImplementedError('book() must be implemented in derived classes.')

    
