class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        ref=arr[0]-arr[1]
        for i in range(len(arr)-1):
            j=i+1

            if abs(ref) != abs(arr[i]-arr[j]):
                return False
        
        return True