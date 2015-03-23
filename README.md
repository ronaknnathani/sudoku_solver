# Sudoku solver
This is a sudoku solver program written in Python.

Input to the script is an unsolved sudoku in a csv file stored in the sudoku_input directory and script writes the solved sudoku to a csv file saved in the directory sudoku_output. For the csv file, the entries in row are comma separated and different rows are new line separated.

To execute the sudoku solver program, execute the **run.sh** script. The Python program uses **numpy** package and it will be installed on executing **run.sh**. It may ask for the root password to complete installation.

New paths for the input csv file or output csv file can be specified by editing the run.sh file. Either a relative or an absolute path will work fine.
