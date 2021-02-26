# SUDOKU

I've always wanted to code up a Sudoku solver. But, last time I tried, I didn't have the skills. 

I'm a lot less dumb now and felt like brushing up on my Python. So, here we are.

# Approach 1 - Very dumb, but very fast human strategy

The first approach was to just see if you could solve puzzles by looking at rows, columns, and regions (I made that term up, but I'm guessing you know what I mean).

This couldn't even solve simply ones. **FAIL**

# Approach 2 - Backtracking Search

Haven't coded this one up yet. But, here's the basic idea:

You need a method that checks whether a given puzzle -- completed or not -- is valid (unique numbers in each row, column, and region).

Then you, go to the first open cell, pick the first possible value that could go in there, and check if the puzzle is still valid. If so, recurse, else move on to the next possible value. 

If at any point you reach the last square, and make a valid puzzle. Store it or return it.