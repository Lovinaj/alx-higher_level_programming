#!/usr/bin/python3


def best_score(my_dict):
    return max(my_dict, key=my_dict.get) if my_dict else None


'''
def best_score(a_dictionary):
    max = 0

    if a_dictionary is None or a_dictionary == {}:
        return None

    for key in a_dictionary:
        value = a_dictionary.get(key)
        if value > max:
            max = value
            key_max = key

    return (key_max)
'''
