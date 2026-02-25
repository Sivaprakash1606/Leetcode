class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx=0
        left, right = 0, len(height)-1

        while left<right:
            h=min(height[left], height[right])
            width=right-left
            maxx=max(maxx,(width*h))
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1

        return maxx            

        # O(n2)    
        # maxx=0
        # left, right= 0, len(height) - 1
        # while left<right:
        #     for i in range(left + 1, right + 1):
        #         contain=min(height[i],height[left])
        #         count=i-left
        #         maxx=max(maxx,contain*count)
        #     left=left+1
        # return maxx
        