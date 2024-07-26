class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using Sliding window 
        res=0
        res_set=set()
        l=0
        for i in range(len(s)):
            while s[i] in res_set:
                res_set.remove(s[l])
                l=l+1
            res_set.add(s[i])
            res=max(res,i-l+1)
        return res    



        # res=""
        # r=""
        # i=0
        # while i <len(s):
        #     if s[i] not in res:
        #         res=res+s[i]  
        #     elif s[i] in res:
        #         if len(res)>len(r):
        #             r=res    
        #         res=res[res.index(s[i]) + 1:] + s[i]
        #     i=i+1   
        # if len(res)>len(r):
        #     return len(res)
        # else:
        #     return len(r)     
        



        