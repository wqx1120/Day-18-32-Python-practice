#Leetcode 417. Pacific Atlantic Water Flow
from collections import deque
def pacificAtlantic_dfs(heights):
    if not heights: return []
    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited, prev_height):
        if ((r, c) in visited or
            r < 0 or c < 0 or r >= m or c >= n or
            heights[r][c] < prev_height):
            return 
        visited.add((r, c))
        dfs(r+1, c, visited, heights[r][c])
        dfs(r-1, c, visited, heights[r][c])
        dfs(r, c+1, visited, heights[r][c])
        dfs(r, c-1, visited, heights[r][c])

    for i in range(m):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, n-1, atlantic, heights[i][n-1])

    for j in range(n):
        dfs(0, j, pacific, heights[0][j])
        dfs(m-1, j, atlantic, heights[m-1][j])

    return list(pacific & atlantic)

def pacificAtlantic_bfs(heights):
    if not heights: return []
    m, n = len(heights), len(heights[0])

    def bfs(starts):
        visited = set(starts)
        q = deque(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr , nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        return visited
    
    pacific_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
    atlantic_starts = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]
    pacific = bfs(pacific_starts)
    atlantic = bfs(atlantic_starts)
    return list(pacific & atlantic)

if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print("DFS Pacific Atlantic Water Flow:", pacificAtlantic_dfs(heights))
    print("BFS Pacific Atlantic Water Flow:", pacificAtlantic_bfs(heights))
