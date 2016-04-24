#!/usr/bin/env python3

import os
import sys

TRANSLATIONS = {
    'poule': 'pull',
}

def main_func():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        return os.system('git')
    command = arguments[0]
    if command not in TRANSLATIONS:
        return os.system(" ".join(['git'] + arguments))
    translation = TRANSLATIONS[command]
    return os.system(" ".join(['git', translation] + arguments[1:]))

if __name__ == '__main__':
    sys.exit(main_func())
