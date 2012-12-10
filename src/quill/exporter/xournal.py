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
    xournal_pen_scale_factor=820
    xournal_x_offset=0
    xournal_y_offset=0

    def new_page(self, page):
        h = self._height = self.xournal_pen_scale_factor
        w = self._width = h * page.aspect_ratio()
        f = self._fileobj
        if not self._first:
            f.write("</layer>"+"\n"+"</page>"+"\n\n")
        self._first = False
        f.write("<page width=\""+str(self._width)+"\" height=\""+str(self._height)+'">\n')
        f.write("<background type=\"solid\" color=\"white\" style=\"lined\" />"+"\n"+"<layer>\n")


    def stroke(self, stroke):
        f = self._fileobj
        # Define RGB color for xournal; setting alpha=1 for now
        color="#"+"{:02x}".format(stroke.red())+"{:02x}".format(stroke.green())+"{:02x}".format(stroke.blue())+"ff"
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
        f.write(str(self.xournal_pen_scale_factor*stroke.get_point(0)[0])+ " "+ 
                str(self.xournal_pen_scale_factor*stroke.get_point(0)[1]+self.xournal_y_offset))
        for point in xrange(stroke.n_points()-1):
            f.write(" "+
                    str(self.xournal_pen_scale_factor*stroke.get_point(point)[0])+" "+ 
                    str(self.xournal_pen_scale_factor*stroke.get_point(point)[1]+self.xournal_y_offset))
        f.write("</stroke>\n")

    def image(self, image):
        pass
