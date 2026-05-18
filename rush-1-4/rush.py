import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""

        for col in range(x):

            # single row or column
            if x == 1 or y == 1:
                line += "B"

            # top left and bottom left
            elif col == 0 and (row == 0 or row == y - 1):
                line += "A"

            # top right and bottom right
            elif col == x - 1 and (row == 0 or row == y - 1):
                line += "C"

            # borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "B"

            # inside
            else:
                line += " "

        print(line)
