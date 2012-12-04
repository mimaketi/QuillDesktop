"""
The about dialog
"""
import gtk

class AboutDialog:
    """
    The about dialog box
    """
    
    def __init__(self, application):
        self.app = application
        self.window  = self.app.builder.get_object("about")
        self.app.builder.connect_signals(self)       

