class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and ((i.isupper() and stack[-1]==i.lower()) or (i.islower() and stack[-1]==i.upper())):
                stack.pop()
                continue
            else:
                stack.append(i)
        return "".join(stack)  


        #Wrong          
        # s.reverse()
        # if len(s)<1:
        #     for i in range(len(s)):
        #             if s[i]==Uppercase:
        #                 s[i].remove() and s[j].remove
        # return s.reverse()  







        