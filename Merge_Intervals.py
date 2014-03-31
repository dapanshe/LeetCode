# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
## pay attention to the situation [1,4],[2,3]  intervals.end = max(i.end,(i-1).end)
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x:x.start)
        i = 1
        while i < len(intervals):
            if intervals[i].start <= intervals[i-1].end:
                intervals[i-1].end = max(intervals[i].end, intervals[i-1].end)
                intervals.pop(i)
            else:
                i += 1
        return intervals
        
