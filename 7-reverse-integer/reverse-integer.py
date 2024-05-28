class Solution:
    def reverse(self, x: int) -> int:
        list1 = str(x)[::-1]
        if list1 == '0':  
            return 0
        if list1[0] == '0':
            list1 = list1[1:]
        if list1[-1] == "-":
            list1 = "-" + list1[:-1]
            if int(list1) < -2**31:
                return 0
        if int(list1) >= 2**31:
            return 0
        return int(list1)    
        
