class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=="]":
                word=""
                while stack[-1] !="[":
                    word=stack.pop()+word
                stack.pop()
                num=""
                while len(stack)>0 and stack[-1].isdigit():
                    num=stack.pop()+num
                num=int(num)    
                word=num*word
                words=word.split()
                stack.extend(words)
            else:
                stack.append(i)
        return "".join(stack)                

                
        