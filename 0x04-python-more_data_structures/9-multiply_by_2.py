def multiply_by_2(a_dictionary):
    squared_dict = {}
    for key, values in a_dictionary.items():
        squared_dict[key] = values ** 2
    return squared_dict
