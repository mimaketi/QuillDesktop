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
    >>> info = [ (t.name, t.size) for t in tarfile.TarFile(tmp).getmembers() ]
    >>> info.sort()
    >>> for name, size in info: print os.path.split(name)[-1], size
    index.quill_data 198
    page_5f55aaab-d1a6-4485-8c60-5bb48bea2319.quill_data 91
    page_9aa10c71-c872-4d2b-b97e-1845fd5a4cfc.quill_data 27794
    page_b5786dad-3947-4846-a230-e084d2d9e2c0.quill_data 2255
    >>> os.unlink(tmp)
"""


import tarfile
import struct
import cStringIO

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
        index = self._pack_index()
        self._save_index(index)
        self._tar.close()

    def _add(self, arcname, data):
        nb_dir = 'notebook_'+self._uuid
        name = nb_dir + '/' + arcname
        info = tarfile.TarInfo(name)
        info.size = len(data)
        fileobj = cStringIO.StringIO(data)
        self._tar.addfile(info, fileobj)

    def _save_index(self, data):
        name = 'index.quill_data'
        self._add(name, data)

    def _save_page(self, data, page):
        name = 'page_' + page.uuid() + '.quill_data'
        self._add(name, data)
        self._page_list.append(page.uuid())

    def _pack_uuid(self, uuid):
        r"""
        TESTS::

            >>> from quill.exporter.quill_exporter import QuillExporter
            >>> exp = QuillExporter('')
            >>> exp._pack_uuid('b5786dad-3947-4846-a230-e084d2d9e2c0')
            '$\x00b5786dad-3947-4846-a230-e084d2d9e2c0'
        """
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
        
    def _pack_page(self, page):
        r"""
        TESTS::

            >>> from quill.exporter.quill_exporter import QuillExporter
            >>> exp = QuillExporter('')
            >>> exp.uuid('b5786dad-3947-4846-a230-e084d2d9e2c0')
            >>> exp._pack_page(sample_book.get_page(1))    # doctest: +ELLIPSIS
            '\x00\x00\x00\x06$\x00b5786dad-3947-4846-a230-e084d2d9e...
        """
        out = ''
        out += struct.pack('>i', 6)   # version
        out += self._pack_uuid(page.uuid())
        out += struct.pack('>i', 1)   # tagset version

        # TODO: save tags
        out += struct.pack('>i', 0)   # number of tags
        
        out += struct.pack('>i', 0)    # dummy1
        out += struct.pack('>i', 0)    # dummy2
        
        # TODO: preserve background
        out += struct.pack('>i', 0)    # paper type

        out += struct.pack('>i', len(page.images()))
        for image in page.images():
            out += self._pack_image(image)
        out += struct.pack('>i', 0)    # dummy
        out += struct.pack('>?', False)    # read only
        out += struct.pack('>f', page.aspect_ratio())
        out += struct.pack('>i', len(page.strokes()))
        for stroke in page.strokes():
            out += self._pack_stroke(stroke)
        out += struct.pack('>i', len(page.lines()))
        for line in page.lines():
            out += self._pack_line(line)
        out += struct.pack('>i', 0)   # dummy
        out += struct.pack('>i', 0)   # number of text boxes
        return out

    def page(self, page):
        out = self._pack_page(page)
        self._save_page(out, page)


    def _pack_index(self):
        out = ''
        out += struct.pack(">i", 4)    # version
        out += struct.pack(">i", len(self._page_list))
        for page_uuid in self._page_list:
            out += self._pack_uuid(page_uuid)
        out += struct.pack(">i", 0)   # current page
        out += struct.pack(">h", len(self._title)) + self._title
        out += struct.pack(">q", self._ctime)
        out += struct.pack(">q", self._mtime)
        out += self._pack_uuid(self._uuid)
        return out
