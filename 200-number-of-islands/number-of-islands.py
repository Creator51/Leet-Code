from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()

        dirs=[[0,1],[0,-1],[1,0],[-1,0]]

        q=deque()

        def bfs(i,j):
            q.append((i,j))

            while q:
                curr_r,curr_c=q.popleft()
                for rc,rw in dirs:
                    new_r=curr_r + rc
                    new_c= curr_c + rw

                    if 0<=new_r<=n-1 and 0<=new_c<=m-1 and (new_r,new_c) not in visited and grid[new_r][new_c]=='1':
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))

        n=len(grid)
        m=len(grid[0])
        cnt=0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j]=='1':
                    bfs(i,j)
                    cnt+=1
        return cnt
        