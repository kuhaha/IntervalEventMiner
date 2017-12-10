# -*- coding: utf-8 -*-

from event import Event
from database import DB


def main():
    print("Sample")
    db = DB.toy()
    db.dump()


if __name__ == '__main__':
    main()
