"""
Automatically Detect Importer from File Extension
"""

from quill.importer.base import QuillImporterError


def autodetect_importer(filename):
    f = filename.lower()
    if f.endswith('.quill'):
        from quill.importer.quill_importer import QuillImporter
        return QuillImporter(filename)
    if f.endswith('.xoj'):
        from quill.importer.xournal import Xournal
        return Xournal(filename)
    raise QuillImporterError('cannot import '+filename)

