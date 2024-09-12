class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for word in words:
            inn=False
            for w in word:
                if w in allowed:
                    inn=True
                else:
                    inn=False   
                    break
            if inn:
                count=count+1
        return count                 


        