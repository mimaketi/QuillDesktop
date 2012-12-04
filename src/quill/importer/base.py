"""
Base class for all importers
"""

class QuillImporterError(Exception):
    pass



class ImporterBase(object):

    def uuid(self):
        import uuid
        return str(uuid.uuid4())

    def title(self):
        return 'Untitled Document'

    def __time_millis_now(self):
        import datetime
        import time
        now = datetime.datetime.now()
        return time.mktime(now.timetuple()) * 1000

    def mtime_millis(self):
        return self.__time_millis_now()

    def ctime_millis(self):
        return self.__time_millis_now()

    def n_pages(self):
        """
        Return the number of pages.

        Must be implemented in derived classes
        """
        raise NotImplemented

    def get_page(self, n):
        """
        Return the n-th page.

        Must be implemented in derived classes
        """
        raise NotImplemented

