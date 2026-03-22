def render_maze(maze, entry, exit):
    height = len(maze)
    width = len(maze[0])

    # draw top border
    print("+" + "---+" * width)

    for y in range(height):

        # draw vertical walls
        line = "|"
        for x in range(width):

            if (x, y) == entry:
                cell_char = " S "
            elif (x, y) == exit:
                cell_char = " E "
            else:
                cell_char = "   "

            if maze[y][x]["E"]:
                line += cell_char + "|"
            else:
                line += cell_char + " "

        print(line)

        # draw bottom walls
        line = "+"
        for x in range(width):
            if maze[y][x]["S"]:
                line += "---+"
            else:
                line += "   +"

        print(line)
