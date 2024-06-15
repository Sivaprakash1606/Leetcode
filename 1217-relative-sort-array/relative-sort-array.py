class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        result=[]
        count={}
        for i in arr1[:]:
            if i not in count and i in arr2:
                count[i]=1
                arr1.remove(i)
            elif i in count and i in arr2:
                count[i]=count[i]+1
                arr1.remove(i)
        for num in arr2:
            if num in count:
                r=[num]*count[num]
                result.extend(r)
        result.extend(arr1)               
        return result





        