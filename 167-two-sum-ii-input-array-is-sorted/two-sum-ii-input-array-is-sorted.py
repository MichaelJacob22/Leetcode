class Solution:
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            if target == numbers[i]+numbers[j]:
                return [i+1,j+1]
            elif(target < numbers[i]+numbers[j]):
                j-=1
            else:
                i+=1    