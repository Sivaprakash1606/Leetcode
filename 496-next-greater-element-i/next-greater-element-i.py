class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash={}
        for i in range(len(nums2)):
            hash[nums2[i]]=i
        for i in range(len(nums1)):
            found=False
            for j in range(hash[nums1[i]]+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    nums1[i]=nums2[j]
                    found=True
                    break
            if found==False:
                nums1[i]=-1
        return nums1                     



        