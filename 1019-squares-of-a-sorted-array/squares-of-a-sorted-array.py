class Solution:
    def sortedSquares(self, nums):
        a = []

        for i in nums:
            a.append(i * i)

        a.sort()

        return a