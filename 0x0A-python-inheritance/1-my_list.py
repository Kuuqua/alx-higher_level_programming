#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
