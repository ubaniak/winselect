from winselect_core import utils
import re

def _all():
    registry = utils.get_registry()
    for key, value in registry.items():
        utils.display_entry(key, value)

def _path():
    registry = utils.get_registry()
    utils.display_entry('Path', registry['Path'])

def _key(pattern):
    registry = utils.get_registry()
    for key, value in registry.items():
        if re.search(pattern, key, re.IGNORECASE):
            utils.display_entry(key, value)

def _search(pattern):
    registry = utils.get_registry()
    for key, value in registry.items():
        if re.search(pattern, key, re.IGNORECASE) or re.search(pattern, value, re.IGNORECASE):
            utils.display_entry(key, value, pattern=pattern)

def main(args):
    if args._all:
        _all()
    if args._path:
        _path()
    if args._key:
        _key(args._key)
    if args._search:
        _search(args._search)
