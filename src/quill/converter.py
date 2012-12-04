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
        raise NotImplemented('cannot import '+self._infile)

    def _init_importer(self):
        f = self._infile.lower()
        if f.endswith('.svg'):
            from quill.exporter.svg import SvgExporter
            return SvgExporter
        if f.endswith('.pdf'):
            from quill.exporter.pdf import PdfExporter
            return PdfExporter
        raise NotImplemented('cannot export '+self._outfile)
    

    def run(self):
        imp = self._imp_class(self._infile)
        exp = self._exp_class(self._outfile)
        for page in imp:
            exp.save(page)
        imp.close()
        exp.close()
