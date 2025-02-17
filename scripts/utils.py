def check_grid(x, y, grid):
    # Check a row
    if set(grid[x]) == {'x'}:
        return "x"
    elif set(grid[x]) == {'o'}:
        return "o"
    
    # Check a column
    column_items = [row[y] for row in grid]
    if set(column_items) == {'x'}:
        return "x"
    elif set(column_items) == {'o'}:
        return "o"
    
    # Check all diagonals
    main_diagonal = [grid[0][0], grid[1][1], grid[2][2]]
    if set(main_diagonal) == {'x'}:
        return "x"
    elif set(main_diagonal) == {'o'}:
        return "o"
    secondary_diagonal = [grid[0][2], grid[1][1], grid[2][0]]
    if set(secondary_diagonal) == {'x'}:
        return "x"
    elif set(secondary_diagonal) == {'o'}:
        return "o"

    return "None"


def print_grid(grid):
    for row in grid:
        for column in row:
            print(f'[{column}]', end="")
        print()
