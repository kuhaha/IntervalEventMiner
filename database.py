# -*- coding: utf-8 -*-

from event import from_list

class DB(object):
    def __init__(self, EL):
        self.EL = EL

    def __len__(self):
        return len(self.EL)

    def dump(self):
        border = "------------------------"
        print(border)
        for el in self.EL:
            print(",".join(map(str, el)))
        print(border)

    @staticmethod
    def toy():
        ltuple = [
            [("A", 1, 4), ("B", 2, 5), ("C", 3, 8), ("D", 6, 7)],
            [("A", 1, 2), ("F", 3, 4), ("G", 5, 6)],
            [("A", 1, 4), ("B", 2, 5), ("C", 3, 8), ("D", 6, 7), ("F", 9, 10)],
            [("A", 1, 3), ("B", 2, 4), ("D", 5, 6), ("F", 7, 8), ("G", 9, 10)],
            [("Q", 1, 2), ("C", 3, 4), ("D", 5, 6)],
            [("P", 1, 2), ("C", 3, 4), ("D", 5, 6)]
        ]
        el = [from_list(lt) for lt in ltuple]
        return DB(el)
