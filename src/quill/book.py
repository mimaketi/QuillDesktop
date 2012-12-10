"""
A Single Notebook

The :class:`book` class stores metadata and the list of pages.

EXAMPLES::
        
    >>> sample_book   # doctest: +ELLIPSIS
    Book title: Example Notebook
    Uuid: 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
    Created ...
    Last modified ...
"""

from datetime import datetime

from quill.decorators import cached_method



class Book(object):
    """
    Metadata for a notebook

    EXAMPLES::
        
        >>> type(sample_book)
        <class 'quill.book.Book'>
    """

    def __init__(self, title, uuid, mtime, ctime, pages):
        """
        The Python constructor.

        This is not meant to be called by hand, but instead from the
        :meth:`~quill.importer.base.get_book` method.

        :param string title: title of the notebook
        :param string uuid: uuid of the notebook
        :param integer mtime: last modification time in milliseconds
        :param integer ctime: creation time in milliseconds 
        :param list pages: pages, either a list or an object
                           implementing `__len__` and `__getitem__`.
        """
        self._title = title
        self._uuid = uuid
        self._mtime_millis = mtime
        self._ctime_millis = ctime
        self._pages = pages

    def uuid(self):
        """
        Return the UUID of the notebook.

        :rtype: string

        EXAMPLES::
        
            >>> sample_book.uuid()
            '1fd6a485-33ed-4a45-a5a1-e06e55fdca57'
        """
        return self._uuid

    def title(self):
        """
        Return the title of the notebook.

        :rtype: string

        EXAMPLES::
        
            >>> sample_book.title()
            'Example Notebook'
        """
        return self._title

    def mtime_millis(self):
        """
        Return the last modification time of the notebook in milliseconds.

        :rtype: integer

        EXAMPLES::
        
            >>> sample_book.mtime_millis()
            1355065045000
        """
        return self._mtime_millis

    def ctime_millis(self):
        """
        Return the creation time of the notebook in milliseconds.

        :rtype: integer

        EXAMPLES::
        
            >>> sample_book.ctime_millis()
            1355064642000
        """
        return self._ctime_millis

    def mtime(self):
        """
        Return the last modification time of the notebook.

        EXAMPLES::
        
            >>> sample_book.mtime()
            datetime.datetime(2012, 12, 9, 14, 57, 25)
        """
        sec = self.mtime_millis() / 1000.0
        return datetime.fromtimestamp(sec)

    def ctime(self):
        """
        Return the creation time of the notebook.

        EXAMPLES::
        
            >>> sample_book.ctime()
            datetime.datetime(2012, 12, 9, 14, 57, 25)
        """
        sec = self.mtime_millis() / 1000.0
        return datetime.fromtimestamp(sec)

    def __pretty_time(self, time):
        """
        Get a datetime object or a int() Epoch timestamp and return a
        pretty string like 'an hour ago', 'Yesterday', '3 months ago',
        'just now', etc
        """
        now = datetime.utcnow()
        diff = now - time 
        second_diff = diff.seconds
        day_diff = diff.days
        if day_diff < 0:
            return 'from future?'
        if day_diff == 0:
            if second_diff < 10:
                return "just now"
            if second_diff < 60:
                return str(second_diff) + " seconds ago"
            if second_diff < 120:
                return  "a minute ago"
            if second_diff < 3600:
                return str( second_diff / 60 ) + " minutes ago"
            if second_diff < 7200:
                return "an hour ago"
            if second_diff < 86400:
                return str( second_diff / 3600 ) + " hours ago"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str(day_diff) + " days ago"
        if day_diff < 31:
            return str(day_diff/7) + " weeks ago"
        if day_diff < 365:
            return str(day_diff/30) + " months ago"
        return str(day_diff/365) + " years ago"

    def pretty_mtime(self):
        return self.__pretty_time(self.mtime())

    def pretty_ctime(self):
        return self.__pretty_time(self.ctime())

    def n_pages(self):
        """
        Return the number of pages.
        """
        return len(self._pages)

    def get_page(self, n):
        """
        Return the n-th page.
        """
        page = self._pages[n]
        page._place_in_book(self)
        return page

    __len__ = n_pages

    __getitem__ = get_page

    def __iter__(self):
        for i in range(self.n_pages):
            yield self.get_page(i)

    def __repr__(self):
        s  = 'Book title: '+self.title()+'\n'
        s += 'Uuid: '+self.uuid()+'\n'
        s += 'Created '+self.pretty_ctime()+'\n'
        s += 'Last modified '+self.pretty_ctime()+'\n'
        return s.strip()

