class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Using Greedy
        if sum(gas)<sum(cost):
            return -1
        p=0
        s=0
        for i in range(0,len(gas)):
            p=p+gas[i]
            p=p-cost[i]
            if p<0:
                p=0
                s=i+1
        return s          
          
        # j=len(gas)-1
        # index=0
        # i=index
        # rem=0
        # while i<=j:
        #     rem=(rem+gas[i])-cost[i]
        #     if rem<1:
        #         index=index+1
        #         i=index
        #         rem=0
        #         continue
        #     if i==j:
        #         i=0
        #         while i<=index:
        #             rem=(rem+gas[i])-cost[i]
        #             if i==index and rem >= 0:
        #                 return index
        #             elif rem<1:
        #                 index=index+1
        #                 i=index
        #                 rem=0
        #                 continue
        # return -1          



        