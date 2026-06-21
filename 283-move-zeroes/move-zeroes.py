class Solution:
    def moveZeroes(self, nums):
        a=len(nums)
        b=[]
        for i in nums:
            if(i!=0):
                b.append(i)
        nums[:]=b+[0 for j in range(0,len(nums)-len(b))]