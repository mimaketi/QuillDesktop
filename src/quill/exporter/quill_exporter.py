"""
Export to Quill

EXAMPLES::

    >>> from quill.exporter.quill_exporter import QuillExporter
    >>> from tempfile import mkstemp
    >>> _, tmp = mkstemp()
    >>> exporter = QuillExporter(tmp)
    >>> exporter.book(sample_book)
    
    >>> import os
    >>> os.path.getsize(tmp)
    >>> import tarfile
    >>> tarfile.TarFile(tmp).getmembers()
    >>> os.unlink(tmp)
"""


import tarfile
import struct

from quill.exporter.base2 import ExporterBase2



class QuillExporter(ExporterBase2):
    
    def __init__(self, filename):
        """
        The Python constructor
        """
        self._output = filename

    def title(self, title):
        self._title = title

    def uuid(self, uuid):
        self._uuid = uuid

    def creation_time(self, ctime, ctime_millis):
        self._ctime = ctime_millis

    def modification_time(self, mtime, mtime_millis):
        self._mtime = mtime_millis

    def begin_export(self):
        self._tar = tarfile.TarFile(self._output, mode='w')
        self._index = ''
        self._page = None
        self._page_list = []

    def end_export(self):
        self._tar.close()

    def _add(self, arcname, data):
        nb_dir = 'notebook_'+self._uuid
        name = nb_dir + '/' + arcname
        info = self._tar.gettarinfo(arcname=name)
        self._tar.add_file(info, data)

    def _save_index(self):
        name = 'index.quill_data'

    def _save_page(self, data, page):
        name = 'page_' + page.uuid() + '.quill_data'
        self._add(name, data)
        self._page_list.append(page.uuid())

    def _pack_uuid(self, uuid):
        uuid = str(uuid)
        assert len(uuid)==36
        return struct.pack('<h', 36) + uuid

    def _pack_image(self, image):
        out = ''
        out += struct.pack('>i', 1)   # version
        out += self._pack_uuid(image.uuid())
        out += struct.pack('>ffff', image.x0(), image.x1(), image.y0(), image.y1())
        out += struct.pack('>?', image.constrain_aspect())
        return out
        
    def _pack_line(self, line):
        out = ''
        out += struct.pack('>i', 1)   # version
        color = (0xff << 24) + (line.red() << 16) + (line.green() << 8) + line.blue()
        print color, line.red(), line.green(), line.blue()
        out += struct.pack('>I', color)
        out += struct.pack('>i', line.thickness())
        out += struct.pack('>i', 5)
        out += struct.pack('>ffff', line.x0(), line.x1(), line.y0(), line.y1())
        return out
        
    def _pack_stroke(self, stroke):
        out = ''
        out += struct.pack('>i', 2)   # version
        color = (0xff << 24) + (stroke.red() << 16) + (stroke.green() << 8) + stroke.blue()
        out += struct.pack('>I', color)
        out += struct.pack('>i', stroke.thickness())
        if stroke.has_pressure():
            out += struct.pack('>i', 0)    # fountain pen tool
        else:
            out += struct.pack('>i', 1)    # pencil tool
        out += struct.pack('>i', stroke.n_points())
        for i in xrange(stroke.n_points()):
            p = stroke.get_point(i)
            out += struct.pack('>fff', *p)
        return out
        
    def page(self, page):
        out = ''
        out += struct.pack('>i', 6)   # version
        out += self._pack_uuid(self._uuid)
        out += struct.pack('>i', 1)   # tag version

        # TODO: save tags
        out += struct.pack('>i', 0)   # number of tags
        
        out += struct.pack('>i', 0)    # dummy1
        out += struct.pack('>i', 0)    # dummy2
        
        # TODO: preserve background
        out = struct.pack('>i', 0)    # paper type

        out += struct.pack('>i', len(page.images()))
        for image in page.images():
            out += self._pack_image(image)
        out += struct.pack('>i', 0)    # dummy
        out += struct.pack('>?', False)    # read only
        out += struct.pack('>f', page.aspect_ratio())
        out += struct.pack('>i', len(page.lines()))
        for line in page.lines():
            out += self._pack_line(line)
        out += struct.pack('>i', len(page.strokes()))
        for stroke in page.strokes():
            out += self._pack_stroke(stroke)
        out += struct.pack('>i', 0)   # dummy
        out += struct.pack('>i', 0)   # number of text boxes
        self._save_page(out, page)

