class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder={0:0}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            r=total%k
            if r not in reminder:
                reminder[r]=i+1
                print(i)
            elif (i+1)-reminder[r]>=2:
                return True
        return False          



        