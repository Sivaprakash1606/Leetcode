class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result=[[0]* n for i in range(n)]
        left=0
        right=n-1
        top=0
        bottom=n-1
        count=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result[top][i]=count
                count=count+1
            top=top+1
            for i in range(top,bottom+1):
                result[i][right]=count
                count=count+1
            right=right-1
            if left<=right:
                for i in range(right,left-1,-1):
                    result[bottom][i]=count
                    count=count+1
                bottom=bottom-1
            if top<=bottom:
                for i in range(bottom,top-1,-1):
                    result[i][left]=count
                    count=count+1
                left=left+1
        return result                            


        