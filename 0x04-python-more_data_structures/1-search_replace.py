#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if z == search else x, my_list))
    return (new_list)
