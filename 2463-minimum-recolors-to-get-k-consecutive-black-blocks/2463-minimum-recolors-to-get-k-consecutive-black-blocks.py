class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        print(len(blocks))
        wndw=list(blocks[0:k])
        count=Counter(wndw)
        b=count['W']
        val=count['W']

        for i in range(1,len(blocks)+1-k):
            if blocks[i-1]=='W':
                b-=1
            if blocks[i+k-1]=='W':
                b+=1
            val=min(val,b)
        return val
            


        