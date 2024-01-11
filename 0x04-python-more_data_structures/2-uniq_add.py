#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    my_list = set(my_list)
    my_list = list(my_list)
    for i in my_list:
        unique_sum += i
    return unique_sum
