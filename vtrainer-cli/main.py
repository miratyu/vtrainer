#!/usr/bin/env python3

from config import DEFAULT_VOCABULARY_FILE

vocabulary = dict()

def load_vocabulary(file=DEFAULT_VOCABULARY_FILE):
    with open(file, 'r') as voc_file:
        for voc_line in voc_file.readlines():
            pair = voc_line.split()
            vocabulary[pair[0]] = pair[1]


def run_contest():
    pass

if __name__ == '__main__':
    print_greetings()
    print_menu()