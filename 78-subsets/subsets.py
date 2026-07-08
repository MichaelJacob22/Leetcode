class Solution:
    def subsets(self, nums):
        b=[]
        def f(i,c):
            nonlocal b

            if i==len(nums):
                b.append(c[:])
                return
            
            c.append(nums[i])
            f(i+1,c)
            c.pop()
            f(i+1,c)

        f(0,[])
        b.sort()
        return b