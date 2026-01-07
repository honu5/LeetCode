class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans=[]
        for i in strs:
            tr=False
            for j in i:
                if j.isalpha():
                    ans.append(len(i))
                    tr=True
                    break
            if not tr:
                ans.append(int(i))
        return max(ans)
                
        