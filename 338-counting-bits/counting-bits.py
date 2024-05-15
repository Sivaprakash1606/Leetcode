class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        if n>=1 :
            dp=[0]*(n+1)
            i=1
            while i<=n:
                a=bin(i)
                dp[i]=a.count('1')
                i=i+1             
            return dp        

                

                         
    
            

        