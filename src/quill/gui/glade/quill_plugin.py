#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Add our custom widget to glade3
"""

import os
import sys


print 'quill_plugin imported'

gui_path = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(gui_path)
quill_path = os.path.split(os.path.split(gui_path)[0])[0]
sys.path.append(quill_path)

for p in sys.path:
    print p

from page_widget import PageWidget


