class Solution:
    def generate(self, numRows: int) -> List[List[int]]: 
        if numRows==0:
            return []
        if numRows ==1:
            return [[1]]    
        if numRows>=2:
            dp=[[1] for k in range(numRows)]
            dp[1]=[1,1]
            for i in range(2,numRows):
                for j in range(1,len(dp[i-1])):
                    dp[i].append(dp[i-1][j-1]+dp[i-1][j])
                dp[i].append(1)
            return dp        
                
           



        