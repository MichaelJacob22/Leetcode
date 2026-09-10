class Solution:
    def validPath(self, n, edges, source, destination):
        graph=[[] for _ in range(n)]

        for i in edges:
            u,v=i
            graph[u].append(v)
            graph[v].append(u)

        vis=[False]*n
        boolean=False

        def dfs(node):
            nonlocal boolean
            vis[node]=True
            if node == destination:
                boolean=True
            
            for nei in graph[node]:
                if not vis[nei]:
                    dfs(nei)
        
        dfs(source)
        return boolean