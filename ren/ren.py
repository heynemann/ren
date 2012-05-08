#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, dirname
import argparse

def main():
    lines = sys.stdin and tuple(sys.stdin) or tuple()

    arguments = sys.argv
    parser = argparse.ArgumentParser(description='Renames a folder or file.', prog="ren")
    parser.add_argument('path', help='the source path to rename', nargs='*')
    parser.add_argument('name', help='the name of the file', nargs=1)

    options = parser.parse_args(arguments[1:])
    name = options.name[0]

    if lines:
        for line in lines:
            move(line, name)
    else:
        from_path = options.path[0]
        move(from_path, name)

def move(from_path, name):
    to_path = join(dirname(from_path), name)

    os.rename(from_path, to_path)
    print "renamed %s to %s" % (from_path, to_path)

if __name__ == '__main__':
    main()
