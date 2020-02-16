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
    r28c15 = Exit(28, 15, "stair")
    floorOne.addSquare(r28c15, r28c15.name)
    r29c15 = Exit(29, 15, "stair")
    floorOne.addSquare(r29c15, r28c15.name)

    r30c15 = Exit(28, 15, "elevator")
    floorOne.addSquare(r30c15, r30c15.name)
    r31c15 = Exit(29, 15, "elevator")
    floorOne.addSquare(r31c15, r31c15.name)
    r32c15 = Exit(29, 15, "elevator")
    floorOne.addSquare(r32c15, r32c15.name)

    r33c15 = Exit(33, 15, "stair")
    floorOne.addSquare(r33c15, r33c15.name)
    r34c15 = Exit(34, 15, "stair")
    floorOne.addSquare(r34c15, r34c15.name)

    #rightside room
    r21c15 = Exit(21, 15, "Cafe Kitchen")
    floorOne.addSquare(r21c15, r21c15.name)

    #leftside rooms
    r20c13 = Exit(20, 13, "Vending Machine/Recycling/ATM")
    floorOne.addSquare(r20c13, r20c13.name)
    r21c13 = Exit(21, 13, "Vending Machine/Recycling/ATM")
    floorOne.addSquare(r21c13, r21c13.name)

    r25c13 = Exit(25, 13, "bathroom")
    floorOne.addSquare(r25c13, r25c13.name)
    r26c13 = Exit(26, 13, "bathroom")
    floorOne.addSquare(r26c13, r26c13.name)

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
    for row in range(19, 25):
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
    
    #line of wall surrounding hallway entrance
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
    for col in range(9, 11):
        row = 19
        add = Wall(row, col, "wall")
        floorOne.addSquare(add, add.name)
        
    for row in range(19, 22):
        for col in range(2 + (row - 19), 5):
            add = Wall(row, col, "wall")
            floorOne.addSquare(add, add.name)
    
    fillerR = 25
    fillerC = 16
    addFiller = Wall(fillerR, fillerC, "wall")
    floorOne.addSquare(addFiller, addFiller.name)
    #print(floorOne.squares)
    count = 0
    for wall in floorOne.squares["wall"]:
        count += 1
        #print("(" + str(wall.x) + ", " + str(wall.y) + ")")
    for ex in floorOne.squares["exit"]:
        count += 1
        #print("(" + str(ex.x) + ", " + str(ex.y) + ")")
    for path in floorOne.squares["path"]:
        count += 1
        #print("(" + str(path.x) + ", " + str(path.y) + ")")
    for elevator in floorOne.squares["elevator"]:
        count += 1
    for br in floorOne.squares["bathroom"]:
        count += 1
    for room in floorOne.squares["Vending Machine/Recycling/ATM"]:
        count += 1
    for kitchen in floorOne.squares["Cafe Kitchen"]:
        count += 1
    print(count)


    huangCenter.addFloor(floorOne, floorOne.level)
generate()
