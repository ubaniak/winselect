from winselect_core import utils

class KeyExistsException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return '[Error] '+value
        

def _append(key, value):
    print(key, value)


def _new(key, value):
    if utils.does_key_exist(key):
        raise KeyExistsException('The given key "' + key + '" allready exists')
    print("Adding", key, ':', value, 'to path')
    utils.add_string(key, value)

def main(args):
    if args._new:
        _new(*args._new)
    if args._append:
        _append(*args._append)
