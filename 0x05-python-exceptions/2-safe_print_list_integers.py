#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p, e = 0, 0
    while p < x:
        try:
            print('{:d}'.format(my_list[p]), end='')
            e += 1
        except (ValueError, TypeError):
            pass
        p += 1
        print()
        return e
