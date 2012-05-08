#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, dirname
import argparse

def main():
    arguments = sys.argv
    parser = argparse.ArgumentParser(description='Renames a folder or file.', prog="ren")
    parser.add_argument('path', help='the source path to rename', nargs=1)
    parser.add_argument('name', help='the name of the file', nargs=1)

    options = parser.parse_args(arguments[1:])
    from_path = options.path[0]
    to_path = join(dirname(from_path), options.name[0])

    os.rename(from_path, to_path)
    print "renamed %s to %s" % (from_path, to_path)

if __name__ == '__main__':
    main()
