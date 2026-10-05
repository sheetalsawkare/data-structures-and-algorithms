class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_interval=[]
        res=[]
        new_s1=newInterval[0]
        insert=False
        for interval in intervals:
            start = interval[0]
            if start>new_s1 and insert==False:
                new_interval.append(newInterval)
                insert=True
            new_interval.append(interval)
        if insert==False:
            new_interval.append(newInterval)
        # now we have the new sorted interval
        # now merge the intervals
        start1=new_interval[0][0]
        end1=new_interval[0][1]
        i=1
        while i<len(new_interval):
            start2=new_interval[i][0]
            end2=new_interval[i][1]
            if start2<=end1:
                start1=start1
                end1=max(end1,end2)
            else:
                res.append([start1,end1])
                start1=start2
                end1=end2
            i+=1
        res.append([start1,end1])
        return res