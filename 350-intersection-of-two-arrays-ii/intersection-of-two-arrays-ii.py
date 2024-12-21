class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in nums1:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1  

        h={}
        for j in nums2:
            if j in h:
                h[j]=h[j]+1
            else:
                h[j]=1            
                    
        result=[]
        sett=set()
        for k in nums1:
            if k not in sett and k in nums1 and k in nums2:
                minn=min(h[k],d[k])
                sett.add(k)
                for l in range(minn):
                    result.append(k)
        return result                    



             
        