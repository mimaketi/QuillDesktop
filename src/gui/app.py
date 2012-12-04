"""
The main application window
"""

import os
import gtk
import pango
import gtk.glade
from main import MainWindow
from about import AboutDialog
from log import Logger

class Application:
    """
    The Quill convert app window
    """
    
    def __init__(self, app_home_dir):
        self.home_dir = app_home_dir
        gladefile = os.path.join(self.home_dir, 'res', 'QuillConvert.xml')
        builder = gtk.Builder()
        builder.add_from_file(gladefile)
        self.window = builder.get_object('main')
        self.text   = builder.get_object('main-text')
        self.about  = builder.get_object('about')
        self.button = builder.get_object('button')
        self.status = builder.get_object('main-statusbar')
        builder.connect_signals(self)
        self.window.show()

    def on_main_destroy(self, widget, data=None):
        gtk.main_quit()
     
    def on_menuitem_about_activate(self, widget, data=None):
        self.about.show()

    def on_about_destroy(self, widget, data=None):
        self.about.hide()

    def on_about_response(self, widget, data=None):
        self.about.hide()

