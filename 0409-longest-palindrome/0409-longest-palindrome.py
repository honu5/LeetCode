class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(s)
        val=0
        max_odd=0
        has_odd=False

        for frq in count.values():
            if frq%2==1:
                val+=frq-1
                has_odd=True
               
            else: val+=frq
        if has_odd:
            val+=1
        return val+max_odd


        