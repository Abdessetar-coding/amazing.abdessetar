from renderer import render_maze

maze = [
    [
        {"N": True, "E": False, "S": False, "W": True},
        {"N": True, "E": True, "S": False, "W": False}
    ],
    [
        {"N": False, "E": False, "S": True, "W": True},
        {"N": False, "E": True, "S": True, "W": False}
    ]
]

render_maze(maze, (0,0), (1,1))