class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        minn=min(len(word1),len(word2))    
        i=0
        while i<minn:
            result=result+word1[i]+word2[i]
            i=i+1
        if len(word1)!=minn:
            return result+word1[i:]
        return result+word2[i:]  
      

   

        