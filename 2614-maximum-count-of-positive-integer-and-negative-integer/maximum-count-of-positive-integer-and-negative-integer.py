class Solution:
    def maximumCount(self, nums):
        a,b=0,0
        for i in range(0,len(nums),1):
            if(nums[i]>0):
                a+=1
            elif(nums[i]<0):
                b+=1
        if(a<=b):
            return b
        else:
            return a