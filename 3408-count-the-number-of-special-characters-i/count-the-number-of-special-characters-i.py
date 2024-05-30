class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        words=set()     
        for i in word:
            if i not in words:
                if i.isupper():
                    if i.lower() in word:
                        count=count+1  
                        words.add(i.lower())                        
                elif i.islower() :
                    if i.upper() in word:
                        count=count+1
                        words.add(i.upper())   
                words.add(i)                
        return count

