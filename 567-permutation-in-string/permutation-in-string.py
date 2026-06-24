class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        elif len(s1)==1:
            if(s1 in s2):
                return True
            return False
        f1={}
        f2={}
        for ch in s1:
            f1[ch]=f1.get(ch,0)+1
        f1=dict(sorted(f1.items()))
        for i in range(len(s1)):
            f2[s2[i]]=f2.get(s2[i],0)+1
        f2=dict(sorted(f2.items()))
        k=0
        v=len(s1)
        for j in range(1,len(s2)-len(s1)+1,1):
            if(f1==f2):
                return True
            else:

                f2[s2[v]]=f2.get(s2[v],0)+1

                if f2.get(s2[k])>1:
                    f2[s2[k]]-=1

                else:
                    f2.pop(s2[k])
                
                f2=dict(sorted(f2.items()))
                k+=1
                v+=1
        if f1==f2:
            return True
        return False

        