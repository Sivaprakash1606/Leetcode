class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using Monotonic Stack
        stack=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop()
                result[j]=i-j
            stack.append(i)
        return result    






        # time limit execeed
        # result=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     days=1
        #     find=False
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             result[i]=days
        #             find=True
        #             break
        #         else:
        #             days=days+1 
        #     if find==False:
        #         result[i]=0
        # return result               


        