class Solution:
    def findCircleNum(self, isConnected):

        vis=[False]*len(isConnected)

        def dfs(city):

            for nei in range(len(isConnected)):
                if not vis[nei] and isConnected[city][nei]==1:
                    vis[nei]=True
                    dfs(nei)

        count = 0
        for i in range(len(isConnected)):
            if not vis[i]:
                count+=1
                dfs(i)
        
        return count