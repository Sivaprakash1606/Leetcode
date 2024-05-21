class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxx=0
        while r>l:
            minn=min(height[r],height[l])
            dist=r-l
            res=minn*dist
            if res>maxx:
                maxx=res
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return maxx                





        