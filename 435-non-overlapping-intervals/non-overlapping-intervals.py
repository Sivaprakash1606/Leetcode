from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        end = float('-inf')  # Tracks the end time of the last added interval
        result = 0  # Count of intervals to remove
        
        # Iterate through the sorted intervals
        for interval in intervals:
            # If the current interval's start time is greater than or equal to the end of the last interval
            if interval[0] >= end:
                # Update the end to the end time of the current interval
                end = interval[1]
            else:
                # Otherwise, increment the removal count since there's an overlap
                result += 1
        
        return result





        # intervals.sort()
        # result=0
        # i=0
        # while i<len(intervals)-1:
        #     curr_end=intervals[i][1]
        #     while i+1<len(intervals) and curr_end > intervals[i+1][0]:
        #         result=result+1
        #         curr_end=min(curr_end,intervals[i+1][1])
        #         i=i+1
        #     i=i+1    
        # return result        





        

        