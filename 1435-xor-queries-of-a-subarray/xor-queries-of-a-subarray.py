class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        # prefix sum without extra memory
        n=len(arr)
        for i in range(1,n):
            arr[i]=arr[i]^arr[i-1]

        result=[]    
        for l,r in queries:
            if l==0:
                result.append(arr[r])
            else:
                ans=arr[r]^arr[l-1]
                result.append(ans)
        return result            

        # prefix sum with extra memory
        # n=len(arr)
        # prefix=[0] * (n+1)

        # for i in range(n):
        #     prefix[i+1]=prefix[i] ^ arr[i]
        
        # result=[]
        # for l,r in queries:
        #     ans=prefix[r+1]^prefix[l]
        #     result.append(ans)
        # return result    



        # Time Limit Exceeded
        # for k,sub in enumerate(queries):
        #     l,r=sub
        #     xor=0
        #     for i in range(l,r+1):
        #         xor=xor^arr[i]
        #     queries[k]=xor
        # return queries      


        