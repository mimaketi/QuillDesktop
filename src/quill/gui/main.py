"""
The main application window
"""

import os
import gtk
import gtk.glade

from gui import viewer

class MainWindow:
    """
    The main window
    """
    
    def __init__(self, application):
        self.app = application
        self.window = self.app.builder.get_object('main')
        vbox = self.app.builder.get_object('main-box')
        vbox.pack_start(Viewer(), True, True, 2)
        print 'Main', vbox
        self.app.builder.connect_signals(self)       

    def on_main_destroy(self, widget, data=None):
        self.app.destroy()
     
    def on_menuitem_about_activate(self, widget, data=None):
        print 'about'
        self.app.show_about_dialog()
        
