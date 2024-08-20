class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = (len(nums1) + len(nums2)) // 2 
        even = (len(nums1) + len(nums2)) % 2 == 0  
        result = []
        l1, l2 = 0, 0
        
        while l1 < len(nums1) or l2 < len(nums2):
            if len(result) > length:
                break
            if l1 < len(nums1) and (l2 >= len(nums2) or nums1[l1] < nums2[l2]):
                result.append(nums1[l1])
                l1 += 1
            else:
                result.append(nums2[l2])
                l2 += 1        
        if even:
            ans = (result[length] + result[length - 1]) / 2.0  
            return ans
        return float(result[length])


        # nums1.extend(nums2)
        # nums1.sort()
        # mid=len(nums1)//2
        # if len(nums1)%2 == 0:
        #     return (nums1[mid-1]+nums1[mid])/2
        # else:
        #     return nums1[mid]   
            


        