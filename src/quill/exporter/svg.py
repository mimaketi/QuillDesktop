"""
Export to Portable Document Format (PDF)

EXAMPLES::

    >>> from quill.exporter.svg import Svg
    >>> from tempfile import TemporaryFile
    >>> tmp = TemporaryFile(suffix='svg')
    >>> Svg(tmp).book(sample_book)
    Title is set to Example Notebook
    UUID is set to 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
    Creation time set to 2012-12-09 14:57:25
    Last modification time set to 2012-12-09 14:57:25
"""

import cairo

from quill.exporter.cairo_surface import CairoSurface


class Svg(CairoSurface):
    """
    Exporter to PDF
    
    :param fileobj: a filename or a file-like object
    """
    
    def __init__(self, fileobj):
        """
        The Python constructor
        """
        height = 842   # A4 paper height in points
        width  = 595
        surface = cairo.SVGSurface(fileobj, width, height)
        super(Svg, self).__init__(surface, width, height)

