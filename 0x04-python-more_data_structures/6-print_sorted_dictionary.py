#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())
    sorted_dict = {key: a_dictionary[key] for key in sort_keys}
    print(sorted_dict)
