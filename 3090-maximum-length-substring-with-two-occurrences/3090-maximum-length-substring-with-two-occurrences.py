class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''l=0
        r=1
        val=0
        i=0
        while l<len(s) and r<=len(s):
            wndw=s[l:r+1]
            count=Counter(wndw)
            most=count.most_common()
            if most[0][1]>2:
                print(most[0][1])
                l+=1
                val=max(val,r-l)
            else:r+=1
            
        return val'''

        lst=list(s)
        n=len(s)
        wndw=lst[0:2]
        l=0
        r=2
        val=2
        while r<n:
            wndw=lst[l:r+1]
            count=Counter(wndw)

            a=count.most_common()[0][1]
            if a>2:
                l+=1
            else:
                val=max(val,r-l+1)
                r+=1
            print(a,r,l,wndw)
        return val


