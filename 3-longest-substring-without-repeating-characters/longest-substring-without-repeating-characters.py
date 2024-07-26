class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=""
        r=""
        i=0
        while i <len(s):
            if s[i] not in res:
                res=res+s[i]  
            elif s[i] in res:
                if len(res)>len(r):
                    r=res    
                res=res[res.index(s[i]) + 1:] + s[i]
            i=i+1   
        if len(res)>len(r):
            return len(res)
        else:
            return len(r)     
        



        