class Solution:
    def merge(self, intervals):
        intervals.sort()

        first=intervals[0][0]
        e=intervals[0][1]

        a=[]

        print(intervals)
        for i in intervals[1:]:

            if i[0] <= e:
                e=max(e,i[1])

            else:
                a.append([first,e])
                first=i[0]
                e=i[1]
        a.append([first,e])
        return a
        