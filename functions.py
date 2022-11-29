import json
import os
import shutil
import subprocess

from config import serverFileFolder


def create_entry(args):
    name = input("Enter a name for this server: ")
    name = name + ".json"

    if os.path.exists(serverFileFolder + name):
        print("That server entry already exists!")
        return

    filepath = serverFileFolder + name
    shutil.copy('config/templates/entry.json', serverFileFolder)
    os.rename(serverFileFolder + 'entry.json', filepath)
    os.system('vim ' + filepath)


def list_scripts(args):
    servers = os.listdir(serverFileFolder)
    for server in servers:
        print(os.path.splitext(server)[0])


def run_script(args):
    name = args[0] + ".json"
    filepath = serverFileFolder + name
    if not os.path.exists(filepath):
        print("Not a valid server entry name")
        return

    entry = json.load(open(filepath, 'r'))
    os.chdir(os.path.expanduser(entry['directory']))
    proc = subprocess.Popen(entry['command'].split(' ')).wait()
    print(proc.pid)


def rename(args):
    original_name = args[0] + ".json"
    filepath = serverFileFolder + original_name

    if not os.path.exists(filepath):
        print("Not a valid server entry name")
        return

    new_name = args[1] + ".json"
    os.rename(filepath, serverFileFolder + new_name)


def edit_entry(args):
    name = args[0] + ".json"
    filepath = serverFileFolder + name

    if not os.path.exists(filepath):
        print("Not a valid server entry name")
        return

    os.system('vim ' + filepath)
