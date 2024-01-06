#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_division = []
    for num in my_list:
        if num % 2 == 0:
            my_division.append(True)
        else:
            my_division.append(False)
    return my_division
