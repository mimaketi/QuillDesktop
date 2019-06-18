"""
Automatically Detect Exporter from File Extension
"""

import os

from quill.exporter.base import QuillExporterError


def autodetect_exporter(filename):
    f = filename.lower()
    if f.endswith('.svg'):
        from quill.exporter.svg import Svg
        return Svg(filename)
    if f.endswith('.pdf'):
        from quill.exporter.pdf import Pdf
        return Pdf(filename)
    if f.endswith('.ps'):
        from quill.exporter.ps import Postscript
        return Postscript(filename)
    if f.endswith('.xoj'):
        from quill.exporter.xournal import Xournal
        return Xournal(filename)
    if f.endswith('.note'):
        from quill.exporter.quill_exporter import QuillExporter
        return QuillExporter(filename)
    ext = os.path.splitext(filename)[-1]
    raise QuillImporterError('unknown export file extension (*' + ext + ')')

