class Puzzle:
    def __init__(self, cells):
        self.cells = cells

    @property
    def unsolved_cells(self):
        counter = 0
        for cell in self.cells:
            if cell.val is None:
                counter += 1
        return counter

    @property
    def total_possibilities_left(self):
        counter = 0
        for cell in self.cells:
            counter += len(cell.values_still_possible)
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

    def solve(self):
        max_iterations = 100

        rows = {}
        cols = {}
        regions = {}

        # Map cells by row, column, and region for O(1) lookup
        for cell in self.cells:
            if cell.row not in rows:
                rows[cell.row] = []
            rows[cell.row].append(cell)

            if cell.col not in cols:
                cols[cell.col] = []
            cols[cell.col].append(cell)

            if cell.region not in regions:
                regions[cell.region] = []
            regions[cell.region].append(cell)

        while self.unsolved_cells > 0 and max_iterations > 0:
            for cell in self.cells:
                # Don't try to solve cells that are already solved
                if cell.is_solved():
                    continue

                # Check rows
                for cell_in_same_row in rows[cell.row]:
                    # Looking at itself so skip
                    if cell.index == cell_in_same_row.index:
                        continue
                    if cell_in_same_row.is_solved():
                        cell.remove_val_from_possible_list(
                            cell_in_same_row.val)

                # Check columns
                for cell_in_same_col in cols[cell.col]:
                    # Looking at itself so skip
                    if cell.index == cell_in_same_col.index:
                        continue
                    if cell_in_same_col.is_solved():
                        cell.remove_val_from_possible_list(
                            cell_in_same_col.val)

                # Check region
                for cell_in_same_region in regions[cell.region]:
                    # Looking at itself so skip
                    if cell.index == cell_in_same_region.index:
                        continue
                    if cell_in_same_region.is_solved():
                        cell.remove_val_from_possible_list(
                            cell_in_same_region.val)

                if cell.index == 6:
                    print(cell.values_still_possible)

                cell.check_if_solved()

            max_iterations -= 1
            print(self.unsolved_cells, self.total_possibilities_left)
