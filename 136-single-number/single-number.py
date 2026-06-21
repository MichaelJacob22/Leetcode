class Solution:
    def singleNumber(self, nums):
        d=0
        for i in range(0,len(nums),1):
            d=d^nums[i]
        return d

        