.. _code:

Programmers Guide
=================

Notebook Data Model
-------------------

The data is abstracted away from any particular file
presentation. Importers and exporters (see below) convert other file
formats into/from the data model.

Quill uses a coordinate system with points :math:`(x,y)` such that:

* The orgin is at the top left
* Off-page coordinates are allowed
* The points on the page satisfy :math:`y\in [0,1]` and :math:`x \in
  [0,\xi]` where :math:`\xi` is the
  :meth:`~quill.page.Page.aspect_ratio`.

The data is organized as follows. The :class:`~quill.book.Book` class
contains metadata and a list of pages. Each :class:`~quill.page.Page`
contains the paper data and a list of all graphics objects on the
page. The following modules implement these:

.. toctree::
   :maxdepth: 2

   quill.book
   quill.page
   quill.stroke
   quill.image


Importing Files
---------------

To create a new importer you should create a new module in
``src/quill/importer`` and derive from
:class:`quill.importer.base.ImporterBase`. Its documentation will tell
you which methods to override. An importer is essentially a factory
object for the data model objects, so you will have to flesh it out by
implementing functions that read your own fileformat and create the
corresponding :mod:`~quill.book` object.

.. toctree::
   :maxdepth: 2

   quill.importer.base
   quill.importer.quill_importer



Exporting Files
---------------

To create a new importer you should create a new module in
``src/quill/importer`` and derive from
:class:`quill.exporter.base.ExporterBase`. Its documentation will tell
you which methods to override. An exporter converts the notebook data
model objects into your own file format, and does not have any access
to the original (imported) file.

.. toctree::
   :maxdepth: 2

   quill.exporter.base
   quill.exporter.base2
   quill.exporter.cairo_context
   quill.exporter.cairo_surface_paginated
   quill.exporter.svg
   quill.exporter.pdf
   quill.exporter.ps


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

