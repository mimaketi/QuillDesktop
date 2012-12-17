"""
Convert notebook files

EXAMPLES::

    >>> from quill.converter import QuillConverter
    >>> import os, tempfile 
    >>> tmpdir = tempfile.mkdtemp()

    >>> pdf = os.path.join(tmpdir, 'output.pdf')
    >>> QuillConverter(quill_file, pdf).run()
    >>> os.path.getsize(pdf)   > 27000
    True

    >>> xoj = os.path.join(tmpdir, 'output.xoj')
    >>> QuillConverter(quill_file, xoj).run()
    >>> os.path.getsize(xoj)
    31787

    >>> svg = os.path.join(tmpdir, 'output.svg')
    >>> QuillConverter(quill_file, svg).run(page_number=0)
    >>> os.path.getsize(svg)
    1334634

    >>> quill = os.path.join(tmpdir, 'output.quill')
    >>> QuillConverter(quill_file, quill).run()
    >>> os.path.getsize(quill)
    122880

    >>> import shutil
    >>> shutil.rmtree(tmpdir)
"""

from quill.importer.autodetect import autodetect_importer
from quill.exporter.autodetect import autodetect_exporter


class QuillConverter(object):

    def __init__(self, in_filename, out_filename):
        self._infile = in_filename
        self._outfile = out_filename
        self._imp = autodetect_importer
        self._exp = autodetect_exporter

    def run(self, page_number=None):
        imp = self._imp(self._infile)
        exp = self._exp(self._outfile)
        book = imp.get_book()
        exp.set_page_numbers(page_number)
        exp.book(book)
