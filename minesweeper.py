# A simulation of minesweeper game

def generate_grid():
    """This function generates a grid with random placements of mines and dashes"""




def minesweeper(grid):
    """A simulation of minesweeper game"""

    num_rows = len(grid)
    num_cols = len(grid)

    output_grid = [["#"] * num_cols for null in range(num_rows)] # Initialize output grid
    for i in range(1, len(grid)): # Code for interior values
        for j in range(1, len(grid)):
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

    # == Code for interior border values ==
    






