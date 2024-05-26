class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                maxx1=s[i:j]
                if maxx1==maxx1[::-1] and len(maxx1)>len(maxx):
                    maxx=maxx1
        return maxx            


        