class Solution:
    def isUgly(self, n: int) -> bool:
        if n==1:
            return True
        elif n<=0:
            return False    
        elif n%2==0:
            n=n//2
            return self.isUgly(n)
        elif n%3==0:
            n=n//3
            return self.isUgly(n)
        elif n%5==0:
            n=n//5
            return self.isUgly(n)
        return False            


        