class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:     
        matrixx=[]   
        count=1
        for i in matrix:
            for j in i:
                matrixx.append(j)
        matrixx.sort()
        return matrixx[k-1]            

                    

        