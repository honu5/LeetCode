class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans=[0]*num_people
        i=1
        n=candies
        while n>0:
            n-=i
            ans[i%num_people-1]+=i
            i+=1
        if n<0:
            ans[((i-1)%num_people)-1]+=n
        
        return ans
        