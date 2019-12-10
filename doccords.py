#!/usr/bin/python3

import re
import sqlite3
import argparse

parser = argparse.ArgumentParser(description='Utility to extract doccords from hoon files and put them into a sqlite db')

parser.add_argument('-d', '--database', action='store', dest='db', default='doccords.db')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose')
parser.add_argument('-p', '--purge', action='store_true', dest='purge')
parser.add_argument('file', action='store')

args = parser.parse_args()

if args.verbose:
    print('opening: ' + args.file)
    
bible = open(args.file)
reg = re.compile("::>[\s\S]*?\+\+.*", re.MULTILINE)
con = sqlite3.connect(args.db)

c = con.cursor()

if args.purge:
    if args.verbose:
        print('droping old table')
    c.execute('drop table if exists doccords')
    con.commit()

if args.verbose:
    print('creating table')

c.execute('create table if not exists doccords (arm text, doccord_raw text)')

for doccord in reg.findall(bible.read()):
    m = doccord.split('++')
    arm = m[-1].lstrip().split()[0]

    if args.verbose:
        print('writing: ' + arm)

    c.execute('insert into doccords values (?, ?)', (arm, doccord))


con.commit()

if args.verbose:
    print('finished')

con.close()

