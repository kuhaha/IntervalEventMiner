# -*- coding: utf-8 -*-

from event import Event
from database import DB


def main():
    db = DB.toy()
    # db.dump()
    db.visualize()


if __name__ == '__main__':
    main()
