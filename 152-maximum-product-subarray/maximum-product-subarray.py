class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=nums[0]
        for i in range(len(nums)):
            prod=nums[i]
            if prod>maxx:
                maxx=prod
            for j in range (i+1, len(nums)):
                prod=nums[j]*prod
                if prod>maxx:
                    maxx=prod
        return maxx            
        