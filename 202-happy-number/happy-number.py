import math
class Solution:
    def isHappy(self, n: int) -> bool:
        # digits = int(math.log10(n)) + 1
        # while digits > 1:
        seen=set()
        while n!=1 and n not in seen :
            seen.add(n)
            summ=0
            while n>0:
                l = n % 10
                summ = summ + (l * l)
                n = n // 10
            # digits = int(math.log10(summ)) + 1
            n=summ
        return n == 1

        