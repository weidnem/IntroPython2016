'''Goal: Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +'''


def BuildFloors(numFloors):
    # Construct a list containing the requested number of floors
    plus = "+"
    minus = "-"
    # Standard definition for a floor
    floor = plus + minus*4 + plus + minus*4 + plus
    floorMaterials = []
    # Create floors
    for x in range(0, numFloors):
        floorMaterials.append(floor)
    return floorMaterials


def BuildWall(wallHeight):
    # Construct a wall of the requested height
    pipe = "|"
    # Standard definition for a wall
    wall = pipe + " "*4 + pipe + " "*4 + pipe
    wallMaterials = []
    # Create Walls
    for x in range(0, wallHeight):
        wallMaterials.append(wall)
    return wallMaterials

# Call Builders
buildingFloors = BuildFloors(3)
buildingWalls = BuildWall(4)

# Create Building
for x in range(0, len(buildingFloors)):
    print(buildingFloors[x])
    for y in range(0, len(buildingWalls)):
        # Check to see if we laid the ground floor (we don't want a basement)
        if x < len(buildingFloors)-1:
            print(buildingWalls[y])
