class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using Greedy
        m=nums[0]
        c=0
        for i in nums:
            if c<0:
                c=0
            c=c+i
            m=max(c,m)    
        return m    
        # if len(nums)==1:
        #     return nums[0]
        # maxx=maxx1=nums[0]
        # for i in range(len(nums)):
        #     maxx1=nums[i]
        #     if maxx1>maxx:
        #         maxx=maxx1
        #     for j in range(i+1,len(nums)):
        #         maxx1=maxx1+nums[j]
        #         if maxx1>maxx:
        #             maxx=maxx1
        # return maxx           

        