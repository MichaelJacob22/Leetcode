class Solution:
    def majorityElement(self, nums):
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

            if d[num] > len(nums) // 2:
                return num