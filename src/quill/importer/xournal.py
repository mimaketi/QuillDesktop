"""
Import Xournal notebook

EXAMPLES::

    >>> print sample_importer    # doctest: +ELLIPSIS
    <quill.importer.xournal.Xournal object at 0x...>
"""

import gzip

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


from quill.importer.base import ImporterBase, QuillImporterError


class Xournal(ImporterBase):
    
    def __init__(self, xournal_filename):
        self._filename = xournal_filename
        f = gzip.open(xournal_filename, 'rb')
        self._tree = ET.ElementTree(file=f)
        self._pages = [ page for page in self._tree.iter(tag='page') ]

    def n_pages(self):
        return len(self._pages)
    
    def get_page(self, n):
        page = self._pages[n]
        for stroke in page.iter(tag='stroke'):
            print stroke.tag, stroke.attrib
            



    
