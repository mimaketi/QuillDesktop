"""
Draw to a Cairo context
"""

import cairo
import gtk

from quill.exporter.base2 import ExporterBase2



class CairoContext(ExporterBase2):
    
    def __init__(self, context, width, height, background=False, cache=None):
        self._width = width
        self._height = height
        self._context = context
        self._background = background
        self._cache = cache

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

    def _get_image_surface(self, image):
        if self._cache is not None:
            try:
                return self._cache[image.uuid()]
            except KeyError:
                pass
        data = image.data()
        loader = gtk.gdk.PixbufLoader()
        loader.write(data)
        loader.close()
        pixbuf = loader.get_pixbuf()
        surface = cairo.ImageSurface(
            cairo.FORMAT_ARGB32, pixbuf.get_width(), pixbuf.get_height())
        cr = gtk.gdk.CairoContext(cairo.Context(surface))
        cr.set_source_pixbuf(pixbuf,0,0)
        cr.paint()
        cr.stroke()
        if self._cache is not None:
            self._cache[image.uuid()] = surface
        return surface

    def image(self, image):
        cr = self._context
        image_surface = self._get_image_surface(image)
        cr.save()
        cr.translate(image.x0(), image.y0())
        w = (image.x1() - image.x0()) / image_surface.get_width()
        h = (image.y1() - image.y0()) / image_surface.get_height()
        cr.scale(w, h)
        cr.set_source_surface(image_surface,0,0)
        cr.paint()
        cr.stroke()
        cr.restore()

