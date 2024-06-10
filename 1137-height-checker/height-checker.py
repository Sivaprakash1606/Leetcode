class Solution:
    def heightChecker(self, heights: List[int]) -> int: 
        expected=sorted(heights)
        if heights==expected:
            return 0
        result=0    
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result+=1
        return result            


        