class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result=[]
        left=0
        right=0
        while right<len(nums)-1:
            if nums[right]+1 != nums[right+1]:
                if left==right:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left])+"->"+str(nums[right]))
                left=right+1
            right+=1

        if left==right:
            result.append(str(nums[left]))
        else:
            result.append(str(nums[left])+"->"+str(nums[right]))       
        return result           




        # if not nums:
        #     return []

        # result = []
        # start = nums[0]
        # end = nums[0]

        # for i in range(1, len(nums)):
        #     if nums[i] != end + 1:
        #         if start == end:
        #             result.append(str(start))
        #         else:
        #             result.append(str(start) + "->" + str(end))
        #         start = nums[i]
        #     end = nums[i]

        # # Handle the last range
        # if start == end:
        #     result.append(str(start))
        # else:
        #     result.append(str(start) + "->" + str(end))

        # return result





        