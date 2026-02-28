class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=Counter(str(n))
        most=count.most_common()
        val=most[-1][0]
        for i in count:
            if count[i]==most[-1][1] and int(i)<=int(val):
                val=i
        return int(val)
        