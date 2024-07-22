class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1])%2==1:
            return num
        even=""
        odd=""    
        for i in num:
            if int(i)%2==1:
                odd=even+i
                even=odd
            else:
                even=even+i  
        return odd                        