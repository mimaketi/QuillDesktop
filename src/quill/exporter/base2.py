"""
More advanced base class

You probably want to implement your exporter on top of this base
class. The default methods just print to stdout.

EXAMPLES::

    >>> from quill.exporter.base2 import ExporterBase2
    >>> ExporterBase2().book(sample_book)    # doctest: +ELLIPSIS
    Beginning export
    Title is set to Example Notebook
    UUID is set to 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
    Creation time set to 2012-12-09 14:57:25
    Last modification time set to 2012-12-09 14:57:25
    New page, aspect ratio 0.707
    Draw image at (0.13,0.605):(0.455,0.739)
    Draw line from (0.175,0.532) to (0.629,0.442)
    Draw line from (0.169,0.433) to (0.632,0.528)
    Draw pen stroke with 40 points
    Draw pen stroke with 8 points
    Draw pen stroke with 59 points
    Draw pen stroke with 31 points
    Draw pen stroke with 44 points
    Draw pen stroke with 36 points
    Draw pen stroke with 22 points
    Draw pen stroke with 9 points
    Draw pen stroke with 6 points
    Draw pen stroke with 18 points
    Draw pen stroke with 21 points
    ...
    Draw pen stroke with 17 points
    Draw pen stroke with 14 points
    Draw pen stroke with 34 points
    Draw pen stroke with 11 points
    Draw pen stroke with 18 points
    Draw pen stroke with 11 points
    Draw pen stroke with 11 points
    Draw pen stroke with 4 points
    Draw pen stroke with 28 points
    Draw pen stroke with 32 points
    Draw pen stroke with 29 points
    Draw pen stroke with 21 points
    New page, aspect ratio 0.707
    Draw pen stroke with 12 points
    Draw pen stroke with 30 points
    Draw pen stroke with 26 points
    Draw pen stroke with 50 points
    Draw pen stroke with 54 points
    New page, aspect ratio 0.707
    Ending export

    >>> ExporterBase2().book(sample_book_xoj)    # doctest: +ELLIPSIS
    Beginning export
    Title is set to Example_Notebook
    UUID is set to ...
    Creation time set to ...
    Last modification time set to ...
    New page, aspect ratio 0.707
    Draw image at (0.13,0.605):(0.455,0.739)
    Draw line from (0.175,0.532) to (0.629,0.442)
    Draw line from (0.169,0.433) to (0.632,0.528)
    Draw pen stroke with 40 points
    Draw pen stroke with 8 points
    Draw pen stroke with 59 points
    Draw pen stroke with 31 points
    Draw pen stroke with 44 points
    Draw pen stroke with 36 points
    Draw pen stroke with 22 points
    Draw pen stroke with 9 points
    Draw pen stroke with 6 points
    Draw pen stroke with 18 points
    Draw pen stroke with 21 points
    ...
    Draw pen stroke with 17 points
    Draw pen stroke with 14 points
    Draw pen stroke with 34 points
    Draw pen stroke with 11 points
    Draw pen stroke with 18 points
    Draw pen stroke with 11 points
    Draw pen stroke with 11 points
    Draw pen stroke with 4 points
    Draw pen stroke with 28 points
    Draw pen stroke with 32 points
    Draw pen stroke with 29 points
    Draw pen stroke with 21 points
    New page, aspect ratio 0.707
    Draw pen stroke with 12 points
    Draw pen stroke with 30 points
    Draw pen stroke with 26 points
    Draw pen stroke with 50 points
    Draw pen stroke with 54 points
    New page, aspect ratio 0.707
    Ending export
"""

from base import ExporterBase





