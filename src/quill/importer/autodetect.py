"""
Automatically Detect Importer from File Extension
"""

import os

from quill.importer.base import QuillImporterError


def autodetect_importer(filename):
    f = filename.lower()
    if f.endswith('.note'):
        from quill.importer.quill_importer import QuillImporter
        return QuillImporter(filename)
    if f.endswith('.xoj'):
        from quill.importer.xournal import Xournal
        return Xournal(filename)
    ext = os.path.splitext(filename)[-1]
    raise QuillImporterError('unknown import file extension (*' + ext + ')')

