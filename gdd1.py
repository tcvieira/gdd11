#!/usr/bin/env python
#resp : texto b tem 60 preposicoes

import sys

prep = 0
foo = ['r','x','w','j','m']
fp = open(sys.argv[1], "r")
line = fp.readline()
words = line.split(' ')
for wd in words:
   if len(wd) == 3 and wd[-1] not in foo and 'l' not in wd:
      prep = prep + 1
print prep
fp.close()

