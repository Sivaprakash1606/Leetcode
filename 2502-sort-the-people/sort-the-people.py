class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)-1):
            for j in range(len(heights)-1):
                if heights[j]>heights[j+1]:
                    continue
                else:
                    names[j],names[j+1]=names[j+1],names[j]
                    heights[j],heights[j+1]=heights[j+1],heights[j]
        return names               
        