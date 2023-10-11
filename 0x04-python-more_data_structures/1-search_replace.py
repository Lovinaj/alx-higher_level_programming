#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    length = len(my_list)

    for i in range(0, length):
        if search == my_list[i]:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])

    return (new_list)

'''
def search_replace(my_list, search, replace):
    return [replace if search == n else n for n in my_list]
'''
