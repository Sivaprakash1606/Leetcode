class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0
        
        # if n%4==0:
        #     return False
        # return True        
        