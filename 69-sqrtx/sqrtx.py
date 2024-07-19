class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low = 1
        high = x
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
