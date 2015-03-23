#!/usr/bin/env bash

# loading dependencies
sudo apt-get install python-numpy

# setting permissions
chmod a+x ./src/Sudoku_solver.py

# executing the script with paths for the input directory to read the unsolved sudoku and output directory to write the solved sudoku
python ./src/Sudoku_solver.py ./sudoku_input/sudoku.csv ./sudoku_output/solved_sudoku.csv
