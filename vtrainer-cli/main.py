#!/usr/bin/env python3

from config import WORKDIR
from vt_ui_texts import *
from os import system
import sys

vocabulary = []

class Record:
    def __init__(self, word, translation, succ = 0, fails = 0):
        self.__word = word
        self.__translation = translation
        self.__succ = succ
        self.__fails = fails

    def iter_survey(self):
        res = input(self.__word + ": ") == self.__translation
        if res:
            self.__succ += 1
            print("Correct!")
        else:
            self.__fails += 1
            print("Wrong :(")

    def __str__(self):
        return "Word: {}\nTranslation: {}\nSuccess attempts: {}\nFailed attempts: {}" \
            .format(self.__word, self.__translation, self.__succ, self.__fails)


def load_vocabulary(file="{}/vocabulary".format(WORKDIR)):
    with open(file, 'r') as voc_file:
        for voc_line in voc_file.readlines():
            word, translation, succ, fails = voc_line.split('\t')
            vocabulary.append(Record(word, translation, int(succ), int(fails)))

def survey():
    system("clear")
    res = []
    for record in vocabulary:
        record.iter_survey()
    print(res)

def load_words():
    word = input("Enter the word: ")
    translation = input()


print(LOGO)

if len(sys.argv) == 1:
    print("\nHelp info")
    sys.exit()
print(GREETING)


cmd = sys.argv[1]
if cmd == 'load':
    pass # load_words()
elif cmd == 'survey':
    load_vocabulary()
    survey()