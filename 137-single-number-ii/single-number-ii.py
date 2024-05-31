class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                if d[i]==1:
                    d[i]=d[i]+1 
                else:
                    del d[i] 
        return list(d.keys())[0]                
        