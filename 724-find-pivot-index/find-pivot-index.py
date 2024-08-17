class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            total_sum -= nums[i]  # This is now the sum of elements to the right of arr[i]
            
            if left_sum == total_sum:
                return i
            
            left_sum += nums[i]  # Update the sum of elements to the left of arr[i]
        
        return -1


        