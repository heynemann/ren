#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, dirname, exists
import argparse

def main(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]

    lines = []
    if not sys.stdin.isatty():
        lines = [line.strip() for line in sys.stdin]

    parser = argparse.ArgumentParser(description='Renames a folder or file.', prog="ren")
    parser.add_argument('name', help='the name of the file', nargs=1)
    parser.add_argument('path', help='the source path to rename', nargs='*')

    options = parser.parse_args(arguments)
    name = options.name[0]

    if lines:
        for line in lines:
            move(line, name)
    else:
        from_path = options.path[0]
        move(from_path, name)

def move(from_path, name):
    to_path = join(dirname(from_path), name)

    if exists(to_path):
        print "%s already exists - skipping..." % to_path
    else:
        os.rename(from_path, to_path)
        print "renamed %s to %s" % (from_path, to_path)

if __name__ == '__main__':
    main(sys.argv[1:])
