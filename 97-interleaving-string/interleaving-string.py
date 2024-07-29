class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,l=len(s1),len(s2),len(s3)
        if m+n != l:
            return False
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in range(1,n+1):
            dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s3[i+j-1]:
                    dp[i][j]=dp[i-1][j]
                if s2[j-1]==s3[i+j-1]:
                    dp[i][j]=dp[i][j] or dp[i][j-1] 
        return dp[m][n] 


        # Wrong one
        # if len(s1) + len(s2) != len(s3):
        #     return False
        # i=0
        # f=0
        # s=0
        # while i < len(s3):
        #     while f < len(s1) and s3[i]==s1[f]:
        #         i=i+1
        #         f=f+1
        #     while s < len(s2) and s3[i] == s2[s]:
        #         s=s+1
        #         i=i+1    
        #     if f<len(s1) and s3[i]!=s1[f]:
        #         return False
        # return True        
        