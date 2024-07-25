from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def custom_sort(word):
            words = list(word)
            n = len(words)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if words[j] > words[j + 1]:
                        words[j], words[j + 1] = words[j + 1], words[j]
            return ''.join(words)
        
        anagrams = []
        sorted_words = []
        
        for word in strs:
            sorted_word = custom_sort(word)
            added = False
            
            for i in range(len(sorted_words)):
                if sorted_words[i] == sorted_word:
                    anagrams[i].append(word)
                    added = True
                    break
            
            if not added:
                sorted_words.append(sorted_word)
                anagrams.append([word])
        
        return anagrams


