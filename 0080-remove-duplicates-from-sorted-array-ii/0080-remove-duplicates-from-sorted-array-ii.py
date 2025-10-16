class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''nums.sort()
        count=1
        ans=1
        last=nums[-1]+1
        i=0
        n=len(nums)
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                ans+=1
            
            if count>2:
                popped=nums.pop(i)
                nums.append(popped)
                count=1
            i+=1
        return ans'''

        count=Counter(nums)
        for num,frq in count.items():
            if frq>2:
                n=frq
                while n>2:
                    nums.remove(num)
                    n-=1
        return len(nums)

        