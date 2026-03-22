from parser import parse_config
import sys
from render import render_maze


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    config = parse_config(sys.argv[1])

    print(config)


if __name__ == "__main__":
    main()
