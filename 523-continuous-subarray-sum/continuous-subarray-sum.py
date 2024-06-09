class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder={0:-1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            r=total%k
            if r not in reminder:
                reminder[r]=i
                print(i)
            elif i-reminder[r]>1:
                return True
        return False          



        