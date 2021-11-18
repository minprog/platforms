# Rotate

Write a Python function to rotate a square matrix (a list of lists) 90 degrees clockwise. For example:


    matrix = [
        [0, 1],
        [2, 3]
    ]

    rotated_matrix = rotate(matrix)

    print_matrix(matrix)
    # prints
    # [0, 1]
    # [2, 3]

    print_matrix(rotated_matrix)
    # prints
    # [2, 0]
    # [3, 1]


In case the matrix is not a square, raise a `NonSquareMatrixError`.


    class NonSquareMatrixError(Exception):
        pass

    def print_matrix(matrix: list[list[int]]) -> None:
        for row in matrix:
            print(row)

    def rotate(matrix: list[list[int]]) -> list[list[int]]:
        # TODO
        pass

> Do **not** use external libraries for this assignment, so no `numpy`! 

Write a Pytest unittest for each of the following in a file called `test_rotate.py`:

* Rotation of a matrix of an even size (2x2)
* Rotation of a matrix of an uneven size (3x3)
* Rotation of a 1x1 matrix
* Rotation of an empty matrix
* Rotation of a non-square matrix
* That rotate does not modify the original matrix
* That four rotations equal the original matrix
