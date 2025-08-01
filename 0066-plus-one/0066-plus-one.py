class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string=''.join(str(num) for num in digits)
        final=int(string)+1
        ans=str(final)
        return [int(s) for s in ans]
        