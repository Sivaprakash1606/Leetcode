class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                l[i]=l[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                l[i]=max(l[i],l[i+1]+1)
        return sum(l)            

        # total=len(ratings)
        # for i in range(len(ratings)-1):
        #     if ratings[i]>=ratings[i+1] or ratings[i]>=ratings[i-1]:
        #         total=total+1
        # if ratings[i+1]>ratings[i+1-1]:
        #     total=total+1        
        # return total        
        