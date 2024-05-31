class Solution(object):
    def singleNumber(self, nums):
        seen = set()
        for i in nums: 
            if i in seen:
                seen.remove(i)  
            else:
                seen.add(i)
        return seen.pop()




        