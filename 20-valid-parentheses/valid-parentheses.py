class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d={"[":"]","(":")","{":"}"}
        for i in s:
            if i in d.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                else:
                    if d[stack[-1]]==i:
                        stack.pop()
                    else:
                        return 0
        if stack ==[]:
            return True
        else:
            return False                        




                      


