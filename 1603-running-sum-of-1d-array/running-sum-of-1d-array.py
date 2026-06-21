class Solution:
    def runningSum(self, nums):
        a=[]
        b=0
        for i in range(0,len(nums),1):
            b=b+nums[i]
            a.append(b)
        return a