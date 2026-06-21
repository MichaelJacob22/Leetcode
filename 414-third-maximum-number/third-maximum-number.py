class Solution:
    def thirdMax(self, nums):
        max=0
        nums=list(set(nums))
        if(len(nums)==2):
            if(nums[0]>=nums[1]):
                max=nums[0]
            else:
                max=nums[1]
        elif(len(nums)==1):
            max=nums[0]
        else:
            b=len(nums)
            for i in range(0,3,1):
                max=nums[0]
                for j in range(0,b,1):
                    if(max<=nums[j]):
                        max=nums[j]
                if(i!=2):
                    nums.remove(max)
                    b-=1
        return max