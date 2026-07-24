from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target="123450"
        start = "".join(str(a) for rows in board for a in rows)
        visited={start}
        neighbour={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
        queue=deque([(start,0)])
        while queue:
            state,moves=queue.popleft()

            if state == target:
                return moves

            z = state.index('0')
            zeros =neighbour[z]

            for i in zeros:
                arr=list(state)
                arr[z] , arr[i] = arr[i] , arr[z]
                new_state = "".join(arr)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state,moves+1))
        return -1