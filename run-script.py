#!/usr/bin/python3
import sys
import functions as fun
from config import *


if not os.path.exists(serverFileFolder):
    os.makedirs(serverFileFolder, exist_ok=True)

keywords = {
    "create": fun.create_entry,
    "run": fun.run_script,
    "list": fun.list_scripts,
    "edit": fun.edit_entry,
    "rename": fun.rename
}

args = sys.argv[1:]

if __name__ == "__main__":
    if args[0] in keywords:
        keywords[args[0]](args[1:])

