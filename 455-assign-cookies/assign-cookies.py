class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=j=0
        while j<len(s):
            if g[i]<=s[j]:
                i=i+1
            j=j+1
            if i==len(g):
                break
        return i        