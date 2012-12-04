"""
The drawing area widget for the page
"""

import gtk
import math


class PageWidget(gtk.DrawingArea):
    __gtype_name__ = 'PageWidget'
    __gsignals__ = {"expose_event": "override" }
 
    def __init__(self):
        gtk.DrawingArea.__init__(self)
  
    def do_expose_event(self, event):
        context = self.window.cairo_create()
        context.rectangle(event.area.x, event.area.y, 
                          event.area.width, event.area.height)
        context.clip()
        self.draw(context, *self.window.get_size())
  
    def draw(self, context, width, height):
        context.set_source_rgb(0.5, 0.0, 0.0) 
        context.rectangle(0, 0, width, height) 
        context.fill()
        context.set_source_rgb(1.0, 0.0, 0.0)
        radius = min(width, height)
        context.arc(width / 2.0, height / 2.0, 
                    radius / 2.0 - 20, 0, 2 * math.pi)  
        context.stroke()


def page_widget_get_type(x):
    return x
