from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque([("0000",0)])
        visited={"0000"}

        while queue:
            state,moves=queue.popleft()

            if state == target:
                return moves        

            for i in range(4):
                
                a=list(state)
                up=a.copy()
                down=a.copy()
                if a[i] == '9':
                    up[i]='0'
                else:
                    up[i]=str(int(up[i])+1)

                if "".join(up) not in visited and "".join(up) not in dead:
                    visited.add("".join(up))
                    queue.append(("".join(up),moves+1))

                if a[i] == '0':
                    down[i]='9'
                else:
                    down[i]=str(int(down[i])-1)
                if "".join(down) not in visited and "".join(down) not in dead:
                    visited.add("".join(down))
                    queue.append(("".join(down),moves+1))

        return -1