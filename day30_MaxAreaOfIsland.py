#LeetCode 695. Max Area of Island

from collections import deque
from typing import List
#----------DFS Approach-----------
def max_area_of_island_dfs(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    max_area = 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area = 1
        area += dfs(r+1, c)
        area += dfs(r-1, c)
        area += dfs(r, c+1)
        area += dfs(r, c-1)
        return area
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area



#----------BFS Approach-----------
def max_area_of_island_bfs(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        grid[r][c] = 0
        area = 1
        while q:
            row, col = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    area += 1
                    q.append((nr, nc))
        return area
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, bfs(r, c))
    return max_area


#----------Test Cases-----------
if __name__ == "__main__":
    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,1,0,1,0,0],
        [0,0,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

    from copy import deepcopy
    print("DFS Max Area of Island:", max_area_of_island_dfs(deepcopy(grid1)))
    print("BFS Max Area of Island:", max_area_of_island_bfs(deepcopy(grid1)))