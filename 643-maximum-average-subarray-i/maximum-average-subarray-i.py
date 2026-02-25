class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=0
        for i in range(k):
            res=nums[i]+res
        maxx=res    
        left, right= 1, k
        while right<len(nums):
            res=res-nums[left-1]
            res=res+nums[right]
            maxx=max(res,maxx)
            left=left+1
            right=right+1
        return maxx/k  


            
            


        