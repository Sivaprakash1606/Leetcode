class Solution:
    def reverse(self, x: int) -> int:
        list1 = str(x)[::-1]
        if list1 == '0':  # If x is 0, return 0
            return 0
        if list1[0] == '0':
            list1 = list1[1:]
        negative = False
        if list1[-1] == "-":
            negative = True
            list1 = "-" + list1[:-1]
        result = int(list1)
        if negative and result < -2**31:
            return 0
        elif not negative and result >= 2**31:
            return 0
        return result