"""
Import Xournal notebook

EXAMPLES::

    >>> from quill.importer.xournal import Xournal
    >>> x = Xournal(xournal_file)
    >>> print x    # doctest: +ELLIPSIS
    <quill.importer.xournal.Xournal object at 0x...>
    >>> book = x.get_book()
    >>> book.title()
    'Example_Notebook'
    >>> book.get_page(0)
    page number 0
"""

import gzip
import math
import os
import base64


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


from quill.importer.base import ImporterBase, QuillImporterError
from quill.book import Book
from quill.page import Page
from quill.stroke import Stroke
from quill.line import Line
from quill.image import Image




class Xournal(ImporterBase):
    
    def __init__(self, xournal_filename):
        self._filename = xournal_filename
        f = gzip.open(xournal_filename, 'rb')
        try:
            self._tree = ET.ElementTree(file=f)
        except IOError as e:
            raise QuillImporterError(str(e))
        self._pages = [ page for page in self._tree.iter(tag='page') ]
            

    def title(self):
        # There is a <title> tag but its not the real title
        # self._tree.find('title').text
        return os.path.splitext(os.path.split(self._filename)[1])[0]


    def n_pages(self):
        return len(self._pages)

    #### From the xournal sources
    #const char *color_names[COLOR_MAX] = {"black", "blue", "red", "green",
    #   "gray", "lightblue", "lightgreen", "magenta", "orange", "yellow", "white"};
    #guint predef_colors_rgba[COLOR_MAX] =
    #  { 0x000000ff, 0x3333ccff, 0xff0000ff, 0x008000ff,
    #    0x808080ff, 0x00c0ffff, 0x00ff00ff, 0xff00ffff,
    #    0xff8000ff, 0xffff00ff, 0xffffffff };
    
    xournal_pen_thickness_factor = 0.5
    xournal_page_scale_factor = 820.0
    xournal_color_constants = {
        'black': (0x0, 0x0, 0x0), 
        'blue': (0x33, 0x33, 0xcc), 
        'red': (0xff, 0x00, 0x0), 
        'green': (0x00, 0x80, 0x0),
        'gray': (0x80, 0x80, 0x80),
        'lightblue': (0x0, 0xc0, 0xff),
        'lightgreen': (0x0, 0xff, 0x00),
        'magenta': (0xff, 0x0, 0xff), 
        'orange': (0xff, 0x80, 0x0), 
        'yellow': (0xff, 0xff, 0x0), 
        'white': (0xff, 0xff, 0xff) }

    def _parse_color(self, color):
        try:
            return self.xournal_color_constants[color]
        except KeyError:
            red   = int(color[1:3], 16)
            green = int(color[3:5], 16)
            blue  = int(color[5:7], 16)
            return (red, green, blue)
        
    def _parse_width(self, width):
        width = [ float(w) / self.xournal_pen_thickness_factor
                  for w in width.split() ]
        max_width = max(width)
        if max_width > 12:
            max_width = 40
        elif max_width > 5:
            max_width = 12
        elif max_width > 2:
            max_width = 5
        elif max_width > 1:
            max_width = 2
        else:
            max_width = 1
        pressure = [ w/max_width for w in width ]
        return max_width, pressure

    def _parse_stroke(self, stroke):
        red, green, blue = self._parse_color(stroke.attrib['color'])
        thickness, pressure = self._parse_width(stroke.attrib['width'])
        xy = [ float(data) / self.xournal_page_scale_factor
               for data in stroke.text.split() ]
        fountain_pen = (len(pressure) > 1)
        if not fountain_pen and len(xy)==4:
            return Line(thickness, red, green, blue, xy[0], xy[1], xy[2], xy[3])
        if fountain_pen:
            points = zip(xy[::2], xy[1::2], pressure)
        else:
            points = zip(xy[::2], xy[1::2], [1.0]*(len(xy)/2))
        return Stroke(fountain_pen, thickness, red, green, blue, points)

    def _parse_image(self, image):
        left   = float(image.attrib['left'])   / self.xournal_page_scale_factor
        right  = float(image.attrib['right'])  / self.xournal_page_scale_factor
        top    = float(image.attrib['top'])    / self.xournal_page_scale_factor
        bottom = float(image.attrib['bottom']) / self.xournal_page_scale_factor
        image = base64.b64decode(image.text)
        uuid = self._random_uuid()
        return Image(uuid, left, top, bottom, right, True, image)

    def get_page(self, n):
        xoj_page = self._pages[n]
        strokes = []
        lines = []
        for xoj_stroke in xoj_page.iter('stroke'):
            stroke = self._parse_stroke(xoj_stroke)
            if isinstance(stroke, Stroke):
                strokes.append(stroke)
            if isinstance(stroke, Line):
                lines.append(stroke)
        images = []
        for xoj_image in xoj_page.iter('image'):
            image = self._parse_image(xoj_image)
            images.append(image)
        aspect_ratio_A4 = 1.0/math.sqrt(2)
        return Page(n, self._random_uuid(), aspect_ratio_A4, strokes, lines, images)



    
