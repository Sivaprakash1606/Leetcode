class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                x = num + 1
                while x in s:
                    x += 1
                longest = max(longest, x - num) 
            
        return longest
        