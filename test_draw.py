import os
from renderer import render_maze

def generate_maze():
    # for now return same maze (later you replace this)
    return [
        [
            {"N": True, "E": False, "S": False, "W": True},
            {"N": True, "E": True, "S": False, "W": False}
        ],
        [
            {"N": False, "E": False, "S": True, "W": True},
            {"N": False, "E": True, "S": True, "W": False}
        ]
    ]


maze = generate_maze()
entry = (0, 0)
exit = (1, 1)

colors = ["white", "red", "green", "blue", "yellow"]
color_index = 0

show_path = False   # we’ll use later

while True:
    os.system("clear")

    render_maze(maze, entry, exit, wall_color=colors[color_index])

    print("\n1) regenerate maze")
    print("2) show/hide path")
    print("3) rotate colors")
    print("4) quit")

    choice = input("choice (1-4): ")

    if choice == "1":
        maze = generate_maze()

    elif choice == "2":
        show_path = not show_path
        print("Path toggled (we add it later)")
        input("press Enter...")

    elif choice == "3":
        color_index = (color_index + 1) % len(colors)

    elif choice == "4":
        break
