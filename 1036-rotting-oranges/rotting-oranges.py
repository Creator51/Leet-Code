class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited = set()
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        q=deque()
        time=0
        n=len(grid)
        m=len(grid[0])
        fresh_orange=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append(([i,j]))
                elif grid[i][j]==1:
                    fresh_orange+=1

        while q and fresh_orange>0:
            for i in range(len(q)):
                curr_r,curr_c=q.popleft()
                
                for rc,rw in dirs:
                    new_r=curr_r+rc
                    new_c=curr_c+rw

                    if 0<=new_r<=n-1 and 0<=new_c<=m-1 and (new_r,new_c) not in visited and grid[new_r][new_c]==1:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
                        fresh_orange-=1 
            time+=1
        
        return time if fresh_orange==0 else -1


        