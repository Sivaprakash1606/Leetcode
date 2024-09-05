class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = mean * (len(rolls)+n)
        current_sum=sum(rolls)
        missing_sum=total_sum - current_sum

        if missing_sum > n*6 or missing_sum < n:
            return []

        res=[]

        while n:
            dice=min(6,missing_sum - n+1)
            res.append(dice)
            missing_sum-=dice
            n-=1
        return res    


        