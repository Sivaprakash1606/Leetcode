class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        maxx=0
        for i,height in enumerate(heights):
            start=i
            while stack and height < stack[-1][0]:
                h,j=stack.pop()
                w=i-j
                area=h*w
                maxx=max(maxx,area)
                start=j
            stack.append((height,start))   
        while stack:
            h,j=stack.pop()
            w=n-j
            area=h*w
            maxx=max(maxx,area)
        return maxx         






        # Time Limit Exceeded
        # stack=[]
        # for i in range(len(heights)):
        #     count=1
        #     for j in range(i-1,-1,-1):
        #         if heights[j]>=heights[i]:
        #             count=count+1
        #         else:
        #             break    
        #     for k in range(i+1,len(heights)):
        #         if heights[k]>=heights[i]:
        #             count=count+1
        #         else:
        #             break 
        #     stack.append(count*heights[i])
        # print(stack)    
        # return max(stack)            



        