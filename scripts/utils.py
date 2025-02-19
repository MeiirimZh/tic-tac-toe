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

    return "none"


def find_pair(grid):
    # Check the rows
    for i in range(len(grid)):
        x = [x for x in grid[i] if x == "x"]
        o = [x for x in grid[i] if x == "o"]
        if len(x) == 2 and len(o) == 0:
            return i, grid[i].index(" ")
        elif len(o) == 2 and len(x) == 0:
            return i, grid[i].index(" ")
    
    # Check the columns
    for i in range(len(grid)):
        column = [grid[x][i] for x in range(3)]
        x = [x for x in column if x == "x"]
        o = [x for x in column if x == "o"]
        if len(x) == 2 and len(o) == 0:
            return column.index(" "), i
        elif len(o) == 2 and len(x) == 0:
            return column.index(" "), i
        
    # Check all diagonals
    main_diagonal = [grid[0][0], grid[1][1], grid[2][2]]
    x = [x for x in main_diagonal if x == "x"]
    o = [x for x in main_diagonal if x == "o"]
    if len(x) == 2 and len(o) == 0:
        return main_diagonal.index(" "), main_diagonal.index(" ")
    elif len(o) == 2 and len(x) == 0:
        return main_diagonal.index(" "), main_diagonal.index(" ")
    
    secondary_diagonal = [grid[0][2], grid[1][1], grid[2][0]]
    x = [x for x in secondary_diagonal if x == "x"]
    o = [x for x in secondary_diagonal if x == "o"]
    found_pair = False

    if len(x) == 2 and len(o) == 0:
        found_pair = True
    elif len(o) == 2 and len(x) == 0:
        found_pair = True

    if found_pair:
        if secondary_diagonal.index(" ") == 0:
            return 0, 2
        elif secondary_diagonal.index(" ") == 2:
            return 2, 0
        else:
            return 1, 1
    
    return None


def print_grid(grid):
    for row in grid:
        for column in row:
            print(f'[{column}]', end="")
        print()
