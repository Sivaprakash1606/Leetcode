class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        n=len(nums)
        for i in range(len(nums)):
            l=i+1
            r=n-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ>0:
                    r=r-1
                elif summ<0:
                    l=l+1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l=l+1
                    r=r-1
        return result

        # using two pointer 
        # nums.sort()
        # n,result=len(nums),[]
        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     l=i+1
        #     r=n-1
        #     while l<r:
        #         summ=nums[i]+nums[l]+nums[r]
        #         if summ>0:
        #             r=r-1
        #         elif summ<0:
        #             l=l+1
        #         else:
        #             result.append([nums[i],nums[l],nums[r]])   
        #             while l<r and nums[l]==nums[l+1]:
        #                 l=l+1
        #             while l<r and nums[r]==nums[r-1]:
        #                 r=r-1
        #             l=l+1
        #             r=r-1
        # return result                


        # st = set()  # Step 1
        # n = len(nums)  # Step 2

        # for i in range(n):  # Step 3
        #     hashset = set()  # Step 4
        #     for j in range(i + 1, n):  # Step 5
        #         # Calculate the 3rd element:
        #         third = -(nums[i] + nums[j])  # Step 6

        #         # Find the element in the set:
        #         if third in hashset:  # Step 7
        #             temp = [nums[i], nums[j], third]  # Step 8
        #             temp.sort()  # Step 9
        #             st.add(tuple(temp))  # Step 10

        #         hashset.add(nums[j])  # Step 11

        # ans = list(st)  # Step 12
        # return ans  # Step 13





            # Wrong - Time Limit execeed...
        # result = []  
        # nums.sort()         
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         rem = -(nums[i] + nums[j]) 
        #         if rem in nums[j + 1:]:
        #             a = [nums[i], nums[j], rem]
        #             if a not in result:
        #                 result.append(a)        
        # return result
                
        # result=[]
        # nums.sort()
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 a=[nums[i],nums[j],nums[k]]
        #                 if a not in result:
        #                     result.append(a)
        #             if nums[i]+nums[j]+nums[k] >0:
        #                 break    
        # return result                
