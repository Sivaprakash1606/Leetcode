class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        interval=[]
        intervals.sort()
        n,m=intervals[0]
        for i in range(1,len(intervals)):
            if m>=intervals[i][0]:
                m=max(m,intervals[i][1])
            else:
                interval.append([n,m])
                n,m=intervals[i]
        interval.append([n,m])        
        return interval      

        
        #Another way
        # result=[]
        # intervals.sort()
        # i=0
        # while i<len(intervals):
        #     nextstart=intervals[i][0] 
        #     currentend=intervals[i][1] 
        #     while i<len(intervals)-1 and currentend>=intervals[i+1][0]:
        #         currentend=max(currentend,intervals[i+1][1])
        #         i=i+1
        #     result.append([nextstart,currentend])    
        #     i=i+1
        # return result    

        # mistaken code  
        # n = intervals[0][1]
        # m = intervals[0][0]
        # i = 1
        # while i < len(intervals)-1:
        #     if n >= intervals[i][0] or m >= intervals[i][0]:
        #         intervals[i][0] = min(intervals[i][0], m)
        #         intervals[i][1] = max(intervals[i][1], n)
        #         del intervals[i-1]
        #     n = intervals[i][1]
        #     m = intervals[i][0]
        #     i += 1
        # return intervals
        