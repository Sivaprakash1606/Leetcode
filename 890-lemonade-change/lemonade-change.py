class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={5:0,10:0,20:0}
        for i in bills:
            if i==20:
                if d[10]>0 and d[5]>0:
                    d[10]=d[10]-1
                    d[5]=d[5]-1
                elif d[5]>2:
                    d[5]=d[5]-3
                else:
                    return False    
            elif i==10:
                if d[5]==0:
                    return False    
                d[5]=d[5]-1
                d[10]=d[10]+1
            else:
                d[5]=d[5]+1
        return True 


              # or 
# class Solution:
#     def lemonadeChange(self,bills:List[int])->bool:
#         fives = 0
#         tens = 0
#         for i in bills:
#             if i == 5:
#                 fives += 1
#             elif i == 10 and fives >= 1:
#                 fives -= 1
#                 tens += 1
#             elif i==20 and fives >= 1 and tens >= 1:
#                 tens -= 1
#                 fives -= 1
#             elif i==20 and fives >=3:
#                 fives -= 3
#             else:
#                 return False 
#         return True                


                    



        