class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for i in words:
            if i in freq:
                freq[i] = freq[i] + 1
            else:
                freq[i] = 1

        heap = []        
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        for _ in range(k):
            if heap:
                value, key = heapq.heappop(heap)
                result.append(key)
        return result