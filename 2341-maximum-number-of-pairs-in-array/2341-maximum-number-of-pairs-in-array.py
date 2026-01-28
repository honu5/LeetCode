class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        count=Counter(nums)
        for  i,frq in count.items():
            if frq%2==1 and i not in ans:
                ans.append(i)
                nums.remove(i)
        n=len(ans) 
        m=(len(nums))/2
        return [m,n]        

        