#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    n_list = []
    for k in range(length):
        if my_list[k] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list

