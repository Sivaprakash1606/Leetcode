class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD=10**9+7
        sub_sum=[]
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                sub_sum.append(s)
                
        # l,r=0,1
        # while r<=n:
        #     summ=nums[l]
        #     sub_sum.append(summ)
        #     while r<n:
        #         summ=summ+nums[r]
        #         sub_sum.append(summ)
        #         r=r+1
        #     l=l+1                

    
        
        # Bubble sort
        # for i in range(len(sub_sum)-1):
        #     for j in range(len(sub_sum)-1):
        #         if sub_sum[j]>sub_sum[j+1]:
        #             sub_sum[j],sub_sum[j+1]=sub_sum[j+1],sub_sum[j]
        sub_sum.sort()
        res=0
        for i in range(left-1,right):
            res=(res+sub_sum[i])%MOD
        return res    


        # return sum(sub_sum[left-1:right])

        # total=0
        # left=left-1
        # while left<right:
        #     total=total+sub_sum[left]
        #     left=left+1
        # return total    



                
        