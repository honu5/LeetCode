class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val=0
        nums={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if nums[s[i]]>=nums[s[i+1]]:
                val+=nums[s[i]]
            else:val-=nums[s[i]]
        val+=nums[s[-1]]
        return val


        