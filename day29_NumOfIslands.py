#LeetCode 200. Number of Islands

from typing import List
from collections import deque
import copy
class Solution:
    #----------DFS Approach-----------
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
    
    #----------BFS Approach-----------
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands
    
#----------Test Cases-----------
if __name__ == "__main__":
    original_grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
solution = Solution()

#Testing DFS Approach
grid_dfs = copy.deepcopy(original_grid)
count_dfs = solution.numIslandsDFS(grid_dfs)
print("Number of islands (DFS):", count_dfs) 


#Testing BFS Approach
grid_bfs = copy.deepcopy(original_grid)
count_bfs = solution.numIslandsBFS(grid_bfs)
print("Number of islands (BFS):", count_bfs)
