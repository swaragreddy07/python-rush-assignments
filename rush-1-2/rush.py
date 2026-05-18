import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""

        for col in range(x):

            # special case for single row or column
            if x == 1 or y == 1:
                line += "*"

            # top left
            elif row == 0 and col == 0:
                line += "/"

            # top right
            elif row == 0 and col == x - 1:
                line += "\\"

            # bottom left
            elif row == y - 1 and col == 0:
                line += "\\"

            # bottom right
            elif row == y - 1 and col == x - 1:
                line += "/"

            # borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "*"

            # inside
            else:
                line += " "

        print(line)