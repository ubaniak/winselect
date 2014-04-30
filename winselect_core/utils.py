try:
    import winreg
except:
    import _winreg as winreg
import re

KEY_PATH = 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment'
READ=0
WRITE=1
ALL=2

class UnknownMode(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return '[Error] do not reconize mode: ' + value

def get_regkey(mode=READ):
    if mode == READ:
        return winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, KEY_PATH, 0, winreg.KEY_READ)
    if mode == WRITE:
        return winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, KEY_PATH, 0, winreg.KEY_WRITE)
    if mode == ALL:
        return winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, KEY_PATH, 0, winreg.KEY_ALL_ACCESS)

    raise UnknownMode(str(mode))

def add_string(key, value):
    regkey = get_regkey(WRITE)
    winreg.SetValueEx(regkey, key, 0, winreg.REG_EXPAND_SZ, value)

def remove(key):
    regkey = get_regkey(ALL)
    winreg.DeleteValue(regkey, key)


def get_registry():
    registry = {}
    regkey = get_regkey()
    try:
        i = 0
        while True:
            reg_tuple = winreg.EnumValue(regkey, i)
            registry[reg_tuple[0]] =  reg_tuple[1]
            i += 1
    except WindowsError:
        pass
    winreg.CloseKey(regkey)
    return registry

def does_key_exist(key):
    registry = get_registry()
    return key in registry

def display_entry(key, value, sep=';', pattern=None):
    if pattern and re.search(pattern, key, re.IGNORECASE):
        print('==> ', key)
    else:
        print(key)
    for path in value.split(sep):
        if pattern and re.search(pattern, path, re.IGNORECASE):
            print("==>* ", path)
        else:
            print("   * ", path)
