# hoon-doccords

A set of utilities for interacting with hoon doccords.

Currently assumes doccords are written in the following format and only apply to arms of cores.

::> some comments
:: more comments
++ some-arm

Run consume.sh with a path to the directory of hoon files that you would like to extract data from. This will create a doccords.db file that can either by directly queried by using sqlite3 or by using the doccords-query.py script.
