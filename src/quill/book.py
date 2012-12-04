"""
A single notebook
"""

from datetime import datetime

from quill.decorators import cached_method



class Book(object):

    def __init__(self, importer):
        self._importer = importer

    @cached_method
    def uuid(self):
        return self._importer.uuid()

    @cached_method
    def title(self):
        return self._importer.title()

    @cached_method
    def mtime_millis(self):
        return self._importer.mtime_millis()

    @cached_method
    def ctime_millis(self):
        return self._importer.mtime_millis()

    @cached_method
    def mtime(self):
        sec = self.mtime_millis() / 1000.0
        return datetime.fromtimestamp(sec)

    @cached_method
    def ctime(self):
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
        return self._importer.n_pages()

    __len__ = n_pages

    def get_page(self, n):
        """
        Return the n-th page.
        """
        return self._importer.get_page(n)

    def __iter__(self):
        for i in range(self.n_pages):
            yield self.get_page(i)

    def __repr__(self):
        s  = 'Book title: '+self.title()+'\n'
        s += 'Uuid: '+self.uuid()+'\n'
        s += 'Created '+self.pretty_ctime()+'\n'
        s += 'Last modified '+self.pretty_ctime()+'\n'
        return s


