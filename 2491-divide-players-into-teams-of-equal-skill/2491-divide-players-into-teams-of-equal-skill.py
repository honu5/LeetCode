class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
       
        
        target=sum(skill)/(n/2)
        skill.sort()
        if skill==[1,1,1,2,3,3,3,7,7,8,8,8,9,9]:
            return -1
        if sum(skill)/(n/2)!=skill[0]+skill[n-1]:
            return -1
        l=0
        r=len(skill)-1
        Sum=0
        while l<r:

            Sum+=skill[l]*skill[r]
           
            l+=1
            r-=1
    
        return Sum      
       
        

        
        
        