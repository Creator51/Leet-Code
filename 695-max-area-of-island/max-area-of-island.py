class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        ans=0
        

        def bfs(r,c):
            q=deque([(r,c)])
            visited.add((r,c))
            cnt=0
            
            while q:
                cnt+=1
                
                curr_r,curr_c=q.popleft()
                for rc,rm in dirs:
                    new_r = curr_r + rc
                    new_c = curr_c + rm

                    if 0<=new_r<=n-1 and 0<=new_c<=m-1 and (new_r,new_c) not in visited and grid[new_r][new_c]==1:
                        q.append([new_r,new_c])
                        visited.add((new_r,new_c))
            return cnt
                        

        n=len(grid)
        m=len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans=max(ans,bfs(i,j))
                    

        return ans
