from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque()
        vis=[False]*len(arr)

        if (start+arr[start])>=0 and (start+arr[start])<len(arr):
            queue.append(arr[start]+start)
            vis[arr[start]+start]=True

        if (start-arr[start])>=0 and (start-arr[start])<len(arr):
            queue.append(start-arr[start])
            vis[start-arr[start]]=True

        while queue:
            node = queue.popleft()

            if arr[node] == 0:
                return True
            
            a=node-arr[node]
            b=node+arr[node]

            if a>=0 and a<len(arr) and not vis[a]:
                queue.append(a)
                vis[a]=True
            
            if b>=0 and b<len(arr) and not vis[b]:
                queue.append(b)
                vis[b]=True
        
        return False