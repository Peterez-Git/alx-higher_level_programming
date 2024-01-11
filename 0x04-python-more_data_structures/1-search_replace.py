def search_replace(my_list, search, replace):
    replace_list = my_list.copy()
    for index, x in enumerate(my_list):
        if search == x:
            replace_list[index] = replace
    return replace_list
