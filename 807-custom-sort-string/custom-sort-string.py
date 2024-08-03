class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1

        wiith=""      
        for j in order:
            if j in d:
                wiith=wiith+(j*d[j])
        for k in s:
            if k not in order:
                wiith=wiith+k
        return wiith        





        