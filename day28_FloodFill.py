#LeetCode 733. Flood Fill

# DFS
def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]
    if original == newColor:
        return image
    def dfs(r, c):
        if r < 0 or r >= rows or c <  0 or c >= cols:
            return
        if image[r][c] != original:
            return
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


#BFS
from collections import deque
def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]
    if original == newColor:
        return image
    queue = deque([sr, sc])
    while queue:
        r, c = queue.popleft()
        if image[r][c] == original:
            image[r][c] = newColor
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    queue.append((nr, nc))
    return image

