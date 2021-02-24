from cell import Cell
from puzzle import Puzzle


class Constructor:
    def __init__(self, puzzle_string):
        self.puzzle_as_list = [int(x) for x in puzzle_string.split(' ')]

    def convert_to_puzzle(self):
        cells_list = []
        for i, val in enumerate(self.puzzle_as_list):
            if val == 0:
                val = None

            cells_list.append(Cell(i, val))

        return Puzzle(cells_list)

    def print_puzzle(self):
        print(self.puzzle_as_list)
