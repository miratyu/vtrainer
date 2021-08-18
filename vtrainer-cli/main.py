#!/usr/bin/env python3

from config import WORKDIR
from vt_ui_texts import *
import sys

vocabulary = dict()

WORKDIR = WORKDIR if len(sys.argv) < 2 else sys.argv[1]
def clear_terminal():
    print(chr(27) + "[2J")

def load_vocabulary(file="{}/vocabulary".format(WORKDIR)):
    with open(file, 'r') as voc_file:
        for voc_line in voc_file.readlines():
            pair = voc_line.split()
            vocabulary[pair[0]] = pair[1]

def menu():
    print(LOGO)
    print(GREETING)
    print(MENU)
    cmd = input("Enter the command number: ")

    if cmd == "1":
        survey()
    elif cmd == "2":
        print("second")

def survey():
    clear_terminal()
    for entry, translation in vocabulary.items():
        print("{} ---- {}".format(entry, translation))

if __name__ == '__main__':
    load_vocabulary()
    menu()