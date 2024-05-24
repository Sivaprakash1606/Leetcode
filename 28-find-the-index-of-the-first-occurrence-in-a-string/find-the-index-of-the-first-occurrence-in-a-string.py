class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        i=0
        while i<len(haystack):
            if haystack[i:l+i] == needle:
                return i
            i=i+1
        return -1        
        