from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        result = 0
        curr_end = intervals[0][1]
        
        # Iterate through intervals starting from the second one
        for i in range(1, len(intervals)):
            # If the current interval's start time is less than the previous end, it's overlapping
            if intervals[i][0] < curr_end:
                # Increment removal count since there's an overlap
                result += 1
            else:
                # Otherwise, update curr_end to the end of the current interval
                curr_end = intervals[i][1]
        
        return result
