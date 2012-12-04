#!/usr/bin/env python

import sys
sys.path.append('src')



if __name__ == '__main__':
    
    from quill.importer.quill_importer import QuillImporter
    from quill.book import Book
    infile = 'test/dcfb8a4d-b6ad-41db-acfc-a6b8c8dd0c63.quill'
    imp = QuillImporter(infile)
    book = Book(imp)
    print book 

    #from quill.converter import QuillConverter
    #infile = 'test/dcfb8a4d-b6ad-41db-acfc-a6b8c8dd0c63.quill'
    #outfile = '/tmp/quill_convert_output.pdf'
    #QuillConverter(infile, outfile).run()






