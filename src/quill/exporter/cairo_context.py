"""
Draw to a Cairo context
"""

import cairo


from quill.exporter.base2 import ExporterBase2



class CairoContext(ExporterBase2):
    
    def __init__(self, context, width, height, background=False):
        self._width = width
        self._height = height
        self._context = context
        self._background = background

    def title(self, title):
        pass

    def uuid(self, uuid):
        pass

    def creation_time(self, ctime, ctime_millis):
        pass

    def modification_time(self, mtime, mtime_millis):
        pass

    def begin_export(self):
        cr = self._context
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)

    def end_export(self):
        pass
        
    def new_page(self, page):
        h = self._height
        w = h * page.aspect_ratio()
        if w>self._width:
            w = self._width
            h = w / page.aspect_ratio()
        self._context.identity_matrix()
        self._context.scale(h, h)
        dx = (self._width-w) / h
        dy = (self._height-h) / h
        self._context.translate(dx/2, dy/2)
        self.background(page)

    def background(self, page):
        if not self._background:
            return
        cr = self._context
        cr.set_source_rgb(1, 1, 1) 
        cr.rectangle(0, 0, page.aspect_ratio(), 1) 
        cr.fill()

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

    def line(self, line):
        cr = self._context
        cr.set_source_rgb(*line.rgb())
        cr.set_line_width(line.thickness() / self._pen_scale_factor)
        cr.move_to(line.x0(), line.y0())
        cr.line_to(line.x1(), line.y1())
        cr.stroke()

    def image(self, image):
        cr = self._context
