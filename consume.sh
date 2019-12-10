#!/bin/sh

find $1 -name '*.hoon' -exec ./doccords.py -v {} \;