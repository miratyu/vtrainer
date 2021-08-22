#!/usr/bin/env python3

from config import WORKDIR
from vt_ui_texts import *
import os
import sys


class Vocabulary:
    def __init__(self, filename="{}/vocabulary".format(WORKDIR)):
        self.__records = set()
        self.__file = filename

        if not os.path.exists(filename):
            print('Given file does`t exist. A file will be created in default directory {}'.format(WORKDIR))
        else:
            with open(filename, 'r') as voc_file:
                for voc_line in voc_file.readlines():
                    word, translation, succ, fails = voc_line.split('\t')
                    self.__records.add(Record(word, translation, int(succ), int(fails)))

    def add(self, record):
        self.__records.add(record)

    def save(self):
        with open(self.__file, 'w') as voc_file:
            for record in self.__records:
                voc_file.write(record.__str__("save"))


class Record:
    def __init__(self, word, translation, succ=0, fails=0):
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

    def __str__(self, format="print"):
        if format == "save":
            return '{}\t{}\t{}\t{}\n'.format(self.__word, self.__translation, self.__succ, self.__fails)
        return "Word: {}\nTranslation: {}\nSuccess attempts: {}\nFailed attempts: {}" \
            .format(self.__word, self.__translation, self.__succ, self.__fails)

    def __eq__(self, obj):
        return self.__word == obj.__word and self.__translation == obj.__translation

    def __hash__(self):
        return (self.__word + self.__translation).__hash__()


vocabulary = Vocabulary()

print(LOGO)

if len(sys.argv) == 1:
    print("\n{} usage: ".format(sys.argv[0]))
    print("\tsurvey - start a survey of existing words")
    print("\tload - load new words")
    sys.exit()
print(GREETING)


cmd = sys.argv[1]
if cmd == 'load':
    word = input("Enter the word: ")
    translation = input("Enter the translation: ")
    vocabulary.add(Record(word, translation))
elif cmd == 'survey':
    os.system("clear")
    res = []
    for record in vocabulary:
        record.iter_survey()
    print(res)
