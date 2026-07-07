class Solution:
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        for i in range(1,n):
            grid[0][i]=grid[0][i]+grid[0][i-1]
        for j in range(1,m):
            grid[j][0]=grid[j][0]+grid[j-1][0]
        
        for k in range(1,m):
            for l in range(1,n):
                grid[k][l]=min(grid[k-1][l],grid[k][l-1])+grid[k][l]

        return grid[m-1][n-1]        