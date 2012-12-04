

class Logger(object):
    def __init__(self, recipient, tag):
        self.recipient = recipient
        self.tag = tag

    def add(self, msg):
        self.msg = msg
        self.recipient.add_log(self)
        

