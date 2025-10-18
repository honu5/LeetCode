class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trustee=[x[0] for x in trust]
        trusted=[x[1] for x in trust]
        count=Counter(trusted)
        for i in range(1,n+1):
            if count[i]<n-1:
                continue
            elif i not in trustee:
                return i
        return -1
        