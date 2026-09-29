class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        a=sorted(nums)

        if nums == a:
            return True
        
        if nums[::-1] == a:
            return True
        
        return False