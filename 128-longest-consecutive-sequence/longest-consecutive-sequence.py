class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        length=0
        for start in nums:
            if start-1 not in num:
                end=start+1
                while end in num:
                    end=end+1
                length=max(length,end-start)
        return length            
        #Not Optimised
        # num=list(set(nums))
        # if not num:
        #     return 0
        # num.sort()
        # i=num[0]
        # count=1
        # c=1
        # for j in range(1,len(num)):
        #     if num[j]==i+1:
        #         i=num[j]
        #         c=c+1
        #         if c>count:
        #             count=c
        #     else:
        #         i=num[j]
        #         c=1
        # return count      
        