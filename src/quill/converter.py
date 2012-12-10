"""
Convert notebook files
"""


class QuillConverter(object):

    def __init__(self, in_filename, out_filename):
        self._infile = in_filename
        self._outfile = out_filename
        self._imp_class = self._init_importer()
        self._exp_class = self._init_exporter()

    def _init_importer(self):
        f = self._infile.lower()
        if f.endswith('.quill'):
            from quill.importer.quill_importer import QuillImporter
            return QuillImporter
        raise NotImplementedError('cannot import '+self._infile)

    def _init_exporter(self):
        f = self._outfile.lower()
        if f.endswith('.svg'):
            from quill.exporter.svg import Svg
            return Svg
        if f.endswith('.pdf'):
            from quill.exporter.pdf import Pdf
            return Pdf
        if f.endswith('.ps'):
            from quill.exporter.ps import Postscript
            return Postscript
        if f.endswith('.xoj'):
            from quill.exporter.xournal import Xournal
            return Xournal
        raise NotImplementedError('cannot export '+self._outfile)
    
    def run(self, page_number=None):
        imp = self._imp_class(self._infile)
        exp = self._exp_class(self._outfile)
        book = imp.get_book()
        exp.set_page_numbers(page_number)
        exp.book(book)
