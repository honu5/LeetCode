class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        s=s.split()
        l=[]
        for i in s:
            i=i[::-1]
            l.append(i)
        for i in l:
            a+=i+" "
        return a[0:len(a)-1]
        