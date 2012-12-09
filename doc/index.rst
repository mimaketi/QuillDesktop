.. Quill View/Converter documentation master file, created by
   sphinx-quickstart on Sun Dec  9 15:37:30 2012.

Welcome to Quill View/Converter's documentation!
================================================

Quill is an open-source handwriting note-taking app for Android
tablets. This program lets you view ``.quill`` backup files on your
desktop, and/or convert them to different formats. 

* Google play market: https://market.android.com/details?id=com.write.Quill
* Google code project page: http://code.google.com/p/android-quill/


Use as a GUI Viewer
-------------------

This program is as PyGTK application, so it will run on pretty much
any platform if you have GTK, PyGTK, and PyCairo installed. Use the
``--gui`` switch to show the graphical user interface.

EXAMPLES::

    [user@localhost]$ quill --gui


Use as a Command-Line Converter
-------------------------------

If you specify input and output filename then the 

EXAMPLES::

    [user@localhost]$ quill file.quill file.pdf


Programmers Guide
-----------------

Want to add support for your favorite file format? Head over to the
:ref:`code` and find out how!


Authors
-------

* Volker Braun
* Nicholas A. Knouf (http://zeitkunst.org)


License
-------

GPL v3


Table of Contents
-----------------

.. toctree::

    code
