class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = set('aeiouAEIOU')
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l] not in vow:
                l=l+1
            elif s[r] not in vow:  
                r=r-1  
            elif s[l] in vow and s[r] in vow:
                s[l],s[r] = s[r],s[l]
                l=l+1
                r=r-1
        return ''.join(s)       


        