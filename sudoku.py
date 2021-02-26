import load

sample = '8 0 0 2 0 0 0 4 6 0 0 7 9 0 0 0 0 0 1 0 0 0 0 0 5 0 0 0 0 0 5 0 0 0 3 2 4 0 8 0 0 0 7 0 1 3 2 0 0 0 7 0 0 0 0 0 6 0 0 0 0 0 9 0 0 0 0 0 3 2 0 0 2 8 0 0 0 6 0 0 3'

puz = load.Constructor(sample)

puzzle = puz.convert_to_puzzle()

print(puzzle.total_possibilities_left)

puzzle.pretty_print()

puzzle.solve()

puzzle.pretty_print()
