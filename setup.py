#!/usr/bin/python

from distutils.core import setup


setup(name='QuillDesktop',
      version='0.1',
      description = "A Desktop Companion for the Quill Android App",
      author = "Volker Braun",
      author_email = "vbraun.name@gmail.com",
      url = "https://github.com/vbraun/QuillDesktop",
      package_dir={'quill': 'src/quill'},
      packages=['quill',
                'quill.gui', 
                'quill.importer',
                'quill.exporter'],
      )
