class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_sort=sorted(s1)
        r=0
        l=len(s1)
        while l<=len(s2):
            master=sorted(s2[r:l])
            if s1_sort==master:
                return True
            r=r+1
            l=l+1   
        return False        
               
            

            






        # s = 0
        # reverse = False
        # start = 0
        # for i in range(len(s2)):
        #     if s2[i] == s1[s]:
        #         s = s + 1
        #     if start == 0:
        #         start = 1    
        #     if s == len(s1):
        #         reverse = True
        # if not reverse:
        #     for i in range(i, i-len(s1), -1):
        #         if s2[i] == s1[s]:
        #             s = s + 1
        #         if start == 0:
        #             start = 1    
        #         if s == len(s1):
        #             reverse = True   
        # return reverse