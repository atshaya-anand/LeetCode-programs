# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        res = []
        intervals.sort()
        i = 0
        
        while i < len(intervals) - 1:
            
            if intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[1][0]:
                max_interval = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = [intervals[i][0], max_interval]
            else:
                res.append(intervals[i])
            if i == len(intervals) - 2:
                res.append(intervals[i+1])

            i += 1
            
        return res