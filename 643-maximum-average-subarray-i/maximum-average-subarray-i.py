class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxx=0
        for i in range(k):
            maxx=nums[i]+maxx
        pre=maxx    
        left, right= 1, k
        while right<len(nums):
            res=pre-nums[left-1]+nums[right]
            maxx=max(res,maxx)
            pre=res
            left=left+1
            right=right+1
        return maxx/k  


            
            


        