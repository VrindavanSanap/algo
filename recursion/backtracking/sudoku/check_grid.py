grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]


def check_grid(grid):
    def check_nums(nums):
        visited = set()
        for elm in nums:
            if elm != 0:
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
