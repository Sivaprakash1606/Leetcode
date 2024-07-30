class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        count=0
        while count<k:
            if i not in arr:
                count=count+1
            i=i+1    
        return i-1     
        