from winselect_core import utils

def _key(key):
    print('[WARNING] going to remove:', key, 'from system environment.')
    print('Continue? [y/N]')
    choice = input()
    while (choice is not 'n') and (choice is not 'y'): choice = input()
    registry = utils.get_registry()
    if key in registry:
        utils.remove(key)
    else:
        print('Key does not exist in registry.')


def main(args):
    if args._key:
        _key(args._key)
