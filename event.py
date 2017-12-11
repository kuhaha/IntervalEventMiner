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

    def getstr(self):
        return str(self.etype)


def from_list(el):
    ret = [Event(t[0], t[1], t[2]) for t in el]
    return ret


import enum
class Relation(enum.Enum):
    Before = 0
    Meet = 1
    Overlap = 2
    Start = 3
    FinishedBy = 4
    Contain = 5
    Equal = 6

    @staticmethod
    def num():
        return 7

    @staticmethod
    def rel2str(rel):
        if rel is Relation.Before:
            return "before"
        elif rel is Relation.Meet:
            return "meet"
        elif rel is Relation.Overlap:
            return "overlap"
        elif rel is Relation.Start:
            return "start"
        elif rel is Relation.FinishedBy:
            return "finished-by"
        elif rel is Relation.Contain:
            return "contain"
        else:
            return "equal"

def relation(e1, e2):
    # Before, Meet, Overlap, Start, Finished-by, Contain, Equal
    ans = [False for _ in Relation]
    if e1.end < e2.start:
        ans[Relation.Before.value] = True
    if e1.end == e2.start:
        ans[Relation.Meet.value] = True
    if e1.end > e2.start and e1.end < e2.end and e1.start < e2.start:
        ans[Relation.Overlap.value] = True
    if e1.start == e2.start and e1.end < e2.end:
        ans[Relation.Start.value] = True
    if e1.end == e2.end and e1.start < e2.start:
        ans[Relation.FinishedBy.value] = True
    if e1.start < e2.start and e1.end > e2.end:
        ans[Relation.Contain.value] = True
    if e1.start == e2.start and e1.end == e2.end:
        ans[Relation.Equal.value] = True
    return ans


class CompositeEvent(object):
    def __init__(self, e1, e2=None, reltype=None, debug=False):
        self.e1 = e1
        self.e2 = e2
        self.reltype = reltype
        self.debug = debug

        if e2 is not None and reltype is not None:
            self.start = min(e1.start, e2.start)
            self.end = max(e1.end, e2.end)
        else:
            self.start = e1.start
            self.end = e1.end

    def is_composite(self):
        return self.e2 is not None and self.reltype is not None

    def getstr(self):
        estr1 = self.e1.getstr()
        if self.e2 is None:
            return estr1
        else:
            estr2 = self.e2.getstr()
            ret = "({} {} {})".format(estr1, Relation.rel2str(self.reltype), estr2)
            return ret


    def __str__(self):
        if not self.is_composite():
            return str(e1)
        else:
            return "({};[{}, {}])".format(self.getstr(), self.start, self.end)


if __name__ == '__main__':
    e1 = Event("A", 1, 4)
    e2 = Event("B", 2, 3)
    # ans = relation(e1, e2)
    # print(str(e1), str(e2), ans)

    ce1 = CompositeEvent(e1)
    ce2 = CompositeEvent(e1, e2, Relation.Contain)
    ce3 = CompositeEvent(ce1, ce2, Relation.Meet, True)
    print(ce3)
