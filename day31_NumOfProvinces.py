#Number of Provinces (LeetCode 547)

from collections import deque
from typing import List
#----------DFS Approach-----------
def findCircleNum_dfs(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        for nei in range(n):
            if isConnected[city][nei] == 1 and not visited[nei]:
                visited[nei] = True
                dfs(nei)
    provinces = 0
    for i in range(n):
        if not visited[i]:
            provinces += 1
            visited[i] = True
            dfs(i)
    return provinces


#----------BFS Approach-----------
def find_circle_num_bfs(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = [False] * n
    provinces = 0

    for i in range(n):
        if not visited[i]:
            provinces += 1
            q = deque([i])
            visited[i] = True
            while q:
                city = q.popleft()
                for nei in range(n):
                    if isConnected[city][nei] == 1 and not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
    return provinces

#----------Test Cases-----------
if __name__ == "__main__":
    isConnected = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
    print("DFS Number of Provinces:", find_circle_num_bfs(isConnected))

    print("BFS Number of Provinces:", find_circle_num_bfs(isConnected))