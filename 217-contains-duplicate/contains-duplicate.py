class Solution:
    def containsDuplicate(self, nums):
        if(len(nums)==len(set(nums))):
            return False
        return True