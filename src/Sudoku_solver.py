###
# author: Ronak Nathani
###

########### Terms used throughout the program ###########
## Rows of the sudoku are defined by letters 'ABCDEFGHI'
## Columns of the sudoku are defined by numbers '123456789'
## A sqaure is represented for e.g. as 'A1'
## The first row is 'A1'....'A9'
## The first column is 'A1'....'I1'
## The collection of nine squares(rows, columns, box) is named a unit
## Peers of a sqaure are all squares in its unit except the square itself
## Every square has 3 units and 20 peers
## given, a dictionary, is the output
#########################################################
import numpy as np
import csv
import string
import sys

print "Running Sudoku Solver...\n"

########### Input sudoku is a string with a '0' for the blank spaces ###########

sudoku_raw = ''
with open(sys.argv[1], 'rb') as csvfile:
    sudoku_reader = csv.reader(csvfile, delimiter=' ')
    for row in sudoku_reader:
        sudoku_raw = sudoku_raw + row[0].translate(string.maketrans("",""), string.punctuation)

########## Converting string sudoku into a list ##########

sudoku_array = range(81)
for i in range(81):
    if sudoku_raw[i]=='0':
        sudoku_array[i]=0
    else:
        sudoku_array[i] = int(sudoku_raw[i])
        
sudoku_matrix = np.asarray(sudoku_array)
sudoku_matrix = sudoku_matrix.reshape(9,9)

########## Squares identifiers e.g. 'A1', peers, units and unitlist ##########

def cross(A,B):
    return [a+b for a in A for b in B]
    
rows = 'ABCDEFGHI'
cols = '123456789'
numbers = cols
squares = cross(rows,cols)
unitlist = ([cross(rows, b) for b in cols] + [cross(a, cols) for a in rows] + 
            [cross(a1,b1) for a1 in ('ABC', 'DEF', 'GHI') for b1 in ('123', '456', '789')])
units = dict((s,[u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(units[s][0] + units[s][1] + units[s][2]) - set([s])) for s in squares)

chars = [c for c in sudoku_array]
given = dict(zip(squares,chars))

########## Unit tests ##########

def test():
    for i in range(81):
        assert(sudoku_raw[i] in '0123456789.'), 'Invalid Sudoku'
    assert len(sudoku_raw)==81, 'Incomplete Sudoku'
    assert all(len(peers[s]) == 20 for s in squares), 'Peers count should be 20'
    assert len(given)==81, 'Problem assigning values to squares'
    assert all(len(units[s]) == 3 for s in squares), 'Unit length should be 3'
    assert len(unitlist) == 27,'Number of units should be 27'
    assert len(squares) == 81, 'Number of squares should be 81'
    
########## Backtracking ##########

def Solve(given):
    for s in squares:
        if given[s]==0:
            for i in range(1,10,1):
                if NoConflict(s,i):
                    given[s]=i
                    if Solve(given):
                        return True
                    given[s]=0
            return False
    return True
    
########## Constraint ##########
    
def NoConflict(s,i):
    for p in peers[s]:
        if given[p] == i:
            return False
    return True
    
########## Write solved sudoku to a csv ##########

def WriteSudoku(given):
    with open(sys.argv[2], 'wb') as csvfile:
        sudoku_writer = csv.writer(csvfile, delimiter=',')
        for i in range(9):
            output_row = ''
            for j in range(9*i, 9*(i+1)):
                output_row = output_row + str(given[squares[j]])
            sudoku_writer.writerow(output_row)

########## Main ##########
    
if __name__ == '__main__':
    test()
    print "The solved sudoku is saved in the output directory:", sys.argv[2], "\n"
    if Solve(given):
        WriteSudoku(given)
    else:
        print "Failed"    