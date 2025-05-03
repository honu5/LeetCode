class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
       
        
        target=sum(skill)/(n/2)
        skill.sort()
        
        if sum(skill)/(n/2)!=skill[0]+skill[n-1]:
            return -1
        l=0
        r=len(skill)-1
        Sum=0
        if skill.count(skill[l])!=skill.count(skill[r]):

                return -1
        while l<r:
            
            

            Sum+=skill[l]*skill[r]
           
            l+=1
            r-=1
    
        return Sum      
       
        

        
        
        