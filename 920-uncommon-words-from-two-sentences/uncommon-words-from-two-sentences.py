class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        str1=s1.split()
        str2=s2.split()

        d={}
        for i in str1:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1 

        for j in str2:
            if j in d:
                d[j]=d[j]+1
            else:
                d[j]=1  

        result=[]
        for key,values in d.items():
            if values ==1:
                result.append(key)
        return result                 


        # wrong one
        # str1=s1.split()
        # str2=s2.split()
        # sets1=set(str1)-set(str2)
        # set2=set(str2)-set(str1)
        # return list(sets1)+list(set2)
        

                        


     
       



        