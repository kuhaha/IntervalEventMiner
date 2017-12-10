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


if __name__ == '__main__':
    e1 = Event("A", 1, 4)
    e2 = Event("B", 2, 3)
    ans = relation(e1, e2)
    print(e1)
    print(e2)
    print(ans)
