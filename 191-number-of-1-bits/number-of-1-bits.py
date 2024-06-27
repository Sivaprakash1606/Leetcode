class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]  
        return binary.count('1')