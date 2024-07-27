class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd={}
        td={}
        for i in range(len(s)):
            if s[i] not in sd and t[i] not in td:
                sd[s[i]]=t[i]
                td[t[i]]=s[i]
            elif s[i] not in sd or t[i] not in td:
                return False
            else:
                if sd[s[i]]!=t[i] or td[t[i]]!=s[i] :
                    return False
        return True            
                    




        