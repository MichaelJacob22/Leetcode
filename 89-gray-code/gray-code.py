class Solution:
    def grayCode(self, n: int) -> List[int]:
        a=[]
        for i in range(1<<n):
            a.append(i^(i>>1))
        return a