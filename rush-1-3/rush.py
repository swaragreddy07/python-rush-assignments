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

            # top left and top right
            elif row == 0 and (col == 0 or col == x - 1):
                line += "A"

            # bottom left and bottom right
            elif row == y - 1 and (col == 0 or col == x - 1):
                line += "C"

            # borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "B"

            # inside
            else:
                line += " "

        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("To run this program, use: python rush1-3.py <x> <y>")
        print("Example: python rush1-3.py 5 3")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        rush(x, y)