"""
Base class for all importers

EXAMPLES::

    >>> sample_importer  # doctest: +ELLIPSIS
    <quill.importer.quill_importer.QuillImporter object at 0x...>
"""

class QuillImporterError(Exception):
    pass



class ImporterBase(object):

    ##################################################################
    #
    # Change the following methods to set metadata and load pages
    #
    ##################################################################

    def title(self):
        """
        Return the title of the book.
        
        :rtype: string
        
        You should overriding this method in derived
        classes. Otherwise a default title will be used.

        EXAMPLES::

            >>> sample_importer.title()
            'Example Notebook'
        """
        return 'Untitled Document'

    def uuid(self):
        """
        Return the UUID of the book.

        :rtype: string
        
        You should overriding this method in derived
        classes. Otherwise a random UUID will be generated.

        EXAMPLES::

            >>> sample_importer.uuid()
            '1fd6a485-33ed-4a45-a5a1-e06e55fdca57'
        """
        import uuid
        return str(uuid.uuid4())

    def mtime_millis(self):
        """
        Return the last modification time in milliseconds.

        :rtype: integer
        
        You should overriding this method in derived
        classes. Otherwise the current time will be used.

        EXAMPLES::

            >>> sample_importer.mtime_millis()
            1355065045000
        """
        return self._time_millis_now()

    def ctime_millis(self):
        """
        Return the creation time in milliseconds.

        :rtype: integer
        
        You should overriding this method in derived
        classes. Otherwise the current time will be used.

        EXAMPLES::

            >>> sample_importer.ctime_millis()
            1355064642000
        """
        return self._time_millis_now()

    def n_pages(self):
        """
        Return the number of pages.

        :rtype: integer
        
        Must be implemented in derived classes.

        EXAMPLES::

            >>> sample_importer.n_pages()
            3
        """
        raise NotImplemented

    def get_page(self, n):
        """
        Return the n-th page.

        :rtype: a :class:`~quill.page.Page` object
        
        Must be implemented in derived classes.

        EXAMPLES::

            >>> sample_importer.n_pages()
            3
        """
        raise NotImplemented

    ##################################################################
    #
    # The remaining methods are not supposed to be changed in derived
    # classes.
    #
    ##################################################################

    def _time_to_millis(self, python_time):
        """
        Helper to convert Python time to milliseconds.
        """
        import datetime
        import time
        return time.mktime(python_time.timetuple()) * 1000

    def _time_millis_now(self):
        """
        Helper to get the current time in milliseconds.
        """
        import datetime
        return self._time_to_millis(datetime.now())

    def __len__(self):
        """
        Implement the list interface for the pages
        """
        return self.n_pages()

    def __getitem__(self, n):
        """
        Implement the list interface for the pages
        """
        return self.get_page(n)

    def get_book(self):
        """
        Create a Book object from the importer.

        :rtype: a :class:`~quill.book.Book` object
        
        You should not override this method. All it does is takes the
        metadata and creates the corresponding :class:`~quill.book`
        object.

        EXAMPLES::

            >>> sample_importer.get_book()  # doctest: +ELLIPSIS
            Book title: Example Notebook
            Uuid: 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
            Created ...
            Last modified ...
        """
        from quill.book import Book
        return Book(title=self.title(), uuid=self.uuid(),
            mtime=self.mtime_millis(), ctime=self.ctime_millis(), 
            pages=self)
