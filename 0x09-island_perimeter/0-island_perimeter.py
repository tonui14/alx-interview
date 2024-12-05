#!/usr/bin/python3

def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island in a grid.

    Args:
    grid (list of list of integers): 2D grid where 1 represents land and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is land (1)
            if grid[i][j] == 1:
                # Start with 4 sides for the perimeter of the land
                perimeter += 4
                
                # Check if there is land to the left
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                
                # Check if there is land to the right
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1
                
                # Check if there is land above
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                
                # Check if there is land below
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1
    
    return perimeter

