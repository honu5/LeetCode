class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        num=sorted(nums)
        l=0
        r=len(nums)-1
        while l<r:
            if num[l]+num[r]==target:
                if num[l]==num[r]:
                    a=nums.index(num[l])
                    ans.append(a)
                    nums.remove(num[l])
                    b=a=nums.index(num[l])+1
                    ans.append(b)
                    return ans
                

                return [nums.index(num[l]),nums.index(num[r])]
            elif num[l]+num[r]>target:
                r-=1
            else : l+=1
     