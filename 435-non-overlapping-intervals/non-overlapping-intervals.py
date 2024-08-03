class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result=0
        i=0
        while i<len(intervals)-1:
            curr_end=intervals[i][1]
            while i+1<len(intervals) and curr_end > intervals[i+1][0]:
                result=result+1
                curr_end=min(curr_end,intervals[i+1][1])
                i=i+1
            i=i+1    
        return result        





        

        