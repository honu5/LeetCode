class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=['A','E','O','I','U','a','e','i','o','u']
        ans=[]
        isx=[]
        s=list(s)
        i=0
        m=0
        while i<len(s):
            if s[i] in vowels:
                ans.append(s[i])
                isx.append(i+m)
                s.pop(i)
                m+=1
            else:i+=1
        ans.sort()
        for i in range(len(ans)):
            s.insert(isx[i],ans[i])

        s=''.join(s)
        return s
        