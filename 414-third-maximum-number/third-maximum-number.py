from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxx1 = -2147483649
        maxx2 = -2147483649
        maxx3 = -2147483649
        
        for i in nums:
            if i > maxx1:
                maxx3 = maxx2
                maxx2 = maxx1
                maxx1 = i
            elif i > maxx2 and i < maxx1:
                maxx3 = maxx2
                maxx2 = i
            elif i > maxx3 and i < maxx2:
                maxx3 = i
        
        if maxx3 == -2147483649:
            return maxx1
        else:
            return maxx3
