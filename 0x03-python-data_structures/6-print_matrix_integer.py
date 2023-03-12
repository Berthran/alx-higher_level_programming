#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    no_rows = len(matrix)
    no_cols = len(matrix[0])

    for i in range(no_rows):
        for j in range(no_cols):
            if j < no_cols - 1:
                print("{}".format(matrix[i][j]), end=" ")
            else:
                print("{}".format(matrix[i][j]), end="")
        print()


if __name__ == "__main__":
    print_matrix_integer()
