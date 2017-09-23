# -*- coding: utf-8 -*-

#--- create backward compatibility with python 2
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

from readWords import readWords

if __name__ == '__main__':
    x=readWords(language='E')

