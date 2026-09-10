from collections import deque

class Solution:
    def numIslands(self, grid):

        m=len(grid)
        n=len(grid[0])

        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        queue=deque()
        count=0

        for nm in range(m):
            for nn in range(n):
                
                if grid[nm][nn]=="1":
                    queue.append((nm,nn))
                    count+=1

                    while queue:
                        i,j=queue.popleft()

                        for dx,dy in moves:
                            ni=i+dx
                            nj=j+dy

                            if 0<=ni<m and 0<=nj<n and grid[ni][nj]=="1":
                                grid[ni][nj]="2"
                                queue.append((ni,nj))
        
        return count