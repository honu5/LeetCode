class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        l=1
        n=len(skill)
        r=n-2
        val=skill[0]+skill[-1]
        prod=skill[0]*skill[-1]
        while l<r:
            if skill[l]+skill[r]!=val:
                return -1
            prod+=(skill[l]*skill[r])
            l+=1
            r-=1
        return prod
        
            

        