"""
The main application window
"""

import os
import gtk
import gtk.glade

class MainWindow:
    """
    The main window
    """
    
    def __init__(self, application):
        self.app = application
        self.window = self.app.builder.get_object("main")
        self.app.builder.connect_signals(self)       

    def on_main_destroy(self, widget, data=None):
        self.app.destroy()
     
    def on_menuitem_about_activate(self, widget, data=None):
        self.app.show_about_dialog()
        
