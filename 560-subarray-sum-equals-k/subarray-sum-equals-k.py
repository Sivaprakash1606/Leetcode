class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  
        
        for num in nums:
            prefix_sum += num 
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  
            else:
                prefix_sum_count[prefix_sum] = 1 
        
        return count
        
        # result=0
        # for i in range(len(nums)):
        #     summ=0
        #     for j in range(i,len(nums)):
        #         summ=summ+nums[j]
        #         if summ==k:
        #             result=result+1
        #             break
        #         elif summ>k:
        #             break    
        # return result             


        # count=0
        # for i in range(len(nums)):
        #     c=nums[i]
        #     if c==k:
        #         count=count+1
        #     for j in range(i+1,len(nums)):
        #         c=c+nums[j]
        #         if c==k:
        #             count=count+1
        # return count       

        