class Solution:
    def pivotInteger(self, n: int) -> int:
        num=0
        a=n
        for i in range(n+1):
            num=num+i       
        for i in range(n):   
            current=a         
            if num==n:
                return current
            else:
                num=num-current
                a=a-1
                n=n+a
        return -1        



        