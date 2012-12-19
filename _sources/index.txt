.. Quill Desktop documentation master file, created by
   sphinx-quickstart on Sun Dec  9 15:37:30 2012.

Welcome to Quill Desktop's documentation!
=========================================

Quill is an open-source handwriting note-taking app for Android
tablets. This program is a desktop companion for it. It lets you view
``.quill`` backup files without your Android device, and/or convert
them to different formats.

* GitHub project page: https://github.com/vbraun/QuillDesktop/
* This documentation: http://vbraun.github.com/QuillDesktop/

If you are looking for Quill the Android app:

* Google play market: https://market.android.com/details?id=com.write.Quill
* Google code project page: http://code.google.com/p/android-quill/


Use as a GUI Viewer
-------------------

This program is as PyGTK application, so it will run on pretty much
any platform if you have GTK, PyGTK, and PyCairo installed. Use the
``--gui`` switch to show the graphical user interface.

EXAMPLES::

    [user@localhost]$ quill --gui


.. image:: screenshot.png
    :align: center
    :alt: Sceenshot of the GUI


Use as a Command-Line Converter
-------------------------------

If you specify input and output filename. The format is automatically
detected from the file extension.

EXAMPLES::

    [user@localhost]$ quill input.quill output.pdf

Possible input file formats are:

* ``input.xoj``: Xournal (http://xournal.sourceforge.net)
* ``input.quill``: Quill's own file format

Possible output file formats are:

* ``output.pdf``: portable document format (PDF)
* ``output.ps``: Postscript (PS)
* ``output.svg``: scalable vector graphics (SVG)
* ``output.xoj``: Xournal's file format
* ``output.quill``: Quill's own file format


Programmers Guide
-----------------

Want to add support for your favorite file format? Head over to the
:ref:`code` and find out how!


Authors
-------

* Volker Braun: Framework, GUI, more export file formats.
* Nicholas A. Knouf (http://zeitkunst.org): Initial quill to SVG
  converter.
* Yuri Shirman: Xournal export


License
-------

GPL v3


Table of Contents
-----------------

.. toctree::

    code
