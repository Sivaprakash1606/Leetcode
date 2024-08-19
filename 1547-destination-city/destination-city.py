class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        def find(allticket, i,res):
            for j in range(len(allticket)):
                find=False
                for k in range(len(allticket)):
                    if res[-1]==allticket[k][0]:
                        res.append(allticket[k][0])
                        res.append(allticket[k][1])
                        allticket.pop(k)
                        find=True
                        break
                if find==False:
                    res=[]
                    return False
            if not allticket:
                return res
        allticket = paths[:]
        res=[]
        for i in range(len(paths)):
            res.append(allticket[i][0])
            res.append(allticket[i][1])
            allticket.pop(i)
            result = find(allticket, i, res)
            if result == False:
                allticket=paths[:]
                res=[]
            else:
                return res[-1]
                    
        
        