class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        i = 0
        while i < count:
            if nums[i] == val:
                del nums[i]
                count -= 1
            else:
                i += 1
        return count

        