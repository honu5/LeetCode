class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        
        for i in range(len(nums)):
            ans=[]
            for j in range(len(nums)):
                ans.append(nums[(i+j)%len(nums)])
       
            if ans==sorted(ans):
                return True
            print(ans)
        return False

        