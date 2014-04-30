import os
import sys
import argparse
import winselect_core

def setup_argparse():
    parser = argparse.ArgumentParser("winselect")
    subparsers = parser.add_subparsers(dest="commands",
                                       description="List of commands")
    # -- list ---------------------------
    _list = subparsers.add_parser('list', help='')
    _list.set_defaults(func=winselect_core._list.main)
    _list.add_argument('--all', dest='_all', action='store_true', 
            help='Shows all the Environment variables')
    _list.add_argument('--path', dest='_path', action='store_true', 
            help='Only shows Path')
    _list.add_argument('-s', '--search', dest='_search', action='store', 
            help='Search all environment variables (keys and values) for the given pattern')
    _list.add_argument('-k', '--key', dest='_key', action='store', 
            help='Search for a specific key')

    # -- add -----------------------------
    _add = subparsers.add_parser('add')
    _add.set_defaults(func=winselect_core._add.main)
    _add.add_argument('-n', '--new', dest='_new', nargs=2, action='store', help='')
    _add.add_argument('-a', '--append', dest='_append', nargs=2, action='store', help='')
    _add.add_argument('-t', '--top', dest='_top', nargs=2, action='store', help='')

    # -- remove -------------------------
    _remove = subparsers.add_parser('remove')
    _remove.set_defaults(func=winselect_core._remove.main)
    _remove.add_argument('-k', '--key', dest='_key', action='store', help='')

    return parser



if __name__=='__main__':
    parser = setup_argparse()
    arguments = parser.parse_args(sys.argv[1:])
    arguments.func(arguments)
