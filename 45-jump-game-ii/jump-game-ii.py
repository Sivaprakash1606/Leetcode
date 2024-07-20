from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        
        while right < len(nums) - 1:
            maxx = 0
            for i in range(left, right + 1):
                maxx = max(maxx, i + nums[i])
            left = right + 1
            right = maxx
            result += 1
            
        return result
         
        
        # n=len(nums)-1
        # i=0
        # current=nums[i]
        # if current==n:
        #     return current 
        # step=1
        # for j in range(i+1,nums[i]-1):
        #     if nums[j]>nums[j+1]:
        #         i=j
        #         current=nums[i]
        #     else:
        #         i=j+1
        #         current=nums[i]
        #     if current>=n:
        #         return step+1
        #     else:
        #         step=step+1    
        # return step          


        # reach=len(nums)-1
        # step=1
        # for i in range(0,reach):
        #     for j in range(i+1,i+nums[i]-1):
        #         maxx=max(nums[j],nums[j+1])
        #         if maxx+step>=reach:
        #             return step
        #     step=step+1    
        # return step        




        