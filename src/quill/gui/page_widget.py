"""
The drawing area widget for the page
"""

import gtk
import math

from quill.exporter.cairo_context import CairoContext

class PageWidget(gtk.DrawingArea):
    __gtype_name__ = 'PageWidget'
    __gsignals__ = {"expose_event": "override" }
 
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self._book = None
        self._page_number = 0
  
    def do_expose_event(self, event):
        context = self.window.cairo_create()
        context.rectangle(event.area.x, event.area.y, 
                          event.area.width, event.area.height)
        context.clip()
        self.draw(context, *self.window.get_size())

    def set_book(self, book):
        self._book = book
        self._page_number = 0
        self.queue_draw()

    def page_number(self):
        return self._page_number
  
    def prev_page(self):
        if self._page_number == 0:
            return
        self._page_number -= 1
        self.queue_draw()
            
    def next_page(self):
        if self._page_number+1 == self._book.n_pages():
            return
        self._page_number += 1
        self.queue_draw()

    def draw(self, context, width, height):
        context.set_source_rgb(0.8, 0.8, 0.8) 
        context.rectangle(0, 0, width, height) 
        context.fill()
        if self._book is None:
            return
        output = CairoContext(context, width, height, background=True)
        output.set_page_numbers(self._page_number)
        output.book(self._book)

