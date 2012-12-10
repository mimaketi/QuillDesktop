"""
Export to Portable Document Format (PDF)

EXAMPLES::

    >>> from quill.exporter.pdf import Pdf
    >>> from tempfile import TemporaryFile
    >>> tmp = TemporaryFile(suffix='pdf')
    >>> Pdf(tmp).book(sample_book)
    Title is set to Example Notebook
    UUID is set to 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
    Creation time set to 2012-12-09 14:57:25
    Last modification time set to 2012-12-09 14:57:25
"""

import cairo

from quill.exporter.cairo_surface_paginated import CairoSurfacePaginated


class Pdf(CairoSurfacePaginated):
    """
    Exporter to PDF
    
    :param fileobj: a filename or a file-like object
    """
    
    def __init__(self, fileobj):
        """
        The Python constructor
        """
        surface = cairo.PDFSurface(fileobj, 1, 1)
        super(Pdf, self).__init__(surface)

