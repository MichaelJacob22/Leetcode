from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for i in permutations(nums):
            a.append(i)
        return a