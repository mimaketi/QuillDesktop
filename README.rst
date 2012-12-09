Quill Converter
===============

A program to view and convert Quill files
(https://code.google.com/p/android-quill/).


Usage
=====

run.py -f FILENAME

This is take a given Quill file (with .quill extension), create a new
directory based on the name of the notebook, and generate a set of
SVGs for each page. Converting this into a PDF can then be done with a
separate program.


Caveats
=======

The GUI requires the Python GTK, cairo, and glade bindings to be
installed. Export to PDF/SVG requires cairo. Import/export of other
file formats only needs Python.

This was done quickly and does not have as much error checking as there should be.

The script doesn't currently deal with earlier Quill formats.

The script doesn't deal with line art.


TODO
====

* Better error handling

* Incorporate tags into SVG metadata

* Deal with aspect ratios

* Deal with line art

* Deal with images

* Deal with earlier quill formats


Authors
=======

* Nicholas A. Knouf (http://zeitkunst.org)
* Volker Braun


License
=======

GPL v3
