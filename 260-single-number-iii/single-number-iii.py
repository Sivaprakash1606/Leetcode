class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=[]
        hash={}
        for i in nums:
            hash[i]=hash.get(i,0)+1
        for key,value in hash.items():  
            if value==1:
                result.append(key)
        return result        
                  
        