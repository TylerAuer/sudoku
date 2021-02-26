from typing import Union
from math import floor

'''
00 01 02 | 03 04 05 | 06 07 08
09 10 11 | 12 13 14 | 15 16 17
18 19 20 | 21 22 23 | 24 25 26
------------------------------
27 28 29 | 30 31 32 | 33 34 35
36 37 38 | 39 40 41 | 42 43 44
45 46 47 | 48 49 50 | 51 52 53
------------------------------
54 55 56 | 57 58 59 | 60 61 62
63 64 65 | 66 67 68 | 69 70 71
72 73 74 | 75 76 77 | 78 79 80
'''

region_names = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]


class Cell:
    def __init__(self, index: int, value: Union[int, None]):
        # row, column, and region are all 1 indexed
        self.row = floor(index / 9)
        self.col = index % 9
        self.val = value
        self.index = index

        region_row = floor(index / 27)
        region_col = floor(index % 9 / 3)
        self.region = region_names[region_row][region_col]

        if value is None:
            self.values_still_possible = [x for x in range(1, 10)]
        else:
            self.values_still_possible = []

    # Returns whether a cell has been narrowed down to a single value
    def is_solved(self):
        if self.val is None:
            return False
        else:
            return True

    def remove_val_from_possible_list(self, value_to_remove):
        if value_to_remove in self.values_still_possible:
            self.values_still_possible.remove(value_to_remove)

    def print_summary(self):
        entry = self.val
        if self.val is None:
            entry = '-'
        print(f'{entry} @ ({self.row}, {self.col}, {self.region})')

    def print_possibilities_list(self):
        print(f'{self.index}: {self.values_still_possible}')

    def check_if_solved(self):
        if len(self.values_still_possible) == 1:
            self.val = self.values_still_possible.pop()
            print(f"Just solved: {self.index}")
