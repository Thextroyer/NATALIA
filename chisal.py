#coding: utf-8

import random


def chisteAl():
    lines = open('chistes.txt').read().splitlines()
    myline =random.choice(lines)
    return myline
