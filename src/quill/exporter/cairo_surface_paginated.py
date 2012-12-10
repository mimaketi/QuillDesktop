"""
Draw to a Cairo surface with a paginated backend
"""

import cairo

from quill.exporter.cairo_context import CairoContext


class CairoSurfacePaginated(CairoContext):

    def __init__(self, surface):
        self._paper_height = 842.0   # A4 paper height in points
        self._paper_width  = 595.0   # A4 paper width in points
        self._surface = surface
        cr = cairo.Context(self._surface)
        super(CairoSurfacePaginated, self).__init__(cr, 0,0)

    def begin_export(self):
        self._first_page = True
        super(CairoSurfacePaginated, self).begin_export()

    def end_export(self):
        if not self._first_page:
            self._context.show_page()
        super(CairoSurfacePaginated, self).end_export()

    def new_page(self, page):
        if not self._first_page:
            self._context.show_page()
        self._first_page = False
        h = self._paper_height
        w = h * page.aspect_ratio()
        if w>self._paper_width:
            w = self._paper_width
            h = w / page.aspect_ratio()
        self._height = h
        self._width = w
        self._surface.set_size(self._width, self._height)
        super(CairoSurfacePaginated, self).new_page(page)

