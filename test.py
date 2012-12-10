#!/usr/bin/env python

import doctest
import sys

sys.path.append('src')



def run_doctests():
    from quill.importer.quill_importer import QuillImporter
    infile = 'test/Example_Notebook.quill'
    imp = QuillImporter(infile)
    book = imp.get_book()
    page = book.get_page(0)
    import quill.importer.base
    doctest.testmod(quill.importer.base, globs={'sample_importer': imp})
    import quill.book
    doctest.testmod(quill.book, globs={'sample_book': book})
    import quill.page
    doctest.testmod(quill.page, globs={'sample_page': page})
    import quill.graphics_object
    doctest.testmod(quill.graphics_object, globs={'sample_stroke': page.strokes()[0]})
    import quill.stroke
    doctest.testmod(quill.stroke, globs={'sample_stroke': page.strokes()[0]})
    import quill.image
    doctest.testmod(quill.image, globs={'sample_image': page.images()[0]})

    import quill.exporter.base
    doctest.testmod(quill.exporter.base, globs={'sample_book': book})
    import quill.exporter.base2
    doctest.testmod(quill.exporter.base2, globs={'sample_book': book})
    import quill.exporter.pdf
    doctest.testmod(quill.exporter.pdf, globs={'sample_book': book})
    import quill.exporter.ps
    doctest.testmod(quill.exporter.ps, globs={'sample_book': book})
    import quill.exporter.svg
    doctest.testmod(quill.exporter.svg, globs={'sample_book': book})
    import quill.exporter.xournal
    doctest.testmod(quill.exporter.xournal, globs={'sample_book': book})


if __name__ == '__main__':
    run_doctests()



