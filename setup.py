#!/usr/bin/python

import os

from distutils.core import setup


setup(name='QuillDesktop',
      version='0.1',
      description = "A Desktop Companion for the Quill Android App",
      author = "Volker Braun",
      author_email = "vbraun.name@gmail.com",
      url = "https://github.com/vbraun/QuillDesktop",
      package_dir={'quill': os.path.join('src', 'quill')},
      package_data={'quill': ['res/QuillDesktop.xml',
                              'res/icons/*',
                              'res/about/*']}, 
      packages=['quill',
                'quill.gui', 
                'quill.importer',
                'quill.exporter'],
      scripts=['quill'],
      license='GNU GPLv3',
      )
