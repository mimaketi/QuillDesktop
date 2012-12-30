"""
Handle Command Line Options and Launch Quill
"""

import sys
import os


def check_gui_prerequisites():
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


def launch_gui(filename=None):
    check_gui_prerequisites()
    import gtk
    from quill.gui.app import Application
    app = Application(filename)
    gtk.main()


description = """
    Quill is an open-source handwriting note-taking app for Android
    tablets. This program is a desktop companion for it. It lets you
    view ``.quill`` backup files without your Android device, and/or
    convert them to different formats."""



def launch():
    from argparse import ArgumentParser
    parser = ArgumentParser(description=description)
    parser.add_argument('input',
                        help='input file name', default=None, nargs='?')
    parser.add_argument('output',
                        help='output file name', default=None, nargs='?')
    parser.add_argument('-p', '--page', dest='page', action='store',
                        default=None, type=int,
                        help='page number to export (default: all pages)')
    parser.add_argument('--gui', dest='gui', action='store_true',
                        default=True, 
                        help='start the gui')
    args = parser.parse_args()
    
    if args.input is not None and args.output is not None:
        from quill.converter import QuillConverter
        QuillConverter(args.input, args.output).run(args.page)

    if args.gui:
        launch_gui(args.input)
