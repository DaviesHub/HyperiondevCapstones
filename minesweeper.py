# Import relevant libraries
import random

# This function assists in generating grids for the main minesweeper
def generate_grid(s):
    """This function generates a square grid with random placements of mines and dashes.
       Dashes appear more than mines so the probability of generating a mine is set to 25%.
       The function receives an integer argument which represents the size of the grid to be constructed.
    """

    sq_grid = [[None] * s for null in range(s)] # Initialize grid to be returned
    items = ["-", "-", "-", "#"]
    for i in range(s):
        for j in range(s):
            idx = int(random.random() * len(items))
            sq_grid[i][j] = items[idx]

    return sq_grid


def minesweeper(grid):
    """This function counts the number of mines adjacent to a spot on a grid"""

    num_rows = len(grid)
    num_cols = len(grid)

    output_grid = [["#"] * num_cols for null in range(num_rows)] # Initialize output grid
    for i in range(1, len(grid)-1): # Code for interior values
        for j in range(1, len(grid)-1):
            mine_count = 0
            if grid[i][j] == "-":
                # Upward check
                if grid[i-1][j-1] == "#":
                    mine_count += 1 # Up-left check

                if grid[i-1][j] == "#":
                    mine_count += 1 # Up-center check

                if grid[i-1][j+1] == "#":
                    mine_count += 1 # Up-right check

                # Leftward check
                if grid[i][j-1] == "#":
                    mine_count += 1 # left-center check

                if grid[i+1][j-1] == "#":
                    mine_count += 1 # Left-down check

                # Rightward check
                if grid[i][j+1] == "#":
                    mine_count += 1 # right-center check

                if grid[i+1][j+1] == "#":
                    mine_count += 1 # Right-down check

                # Downward check
                if grid[i+1][j] == "#":
                    mine_count += 1 # left-center check

                output_grid[i][j] = str(mine_count)
            
            else:
                output_grid[i][j] = "#"

    # == Code for corner values ==
    # Top left corner
    if grid[0][0] == "-":
        mine_count = 0
        if grid[0][1] == "#":
            mine_count += 1 # Adjacent right

        if grid[1][1] == "#":
            mine_count += 1 # Adjacent diagonal

        if grid[1][0] == "#":
            mine_count += 1 # Adjacent bottom

        output_grid[0][0] = mine_count

    else:
        output_grid[0][0] = "#"

    # Top right corner
    if grid[0][-1] == "-":
        mine_count = 0
        if grid[0][-2] == "#":
            mine_count += 1 # Adjacent left

        if grid[1][-2] == "#":
            mine_count += 1 # Adjacent diagonal

        if grid[1][-1] == "#":
            mine_count += 1 # Adjacent bottom

        output_grid[0][-1] = mine_count

    else:
        output_grid[0][-1] = "#"

    # Bottom left corner
    if grid[-1][0] == "-":
        mine_count = 0
        if grid[-1][1] == "#":
            mine_count += 1 # Adjacent right

        if grid[-1][1] == "#":
            mine_count += 1 # Adjacent diagonal

        if grid[-2][0] == "#":
            mine_count += 1 # Adjacent top

        output_grid[-1][0] = mine_count

    else:
        output_grid[-1][0] = "#"

    # Bottom right corner
    if grid[-1][-1] == "-":
        mine_count = 0
        if grid[-1][-2] == "#":
            mine_count += 1 # Adjacent left

        if grid[-2][-2] == "#":
            mine_count += 1 # Adjacent diagonal

        if grid[-2][-1] == "#":
            mine_count += 1 # Adjacent top

        output_grid[-1][-1] = mine_count
    
    else:
        output_grid[-1][-1] = "#"

    # == Code for interior border values ==
    # Top borders
    for j in range(1, num_cols-1):
        if grid[0][j] == "-":
            mine_count = 0
            if grid[0][j-1] == "#": # Left Center check
                mine_count += 1

            if grid[1][j-1] == "#": # Left diagonal check
                mine_count += 1

            if grid[1][j] == "#": # Bottom center check
                mine_count += 1

            if grid[0][j+1] == "#": # Right center check
                mine_count += 1

            if grid[1][j+1] == "#": # Right diagonal check
                mine_count += 1

            output_grid[0][j] = mine_count

        else:
            output_grid[0][j] = "#"

    # Bottom borders
    for j in range(1, num_cols-1):
        if grid[-1][j] == "-":
            mine_count = 0
            if grid[-1][j-1] == "#": # Left Center check
                mine_count += 1

            if grid[-2][j-1] == "#": # Left diagonal check
                mine_count += 1

            if grid[-2][j] == "#": # Top center check
                mine_count += 1

            if grid[-1][j+1] == "#": # Right center check
                mine_count += 1

            if grid[-2][j+1] == "#": # Right diagonal check
                mine_count += 1

            output_grid[-1][j] = mine_count

        else:
            output_grid[-1][j] = "#"

    # Left borders
    for i in range(1, num_rows-1):
        if grid[i][0] == "-":
            mine_count = 0
            if grid[i-1][0] == "#": # Top Center check
                mine_count += 1

            if grid[i-1][1] == "#": # Top diagonal check
                mine_count += 1

            if grid[i][1] == "#": # Right center check
                mine_count += 1

            if grid[i+1][1] == "#": # Bottom diagonal check
                mine_count += 1

            if grid[i+1][0] == "#": # Bottom center check
                mine_count += 1

            output_grid[i][0] = mine_count

        else:
            output_grid[i][0] = "#"

    # Right borders
    for i in range(1, num_rows-1):
        if grid[i][-1] == "-":
            mine_count = 0
            if grid[i-1][-1] == "#": # Top Center check
                mine_count += 1

            if grid[i-1][-2] == "#": # Top diagonal check
                mine_count += 1

            if grid[i][-2] == "#": # Right center check
                mine_count += 1

            if grid[i+1][-2] == "#": # Bottom diagonal check
                mine_count += 1

            if grid[i+1][-1] == "#": # Bottom center check
                mine_count += 1

            output_grid[i][-1] = mine_count

        else:
            output_grid[i][-1] = "#"

    return output_grid

g = generate_grid(5)
print(g)
print(minesweeper(g))