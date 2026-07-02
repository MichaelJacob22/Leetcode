class Solution:
    def insert(self, intervals, newInterval):
        a=[]
        a=intervals
        a.append(newInterval)
        a.sort()
        
        b=[]


        first=a[0][0]
        last=a[0][1]

        for i in a[1:]:
            print(first, last)
            if i[0]<=last:
                last=max(last,i[1])

            else:
                b.append([first,last])
                first=i[0]
                last=i[1]

        b.append([first,last])
        return b


        