import os
import sys
import urllib.request

fp = open('result.txt', 'r', encoding = 'utf-8')
string = ''

while True :
    line = fp.readline()
    string += line
    if not line :
        break
    print(string)

fp.close()

