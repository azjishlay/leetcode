from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def dfs(row, col, grid):
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[row])
                or grid[row][col] == "0"
            ):
                return 0

            grid[row][col] = "0"  # sink it, i.e. change "1" to "0"

            dfs(row - 1, col, grid)  # top
            dfs(row + 1, col, grid)  # bottom
            dfs(row, col - 1, grid)  # left
            dfs(row, col + 1, grid)  # right
            return 1

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    islands += dfs(row, col, grid)

        return islands


# TESTCASE

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
a1 = 1

grid2 = [
    ["1", "0", "1", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["1", "1", "1", "0", "0"],
]
a2 = 2

grid3 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
a3 = 3


def test():
    print(Solution().numIslands(grid1) == a1)
    print(Solution().numIslands(grid2) == a2)
    print(Solution().numIslands(grid3) == a3)


def main():
    test()


if __name__ == "__main__":
    main()
