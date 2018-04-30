import string
import time
import random
from termcolor import colored

NAME = "h4ck3rb01 2000"
linelen = 20
target = "This my jam"
result = ''
pos = 0
letters = string.ascii_letters + string.punctuation + " "

for i in range(100):
    print()

print("#"*linelen + NAME + "#"*linelen + "\n" + "#"*linelen  + "cybrocorp inc." + "#"*linelen)
print("#"*linelen + "     2017 (C) " + "#"*linelen + "\n" + "#"*linelen + " "*len(NAME) + "#"*linelen)
print("deciphering:")
iter = 0
while pos < len(target):
    char = letters[iter]
    perc = "{0:.2f}".format(pos/len(target)*100)
    print("{}%\t{}{}".format(perc,result,char), end = "")
    time.sleep(0.01)
    print('\r', end = '')
    iter = (iter + 1) % len(letters)
    if char == target[pos]:
        result = result + char
        pos += 1

i = 0
while i < 100:
    if i % 2 == 0:
        print('\r', end = '')
        print('\t'*len(target), end = '')
    else:
        print('\r', end = '')
        print('100.00% '+ result, end = '')
    i = i + 1

    time.sleep(0.1)
