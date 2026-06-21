class Solution:
    def findTheDifference(self, s, t):
        for ch in t:
            count1 = 0
            count2 = 0

            for c in s:
                if c == ch:
                    count1 += 1

            for c in t:
                if c == ch:
                    count2 += 1

            if count1 != count2:
                return ch