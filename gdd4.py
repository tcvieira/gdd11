#!/usr/bin/env python

'''
resp = 71
'''

import sys

order = {'v':0, 'r':1, 'x':2, 'w':3, 'f':4, 'k':5, 'p':6, 'h':7, 'q':8, 'l':9, 'j':10, 'c':11, 'n':12, 's':13, 'm':14, 'g':15, 't':16, 'd':17, 'b':18, 'z':19}
bnumbers = 0

fp = open(sys.argv[1], 'r')
lines = fp.readlines()
words = list(lines[0].split(' '))
words_aux = list()
for word in words:
   word_aux = list()
   for char in word:
      word_aux.append(order[char])
      #words_aux.append(int(''.join(map(str,word_aux)))) transforma a lista de str numericas em uma lista de int -- n precisou
      words_aux.append(word_aux)
numbers = list()
for word in words_aux:
   pot = 0
   num = 0
   #word.reverse() -- n foi preciso inverter
   for char in word:
      num = num + (int(char)*(20**pot))
      pot = pot + 1
   numbers.append(num)
numbers = list(set(numbers))
for num in numbers:  
   if (num >= 574908) and (num % 5 == 0):
      bnumbers = bnumbers + 1
print bnumbers