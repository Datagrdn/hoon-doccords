#!/usr/bin/python3

import sqlite3
import argparse

parser = argparse.ArgumentParser(description='Simple interface to query doccords sqlite db')

parser.add_argument('-d', '--database', action='store', dest='db', default='doccords.db')
parser.add_argument('arm', action='store')

args = parser.parse_args()

con = sqlite3.connect(args.db)

c = con.cursor()

print(args.arm)

c.execute('SELECT doccord_raw FROM doccords WHERE arm = ? COLLATE NOCASE', (args.arm, ))

print(c.fetchone()[0])

con.close()