# -*- coding: utf-8 -*-

from event import from_list

# for visualize
import matplotlib as mpl
import matplotlib.patches as pch
import matplotlib.pyplot as plt
import seaborn as sns

class DB(object):
    def __init__(self, EL):
        self.EL = EL
        self.EtypeL = [[et.etype for et in el] for el in EL]
        self.event_set = set({})
        self.maxend = 0
        self.div = 1.0
        for el in self.EL:
            eset_local = set({})
            for event in el:
                eset_local.add(event.etype)
                self.event_set.add(event.etype)
            self.div = min(self.div, 1.0 / len(eset_local))
            self.maxend = max(self.maxend, el[-1].end)

        self.cpt = sns.color_palette(n_colors=len(self.event_set) + 1)
        self.colors = dict()
        counter = 0
        for et in self.event_set:
            self.colors[et] = self.cpt[counter]
            counter += 1
        for key in self.colors:
            print(key, self.colors[key])

    def __len__(self):
        return len(self.EL)

    def visualize(self):
        assert len(self) < 10
        N = len(self)
        print(N, self.maxend)
        plt.figure()
        ax = plt.gca()
        # ax.axis("off")

        for idx, el in enumerate(self.EL):
            # determine y locations
            loc_y = dict()
            for jdx, et in enumerate(self.EtypeL[idx]):
                loc_y[et] = jdx * self.div
            for event in el:
                xy = (event.start, idx + loc_y[event.etype])
                boxc = self.colors[event.etype]
                patch = pch.Rectangle(xy=xy, width=event.width, height=self.div, color=boxc, alpha=0.5)
                ax.add_patch(patch)

        plt.xlim(-0.5, self.maxend +0.5)
        plt.ylim(-0.5, N + 0.5)
        plt.xticks(range(self.maxend + 1))
        plt.yticks(range(N + 1))
        plt.tight_layout()
        # plt.show()
        plt.savefig("db_vis.png")
        plt.close()

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
