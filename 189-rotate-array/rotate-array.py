class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = 1
        while l <= k:
            v = nums.pop()
            nums.insert(0, v)
            l += 1  
        return nums
        