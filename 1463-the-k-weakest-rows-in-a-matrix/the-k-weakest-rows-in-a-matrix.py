class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        for i in range(len(mat)):
            summ=sum(mat[i])
            heapq.heappush(heap,(-summ,-i))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        while heap:
            sol,i=heapq.heappop(heap)
            result.append(-i)
        return result[::-1]            
    



        