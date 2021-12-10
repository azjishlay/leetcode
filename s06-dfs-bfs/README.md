# s06-dfs-bfs

## [Number of Islands](https://leetcode.com/problems/number-of-islands/)

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```
Output: 1

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```
Output: 3
 

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`.

***

### Notes

DFS (Depth First Search):
* Search or traverse a graph or tree by going down a path, explore it completely, and then go back and explore a different path until the end.
* Done recursively using call stack, and iteratively using Stack.
    

BFS (Breadth First Search):
* Same as DFS, but keeps track of visited path and keeps going down, no need to go back up the path
* Done iteratively using Queue
* Can also be done recursively, but does not make sense logically


**Example:**
```
    1
   / \
  3   7
 / \   \
4   5   10
```

DFS:
    In-order Traversal => Left, root, right (recursively)

`4, 3, 5, 1, 7, 10`

BFS:
    Level order traversal => Level by level

`1, 3, 7, 4, 5, 10`