class ExporterBase2(ExporterBase):
    
    ##################################################################
    #
    # Easier way to implement your own exporter: define exporters for
    # metadata and graphics objects.
    #
    ##################################################################

    def begin_export(self):
        """
        Hook to be called at the beginning of the export process.

        You should override this method in your own exporter to set it
        up. This method returns nothing.
        """
        print 'Beginning export'

    def end_export(self):
        """
        Called at the beginning of the export process.

        You should override this method in your own exporter to tear
        it down. This method returns nothing.
        """
        print 'Ending export'

    def title(self, title):
        """
        Set the title.

        :param string title: the notebook title

        This method will be called before the first empty page (see
        :meth:`new_page`) is inserted. You should override this method
        to save it in your exported document.
        """
        print 'Title is set to '+title

    def uuid(self, uuid):
        """
        Set the notebook UUID.

        :param string uuid: the notebook UUID

        This method will be called before the first empty page (see
        :meth:`new_page`) is inserted. You should override this method
        to save it in your exported document.
        """
        print 'UUID is set to '+uuid

    def creation_time(self, ctime, ctime_millis):
        """
        Set the notebook creation time.

        :param datetime ctime: the creation time as python object

        :param integer ctime_millis: the creation time as milliseconds

        This method will be called before the first empty page (see
        :meth:`new_page`) is inserted. You should override this method
        to save it in your exported document.
        """
        print 'Creation time set to '+str(ctime)
        
    def modification_time(self, mtime, mtime_millis):
        """
        Set the notebook last-modified time.

        :param datetime mtime: the last modification time as python
                               object 

        :param integer mtime_millis: the last modification time as
                                     milliseconds

        This method will be called before the first empty page (see
        :meth:`new_page`) is inserted. You should override this method
        to save it in your exported document.
        """
        print 'Last modification time set to '+str(mtime)

    def new_page(self, page):
        """
        Add a new empty page to the exported document.

        :param page: the page to export, instance of
                     :class:`~quill.page.Page`

        You should override this method to add a new empty page with
        the specified aspect ratio and background to your document.
        """
        print 'New page, aspect ratio '+str(round(page.aspect_ratio(), 3))

    def stroke(self, stroke):
        """
        Add a pen stroke to the current page.

        :param stroke: the pen stroke to export, instance of
                       :class:`~quill.stroke.Stroke`

        You should override this method to draw the pen stroke on the
        most recently added page. This method will only be called
        after an empty page (see :meth:`new_page`) has been inserted.
        """
        print 'Draw '+str(stroke)
        
    def line(self, line):
        """
        Add a straight line to the current page.

        :param line: the line to export, instance of
                     :class:`~quill.line.Line`

        You should override this method to draw the pen stroke on the
        most recently added page. This method will only be called
        after an empty page (see :meth:`new_page`) has been inserted.
        """
        print 'Draw '+str(line)
        
    def image(self, image):
        """
        Add an image to the current page.

        :param image: the image to export, instance of
                      :class:`~quill.image.Image`

        You should override this method to draw the image on the
        most recently added page. This method will only be called
        after an empty page (see :meth:`new_page`) has been inserted.
        """
        print 'Draw '+str(image)

    ##################################################################
    #
    # The rest is the implementation of the book() method, you
    # shouldn't have to override anything.
    #
    ##################################################################

    def book(self, book):
        """
        Export the notebook.

        :param book: the notebook to export, instance of
                     :class:`~quill.book.Book`

        .. warning::
        
            You should not have to override this method, it defers
            drawing to the other methods.
        """
        self.begin_export()
        self.title(book.title())
        self.uuid(book.uuid())
        self.creation_time(book.ctime(), book.ctime_millis())
        self.modification_time(book.mtime(), book.mtime_millis())
        for i in self.get_page_numbers(book):
            page = book.get_page(i)
            self.page(page)
        self.end_export()
    
    def page(self, page):
        """
        Export a page

        :param page: the page to export, instance of
                     :class:`~quill.page.Page`

        .. warning::
        
            You should not have to override this method, it defers
            drawing to the other methods.
        """
        self.new_page(page)
        for image in page.images():
            self.image(image)
        for line in page.lines():
            self.line(line)
        for stroke in page.strokes():
            self.stroke(stroke)



