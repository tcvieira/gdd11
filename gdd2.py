#!/usr/bin/env python
#resp : 72 verbos 19 verbos em primeira pessoa

import sys

verb = 0
verb1 = 0
foo = ['r','x','w','j','m']
fp = open(sys.argv[1], "r")
line = fp.readline()
words = line.split(' ')
for wd in words:
   if len(wd) >= 8 and wd[-1] not in foo:
      verb = verb + 1
      if wd[0] in foo:
         verb1 = verb1 + 1
print verb, verb1
fp.close()

