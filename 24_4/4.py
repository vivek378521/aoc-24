def read_grid_from_file(filename):
    with open(filename, "r") as file:
        grid = [list(line.strip()) for line in file]

    return grid


def find_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    xmas_count = 0
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_xmas(r, c, dr, dc):
        pattern = ["X", "M", "A", "S"]
        for i, letter in enumerate(pattern):
            new_r, new_c = r + i * dr, c + i * dc
            if not is_valid(new_r, new_c) or grid[new_r][new_c] != letter:
                return False

        return True

    # Iterate through every possible starting position
    for r in range(rows):
        for c in range(cols):
            # If the current cell is 'X', check in all 8 directions
            if grid[r][c] == "X":
                for dr, dc in directions:
                    if check_xmas(r, c, dr, dc):
                        xmas_count += 1

    return xmas_count


def find_x_mas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    x_set = {"M", "S"}

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                if {grid[r - 1][c - 1], grid[r + 1][c + 1]} == x_set and {
                    grid[r - 1][c + 1],
                    grid[r + 1][c - 1],
                } == x_set:
                    count += 1

    return count


filename = "4.txt"
grid = read_grid_from_file(filename)
result = find_x_mas_occurrences(grid)
print(f"Number of XMAS occurrences: {result}")
