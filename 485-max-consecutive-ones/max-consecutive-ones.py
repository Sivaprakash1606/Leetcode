class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        count=0
        for i in nums:
            if i==1:
                count=count+1
            else:
                result=max(count,result)
                count=0        
        return max(count,result)         

        