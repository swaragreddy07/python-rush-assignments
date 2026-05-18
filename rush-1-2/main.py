import sys
from rush import rush

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("To run this program, use: python main.py <x> <y>")
        print("Example: python main.py 5 3")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        rush(x, y)