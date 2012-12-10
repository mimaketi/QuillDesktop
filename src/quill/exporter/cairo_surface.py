"""
Draw to a Cairo surface
"""

import cairo


from quill.exporter.base2 import ExporterBase2



class CairoSurface(ExporterBase2):
    
    def __init__(self, surface, width, height):
        self._width = width
        self._height = height
        self._surface = surface

    def begin_export(self):
        cr = self._context = cairo.Context(self._surface)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)

    def end_export(self):
        self._surface.flush()
        
    def new_page(self, page):
        self._context.identity_matrix()
        self._context.scale(self._height, self._height)

    _pen_scale_factor = float(1600.0)

    def stroke(self, stroke):
        cr = self._context
        cr.set_source_rgb(*stroke.rgb())
        if stroke.has_pressure():
            # width changes, each segment is its own stroke
            p1 = stroke.get_point(0)
            for i in xrange(stroke.n_points() - 1):
                p0 = p1
                p1 = stroke.get_point(i+1)
                cr.set_line_width(stroke.thickness() 
                                  / self._pen_scale_factor
                                  * (p0[2] + p1[2])/2)
                cr.move_to(p0[0], p0[1])
                cr.line_to(p1[0], p1[1])
                cr.stroke()
        else:
            # constant width, join all segment into one stroke
            cr.set_line_width(stroke.thickness() / self._pen_scale_factor)
            p1 = stroke.get_point(0)
            for i in xrange(stroke.n_points() - 1):
                p0 = p1
                p1 = stroke.get_point(i+1)
                cr.move_to(p0[0], p0[1])
                cr.line_to(p1[0], p1[1])
                cr.stroke()

    def image(self, image):
        cr = self._context
