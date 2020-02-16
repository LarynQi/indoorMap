# from openlocationcode import openlocationcode as olc

# #def encode(latitude, longitude, codeLength=PAIR_CODE_LENGTH_):

# loc1 = olc.encode(37.4281906, -122.1741650, 13)
# loc2 = olc.encode(37.4281714, -122.1741952, 13)
# print(loc1)
# print(loc2)

# def neighbors(row, col):
#     return [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
#     [row, col - 1], [row, col + 1],
#     [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]]

# # img = [
# # [1, 1, 1, 1, 1, 1, 1, 1],
# # [1, 1, 1, 1, 1, 1, 2, 0],
# # [1, 0, 0, 1, 0, 2, 1, 1],
# # [1, 2, 2, 2, 2, 0, 1, 0],
# # [1, 1, 1, 2, 2, 0, 1, 0],
# # [1, 1, 1, 2, 2, 2, 2, 0],
# # [1, 1, 1, 1, 1, 2, 1, 1],
# # [2, 2, 1, 1, 1, 2, 2, 1],
# # ]

# img = [
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 0, 0],
# [1, 0, 0, 1, 1, 0, 1, 1],
# [1, 1, 0, 0, 0, 0, 1, 0],
# [1, 1, 1, 0, 0, 0, 1, 0],
# [1, 1, 1, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0, 1, 1],
# [0, 0, 1, 1, 1, 0, 0, 1],
# ]

# def floodFill(arr, curr, target, color1, color2, path):
#     height = len(arr)
#     width = len(arr[0])

#     r1, c1 = curr[0], curr[1]
#     r2, c2 = target[0], target[1]

#     if r1 == r2 and c1 == c2:
#         #arr[r2][c2] = 100
#         return path + [[r2, c2]]
#     #edge of the board
#     if r1 < 0 or r1 >= height:
#         return
#     if c1 < 0 or c1 >= width:
#         return
#     #invalid color
#     if arr[r1][c1] != color1:
#         return

#     arr[r1][c1] = color2

#     #visited.append([r1, c1])
#     #path.append([r1, c1])

#     moves = neighbors(r1, c1)
#     results = []
#     for move in moves:
#         #if move not in visited:
#         result = floodFill(arr, move, target, color1, color2, path + [[r1, c1]])
#         #results.append(result)
#         if result is not None and result[len(result) - 1] == [r2, c2]:
#             return result
#     #print(results)
#     # shortest = height * width
#     # for result in results:
#     #     if result is not None and len(result) < shortest and result[len(result) - 1] == [r2, c2]:
#     #         return result

# def highlight(arr, path):
#     for coord in path:
#         r = coord[0]
#         c = coord[1]
#         arr[r][c] = 9

# def flood_img():
#     print("Input")

#     for i in img:
#         print(i)

#     start = [4, 4]
#     end = [7, 6]
#     #floodFill(img, *replace_point, col1=2, col2=3)
#     path = floodFill(img, start, end, 0, 2, [])
#     highlight(img, path)

#     print("-" * 25)
#     print("Output")
#     for i in img:
#         print(i)
#     print("Path: ")
#     print(path)


# flood_img()


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


