class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        left = 0
        right = 0
        while right < len(nums) - 1:
            if nums[right] + 1 != nums[right + 1]:
                if left == right:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[right]))
                left = right + 1
            right += 1

        # Handle the last range
        if left == right:
            result.append(str(nums[left]))
        else:
            result.append(str(nums[left]) + "->" + str(nums[right]))

        return result
