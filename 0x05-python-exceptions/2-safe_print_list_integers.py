#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, e = 0, 0
    while p < x:
        try:
            print('{:d}'.format(my_list[i]), end='')
            e += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return e
