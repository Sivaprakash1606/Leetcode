class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""        
        # if int(num[-1])%2==1:
        #     return num
        # even=""
        # odd=""    
        # for i in num:
        #     if int(i)%2==1:
        #         odd=even+i
        #         even=odd
        #     else:
        #         even=even+i  
        # return odd                        