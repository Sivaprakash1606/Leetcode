class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary=bin(n)[2:]
        num=n
        count=0
        while num>0:
            quotient=num//2
            reminder=num%2
            num=quotient
            if reminder==1:
                count=count+1
        return count        

        
        