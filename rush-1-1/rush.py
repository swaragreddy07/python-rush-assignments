import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""

        for col in range(x):

            # corners
            if (row == 0 or row == y - 1) and (col == 0 or col == x - 1):
                line += "o"

            # top and bottom
            elif row == 0 or row == y - 1:
                line += "-"

            # left and right
            elif col == 0 or col == x - 1:
                line += "|"

            # inside space
            else:
                line += " "

        print(line)