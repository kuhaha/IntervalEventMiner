# -*- coding: utf-8 -*-

class Event(object):
    def __init__(self, etype, start, end):
        self.etype = etype
        self.start = start
        self.end = end
        self.width = self.end - self.start

    def __eq__(self, that):
        return self.etype == that.etype and self.start == that.start and self.end == that.end

    def __str__(self):
        return "({};[{}, {}])".format(self.etype, self.start, self.end)


def from_list(el):
    ret = [Event(t[0], t[1], t[2]) for t in el]
    return ret
