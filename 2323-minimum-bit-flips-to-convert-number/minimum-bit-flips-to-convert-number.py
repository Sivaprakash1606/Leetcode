class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=self.binary(start)
        b=self.binary(goal)
        
        max_len=max(len(a),len(b))
        a=self.zeros(a,max_len)
        b=self.zeros(b,max_len)    

        count=0
        for i in range(max_len):
            if a[i]!=b[i]:
                count=count+1
        return count

    def binary(self,decimal):
        binaryy=""
        while decimal>0:
            binaryy=str(decimal%2)+binaryy
            decimal=decimal//2
        return binaryy if binaryy !="" else "0"

    def zeros(self,num,max_len):
        while len(num)<max_len:
            num="0"+num
        return num    

        
             
        
        


        
        