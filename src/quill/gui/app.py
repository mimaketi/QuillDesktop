"""
The main application window
"""

import os
import sys
import gtk
import pango
import gtk.glade
import pkgutil

from about import AboutDialog
from page_widget import PageWidget

from quill.importer.base import QuillImporterError
from quill.exporter.base import QuillExporterError
from quill.importer.autodetect import autodetect_importer
from quill.exporter.autodetect import autodetect_exporter


class Application:
    """
    The Quill convert app window
    """
    
    def __init__(self, filename=None):
        self._home_dir = d = os.path.dirname(sys.modules['quill'].__file__)
        gladefile = os.path.join(self._home_dir, 'res', 'QuillDesktop.xml')
        builder = gtk.Builder()
        builder.add_from_file(gladefile)
        self.window = builder.get_object('main')
        self.viewer = builder.get_object('main-page_viewer')
        self.status = builder.get_object('main-statusbar')
        self.dlg_error = builder.get_object('error_dialog')
        self.dlg_about = builder.get_object('about')
        self.dlg_open  = builder.get_object('filechooser-open')
        self.dlg_save  = builder.get_object('filechooser-save')
        builder.connect_signals(self)
        self._book = None
        if filename is not None:
            self.open_file(filename)
        self.window.show()

    def error(self, msg, title='Error:'):
        dlg = self.dlg_error
        dlg.set_markup('<span size="large"><b>'+title+'</b></span>')
        dlg.format_secondary_text(msg)
        self.set_status(title + ' ' + msg)
        dlg.run()

    def on_error_dialog_response(self, widget, data=None):
        self.dlg_error.hide()

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
        url = "http://vbraun.github.com/QuillDesktop"
        import webbrowser
        webbrowser.open(url, new=2)

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
        self.set_status('open')
        self.dlg_open.hide()
        if data==0:
            filename = widget.get_filename()
            self.open_file(filename)

    def on_filechooser_save_response(self, widget, data=None):
        self.set_status('save')
        self.dlg_save.hide()
        if data==0:
            filename = widget.get_filename()
            self.save_file(filename)
            
    def open_file(self, filename):
        self._file = filename
        try:
            imp = autodetect_importer(self._file)
            book = self._book = imp.get_book()
        except QuillImporterError as e:
            self.error(str(e), title='Error importing file:')
            return
        self.viewer.set_book(book)
        self.set_status('Opened '+filename)

    def save_file(self, filename):
        try:
            exp = autodetect_exporter(filename)
            if not exp.is_multipage():
                exp.set_page_numbers(self.viewer.page_number())
            exp.book(self._book)
        except QuillExporterError as e:
            self.error(str(e), title='Error exporting file:')
            return
        self.set_status('Saved '+filename)
        
    


