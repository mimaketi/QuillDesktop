"""
Convert notebook files
"""

from quill.importer.autodetect import autodetect_importer
from quill.exporter.autodetect import autodetect_exporter


class QuillConverter(object):

    def __init__(self, in_filename, out_filename):
        self._infile = in_filename
        self._outfile = out_filename
        self._imp_class = autodetect_importer(in_filename)
        self._exp_class = autodetect_exporter(out_filename)

    def run(self, page_number=None):
        imp = self._imp_class(self._infile)
        exp = self._exp_class(self._outfile)
        book = imp.get_book()
        exp.set_page_numbers(page_number)
        exp.book(book)
