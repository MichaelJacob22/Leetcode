class Solution:
    def missingNumber(self, nums):
        a=int((len(nums)*(len(nums)+1)/2))
        b=0
        for i in nums:
            b+=i
        return(a-b)
        