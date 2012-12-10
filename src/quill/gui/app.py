"""
The main application window
"""

import os
import gtk
import pango
import gtk.glade

from about import AboutDialog
from page_widget import PageWidget


class Application:
    """
    The Quill convert app window
    """
    
    def __init__(self, app_home_dir, filename=None):
        self.home_dir = app_home_dir
        gladefile = os.path.join(self.home_dir, 'res', 'QuillDesktop.xml')
        builder = gtk.Builder()
        builder.add_from_file(gladefile)
        self.window = builder.get_object('main')
        self.viewer = builder.get_object('main-page_viewer')
        if filename is not None:
            self.viewer.set_file(filename)
        self.status = builder.get_object('main-statusbar')
        self.dlg_about = builder.get_object('about')
        self.dlg_open  = builder.get_object('filechooser-open')
        self.dlg_save  = builder.get_object('filechooser-save')
        builder.connect_signals(self)
        self.window.show()

    def log(self, msg):
        print 'Log:', msg

    def set_status(self, msg, context='default'):
        context = self.status.get_context_id(context)
        self.status.pop(context)
        self.status.push(context, msg)

    def on_main_destroy(self, widget, data=None):
        gtk.main_quit()
     
    def on_menuitem_about_activate(self, widget, data=None):
        self.dlg_about.run()

    def on_about_response(self, widget, data=None):
        self.dlg_about.hide()

    def on_menuitem_manual_activate(self, widget, data=None):
        print 'See manual'

    def on_menuitem_open_activate(self, widget, data=None):
        self.dlg_open.run()

    def on_menuitem_save_activate(self, widget, data=None):
        self.dlg_save.run()

    def on_toolbutton_open_clicked(self, widget, data=None):
        self.dlg_open.run()

    def on_toolbutton_save_clicked(self, widget, data=None):
        self.dlg_save.run()

    def on_toolbutton_prev_clicked(self, widget, data=None):
        self.viewer.prev_page()

    def on_toolbutton_next_clicked(self, widget, data=None):
        self.viewer.next_page()

    def on_filechooser_open_response(self, widget, data=None):
        print 'open response', widget, data
        self.set_status('open')
        self.dlg_open.hide()
        if data==0:
            filename = widget.get_filename()
            print filename
            self.viewer.set_file(filename)

    def on_filechooser_save_response(self, widget, data=None):
        print 'save response', widget, data
        self.set_status('save')
        self.dlg_save.hide()
        if data==0:
            filename = widget.get_filename()
            print filename


    

