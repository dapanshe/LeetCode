# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.insert(0, Interval(-1001,-1000))
        intervals.append(Interval(100000,100001))
        in_head = False
        in_tail = False
        i = 1
        start = newInterval.start
        end   = newInterval.end
        while i < len(intervals):
            if intervals[i-1].start <= start and start < intervals[i].start:
                head = i-1
                if start <= intervals[i-1].end:
                    in_head = True
            if intervals[i-1].end < end and end <= intervals[i].end:
                tail = i
                if end >= intervals[i].start:
                    in_tail = True
            i += 1
        if in_head and in_tail:
            intervals[tail].start = intervals[head].start
            intervals[head:tail] = []
        if in_head and not in_tail:
            intervals[head].end = end
            intervals[head+1:tail] = []
        if not in_head and in_tail:
            intervals[tail].start = start
            intervals[head+1:tail] = []
        if not in_head and not in_tail:
            intervals[head+1:tail] = []
            intervals.insert(head+1,Interval(start,end))
        return intervals[1:-1]
