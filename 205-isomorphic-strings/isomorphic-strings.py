class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for s_char, t_char in zip(s, t):
            if (s_char in s_to_t and s_to_t[s_char] != t_char) or (t_char in t_to_s and t_to_s[t_char] != s_char):
                return False
            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char
        
        return True
                    




        