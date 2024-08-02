class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        curr=0
        while curr<len(intervals) and intervals[curr][1]<newInterval[0]:
            result.append(intervals[curr])
            curr=curr+1
        while curr<len(intervals) and newInterval[1]>=intervals[curr][0]:
            newInterval[0]=min(newInterval[0],intervals[curr][0])
            newInterval[1]=max(newInterval[1],intervals[curr][1])
            curr=curr+1
        result.append([newInterval[0],newInterval[1]])   
        while curr<len(intervals):
            result.append(intervals[curr])
            curr=curr+1
        return result     






        #wrong
        # n,m=newInterval[0],newInterval[1]
        # result=[]
        # for i in range(len(intervals)):
        #     if n<=intervals[i][1]:
        #         intervals[i][1]=max(intervals[i][1],m)
        #         n=intervals[i][0]
        #         m=intervals[i][1]
        #     else:
        #         result.append(intervals[i]) 
        # result.append(intervals[i])           
        # return result   

            

        