from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordset=set(wordList)

        if endWord not in wordset:
            return 0

        queue=deque([(beginWord,1)])
        visited={beginWord}

        while queue:
            state,moves = queue.popleft()

            if state == endWord:
                return moves

            for i in range(len(beginWord)):
                arr=list(state)
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    arr[i]=ch
                    new_arr="".join(arr)

                    if new_arr in wordset and new_arr not in visited:
                        visited.add(new_arr)
                        queue.append((new_arr,moves+1))
        return 0
                