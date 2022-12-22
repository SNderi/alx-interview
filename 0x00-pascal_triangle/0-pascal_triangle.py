#!/usr/bin/python3
""" An algorithm to create the Pascal's triangle. """


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        pascal = []
    elif n == 1:
        pascal = [[1]]
    else:
        pascal = [[1], [1, 1]]
        row = [1, 1]
        i = 1
        while i < n - 1:
            j = -1
            approw = []
            while j < (len(row) + 1) // 2:
                if j < 0:
                    approw.append(row[j + 1])
                elif j + 1 >= len(row):
                    approw.append(row[j])
                else:
                    approw.append(row[j] + row[j + 1])
                j += 1
            ch = (len(row)+1) // 2
            if (len(row) + 1) % 2 == 0:
                app = approw[:ch - 1]
                approw = approw + app[::-1]
            else:
                app = approw[:ch]
                approw = approw + app[::-1]
            row = approw
            pascal.append(approw)
            i += 1

    return pascal
