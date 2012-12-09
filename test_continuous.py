#!/usr/bin/env python

import doctest
import sys
import time
import os

sys.path.append('src')

import os
from pyinotify import WatchManager, Notifier, ThreadedNotifier, EventsCodes, ProcessEvent


class PTmp(ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print '='*79
        print 'Wrote: %s' %  os.path.join(event.path, event.name)
        time.sleep(0.5)
        os.system('./test.py')


def inotify_watch():
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

if __name__ == '__main__':
    inotify_watch()



