"""
Given a rectangular matrix of characters matrix, which represents a 2-dimensional field where each cell contains the following types of cells:
'.' represents an empty cell,
'#' represents an obstacle,
'F' corresponds to a cell of a connected figure.

Gravity makes the figure fall toward the bottom of the field, until one of its cells reaches the ground (bottom edge of the matrix), or meets an obstacle. 
The task is to return the state of the field after the figure stops falling.

[['.', 'F', 'F', 'F', '.'],
 ['.', '.', 'F', '.', '.'],
 ['#', '.', '.', '#', '.'],
 ['.', '.', '.', '.', '.']]
=> 
[['.', '.', '.', '.', '.'],
 ['.', 'F', 'F', 'F', '.'],
 ['#', '.', 'F', '#', '.'],
 ['.', '.', '.', '.', '.']]

"""
