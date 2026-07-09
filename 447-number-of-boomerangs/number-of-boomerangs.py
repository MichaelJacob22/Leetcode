class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)):
            f={}
            for j in range(len(points)):
                if i==j:
                    continue
                
                dx=points[i][0]-points[j][0]
                dy=points[i][1]-points[j][1]

                dist=dx*dx +dy*dy

                f[dist]=f.get(dist,0)+1

            for count in f.values():
                ans+= count*(count-1)

        return ans
