class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        b=''.join(str(a)for a in digits)
        c=int(b)+1
        d=str(c)
        return [int(n) for n in d]