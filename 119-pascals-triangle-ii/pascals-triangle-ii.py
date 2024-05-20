class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]        
        dp = [[1] for k in range(rowIndex+1)]
        dp[1] = [1,1]
        for i in range(2, rowIndex+1):
            for j in range(1,len(dp[i-1])):
                dp[i].append(dp[i-1][j-1]+dp[i-1][j])
            dp[i].append(1)
        return dp[-1]
