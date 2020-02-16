from building import *
from floor import *
from square import *
def generate():
    huangCenter = Building(2, 0, "Huang Center")
    floorOne = Floor(1, 31, 34)
    
    #squares = floorOne.squares

    #bottom left
    for row in range(25, 34):
        for col in range(9):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #bottom right
    for row in range(25, 34):
        for col in range(17, 31):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #far right 2 cols
    for row in range(25):
        for col in range(29, 31):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #far right exit
    for row in range(11, 17):
        add = Exit(row, 28, "exit")
        floorOne.addSquare(add, add.name)

    #square of paths to the right of stairs
    for row in range(9, 20):
        for col in range(19, 28):
            add = Path(row, col, True, "path")
            floorOne.addSquare(add, add.name)

    #top right triangle walls
    for row in range(9):
        for col in range(21 + row, 29):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #hardcoded walls below tip of ^ triangle
    r8c28 = Wall(8, 28, "wall")
    floorOne.addSquare(r8c28, r8c28.name)
    r9c28 = Wall(9, 28, "wall")
    floorOne.addSquare(r9c28, r9c28.name)
    r10c28 = Wall(10, 28, "wall")
    floorOne.addSquare(r10c28, r10c28.name)

    #triangle of walls row 19-24
    for row in range(19, 25):
        for col in range(28 - (row - 19), 29):
            if col != 20:
                add = Wall(row, col, "wall")
                floorOne.addSquare(add, add.name)
            
    #hardcoded walls above tip of ^ triangle
    r17c28 = Wall(17, 28, "wall")
    floorOne.addSquare(r17c28, r17c28.name)
    r18c28 = Wall(18, 28, "wall")
    floorOne.addSquare(r18c28, r18c28.name)

    #top left triangle of walls
    for row in range(9):
        for col in range(9 - row):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #GOAL STUFF

    #left L of walls
    for row in range(9, 25):
        add = Wall(row, 0, "wall")
        floorOne.addSquare(add, add.name)
    for row in range(19, 23):
        for col in range(1, 1 + (row - 18)):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    for row in range(23, 25):
        for col in range(1, 5):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #hallway rightside exits
    # for row in range(26, 28):
    #     col = 15
    #     add = Exit(row, col, "stair")
    #     floorOne.addSquare(add, add.name)

    r26c15 = Exit(26, 15, "stair")
    floorOne.addSquare(r26c15, r26c15.name)
    r27c15 = Exit(27, 15, "stair")
    floorOne.addSquare(r27c15, r27c15.name)

    r28c15 = Exit(28, 15, "elevator")
    floorOne.addSquare(r28c15, r28c15.name)
    r29c15 = Exit(29, 15, "elevator")
    floorOne.addSquare(r29c15, r29c15.name)
    r30c15 = Exit(30, 15, "elevator")
    floorOne.addSquare(r30c15, r30c15.name)

    r31c15 = Exit(31, 15, "stair")
    floorOne.addSquare(r31c15, r31c15.name)
    r32c15 = Exit(32, 15, "stair")
    floorOne.addSquare(r32c15, r32c15.name)

    #below these stairs ^
    r33c15 = Wall(33, 15, "wall")
    floorOne.addSquare(r33c15, r33c15.name)


    #above cafe kitchen
    for row in range(20, 23):
        col = 15
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    #rightside room
    r23c15 = Exit(23, 15, "Cafe Kitchen")
    floorOne.addSquare(r23c15, r23c15.name)

    #between cafe kitchen and exits below (wall)
    for row in range(24, 26):
        col = 15
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    #above vending machine
    for row in range(20, 23):
        col = 13
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    #leftside rooms
    r23c13 = Exit(23, 13, "Vending Machine/Recycling/ATM")
    floorOne.addSquare(r23c13, r23c13.name)
    r24c13 = Exit(24, 13, "Vending Machine/Recycling/ATM")
    floorOne.addSquare(r24c13, r24c13.name)

    for row in range(25, 28):
        col = 13
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    r28c13 = Exit(28, 13, "bathroom")
    floorOne.addSquare(r28c13, r28c13.name)
    r29c13 = Exit(29, 13, "bathroom")
    floorOne.addSquare(r29c13, r29c13.name)
    for row in range(30, 34):
        col = 13
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    #hallway path
    for row in range(19, 34):
        col = 14
        add = Path(row, col, True, "path")
        floorOne.addSquare(add, add.name)

    #leftside big room path
    for row in range(8, 19):
        for col in range(1, 9):
            add = Path(row, col, True, "path")
            floorOne.addSquare(add, add.name)

    #topside big room path
    for row in range(8):
        for col in range(9, 21):
            add = Path(row, col, True, "path")
            floorOne.addSquare(add, add.name)
    
    #topleft path triangle
    for row in range(1, 8):
        for col in range(9 - row, 9):
            add = Path(row, col, True, "path")
            floorOne.addSquare(add, add.name)

    #topright path triangle
    for row in range(1, 8):
        for col in range(21, 21 + row):
            add = Path(row, col, True, "path")
            floorOne.addSquare(add, add.name)
    
    #filler path line below ^ triangle
    for col in range(18, 28):
        row = 8
        add = Path(row, col, True, "path")
        floorOne.addSquare(add, add.name)
    
    #filler path line (vert) lining up with ^
    for row in range(9, 17):
        col = 18
        add = Path(row, col, True, "path")
        floorOne.addSquare(add, add.name)
    
    
    #bottom right rectangle far right
    for row in range(20, 25):
        for col in range(19, 23):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    #bottom right rectangle left of right
    for row in range(20, 25):
        for col in range(16, 19):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    #bottom right triangle
    for row in range(20, 24):
        for col in range(23, 27 - (row - 20)):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #top wall of mid stairs
    for col in range(9, 18):
        row = 8
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    #rect wall behind mid stairs
    for row in range(9, 17):
        for col in range(10, 18):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)

    #3 walls directly below mid stairs
    for row in range(14, 17):
        col = 9
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)

    #middle stairs
    for row in range(9, 14):
        col = 9
        add = Exit(row, col, "stair")
        floorOne.addSquare(add, add.name)

    #below stair walls path
    for row in range(17, 19):
        for col in range(9, 19):
            add = Path(row, col, True, "path")
            floorOne.addSquare(add, add.name)
    
    #line of wall surrounding hallway entrance ***
    for col in range(9, 19):
        row = 19
        if col != 14:
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    #behind atm room wall
    for row in range(20, 34):
        for col in range(9, 13):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    #behind that wall ^
    for row in range(19, 25):
        for col in range(5, 9):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    #two filler in brown
    # for col in range(9, 11):
    #     row = 19
    #     add = Wall(row, col, "wall")
    #     floorOne.addSquare(add, add.name)
        
    #triangle near removed elevator
    for row in range(19, 22):
        for col in range(2 + (row - 19), 5):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    # fillerR = 25
    # fillerC = 16
    # addFiller = Wall(fillerR, fillerC, "wall")
    # floorOne.addSquare(addFiller, addFiller.name)
    #print(floorOne.squares)

    # walls behind rightside hallway exits
    
    for row in range(25, 34):
        col = 16
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)
    count = 0
    check = {}
    for row in range(34):
        for col in range(31):
            check[(row, col)] = 0
    for wall in floorOne.squares["wall"]:
        count += 1
        check[(wall.x, wall.y)] = check.get((wall.x, wall.y), 0) + 1
        #print("(" + str(wall.x) + ", " + str(wall.y) + ")")
    for ex in floorOne.squares["exit"]:
        count += 1
        check[(ex.x, ex.y)] = check.get((ex.x, ex.y), 0) + 1
    for stair in floorOne.squares["stair"]:
        count += 1
        check[(stair.x, stair.y)] = check.get((stair.x, stair.y), 0) + 1
        #print("(" + str(ex.x) + ", " + str(ex.y) + ")")
    for path in floorOne.squares["path"]:
        count += 1
        check[(path.x, path.y)] = check.get((path.x, path.y), 0) + 1
        #print("(" + str(path.x) + ", " + str(path.y) + ")")
    for elevator in floorOne.squares["elevator"]:
        count += 1
        check[(elevator.x, elevator.y)] = check.get((elevator.x, elevator.y), 0) + 1
    for br in floorOne.squares["bathroom"]:
        count += 1
        check[(br.x, br.y)] = check.get((br.x, br.y), 0) + 1
    for room in floorOne.squares["Vending Machine/Recycling/ATM"]:
        count += 1
        check[(room.x, room.y)] = check.get((room.x, room.y), 0) + 1
    for kitchen in floorOne.squares["Cafe Kitchen"]:
        count += 1
        check[(kitchen.x, kitchen.y)] = check.get((kitchen.x, kitchen.y), 0) + 1
    for coord in check.keys():
        if check[coord] > 1:
            print(coord)
        if check[coord] == 0:
            print(str(coord) + "none")
    print(count)


    huangCenter.addFloor(floorOne, floorOne.level)
    return huangCenter
generate()
