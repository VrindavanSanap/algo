import numpy as np
grid = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(np.matrix(grid))

def check_grid(grid):
    def check_nums(nums):
        visited = set()
        for elm in nums:
            if elm != ".":
                if elm in visited:
                    return False
                visited.add(elm)
        return True

    # check rows
    if not all([check_nums(row) for row in grid]):
        return False

    # check columns
    if not all([check_nums(column) for column in zip(*grid)]):
        return False

    # check boxes
    for j in range(0, 9, 3):
        for i in range(0, 9, 3):
            sliced_part = [row[i:i+3] for row in grid[j:j+3]]
            res = [element for sublist in sliced_part for element in sublist]
            if not check_nums(res):
                return False
    return True


if __name__ == "__main__":
    print(check_grid(grid))