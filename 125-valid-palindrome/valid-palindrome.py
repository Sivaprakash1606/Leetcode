class Solution:
    def isPalindrome(self, s: str) -> bool:
        f, l=0, len(s)-1
        while f<l:
            if not s[f].isalnum():
                f=f+1
            elif not s[l].isalnum():
                l=l-1   
            elif s[f].lower() != s[l].lower():
                return False
            else:
                f=f+1
                l=l-1
        return True                 