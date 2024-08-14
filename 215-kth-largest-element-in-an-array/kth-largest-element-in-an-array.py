class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums) 
        for j in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)    

        
        
        # Time Limit Exceeded
        # for i in range(k-1):
        #     nums.remove(max(nums))
        # return max(nums)    