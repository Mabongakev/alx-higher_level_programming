#!/usr/bin/python3
def uppercase(str):
    for itr in str:
        tmp = itr
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(itr) - 32)
        print("{}".format(tmp), end='')
    print()
