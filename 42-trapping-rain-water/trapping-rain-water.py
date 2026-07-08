class Solution:
    def trap(self, height):
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        water=0

        while l<r:
            if height[l] <= height[r]:
                lmax=max(height[l],lmax)
                water+=lmax-height[l]
                
                l+=1

            else:
                rmax=max(height[r],rmax)
                water+=rmax-height[r]

                r-=1

        return water