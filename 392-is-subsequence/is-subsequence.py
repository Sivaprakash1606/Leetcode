class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1=0
        p2=0
        while p1<len(t) and p2<len(s):
            if t[p1]== s[p2]:
                p1=p1+1
                p2=p2+1
            else:
                p1=p1+1
        if p2 == len(s):
            return True
        else:
            return False                
