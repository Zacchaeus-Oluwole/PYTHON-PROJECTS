'''
This program generates twelve random words from wordlist.txt and store it in scanned.txt file.
It enables you to enter the number of list you want
'''

import random

word = open("wordlist.txt")
lineword = word.read()
listTxt = lineword.splitlines()

txtList = []
get = int(input("Enter number of list : "))
# open file in write mode
with open('scanned.txt', 'w') as fp:
    while True:
        randChoices = random.choices(listTxt, k= 12)
        txtList.append(randChoices)
        if len(txtList) == get:
            for list in txtList:
                l = ' '.join(list)
                print(l)
                # write each item on a new line
                fp.write("%s\n" % l)
            break