class Solution:
    def countBattleships(self, grid: List[List[str]]) -> int:
        visited=set()
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(i,j):
            q=deque([(i,j)])
            visited.add((i,j))

            while q:
                curr_r,curr_c = q.popleft()

                for rc,rw in dirs:
                    new_r=curr_r + rc
                    new_c=curr_c + rw

                    if 0<=new_r<=n-1 and 0<=new_c<=m-1 and (new_r,new_c) not in visited and grid[new_r][new_c]=="X":
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
                        bfs(new_r,new_c)

        n=len(grid)
        m=len(grid[0])

        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='X' and (i,j) not in visited:
                    bfs(i,j)
                    ans+=1

        return ans
        