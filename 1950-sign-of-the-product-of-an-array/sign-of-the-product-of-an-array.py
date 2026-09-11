import math

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a=math.prod(nums)

        if a==0:
            return 0
        elif a>0:
            return 1
        else:
            return -1