class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        res=""
        length=min(len(word) for word in strs)
        for j in range(length):
            while i < len(strs)-1:
                if strs[i][j]!=strs[i+1][j]:
                    return res
                i=i+1
            i = 0    
            res=res+strs[i][j]
        return res          

      

                        

                    

