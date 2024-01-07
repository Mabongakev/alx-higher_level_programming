#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        maxim = my_list[0]
        for k in range(len(my_list)):
            if my_list[k] > maxim:
                maxim = my_list[k]
        return maxim
