from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n=len(heights)
        m=len(heights[0])
        def bfs(node):
            queue=deque(node)
            vis=set()
            for o in node:
                vis.add(o)

            while queue:
                i,j=queue.popleft()

                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    ni=i+dx
                    nj=j+dy

                    if 0<=ni<n and 0<=nj<m and (ni,nj) not in vis:
                        if heights[ni][nj]>=heights[i][j]:
                            vis.add((ni,nj))
                            queue.append((ni,nj))
            return vis

        atlantic=[]
        for i in range(n):
            atlantic.append((i,m-1))
        for j in range(m):
            atlantic.append((n-1,j))

        pacific=[]
        for i in range(n):
            pacific.append((i,0))
        for j in range(m):
            pacific.append((0,j))

        a=bfs(atlantic)
        p=bfs(pacific)

        ans=[]
        for r in range(n):
            for c in range(m):
                if (r,c) in a and (r,c) in p:
                    ans.append([r,c])

        return ans