"""
Xournal export

This is a hacky first approach. Should use some xml library to
generate the output, of course.

EXAMPLES::

    >>> from quill.exporter.xournal import Xournal
    >>> from tempfile import TemporaryFile
    >>> tmp = TemporaryFile(suffix='pdf')
    >>> Xournal(tmp).book(sample_book)
"""

import gzip
import math
import base64

from quill.exporter.base2 import ExporterBase2



class Xournal(ExporterBase2):
    
    def __init__(self, fileobj):
        self._fileobj = fileobj

    def title(self, title):
        f = self._fileobj
        f.write("<title>"+title+"</title>"+"\n")
        pass

    def uuid(self, uuid):
        pass

    def creation_time(self, ctime, ctime_millis):
        pass

    def modification_time(self, mtime, mtime_millis):
        pass

    def begin_export(self):
        self._first = True
        f = self._fileobj
        if isinstance(f, basestring):
            f = self._fileobj = gzip.open(f, 'wb')
        f.write("<?xml version=\"1.0\" standalone=\"no\"?>"+"\n"+
                "<xournal version=\"0.4.7\">"+"\n"+
                "<!-- Xournal document, converted from Quill -->"+"\n")

    def end_export(self):
        f = self._fileobj
        if not self._first:
            f.write("</layer>"+"\n"+"</page>"+"\n\n")
        del self._first
        f.write("</xournal>")
        f.close()

    quill_pen_scale_factor = float(1600.0)
    xournal_pen_thickness_factor=0.5
    xournal_page_scale_factor=820
    xournal_x_offset=0
    xournal_y_offset=0

    def new_page(self, page):
        h = self._height = self.xournal_page_scale_factor
        w = self._width = int(h * page.aspect_ratio())
        f = self._fileobj
        if not self._first:
            f.write("</layer>"+"\n"+"</page>"+"\n\n")
        self._first = False
        f.write("<page width=\""+str(self._width)+"\" height=\""+str(self._height)+'">\n')
        f.write("<background type=\"solid\" color=\"white\" style=\"lined\" />"+"\n"+"<layer>\n")


    def stroke(self, stroke):
        f = self._fileobj
        # Define RGB color for xournal; setting alpha=1 for now
        color = "#{0:02x}{1:02x}{2:02x}ff".format(
            stroke.red(), stroke.green(), stroke.blue())
        f.write("<stroke tool=\"pen\" color=\"")
        f.write(color)
        f.write("\" width=\"")
        if stroke.has_pressure():
            thickness = self.xournal_pen_thickness_factor * stroke.thickness()
            f.write(str(thickness*stroke.get_point(0)[2]))
            for point in xrange(stroke.n_points()-1):
                f.write(" "+str(thickness*stroke.get_point(point)[2]))
        else:
            f.write(str(self.xournal_pen_thickness_factor*stroke.thickness()))
        f.write("\">\n")
        f.write(str(self.xournal_page_scale_factor*stroke.get_point(0)[0])+ " "+ 
                str(self.xournal_page_scale_factor*stroke.get_point(0)[1]+self.xournal_y_offset))
        for point in xrange(stroke.n_points()-1):
            f.write(" "+
                    str(self.xournal_page_scale_factor*stroke.get_point(point)[0])+" "+ 
                    str(self.xournal_page_scale_factor*stroke.get_point(point)[1]+self.xournal_y_offset))
        f.write("</stroke>\n")

    def line(self, line):
	f = self._fileobj
        color = "#{0:02x}{1:02x}{2:02x}ff".format(
            line.red(), line.green(), line.blue())
        f.write("<stroke tool=\"pen\" color=\"")
        f.write(color)
        f.write("\" width=\"")
        f.write(str(self.xournal_pen_thickness_factor*line.thickness()))
	f.write("\">\n")
        x_start = line.x0()*self.xournal_page_scale_factor
        y_start = line.y0()*self.xournal_page_scale_factor
        x_end = line.x1()*self.xournal_page_scale_factor
        y_end = line.y1()*self.xournal_page_scale_factor
#        x_point = x_start
#        y_point = y_start
#        length = math.sqrt((x_end-x_start)**2+(y_end-y_start)**2)
#        steps = int(length/3)
#	dx = 3 * (x_end-x_start)/length
#	dy = 3 * (y_end-y_start)/length
#	for n in range(0,steps):
#	    f.write(str(x_point)+" "+str(y_point+self.xournal_y_offset)+" ")
#	    x_point = x_point + dx
#	    y_point = y_point + dy
        f.write(str(x_start)+" "+str(y_start+self.xournal_y_offset)+" "+str(x_end)
                +" "+str(y_end+self.xournal_y_offset)+"\n</stroke>\n")
#	f.write(str(x_end)+" "+str(y_end+self.xournal_y_offset)+"\n</stroke>\n ")


    def image(self, image):
        f = self._fileobj
        image_base64 = base64.b64encode(image.data())
        f.write("<image left=\""+str(self.xournal_page_scale_factor*image.x0())+"\" top=\""
                +str(self.xournal_page_scale_factor*image.y0())+"\" right=\""+
                str(self.xournal_page_scale_factor*image.x1())+"\" bottom=\""
                +str(self.xournal_page_scale_factor*image.y1())+"\">")
        f.write(image_base64)
        f.write("</image>")
        
