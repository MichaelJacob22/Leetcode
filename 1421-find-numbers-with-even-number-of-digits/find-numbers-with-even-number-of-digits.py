class Solution:
    def findNumbers(self, nums):
        a=0
        for j in range(0,len(nums),1):
            if(len(str(nums[j]))%2==0):
                a+=1
        return a
        