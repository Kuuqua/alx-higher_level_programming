#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = -9999
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
