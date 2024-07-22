class Solution:
    def addDigits(self, num: int) -> int:
        string=str(num)
        if len(string)==1:
            return num
        summ=0
        for i in string:
            summ=summ+int(i)
        return self.addDigits(summ)



        