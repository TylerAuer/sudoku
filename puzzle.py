class Puzzle:
    def __init__(self, cells):
        self.cells = cells

    @property
    def unsolved_cells(self):
        counter = 0
        for cell in self.cells:
            if cell.val is not None:
                counter += 1
        return counter

    def pretty_print(self):
        line = ''
        for i, cell in enumerate(self.cells):
            # Convert None to '-'
            print_val = cell.val
            if print_val is None:
                print_val = '.'

            line += f' {print_val}'  # Add to triplet

            # Add pipe to separate regions
            if i % 3 == 2 and i % 9 != 8:
                line += ' |'

            # Handle finished line
            if i % 9 == 8:
                print(line)
                line = ''

            # Add ---- between regions
            if i % 27 == 26 and i != 80:
                print('-' * 22)

        print(' ')
        print(f'{self.unsolved_cells} cells left')
