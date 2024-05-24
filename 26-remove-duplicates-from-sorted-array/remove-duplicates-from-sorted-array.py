class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=list(sorted(set(nums)))
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)    





   
        