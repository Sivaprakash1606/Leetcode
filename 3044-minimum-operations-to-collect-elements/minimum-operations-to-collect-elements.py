class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection=[]
        operation=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=k and nums[i] not in collection:
                collection.append(nums[i])
            operation+=1    
            if len(collection)==k:
                break
        return operation        

           