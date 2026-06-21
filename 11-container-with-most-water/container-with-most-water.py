class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        m=0
        temp_max=0
        while i<j:
            if(height[i] > height[j]):
                temp_max=height[j]*(j-i)
                j-=1
            else:
                temp_max=height[i]*(j-i)
                i+=1
            m=max(m,temp_max)
        return m