#!/usr/bin/env python

import doctest
import sys

sys.path.append('src')

try:
    import os
    from pyinotify import WatchManager, Notifier, ThreadedNotifier, EventsCodes, ProcessEvent
    HAVE_PY_INOTIFY = True
except ImportError:
    HAVE_PY_INOTIFY = False




def inotify_watch():

    class PTmp(ProcessEvent):
        def process_IN_CLOSE_WRITE(self, event):
            print "Wrote: %s" %  os.path.join(event.path, event.name)
            run()

    wm = WatchManager()
    mask = EventsCodes.ALL_FLAGS['IN_CLOSE_WRITE']
    wdd = wm.add_watch('src', mask, rec=True)
    notifier = Notifier(wm, PTmp())
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break


import quill.importer.base
import quill.book

def run():
    from quill.importer.quill_importer import QuillImporter
    infile = 'test/Example_Notebook.quill'
    imp = QuillImporter(infile)
    book = imp.get_book()
    reload(quill.importer.base)
    doctest.testmod(quill.importer.base, globs={'sample_importer': imp})
    reload(quill.book)
    doctest.testmod(quill.book, globs={'sample_book': book})
    


if __name__ == '__main__':
    inotify_watch()

    #$run()



