class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        def dfs(cur):
            if cur>n:
                return 
            res.append(cur)    
            for i in range(10):
                dfs(cur*10+i)

        for i in range(1,10):
            dfs(i)        

        return res        

        