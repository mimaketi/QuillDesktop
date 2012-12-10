#!/usr/bin/env python

import sys
sys.path.append('src')

try:
    import pygtk
    pygtk.require('2.0')
except:
    print 'You need PyGTK version 2 or higher!'
    sys.exit(1)

try:
    import gtk
    import gtk.glade
except:
    print 'You need the Python Glade interface!'
    sys.exit(1)

try:
    import cairo
except:
    print 'You need the Python Cairo interface!'
    sys.exit(1)


import os
app_home_dir = os.getcwd()
print 'App home dir = '+app_home_dir

if __name__ == '__main__':
    from quill.gui.app import Application
    app = Application(app_home_dir)
    gtk.main()






