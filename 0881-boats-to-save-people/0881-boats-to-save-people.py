class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boat=0
        

        while l <= r:

            if people[r] + people[l] > limit:
                
                r -= 1
                boat+=1

            else:
                
                l += 1
                r -= 1
                boat+=1

    
        return boat
