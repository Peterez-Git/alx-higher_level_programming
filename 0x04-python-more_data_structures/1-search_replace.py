def search_replace(my_list, search, replace):
    replace_list = []
    for i in my_list:
        if i == search:
            replace_list.append(replace)
        else:
            replace_list.append(i)
    return replace_list
