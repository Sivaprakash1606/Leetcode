class Solution:
    def maxDepth(self, s: str) -> int:
        maxx=0
        count=0
        for i in s:
            if i=="(":
                count=count+1
            elif i==")":
                count=count-1 
            maxx=max(maxx,count)       
        return maxx      
        