class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        for i in nums[:k]:
            min_heap.append(i)
        heapq.heapify(min_heap)
        for j in range(k,len(nums)):
            if nums[j]>min_heap[0]:
                heapq.heappushpop(min_heap,nums[j])  
        return min_heap[0]         

        # Using max-heap
        # for i in range(len(nums)):
        #     nums[i]=-nums[i]
        # heapq.heapify(nums) 
        # for j in range(k-1):
        #     heapq.heappop(nums)
        # return -heapq.heappop(nums)    

        

        # Time Limit Exceeded
        # for i in range(k-1):
        #     nums.remove(max(nums))
        # return max(nums)    