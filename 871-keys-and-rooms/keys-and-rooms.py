from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        queue=deque()
        vis=[False]*len(rooms)

        queue.append(0)
        vis[0]=True

        while queue:
            node=queue.popleft()

            for nei in rooms[node]:
                if not vis[nei]:
                    queue.append(nei)
                    vis[nei]=True
        return all(vis)