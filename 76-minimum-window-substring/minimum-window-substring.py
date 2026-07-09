class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ""
        maps={}
        for ch in t:
            maps[ch]=maps.get(ch,0)+1

        start=0
        startindex=0
        end=0
        count=(sum(i for i in maps.values()))
        minlen=float('INF')
        while end < len(s):

            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] >= 0:
                    count -= 1

            while count == 0:
            
                if end - start + 1 < minlen:
                    minlen = end - start + 1
                    startindex = start

                if s[start] in maps:
                    maps[s[start]] += 1
                    if maps[s[start]] > 0:
                        count += 1
                        
                start += 1
            end += 1
        if minlen == float('inf'):
            return ""
        else:
            return s[startindex:startindex+minlen]
                