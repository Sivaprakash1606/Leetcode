class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        max_len=0
        for i,char in enumerate(s):
            if char=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len                

        # mistake
        # stack=[-1]
        # maxx_len=0
        # for i in s:
        #     if i == "(":
        #         stack.append(i)
        #     else:
        #         if len(stack)>=1:
        #             count=count+2
        #             stack.pop()
        #         else:
        #             continue
        # return count                          


