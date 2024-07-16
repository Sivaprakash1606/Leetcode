class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s=nums[0]
        for i in range(1,len(nums)):
            if s>0:
                s=s-1
                step=max(nums[i],s)
                s=step
            else:
                return False
        return True            




        