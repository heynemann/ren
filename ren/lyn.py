#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, dirname, exists, split, abspath
import argparse

def main(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]

    lines = []
    if not sys.stdin.isatty():
        lines = [line.strip() for line in sys.stdin]

    parser = argparse.ArgumentParser(description='Renames a folder or file.', prog="ren")
    parser.add_argument('--samelevel', default=False, action='store_true')
    parser.add_argument('path', help='the source path to rename', nargs='?')
    parser.add_argument('name', help='the name of the file', nargs=1)

    options = parser.parse_args(arguments)
    name = options.name[0]
    same_level = options.samelevel

    if lines:
        for line in lines:
            link(line, name, same_level)
    else:
        from_path = options.path[0]
        link(from_path, name, same_level)

def link(from_path, name, same_level):
    to_path = join(dirname(from_path), name)

    if exists(to_path):
        print "%s already exists - skipping..." % to_path
    else:
        if same_level:
            cur_dir = abspath(os.curdir)
            link_dir = abspath("%s/../" % from_path)
            print "link_dir: %s" % link_dir
            os.chdir(link_dir)

            relative_from = split(from_path)[-1]
            relative_to = './%s' % name
            os.symlink(relative_from, relative_to)
            print "sym linked at %s - %s to %s" % (link_dir, relative_from, relative_to)
            os.chdir(cur_dir)
        else:
            os.symlink(from_path, to_path)
            print "sym linked %s to %s" % (from_path, to_path)

if __name__ == '__main__':
    main(sys.argv[1:])
