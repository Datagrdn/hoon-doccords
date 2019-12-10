#!/bin/sh

find $1 -name '*.hoon' -exec ./extract.py -v {} \;