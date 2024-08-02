# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort()
#         result=0
#         for i in range(len(intervals)):
#             curr_end=intervals[i][1]
#             while i+1<len(intervals) and curr_end > intervals[i+1][0]:
#                 result=result+1
#                 curr=min(curr_end,intervals[i+1][1])
#                 i=i+1
#         return result        

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their start time
        intervals.sort()
        result = 0
        
        # Iterate over the intervals
        i = 0
        while i < len(intervals) - 1:
            curr_end = intervals[i][1]

            # Check for overlapping intervals
            while i + 1 < len(intervals) and curr_end > intervals[i + 1][0]:
                result += 1
                # Update curr_end to the minimum end of overlapping intervals
                curr_end = min(curr_end, intervals[i + 1][1])
                # Move to the next interval
                i += 1
            
            # Move to the next non-overlapping interval
            i += 1
        
        return result






        

        